---
{"dg-publish":true,"dg-path":"Rebuilding a Terraform State File.md","permalink":"/rebuilding-a-terraform-state-file/","tags":["blogs"]}
---


## Setting the Table

If you are reading this, you are either having a bad day, or are the sort of person that likes to watch horror movies.  
Rebuilding the *state file* for Terraform is not something that anyone ever plans to do, and is about as fun as it sounds.  
Note that my experience is with Azure and my tools / process are focusing on that. If anyone has thoughts on this process for other platforms please reach out and let me know, I'd love to know how it gets done elsewhere.
  
When I'm talking about rebuilding the state file, we had a client come to use that has *hundreds of resources* deployed in Azure (Just under 600), and the Terraform config was used to deploy all of that and represents the environment perfectly... but the state file itself was lost. *We needed a way to import all the resources into state without changing the resources or the config.*

This is easier said than done, as one option you have to import into State is to run `terraform import` in your cli, but this will try to run a Plan after the import.  
This Plan can be a pain as you can run into issues with `(Known after Apply)`, as it will report that the Import is prepared, but then fail to actually finish the import.

```bash
❯ terraform import random_integer.import 15390,1,50000
random_integer.import: Importing from ID "15390,1,50000"...
random_integer.import: Import prepared!
  Prepared random_integer for import
random_integer.import: Refreshing state... [id=15390]
╷
│ Error: Invalid count argument
│
│   on main.tf line 16, in resource "random_integer" "example2":
│   16:   count = random_integer.example.result
│
│ The "count" value depends on resource attributes that cannot be determined until apply, so
│ Terraform cannot predict how many instances will be created. To work around this, use the
│ -target argument to first apply only the resources that the count depends on.
```

Since Terraform is only doing a Plan, and is working against your local files, a *dirty trick* I use to get around this issue is to just remove the offending resources from my local `.tf` files (Assuming they are all in Git and backed up, let's not make a bad day worse!).  
*This can get you out of a bind when you are trying to import 5-10 resources, but on the scale of hundreds this is a nightmare*. The `terraform import` command only lets you import one resource at a time, and cherry-picking resources to delete from your `.tf` files is easier said than done when those resources are nested in modules, which can unravel your config even further making this import command not a viable path. It also requires you to have direct access to the state file, which I always avoid handing this out anyway (even to myself), and instead do all the Plan / Apply in CI/CD.

So the `terraform import` command is a pain, there has to be a better way, right? There is!  
The `import` block allows you to import at Apply time which helps get around some of these timing issues. It also is just a nicer workflow as now you yourself don't need access to the state file directly, and can run Imports through your CI/CD without additional complexity.

```hcl
resource "random_integer" "import" {
  min = 1
  max = 100
}
import {
  to = random_integer.import
  id = "15390,1,50000"
}
```

*I always advocate that `import` blocks are the way to go,* it's a much more "Terraform" experience the whole way around.  
Further documentation on how to actually make these is [available here](https://developer.hashicorp.com/terraform/language/import).

## Laying out the Cutlery

Alright, we have mastered the understanding of how to import to State, *how do we scale this out to dozens or even hundreds of resources*? This is the fun part: *it does not scale*.  
Each `import` block needs to be handcrafted somehow to line up to the Resource Blocks we already have.  
There are some tools out there for generating your cloud configuration into Terraform `.tf` files (including the new `-generate-config-out` command coming soon to Terraform CLI), but the vast majority of these tools won't pattern match existing resources to existing config.  
If you are working on the scale of 1-50 resources to import, I'd still strongly consider making a coffee or two, and just sitting down and make these blocks by hand. It sucks, it isn't fancy, but it is what it is. There are tricks to be had with clever search and replaces to work at scale on your files, and even better processes using macros and clever tactics with Vim, but that is a blog post for another day.

## Eating the Elephant

What if you are in the situation where you have *hundreds* of resources to import from Azure, and there is no way to get this to work besides having *every single import block configured all at once*.  
In comes the [Terraform-State-Importer](https://github.com/Azure/terraform-state-importer) tool. At the time of writing this tool is still rough around the edges and is overall very new, but I can vouch for its effectiveness at getting the job done when nothing else will.

Quick hits on this tool:
- Works against a Local state file, so you may need to add a `_override.tf` file that specifies `terraform { backend "local" {} }`, and run a `terraform init -migrate-state`.
- Runs Resource Graph queries, matching the results to Terraform Resource Blocks.  
    - To do this, you will need to log in with `azcli`, and have `Contributor` permissions at the Pseudo Root Management Group or Tenant Root Group.
- After running the tool, it generates a `issues.csv` that gets attended to as a next step.
    - This includes ambiguous results where multiple Azure Resources in query results could match a Resource Block, or Azure Resources in query results that do not appear to have a matching Resource Block.
- When there are no Issues left, it will generate the required Import and Destroy blocks in Terraform.

Something that may help to understand early in the process is that under the hood it does this matching based on the `resource_id` from Azure, and the `name` field of your Resource Blocks, which is how it manages to work for both `AzureRm` and `AzApi`.

```go
# Snippet from analyzer/mapping.go
        # Match if name is exactly the same
			if resource.ResourceNameMatchType == types.NameMatchTypeExact && strings.ToLower(graphResource.Name) == strings.ToLower(resource.ResourceName) {
				resource.MappedResources = append(resource.MappedResources, graphResource)
			}
            
        # Match if the Resource ID contains the Name
			if resource.ResourceNameMatchType == types.NameMatchTypeIDContains && strings.Contains(strings.ToLower(graphResource.ID), strings.ToLower(resource.ResourceName)) {
				resource.MappedResources = append(resource.MappedResources, graphResource)
			}
            
        # Match if the Resource ID ends with the Name
			if resource.ResourceNameMatchType == types.NameMatchTypeIDEndsWith && strings.HasSuffix(strings.ToLower(graphResource.ID), strings.ToLower(resource.ResourceName)) {
				resource.MappedResources = append(resource.MappedResources, graphResource)
			}
```

### Getting Started with Terraform-state-importer

Certainly have a read of the [readme found in the repo](https://github.com/Azure/terraform-state-importer), and when you are ready download the latest binary for your OS from the releases page (At time of writing it is `0.0.12`).  
The rest of this guide is not a replacement for the readme, but is just my notes from my experience.

There are many situations this tool is handy, and lots of workflows to reach the goal with the tool. My use case is the full rebuild of a state file that went missing, and I wanted to keep the tooling as reusable as possible, as the Terraform Root Module that we needed to rebuild is a template we have used many times for our Core Element product, so it's worth keeping around. The tool is originally built to migrate from CAF Landing Zone module/submodules to new Azure Verified Modules, but it's perfectly within its capability to be used how I used it here.

The core of the workflow is around the **Config.yaml** file that tells the tool:
- A list of `subscriptionIDs` to look for Resources in.
- A list of `managementGroupIDs` to look Management Groups in.
- What Resource ID Patterns to ignore using regex under the `ignoreResourceIDPatterns` list.
- What Terraform Resource Blocks to ignore using regex under the `ignoreResourceTypePatterns` list.
- What Resource Graph Queries to run against Azure to actually find Resources in the `resourceGraphQueries` list.
- How to calculate the Resource Names when it isn't obvious in the `nameFormats` list.
- How to delete Resources when instructed to in the `issues.csv`, under the `deleteCommands` list.  
For me I spent the vast majority of my time in this file, adding more queries and refining the ignore list to generate the least amount of issues in the `issues.csv` as possible.

There is a choice to be made regarding the queries: Do you want to collect every Resource possible, or just the ones you know you are using?  
I chose to collect every Resource I could, and then to ignore the Resource IDs I don't care about in the `config.yaml`.  
I started by combining all of the example `config.yaml` files from the source repo for the tool, and then added some stuff as I went:

```yaml
resourceGraphQueries:
  - name: "Resource Groups"
    scope: "Subscription"
    query: |
      resourcecontainers
      | where type == "microsoft.resources/subscriptions/resourcegroups"
      | project id, name, type, location, subscriptionId, resourceGroup = name
  - name: "Top Level Resources"
    scope: "Subscription"
    query: |
      resources
      | project name, id, type, location, subscriptionId, resourceGroup
  - name: "Virtual Network Subnets"
    scope: "Subscription"
    query: |
      resources
      | where type == "microsoft.network/virtualnetworks"
      | project id, name, type, location, subscriptionId, resourceGroup, subnets = properties.subnets
      | mv-expand subnets
      | project name = tostring(subnets.name), id = tostring(subnets.id), type = tostring(subnets.type), location, subscriptionId, resourceGroup
  - name: "Virtual Network Peerings"
    scope: "Subscription"
    query: |
      resources
      | where type == "microsoft.network/virtualnetworks"
      | project id, name, type, location, subscriptionId, resourceGroup, peerings = properties.virtualNetworkPeerings
      | mv-expand peerings
      | project name = tostring(peerings.name), id = tostring(peerings.id), type = tostring(peerings.type), location, subscriptionId, resourceGroup
  - name: "Management Groups"
    scope: "ManagementGroup"
    query: |
      resourcecontainers
      | where type == "microsoft.management/managementgroups"
      | project id, name, type, location, subscriptionId, resourceGroup
  - name: "Management Group Subscriptions"
    scope: "ManagementGroup"
    query: |
      resourcecontainers
      | where type == "microsoft.resources/subscriptions"
      | extend mgAncestors = properties.managementGroupAncestorsChain
      | where array_length(mgAncestors) > 0
      | extend directParentMg = mgAncestors[0].name
      | where directParentMg != "Tenant Root Group"
      | extend fullPath = strcat("/providers/Microsoft.Management/managementGroups/", directParentMg, "/subscriptions/", subscriptionId)
      | project id = fullPath,
                name = fullPath,
                type = "microsoft.management/managementgroups/subscriptions",
                location = "",
                subscriptionId = subscriptionId,
                resourceGroup = ""
  - name: "Policy Definitions"
    scope: "ManagementGroup"
    query: |
      policyresources
      | where type == "microsoft.authorization/policydefinitions"
      | project id, name, type, location, subscriptionId, resourceGroup
  - name: "Policy Set Definitions"
    scope: "ManagementGroup"
    query: |
      policyresources
      | where type == "microsoft.authorization/policysetdefinitions"
      | project id, name, type, location, subscriptionId, resourceGroup
  - name: "Policy Assignments"
    scope: "ManagementGroup"
    query: |
      policyresources
      | where type == "microsoft.authorization/policyassignments"
      | project id, name, type, location, subscriptionId, resourceGroup
  - name: "Role Definitions"
    scope: "ManagementGroup"
    query: |
      authorizationresources
      | where type == "microsoft.authorization/roledefinitions"
      | where properties.type == "CustomRole"
      | project id = strcat(properties.assignableScopes[0], id), name, type, location, subscriptionId, resourceGroup
  - name: "Role Assignments for Policy Assignments"
    scope: "ManagementGroup"
    query: |
      authorizationresources
      | where type == "microsoft.authorization/roleassignments"
      | where properties.description != "Created by ALZ Terraform provider. Assignment required for Azure Policy."
      | extend principalId = tostring(properties.principalId)
      | join kind=inner(
      policyresources
      | where type == "microsoft.authorization/policyassignments"
      | where isnotnull(identity)
      | extend bag_key = tostring(bag_keys(identity.userAssignedIdentities)[0])
      | extend bag_value = identity.userAssignedIdentities[bag_key]
      | extend principalId = tostring(coalesce(bag_value.principalId, identity.principalId))
      ) on principalId
      | project id, name, type, location, subscriptionId, resourceGroup
  - name: "Route Table Routes"
    scope: "Subscription"
    query: |
      resources
      | where type == "microsoft.network/routetables"
      | project id, name, type, location, subscriptionId, resourceGroup, routes = properties.routes
      | mv-expand routes
      | project id = strcat(id, '/routes/', tostring(routes.name)), name = tostring(routes.name), type = "microsoft.network/routetables/routes", location, subscriptionId, resourceGroup
```

```yaml
ignoreResourceIDPatterns:
  # Ignore policy assignments at subscription scope
  - "/subscriptions/.*/providers/Microsoft.Authorization/policyAssignments"
  # Ignore Sub Role Assignment and Defs
  - "/subscriptions/.*/providers/Microsoft.Authorization/RoleAssignments/"
  - "/subscriptions/.*/providers/Microsoft.Authorization/RoleDefinitions/"
  # Ignore activity log resource group
  - "resourceGroups/Default-ActivityLogAlerts"
  # Ignore default network watcher resource group
  - "resourceGroups/NetworkWatcherRG"
  # Ignore deprecated monitoring solutions
  - "Microsoft.OperationsManagement/solutions/ChangeTracking"
  - "Microsoft.OperationsManagement/solutions/SecurityInsights"
  # Ignore UnusedResourceId
  - "Microsoft.HybridCompute/machines"
  - "resourceGroups/.*/providers/Microsoft.Web/connections"
  - "providers/Microsoft.AzureArcData"
  - "Microsoft.Compute/snapshots"
  - "virtualMachines/.*"
  - "/providers/Microsoft.Management/managementGroups/mg-i-dont-want-to-import"
  - "/subscriptions/.*/resourceGroups/managed-in-another-tf-project"
  - ...
```

### The Workflow Loop

To get to a completed `config.yaml`, I was rerunning the tool (with the `--skipInitPlanShow` flag to not constantly rerun the `terraform plan`, as that took a lot of time), and then working at chipping away at the issues in the csv.  
As in the [Issues Resolution](https://github.com/Azure/terraform-state-importer?tab=readme-ov-file#issue-resolution) section of the readme, the `UnusedResourceID` was the easiest to chip away at by placing into the `config.yaml`, `NoResourceID` tells you that you need to adjust your `resourceGraphQueries` and/or your `nameFormats`, and `MultipleResourceIDs` is probably the hardest to solve as you may be able to fix your queries/names, but in my experience I was not able to solve it all in a time efficient way over just working in the `issues.csv`.  
For some Resources, I did end up making a `manual-imports.tf` to hand-craft import blocks for some of the more tricky Resources that I could not get a query to work for, but this was only *~5 blocks* which was pretty reasonable.  
Once the `issues.csv` has reached a reasonable amount of resources, you can then copy the file giving it a new name (something like `issues-attended.csv`), and then attend to the issues listed by telling the tool how to handle each issue id.

| Issue ID | Issue Type          | Resource Address                                                                                                                                                                                                                | Resource Name           | Resource Type                              | Resource Sub Type | Resource Location | Mapped Resource ID                                                                                                                        | Action | Action ID |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ------------------------------------------ | ----------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- |
| i-88021  | MultipleResourceIDs | module.core.module.alz.azurerm_management_group_policy_assignment.enterprise_scale["/providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations"]      | Deny-RSG-Locations      | azurerm_management_group_policy_assignment |                   | australiaEast     | /providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations      | Use    |           |
| i-88021  | MultipleResourceIDs | module.core.module.alz.azurerm_management_group_policy_assignment.enterprise_scale["/providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations"]      | Deny-RSG-Locations      | azurerm_management_group_policy_assignment |                   | australiaEast     | /providers/Microsoft.Management/managementGroups/org-development/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations   | Ignore |           |
| i-88021  | MultipleResourceIDs | module.core.module.alz.azurerm_management_group_policy_assignment.enterprise_scale["/providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations"]      | Deny-RSG-Locations      | azurerm_management_group_policy_assignment |                   | australiaEast     | /providers/Microsoft.Management/managementGroups/org-production/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations    | Ignore |           |
| i-88021  | MultipleResourceIDs | module.core.module.alz.azurerm_management_group_policy_assignment.enterprise_scale["/providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations"]      | Deny-RSG-Locations      | azurerm_management_group_policy_assignment |                   | australiaEast     | /providers/Microsoft.Management/managementGroups/org-reporting/providers/Microsoft.Authorization/policyAssignments/Deny-RSG-Locations     | Ignore |           |
| i-3b4c8  | MultipleResourceIDs | module.core.module.alz.azurerm_management_group_policy_assignment.enterprise_scale["/providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-Resource-Locations"] | Deny-Resource-Locations | azurerm_management_group_policy_assignment |                   | australiaEast     | /providers/Microsoft.Management/managementGroups/org-business/providers/Microsoft.Authorization/policyAssignments/Deny-Resource-Locations | Use    |           |
| ...      | ...                 | ...                                                                                                                                                                                                                             | ...                     | ...                                        | ...               | ...               | ...                                                                                                                                       | ...    | ...       |

### The Last step

With our new `issues-attended.csv` we can run the tool one last time with `--issuesCsv issues-attended.csv`, and we know we are done when it generates the `import.tf`.  
Now we can commit this to our repo (removing the `_override.tf` file to restore the backend) and run one last set of plans to confirm if the `import` blocks are all correct. I had a few IDs that needed to have their casing fixed, but otherwise it was very successful.

With all the Imports working how we want... we are done!  
I was sceptical that the Apply would not work with *~600 import blocks*, but they all worked without a hitch.

## Dessert?

This writeup might make it seem easy (maybe it doesn't), but for me it took **~16 hours** to get all near 600 resources imported. I don't think there are any shortcuts, but certainly the `terraform-state-importer` tool is fantastic, ask me how I would have done this even 6 months ago, and I honestly don't know if we could have done this.

The TL;DR for deciding how to start your import journey:
- If you have full ownership of the state file and just need to get a handful of resources imported, use `terraform import` in the cli.
- If you want to work in CI/CD to import to the state file in a predictable way, and only have a few handful of resources to be imported, use `import` blocks in your `.tf` files.
- If you have a daunting amount of resources to import, and need a way to programmatically map Azure Resource IDs to Resource Blocks, work with the `terraform-state-importer`.

If you do need to work with the `terraform-state-importer`:
- Start building a `config.yaml` that gets you all the Azure Resource IDs you need to map out.
- Update the `issues.csv` and the `config.yaml` to attend to every single issue, and generate the `import.tf` file.
- Do the last modifications to the Resource IDs in the `import` blocks to make sure the Plan reports no errors or unwanted changes.
- Merge it in, and enjoy a job well done.

But the best way overall to fix the state file: *Never end up in this situation*. Always backup the state file, it is a very important part of the Terraform tooling, and should be treated as such.

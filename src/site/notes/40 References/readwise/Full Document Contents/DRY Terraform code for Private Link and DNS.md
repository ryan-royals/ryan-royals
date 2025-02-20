---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/dry-terraform-code-for-private-link-and-dns/","tags":["rw/articles"]}
---

![rw-book-cover](https://1138blog.files.wordpress.com/2023/08/image-4.png)

After last week’s almost-philosophical [post on network complexity](https://blog.cloudtrooper.net/2023/08/11/is-computer-networking-too-complex/), let’s move on to more mundane tasks. Today I will focus on how to write efficient Terraform code to connect private endpoints and DNS, without having to copy/paste literally hundreds of lines.

First things first: what the heck am I talking about? [Private endpoints](https://learn.microsoft.com/azure/private-link/private-endpoint-overview) are a way of surfacing Azure managed services inside of your private virtual network. For example, if you have a storage account called `cloudtrooper`, it would typically be exposed under the fully qualified domain name of `cloudtrooper.blob.core.windows.net`, which would resolve to a public IP address accessible over the Internet. Private endpoints can expose the storage account not with a public, but with a private IP address inside of your Virtual Network. Why would you want to do that? Mostly so that you can block access to other storage accounts out there, and prevent data exfiltration.

#### The DNS dance

One of the most complex tasks of private endpoints is not creating the endpoint itself, but to manage DNS resolution for its users. This is because the storage account’s fully qualified name hasn’t changed: it is still `cloudtrooper.blob.core.windows.net`, but now your users need to resolve it to a private IP address.

The way to do that is creating a certain [private DNS zone](https://learn.microsoft.com/azure/dns/private-dns-privatednszone) and associate it to the Virtual Networks where those clients are (or to be accurate, where the DNS servers of those clients are). The private DNS zone cannot be just any domain, but there are specific zone names for each private endpoint type, as documented in [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/azure/private-link/private-endpoint-dns#azure-services-dns-zone-configuration). For our example, for blob resources in storage accounts we would create a private DNS zone for `privatelink.blob.core.windows.net`.

You might be tempted to go and create an A record for the storage account (`cloudtrooper` in this example) in that DNS zone, containing the private IP address of your storage account’s endpoint. However, but there is a better way to do it: you can “link” the endpoint with the zone, and the A record (or records, some endpoints require more than one) will be created for you. This “link” between endpoints and zones is called a “zone group”.

#### Creating zone groups automatically

So whenever somebody creates a private endpoint for any Azure managed resource, they would call the network administrator so that she can link it to the correct private DNS zone. Mmmh, that doesn’t sound too “agile”, does it? Worry not – you can automate this linking of private endpoints to DNS zones with Azure Policy.

As described in [Private Link and DNS integration at scale](https://learn.microsoft.com/azure/cloud-adoption-framework/ready/azure-best-practices/private-link-and-dns-integration-at-scale), you can create a special type of Azure Policy called “Deploy If Not Exists”, that will look for endpoints without zone groups (not linked to any DNS zone), and when they find one, they will connect it automatically to a pre-defined DNS private zone.

Fantastic! We can even create that Azure Policy via Terraform, to follow cloud best practices using Infrastructure as Code. The whole process would look like this:

![](https://1138blog.files.wordpress.com/2023/08/image-2.png)
#### Expanding to multiple endpoint types

Easy enough! Now we just need to expand your code to cover all possible endpoint types. At the time of this writing there are 101 documented private endpoint types in [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/azure/private-link/private-endpoint-dns#azure-services-dns-zone-configuration). So you might end up doing this:

![](https://1138blog.files.wordpress.com/2023/08/image-3.png)
A copy/paste exercise where 99% of the code is identical doesn’t sound like a good programming practice. There has to be a better way to do it.

#### DRY Terraform code for Azure Policy

DRY (Don’t Repeat Yourself) is a cool acronym to designate the coding best practice suggesting to not have duplicate code in whatever you are programming. The goal would be achieving something like the picture below, where a single Terraform template can create all of the policies required to manage each private endpoint type:

![](https://1138blog.files.wordpress.com/2023/08/image-4.png)
You can find such a Terraform module in my repo <https://github.com/erjosito/azpolicy-tf>. This repo uses Terraform loop mechanisms to generate copies of the same basic policy customized for each private endpoint type.

The code consists of a Terraform module that, among other parameters, takes as input a dictionary with endpoint types as keys, and the private DNS zones that they will be associated to as values (see the [module README](https://github.com/erjosito/azpolicy-tf/blob/main/modules/dns-zone-group/README.md) for more details on the utilization of the module). Note that the list of private endpoint types and the corresponding DNS zones in the example below is not complete:

```
"blob"      = "privatelink.blob.core.windows.net"
"file"      = "privatelink.file.core.windows.net"
"table"     = "privatelink.table.core.windows.net"
"queue"     = "privatelink.queue.core.windows.net"
"dfs"       = "privatelink.dfs.core.windows.net"
"web"       = "privatelink.web.core.windows.net"
"sqlServer" = "privatelink.database.windows.net"
"sites"     = "privatelink.azurewebsites.net"

```

The module will loop over the items of the parameter, and create the private DNS zones and the corresponding Azure Policy definitions.

Caution! This approach will not be valid for certain specific types of private endpoints:

* In some situations, the Azure service needs to control the private DNS zone itself (such as AKS, see [Create a private AKS cluster](https://learn.microsoft.com/azure/aks/private-clusters?tabs=azure-portal#configure-a-private-dns-zone).
* In other cases, the DNS zone contains the resource region name, so the policy must be region-specific and match the resource region too (or extract the region of the resource and create a region-specific DNS zone), such as Azure Batch. You can find these resources in [Azure Private Endpoint DNS configuration](https://learn.microsoft.com/azure/private-link/private-endpoint-dns#azure-services-dns-zone-configuration), the zone name would be described as `{regionName}.privatelink.batch.azure.com`.

And yet, this approach will cover for the majority of Azure Private Endpoint types, thus significantly reducing the footprint of your Terraform code.

#### Terraform loops

The module uses different Terraform techniques, most notably three types of loops:

* Resource loops with the `for_each` attribute
* Dynamic blocks with the `for_each` attribute
* Variable construction with the `for` operator

The module firstly creates the DNS zones over a resource loop powered by the `for_each` attribute of the resource:

```
resource "azurerm_private_dns_zone" "example" {
  **for\_each = toset(values(var.zone\_assignments))**
  name                = each.value
  resource_group_name = var.zone_rg_name 
}

```

The individual Azure policies are created using a similar loop with a `foreach` property. The key part though is the `replace` function used to customize both the policy and the parameters definition:

```
resource "azurerm_policy_definition" "zone_group" {
  **for\_each = toset(keys(var.zone\_assignments))**
  name                = "${each.value}-zone-group"
  policy_type         = "Custom"
  mode                = "All"
  display_name        = "Connect ${each.value} endpoints to DNS private zones"
  management_group_id = var.definition_management_group
  policy_rule         = **replace(file("${path.module}/policy-rule.json"), "\_ENDPOINT\_TYPE\_", each.value)**
  parameters          = **replace(file("${path.module}/policy-parameters.json"), "\_ENDPOINT\_TYPE\_", each.value)**
}

```

These policy definitions are grouped in a policy set (also known as policy initiative), which makes use of the dynamic block concept in Terraform to provide the different policy definition IDs created in the previous step. Note as well how `jsondecode` and `jsonencode` can be used to convert from string to object and vice versa:

```
resource "azurerm_policy_set_definition" "zone_group" {
  name = "zone-group"
  policy_type = "Custom"
  display_name = "Zone Group for endpoints"
  management_group_id = var.definition_management_group
  parameters = jsonencode(**{for s in keys(var.zone\_assignments) : "${s}PrivateDnsZoneId" => jsondecode(local.initiative\_param\_template)}**)
  **dynamic** policy_definition_reference {
    **for\_each** = toset(keys(var.zone_assignments))
    content {
      policy_definition_id = azurerm_policy_definition.zone_group[policy_definition_reference.value].id
      parameter_values     = "{\"${policy_definition_reference.value}PrivateDnsZoneId\": {\"value\": \"[parameters('${policy_definition_reference.value}PrivateDnsZoneId')]\"}}"
    }
  }
}

```

Lastly, the policy set assignment needs to provide the correct values for each of the parameters created for the policy definitions. For this purpose, the Terraform `for` function can be used to create a dictionary that can be then serialized and provided as value to the `parameters` attribute of the assignment resource:

```
resource "azurerm_management_group_policy_assignment" "zone_group" {
  name                 = "PLink and DNS" # Max 24 characters
  location             = var.assignment_location
  management_group_id  = var.definition_management_group
  policy_definition_id = azurerm_policy_set_definition.zone_group.id
  description          = "Link automatically private endpoints to DNS private zones"
  display_name         = "Link automatically private endpoints to DNS private zones"
  parameters           = jsonencode({**for k, v in var.zone\_assignments** : "${k}PrivateDnsZoneId" => jsondecode("{ \"value\": \"${data.azurerm_subscription.primary.id}/resourceGroups/${var.zone_rg_name}/providers/Microsoft.Network/privateDnsZones/${v}\" }")})
  identity { 
    type = "SystemAssigned" 
  }
}

```

#### That’s all!

Hopefully you could find in this post some tricks to simplify your Terraform code and keep it DRY.

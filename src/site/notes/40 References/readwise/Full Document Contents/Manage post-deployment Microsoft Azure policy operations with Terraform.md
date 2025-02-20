---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/manage-post-deployment-microsoft-azure-policy-operations-with-terraform/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1669225392-terraform-and-azure-logo.jpeg)

HashiCorp and Microsoft have partnered to create a number of [Terraform modules](https://developer.hashicorp.com/terraform/tutorials/modules/module) that build an N-tier architecture following Microsoft's [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/architecture/framework/) and security best practices. This is the third in a series of blog posts demonstrating how to [build a secure Azure reference architecture](https://www.hashicorp.com/blog/building-a-secure-azure-reference-architecture-with-terraform) and [deploy securely into Azure with HashiCorp Terraform, Vault, and Azure security tooling](https://www.hashicorp.com/blog/deploying-securely-into-azure-architecture-with-terraform-cloud-and-hcp-vault).

This installment looks at post-deployment operations as well as the management and control of the environment policies. We will use these services:

* [Microsoft Defender for Cloud](https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-cloud-introduction)
* [Azure ARC](https://azure.microsoft.com/en-us/products/azure-arc)
* [Azure Policy](https://azure.microsoft.com/en-us/products/azure-policy/?ef_id=_k_CjwKCAjwtuOlBhBREiwA7agf1t2oF7NjjZgSo6uAon4gdldGZex80O81kPPx9LIm8Ki5Xd2wh9eWtBoCw6wQAvD_BwE_k_&OCID=AIDcmm5edswduu_SEM__k_CjwKCAjwtuOlBhBREiwA7agf1t2oF7NjjZgSo6uAon4gdldGZex80O81kPPx9LIm8Ki5Xd2wh9eWtBoCw6wQAvD_BwE_k_&gad=1&gclid=CjwKCAjwtuOlBhBREiwA7agf1t2oF7NjjZgSo6uAon4gdldGZex80O81kPPx9LIm8Ki5Xd2wh9eWtBoCw6wQAvD_BwE)

#### Reference architecture

Similar to the previous posts, this post will use an [N-tier architecture](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/n-tier), since it is a common starting point for traditional on-premises applications migrating to Azure infrastructure. It is the same secure N-tier architecture built in the last post. 

The code for this architecture can be found in this [GitHub repository](https://github.com/dawright22/Secure-N-Tier-Arch-With-Defender.git).

![A](https://www.datocms-assets.com/2885/1681399105-image-1-n-tier-architecture.png)#### The building blocks

Building and deploying infrastructure is one side of the operational coin, maintaining and running it is the other. So far, this series has focused on building and deploying architecture. This post focuses on infrastructure maintenance, specifically additions, moves, and changes.

In the environment described above, we used some key services to build in the necessary security and control. The services used are Defender for Cloud and Azure ARC with Azure Policies. Azure Policies is the key element that ties these features together. 

Here’s a brief overview of these functions, highlighting how they rely on Azure Policies (for more detail, read part one in this series: [Building a secure Azure reference architecture with Terraform](https://www.hashicorp.com/blog/building-a-secure-azure-reference-architecture-with-terraform)): 

##### Microsoft Defender for Cloud

Azure Cloud Defender is a comprehensive security suite offered by Microsoft Azure. It provides advanced threat protection and security management capabilities for Azure resources. Microsoft Defender utilizes Azure Policies as part of its security and compliance management capabilities. Azure Policies can be used to enforce specific security rules and configurations across your Azure resources.

##### Azure ARC

Azure ARC is a service that extends Azure management capabilities to hybrid and multi-cloud environments. It enables you to manage and govern resources hosted outside of Azure, such as on-premises servers, edge devices, and other cloud platforms. Azure Arc also integrates with Azure Policy to enforce governance and compliance across these distributed resources. Check out the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/manage/hybrid/server/best-practices/aws-terraform-al2) to see how to deploy and link an AWS Linux EC2 instance into Azure Arc for management using Terraform.

##### Azure Policies

Azure Policies are a critical component of the Azure cloud computing platform, allowing users to enforce and govern compliance, security, and management requirements within their Azure environments. They provide a declarative approach to define and enforce rules and constraints on Azure resources, ensuring that the deployed resources meet specific organizational standards and regulatory requirements.

At a high level, Azure Policies are a set of rules defined in JSON format that are applied to Azure resources. These rules specify conditions and actions that are enforced on resources during their lifecycle. Azure Policies can be assigned at different scopes, including the management group, subscription, resource group, or individual resource level, allowing for granular control over resource deployments.

#### The challenge

Taking advantage of these tools provides benefits when first deploying into a greenfield environment. However, if you look closer at the policies deployed as part of the N-tier architecture, there could be issues for further deployments. In some scenarios, users encounter some [policy unexpected behaviors](https://techcommunity.microsoft.com/t5/azure-paas-blog/trigger-condition-and-evaluation-workflow-of-azure-policy/ba-p/3436597) because they do not understand policy workflow and design an incorrect custom policy definition.

By using the principle of a policy set definition, you can apply a collection of related policies that align with outcomes, such as the [Azure Security Benchmark (ASB)](https://learn.microsoft.com/en-us/security/benchmark/azure/overview). These policies cover security areas such as identity and access management, network security, data protection, encryption, logging and monitoring, virtual machine configurations, and more, all packaged together under the ASB policy initiative. Below is an example of how we apply this policy into our N-tier architecture.

```
resource "azurerm_subscription_policy_assignment" "asb_assignment" {
name = "${var.name}-azuresecuritybenchmark"
display_name = "Azure Security N-tier Benchmark"
policy_definition_id="/providers/Microsoft.Authorization/policySetDefinitions/1f3afdf9-d0c9-4c3d-847f-89da613e70a8"
subscription_id = data.azurerm_subscription.current.id
}
```
When the N-tier architecture enables this policy, Azure Defender automatically deploys the Qualys vulnerability assessment provider to all supported machines that don't already have it installed:

```
resource "azurerm_subscription_policy_assignment" "va-auto-provisioning" {
name = "${var.name}-va-autoprovisioning"
display_name = "Configure machines to receive a vulnerability assessment provider"
policy_definition_id = "/providers/Microsoft.Authorization/policyDefinitions/13ce0167-8ca6-4048-8e6b-f996402e3c1b"
subscription_id = data.azurerm_subscription.current.id
identity {
type = "SystemAssigned"
}
location = var.resource_group_location
parameters = <
```
Policies like these, once deployed, enforce the action they were designed to do. For example, as part of the ASB policy set, there is a [policy definition](https://www.azadvertizer.net/azpolicyadvertizer/ef619a2c-cc4d-4d03-b2ba-8c94a834d85b.html) that allows you to place your API management service in a non-internet routable network that you control access to. 

This restriction may be key to your overall security but could also stop new services from being deployed, particularly if the policy checks before all the necessary security rules are applied to your new API.

#### The solution

Let’s review the deployed solution. When looking at the policies used in the N-tier architecture deployment, you can see that there is a difference in the definitions: One is a policy and the other an initiative. To understand the difference between these two concepts, you can read this Microsoft blog post on [Azure Policy Initiatives vs Azure Policies: When should I use one over the other](https://techcommunity.microsoft.com/t5/itops-talk-blog/azure-policy-initiatives-vs-azure-policies-when-should-i-use-one/ba-p/1229167)? Basically, an initiative is a set of policies grouped together. You can also use a web-based tool like [AzAdvertizer](https://www.azadvertizer.net/index.html) to visualize the policies deployed.

By using Terraform you can create logic to add to your code to manipulate your policies. The code snippets below piece together the functions and their actions.

You need to add some basic parameters for the policy scope with which to limit the exemption. Use the resource name and the name context in the N-tier environment and pull the current subscription and resource group information from the name variable:

```
//variable for resource group
variable "resource_group_name" {
type = string
default = ""
}

//variable for name
variable "name" {
type = string
default = ""
}

data "azurerm_subscription" "current" {}

data "azurerm_resource_group" "rg" {
name = var.resource_group_name
}

data "azurerm_policy_assignment" "VApolicy" {
name = "${var.name}-va-autoprovisioning"
scope_id = data.azurerm_subscription.current.id
}
```
Now you have your scope, which defines what resources are affected by the policy. Then you can create a policy exception. 

While Azure policies are typically applied uniformly across an entire subscription or management group, exceptions can be configured to exclude certain resources from the policy's enforcement. As such, use this mechanism to create a time-based exception to allow the resource to be deployed:

```
resource "azurerm_resource_policy_exemption" "exemption1" {
name = "exemption1"
resource_id = data.azurerm_resource_group.rg.id
policy_assignment_id = data.azurerm_policy_assignment.VApolicy.id
exemption_category = "Waiver"
expires_on = time_offset.policy_update.rfc3339
}
```
To define the time period within the policy, use a HashiCorp [time provider](https://registry.terraform.io/providers/hashicorp/time/latest/docs), which allows you to easily define an offset time resource. An offset time resource keeps a UTC timestamp stored in the Terraform state. You can access this using the `time_offset`. The base value is the current time, which is then “offset” from the current time by the defined value in the offset. In this case it’s 10 minutes:

```
resource "time_offset" "policy_update" {
offset_minutes = 10
}
```
This new time [current time plus 10 minutes] is then added as an expiry date in your policy exception as `expires_on = time_offset.policy_update.rfc3339` and removes any resources from being exempt at this time. This window allows the deployment to happen and then return the policy back to its original state.

Put it all together and you have the following code, which could be added to your deployment to help automate your policy control:

```
provider "azurerm" {
features {}
}
//variable for resource group
variable "resource_group_name" {
type = string
default = ""
}

//variable for name
variable "name" {
type = string
default = ""
}

data "azurerm_subscription" "current" {}

data "azurerm_resource_group" "rg" {
name = var.resource_group_name
}

data "azurerm_policy_assignment" "AzureSecurityBenchmarkpolicy" {
name = "${var.name}-azuresecuritybenchmark"
scope_id = data.azurerm_subscription.current.id
}

data "azurerm_policy_assignment" "VApolicy" {
name = "${var.name}-va-autoprovisioning"
scope_id = data.azurerm_subscription.current.id
}

resource "time_offset" "policy_update" {
offset_minutes = 10
}

resource "azurerm_resource_policy_exemption" "exemption1" {
name = "exemption1"
resource_id = data.azurerm_resource_group.rg.id
policy_assignment_id = data.azurerm_policy_assignment.VApolicy.id
exemption_category = "Waiver"
expires_on = time_offset.policy_update.rfc3339
}

output "VApolicy-assignment" {
value = data.azurerm_policy_assignment.VApolicy.id
}

output "exemption1-id" {
value = azurerm_resource_policy_exemption.exemption1.id
}
```
#### Next steps

Incorporating security tools along with best practices into your infrastructure as code is essential for maintaining secure and reliable infrastructure. By doing so, organizations help ensure that their cloud deployments are secure, compliant, and easily maintainable. 

Be sure to also check out our video on [Securing your cloud with Terraform foundational policy library](https://www.youtube.com/watch?v=PMH516I8Pdk) and join Microsoft and HashiCorp for our ongoing webinar series: [Enforce Compliance with Azure Identity and HashiCorp Vault](https://www.hashicorp.com/campaign/security-webinar-series-with-hashicorp-and-microsoft-azure-north-america).

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/ghosted-by-arm-how-to-import-lost-azure-resources-into-terraform/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn-images-1.medium.com/proxy/1*TGH72Nnw24QL3iV9IOm4VA.png)

Provisioning resources through Terraform is generally smooth, but anyone who has worked extensively with any cloud provider knows that issues sometimes arise from unexpected places. When working with Azure, for instance, we can encounter cases where the response is either a “false negative” (the request was recorded as failed but actually succeeded) or where the Terraform provider simply timed out before the control plane (Azure Resource Manager, or ARM) responded.

This can be a significant problem when dealing with resources that take longer to provision. For example, creating a Virtual Hub as part of a Virtual WAN (V-WAN) setup in Azure. Provisioning a Virtual Hub can take considerable time, and if Terraform receives an erroneous “failure” response, it can leave the hub untracked in the Terraform state even though it’s fully operational in Azure. In this article, I’ll walk through how to use Terraform’s import block to efficiently solve this problem.

Let’s say we’re setting up a Virtual WAN using a V-WAN module in Terraform. Here’s the basic configuration for the module:

```
module "vwan" {  
  
  source  = "markti/azure-terraformer/azurerm//modules/network/vwan"  
  version = "1.0.19"  
  
  resource_group_name    = azurerm_resource_group.main.name  
  location               = azurerm_resource_group.main.location  
  name                   = "vwan-${var.application_name}"  
  primary_address_prefix = var.address_space  
  additional_regions     =…
```

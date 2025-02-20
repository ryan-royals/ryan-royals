---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/breaking-up-is-hard-to-do-from-nested-blocks-to-stand-alone-resources-with-azure-storage-network/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn-images-1.medium.com/proxy/1*TGH72Nnw24QL3iV9IOm4VA.png)

The Azure Storage Account resource has a nested block called `network_rules`. Often times when resources in the `azurerm` are first authored, there is one monolithic resource that has everything on one big resource type with a plethora of nested blocks.

As the provider matures over time these monolithic resource types start getting split up into sub-resource types that can be provisioned as stand-alone resources. Another good example of this is the `azurerm_virtual_network` resource which allows you to provision subnets using one or more `subnet` nested blocks — or stand-alone `azurerm_subnet` resource blocks.

One of the tricky parts about these dual modalities is that if both are used together Terraform would have a hard time figuring out which one takes priority. Therefore, when this situation manifests, the Terraform provider authors require you to make a choice. Either you use nested blocks on that monolithic root resource type or you exclusively use stand-alone resource blocks.

I stumbled across a (new to me) resource type called `azurerm_storage_account_network_rules` and was excited to try it out. I dutifully removed the nested block in my `azurerm_storage_account` and split it off into its own stand-alone resource block.

```
Error: A resource with the ID…
```

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-cloud-now-supports-multiple-configurations-for-dynamic-provider-credentials/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1620073839-blog-library-product-terraform-cloud-tfc-black-corner-iconography.jpg)

Earlier this year, we built upon the workload identity functionality in HashiCorp Terraform Cloud by adding a new authentication method, [dynamic provider credentials](https://www.hashicorp.com/blog/terraform-cloud-adds-dynamic-provider-credentials-vault-official-cloud-providers), for the [major cloud providers](https://registry.terraform.io/browse/providers), the HashiCorp Vault provider, and Vault’s [dynamic secrets engines](https://www.hashicorp.com/blog/terraform-cloud-adds-vault-backed-dynamic-credentials). This native support lets users authenticate to providers using short-lived, just-in-time credentials in their Terraform Cloud workflows. The enhancement helps users reduce the risk of exposure from storing long-lived static credentials and avoid the burden of manual secret rotation.

Terraform offers users the ability to define multiple configurations for the same provider on a per-resource or per-module basis with [aliases](https://developer.hashicorp.com/terraform/language/providers/configuration#alias-multiple-provider-configurations). However, with the previous dynamic provider credentials releases, users could configure only one set of credentials per provider and workspace. This limitation hindered users who had multiple aliases for the same provider, as they couldn't fully embrace the benefits of the new authentication functionality.

#### Introducing multiple configurations

Multiple configurations for dynamic provider credentials address this problem by allowing users to authenticate multiple aliases of the same provider within a single workspace when provisioning infrastructure. This can be especially useful when provisioning across multiple regions and accounts, or targeting multiple clusters within the same provider. 

Users can now configure workspaces with additional environment variables for a provider alias to authenticate with dynamic provider credentials. This allows them to:

* Use dynamic provider credentials to uniquely authenticate multiple aliases of the same provider in a workspace
* Configure separate cloud provider aliases with different roles/permissions in different accounts or regions

![Variables](https://www.datocms-assets.com/2885/1690735958-screenshot-2023-07-30-at-12-52-05-pm.png)#### Summary and resources

Dynamic credential management plays a key part in ensuring a secure provisioning workflow with Terraform and the providers it interacts with. To learn more about multiple configurations for dynamic provider credentials and how Terraform can help ensure security best practices in your provisioning workflows, please refer to the [Specifying multiple configurations](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/dynamic-provider-credentials/specifying-multiple-configurations) page in the dynamic provider credentials documentation.Environment variables assigned to a workspace enable dynamic provider credentials for multiple instances of the AWS provider with unique roles.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/enhancing-azure-deployments-with-azure-rm-and-az-api-terraform-providers/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1620082218-blog-library-product-terraform-azure-dark-logomark-lockup.jpg?w=1200&h=630&fit=crop&auto=format)

In addition to the AzureRM Terraform provider, Microsoft maintains another Terraform provider for Azure services: AzAPI, [which recently reached version 2.0](https://techcommunity.microsoft.com/t5/azure-tools-blog/announcing-azapi-2-0/ba-p/4275733).  With this new release, we collaborated with Microsoft to offer a comparison guide to help Terraform users decide which provider to use. This blog will look at the ideal scenarios for each provider with clear guidance, particularly those familiar with the AzureRM provider.

#### Comparing AzureRM and AzAPI Terraform providers

At a high level, AzureRM provides a stable, well-tested layer on top of Azure APIs. It handles the entire resource lifecycle — creation, updates, and deletion — while managing breaking changes, ensuring smooth operations. AzureRM is ideal for users looking for stability and simplified configuration management.

On the other hand, AzAPI is a lightweight wrapper around Azure APIs, enabling direct and early access to the latest Azure features. It allows for quicker adoption of new services or workarounds for AzureRM limitations, making it ideal for users who need the latest Azure services and functionality as fast as possible. The sections below look deeper into what these differences mean for you.

#### AzureRM: A proven, simplified approach

AzureRM abstracts complexity by managing Azure API versions on your behalf. The provider ensures that resources are fully compatible with one another and that configuration changes don't introduce breaking issues, thanks to its rigorous testing. If you're using resources that don't require constant updates or access to the latest API versions, AzureRM provides a more stable and simplified experience.

Key benefits of AzureRM:

* **Automatic API versioning:** AzureRM handles API version compatibility, making upgrades seamless.
* **Simplicity:** Resource property names are intuitive (e.g., `disk_size_in_gb` vs. `disk_size`), reducing the need to consult Azure API documentation frequently.
* **Comprehensive documentation:** AzureRM offers extensive resources and examples for each service, making it easier to onboard and use in your projects.

AzureRM is ideal for scenarios where you prioritize stability, want to minimize complexity, and don't need the very latest features.

#### AzAPI: Cutting-edge access to Azure APIs

AzAPI, by contrast, provides a thinner layer, allowing for direct access to the latest Azure API versions as soon as they're available. It's perfect for scenarios where you need quick access to preview features before they are fully supported in AzureRM.

Key benefits of AzAPI:

* **Immediate API access:** AzAPI gives users access to the latest API versions for Azure resources, allowing teams to use new Azure services and features sooner.
* **Targeted resource updates:** With the `azapi_update_resource` function, you can modify specific resource properties without upgrading the entire resource or provider.
* **Fine-grained control:** AzAPI's approach to resource versioning allows for more control over the infrastructure configuration, giving users the ability to choose API versions that best fit their needs.

AzAPI is recommended for scenarios where early access to new Azure features is crucial, or when you need granular control over resource versions.

#### Documentation and community support

AzureRM has a more extensive collection of blog posts, community contributions, and official documentation. This makes it easier for new users to find examples and ramp up quickly.

AzAPI, while newer, follows Azure's API structures more closely, making it easier for users familiar with Bicep or ARM templates to understand.

#### When to use each provider

**Choose AzureRM** if you prioritize stability, simplicity, and automatic versioning. It's best for teams that want to minimize the complexity of managing infrastructure and don't need immediate access to new Azure features.

**Choose AzAPI** if you need cutting-edge access to the latest Azure APIs or need to customize resource configurations without waiting for AzureRM to be updated. It's ideal for teams that require rapid innovation and fine-grained control over API versions.

Both providers provide a first-class experience, backed by Microsoft and HashiCorp, and can be adapted based on your needs. You can also transition between them seamlessly with tools like the upcoming Azure Terraform Migration tool release ([aztfmigrate](https://github.com/Azure/aztfmigrate)), making it easy to adjust your approach as your infrastructure evolves.

We hope this guide along with Microsoft's guide to [Unlocking the Best of Azure with AzureRM and AzAPI Providers](https://aka.ms/tf/providermessaging) helps you determine when to use AzureRM versus AzAPI, ensuring you get the most out of your Terraform and Azure infrastructure.

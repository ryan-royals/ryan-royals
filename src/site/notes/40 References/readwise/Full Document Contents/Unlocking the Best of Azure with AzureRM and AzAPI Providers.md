---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/unlocking-the-best-of-azure-with-azure-rm-and-az-api-providers/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/favicon.ico)

![play](https://techcommunity.microsoft.com/html/assets/TTS_reader_azure/images/listen-icon.svg)
With the recent release of AzAPI 2.0, Azure offers two powerful Terraform providers to meet your infrastructure needs: AzureRM and AzAPI. The key question is, when should you use each one? This article offers a clear guide for Terraform users, particularly those familiar with the AzureRM provider, on some ideal scenarios for each. The recommendations provided within this post are jointly provided between HashiCorp and Microsoft; [click here for HashiCorp's blogpost.](https://www.hashicorp.com/blog/enhancing-azure-deployments-with-azurerm-and-azapi-terraform-providers)

#### **Overview**

At a high level, AzureRM provides a stable, well-tested layer on top of Azure APIs. It handles the entire resource lifecycle—creation, updates, and deletion—while managing breaking changes, and ensuring smooth operations. AzureRM is ideal for users looking for stability and simplified configuration management.

On the other hand, AzAPI is a lightweight wrapper around Azure APIs, enabling direct and early access to the latest Azure features. It allows for quicker adoption of new services or workarounds for AzureRM limitations, making it ideal for users who need cutting-edge functionality. Below, we’ll dive into the differences between the two providers and when to use each.

#### **AzureRM: A Proven, Simplified Approach**

AzureRM abstracts complexity by managing Azure API versions on your behalf. The provider ensures that resources are fully compatible with one another and that configuration changes don’t introduce breaking issues, thanks to its rigorous testing. If you’re using resources that don’t require constant updates or access to the latest API versions, AzureRM provides a more stable and simplified experience.

Key benefits of AzureRM:

* **Automatic API Versioning**: AzureRM handles API version compatibility, making upgrades seamless.
* **Simplicity**: Resource property names are intuitive (e.g., disk\_size\_in\_gb vs. disk\_size), reducing the need to consult Azure API documentation frequently.
* **Comprehensive Documentation**: AzureRM offers extensive resources and examples for each service, making it easier to onboard and use in your projects.

AzureRM is ideal for scenarios where you prioritize stability, want to minimize complexity, and don’t need the very latest features.

#### **AzAPI: Cutting-Edge Features and Access to Azure APIs**

AzAPI, by contrast, provides a thinner layer, allowing for direct access to the latest Azure API versions as soon as they’re available. It’s well suited for scenarios where you need quick access to features before they are fully supported in AzureRM.

Key benefits of AzAPI:

* **Immediate API Access**: AzAPI gives users access to the latest API versions forAzure resources, allowing teams to use new Azure services and features sooner.
* **Targeted Resource Updates**: With the azapi\_update\_resource function, you can modify specific resource properties without upgrading the entire resource or provider.
* **Fine-Grained Control**: AzAPI provides resource versioning to allow for more control over the infrastructure configuration. User defined retryable errors, HTTP headers, URL control and resource replacement definitions are a few other ways AzAPI provides granular control.

AzAPI is recommended for scenarios where early access to new Azure features is crucial, or when you need granular control over your infrastructure.

#### **Documentation and Community Support**

AzureRM has a more extensive collection of blog posts, community contributions, and official documentation. This makes it easier for new users to find examples and ramp up quickly.

AzAPI, while newer, follows Azure’s API structures more closely, making it easier for users familiar with Bicep or ARM templates to understand.

#### **Conclusion: When to Use Each Provider**

**Choose AzureRM** if you prioritize **stability, simplicity**, and **automatic versioning**. It’s best for teams that want to minimize the complexity of managing infrastructure and don’t need immediate access to new Azure features.

**Choose AzAPI** if you need **cutting-edge access** to the latest Azure APIs or need to **customize resource configurations** without waiting for AzureRM to be updated. It’s ideal for teams that require rapid innovation and fine-grained control over API versions.

Both providers provide a first-class experience, backed by Microsoft and HashiCorp, and can be adapted based on your needs. You can also transition between them seamlessly with tools like the upcoming Azure Terraform Migration tool release ([aztfmigrate](https://github.com/Azure/aztfmigrate)), making it easy to adjust your approach as your infrastructure evolves.

We hope this guide helps you determine when to use AzureRM or AzAPI, ensuring you get the most out of your Terraform and Azure infrastructure.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-azure-rm-provider-4-0-adds-provider-defined-functions/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1620082218-blog-library-product-terraform-azure-dark-logomark-lockup.jpg?w=1200&h=630&fit=crop&auto=format)

Today, we are announcing the general availability of the HashiCorp [Terraform AzureRM provider 4.0](https://registry.terraform.io/providers/hashicorp/azurerm/latest). This version includes new capabilities to improve the extensibility and flexibility of the provider: provider-defined functions and improved resource provider registration. Initially launched in [April 2024](https://www.hashicorp.com/blog/terraform-1-8-improves-extensibility-with-provider-defined-functions), provider-defined functions allow anyone in the Terraform community to build custom functions within providers to extend the capabilities of Terraform.

This post reviews the details and benefits of this new major version of the provider and also covers a handful of new features released this year.

#### 2024 AzureRM provider highlights

Since the provider’s last major release in March 2022, we’ve added support for some 340 resources and 120 data sources, bringing the totals to more than 1,101 resources and almost 360 data sources as of mid-August, 2024. As the Terraform AzureRM provide[r](https://registry.terraform.io/providers/hashicorp/aws/latest/docs) download count tops 660 million, Microsoft and HashiCorp continue to develop new, innovative integrations that further ease the cloud adoption journey for enterprise organizations. This year we focused on improving the user experience for practitioners by adding new services to the AzureRM provider including:

* [Provider-defined functions](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#provider-functions)
* [Improved resource provider registration](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#improved-resource-provider-registration)
* [Additional properties for subnets in the virtual network resource](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#additional-properties-for-subnets-in-the-virtual-network-resource)

#### Provider-defined functions

With the release of [Terraform 1.8](https://www.hashicorp.com/blog/terraform-1-8-improves-extensibility-with-provider-defined-functions) in April, providers can implement custom functions that you can call from the Terraform configuration. The latest release of the Terraform AzureRM provider adds two Azure-specific provider functions to let users correct the casing of their resource IDs, or to access the individual components of it.

The `normalise_resource_id` function attempts to normalize the case-sensitive system segments of a resource ID as required by the Azure APIs:.

```
output "test" {
 value = provider::azurerm::normalise_resource_id("/Subscriptions/12345678-1234-9876-4563-123456789012/ResourceGroups/resGroup1/PROVIDERS/microsoft.apimanagement/service/service1/gateWays/gateway1/hostnameconfigurations/config1")
}

# Result: /subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.ApiManagement/service/service1/gateways/gateway1/hostnameConfigurations/config1

```

The `parse_resource_id` function takes an Azure resource ID and splits it into its component parts:

```
locals {
 parsed_id = provider::azurerm::parse_resource_id("/subscriptions/12345678-1234-9876-4563-123456789012/resourceGroups/resGroup1/providers/Microsoft.ApiManagement/service/service1/gateways/gateway1/hostnameConfigurations/config1")
}

output "resource_group_name" {
 value = local.parsed_id["resource_group_name"]
}

output "resource_name" {
 value = local.parsed_id["resource_name"]
}

# Result:
# Outputs:
# 
# resource_group_name = "resGroup1"
# resource_name = "config1"

```

#### Improved resource provider registration

Previously, the AzureRM provider took an all-or-nothing approach to Azure resource provider registration, where the Terraform provider would either attempt to register a fixed set of 68 providers upon initialization or registration could be skipped entirely by setting `skip_provider_registration = true` in the provider block. This limitation didn’t match Microsoft’s recommendations, which is to register resource providers only as needed to enable the services you’re actively using. With the addition of two new feature flags, [resource\_provider\_registrations](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#resource_provider_registrations) and [resource\_providers\_to\_register](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#resource_providers_to_register), users now have more control over which providers to automatically register or whether to continue managing a subscription’s resource provider registrations outside of Terraform.

#### Changes and deprecations

Since the last major release, the AzureRM provider has accumulated resources and properties that have been deprecated, renamed, or are no longer supported by Azure. As version 4.0 is a major release, we have removed a number of [resources](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#behaviour-changes-and-removed-properties-in-resources) and [data sources](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#behaviour-changes-and-removed-properties-in-data-sources) that have been deprecated over the course of the provider’s lifetime. A complete list of behavior changes and removed properties can be found in the [AzureRM provider 4.0 upgrade guide](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide#behaviour-changes-and-removed-properties-in-resources).

#### Learn more about Microsoft and HashiCorp

The latest version of the AzureRM provider is available today. These features and enhancements will help simplify configurations and improve the overall experience of using the provider. Because this release introduces breaking changes, we recommend pinning your provider version to protect against unexpected results. For a complete list of the changes in 4.0, please review the [AzureRM provider upgrade guide](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide).

Please share any bugs or enhancement requests with us via [GitHub issues](https://github.com/hashicorp/terraform-provider-azurerm/issues). We are thankful to our partners and community members for their valuable contributions to the HashiCorp Terraform ecosystem.

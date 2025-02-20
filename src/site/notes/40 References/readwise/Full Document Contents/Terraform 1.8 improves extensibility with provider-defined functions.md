---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-1-8-improves-extensibility-with-provider-defined-functions/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1712694043-share-terraform-1-8-improves-extensibility-with-provider-defined-functions.png?w=1200&h=630&fit=crop&auto=format)

Today, we are announcing the general availability of HashiCorp Terraform 1.8, which is [ready for download](https://developer.hashicorp.com/terraform/downloads) and immediately available for use in [Terraform Cloud](https://www.hashicorp.com/products/terraform). This version includes two new capabilities to improve the extensibility and flexibility of Terraform: provider-defined functions and refactoring across resource types.

#### Provider-defined functions

Terraform includes a wide selection of [built-in functions](https://developer.hashicorp.com/terraform/language/functions) to perform many common operations during provisioning. While they address many general use cases, there have been many requests from the community for more specialized functions and custom logic. With Terraform 1.8, we are excited to introduce *provider-defined functions*, which allow anyone in the community and HashiCorp’s partner ecosystem to extend the capabilities of Terraform.

Provider-defined functions can be used in any Terraform expression, including input validation conditions, output values, local values, data sources, and resource blocks. Additionally, provider-defined functions can be used with [checks](https://developer.hashicorp.com/terraform/language/checks) and [tests](https://developer.hashicorp.com/terraform/language/tests), which commonly require more complex business logic to write custom assertions that address unique validation scenarios. Provider-defined functions are invoked with the syntax `provider::::([arguments])`. Examples of available functions include [`rfc_3339_parse`](https://registry.terraform.io/providers/hashicorp/time/latest/docs/functions/rfc3339_parse) in v0.11 of the official `time` provider and [`direxists`](https://registry.terraform.io/providers/hashicorp/local/latest/docs/functions/direxists) in v2.5 of the `local` provider.

An initial set of functions are now available in the [AWS](https://registry.terraform.io/providers/hashicorp/aws/latest), [Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest), and [Kubernetes](https://registry.terraform.io/providers/hashicorp/kubernetes/latest) providers. For more details and examples, check out [Terraform 1.8 provider functions for AWS, Google Cloud, and Kubernetes](https://www.hashicorp.com/blog/terraform-1-8-adds-provider-functions-for-aws-google-cloud-and-kubernetes). The latest version of the [HashiCorp Terraform extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform) also includes syntax highlighting and auto-completion support for provider-defined functions.

![The](https://www.datocms-assets.com/2885/1712694133-editor-screenshot.png)To learn how to develop your own provider-defined functions, refer to the [Functions section of the Terraform Plugin Framework documentation](https://developer.hashicorp.com/terraform/plugin/framework/functions) and try it yourself with the new [Implement a function tutorial](https://developer.hashicorp.com/terraform/tutorials/providers-plugin-framework/providers-plugin-framework-functions), part of the [Custom framework providers collection](https://developer.hashicorp.com/terraform/tutorials/providers-plugin-framework).

#### Refactor across resource types

Refactoring code is a common practice for Terraform authors, whether it’s to break up a large configuration into multiple modules or simply to rename resources. Terraform provides two mechanisms to support refactoring operations while preserving the state of existing resources: the `moved` block introduced in Terraform 1.1 and the `terraform state mv` command. But there is another class of refactoring that involves changing the type of a resource. Changing the resource type previously required a multi-step operation to manually remove the resource from state without destroying it, update the code, and then re-import to the new resource type.

In Terraform 1.8, supported resources can be moved between resource types with a new, faster, and less error-prone method. Some use cases for this method include:

* Renaming a provider after an acquisition or rebrand
* Splitting a resource into more specific types
* API changes such as service renames or versioned resources
* Cross-provider moves

Providers can add support for this capability by declaring which resources can be refactored between types. An example `moved` block might look like this:

```
# Old resource type (commented out)
# resource "myprovider_old_resource_type" "example" {
#   # resource attributes...
# }

# New resource type
resource "myprovider_new_resource_type" "example" {
  # resource attributes...
}

moved {
  from = myprovider_old_resource_type.example
  to   = myprovider_new_resource_type.example
}

```
#### Get started with Terraform 1.8

To learn more about these features and all of the enhancements in Terraform 1.8, review the full [Terraform 1.8 changelog](https://github.com/hashicorp/terraform/releases/tag/v1.8.0). To get started with HashiCorp Terraform:

* [Download Terraform 1.8](https://developer.hashicorp.com/terraform/downloads)
* [Sign up for a free Terraform Cloud account](https://app.terraform.io/public/signup/account)
* Read the [Terraform 1.8 upgrade guide](https://developer.hashicorp.com/terraform/language/v1.8.x/upgrade-guides)
* Get hands-on with tutorials at [HashiCorp Developer](https://developer.hashicorp.com/terraform/tutorials)

As always, this release wouldn't have been possible without the great community feedback we've received via GitHub issues and from our customers. Thank you!

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-cloud-private-registry/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)

The Terraform Registry at [registry.terraform.io](https://registry.terraform.io) is public, but many organizations use modules, providers, or Sentinel policies that cannot or do not need to be publicly available.

You can load private modules [directly from version control and other sources](https://developer.hashicorp.com/terraform/language/modules/sources), but those methods do not support [version constraints](https://developer.hashicorp.com/terraform/language/modules/syntax#version) or a browsable marketplace, both of which are important for enabling a producers-and-consumers content model in a large organization. You will benefit from a private registry if your teams need access to a common set of providers, modules, or policies.

[Terraform Cloud](https://www.hashicorp.com/products/terraform) includes a [private registry](https://developer.hashicorp.com/terraform/cloud-docs/registry) that is available to all accounts, including free organizations. Unlike the public registry, the private registry can import modules and providers from your private VCS repositories on any of Terraform Cloud's supported VCS providers. It also lets you upload and manage private, custom providers through the Terraform Cloud API and curate a list of commonly-used public providers and modules.

You can seamlessly [reference private modules and providers](https://developer.hashicorp.com/terraform/cloud-docs/registry/using) in your Terraform configurations, and the Terraform Cloud UI provides a searchable marketplace to help users find the components they need.

#### Other Private Registries

Terraform can use versioned modules from any service that implements [the registry API](https://developer.hashicorp.com/terraform/registry/api-docs). The Terraform open source project does not provide a server implementation, but we welcome community members to create their own private registries by following the published protocol.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/simplifying-assertions-in-terraform-using-provider-defined-functions/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1714171194-blog-library-product-terraform-black.jpg?w=1200&h=630&fit=crop&auto=format)

Continuously validating your HashiCorp Terraform configurations greatly improves the user experience for those managing infrastructure. Continuous validation helps you deploy predictable and reliable infrastructure and provides direct feedback after changes are made. For instance, verifying if a website returns the expected status code post-deployment or the validity of a certificate after each run allows for early issue identification and resolution, minimizing impact and maintaining the integrity of a system.

This post explores strategies for assertions and validations using a custom Terraform provider. By implementing these assertions and validations, you can `terraform apply` with greater confidence, which helps ensure your infrastructure meets your criteria, follows best practices, and reduces the risk of misconfigurations.

#### Terraform Assert provider

The [Assert provider](https://registry.terraform.io/providers/bschaatsbergen/assert/latest) for Terraform, a provider managed by the community, offers a rich set of assertion capabilities through provider-defined functions such as `http_success()`, `expired()`, and `between()`. These assertion functions simplify your Terraform configurations, making it easier to do variable validation, continuous validation, and testing.

The Assert provider functions complement Terraform’s [built-in functions](https://developer.hashicorp.com/terraform/language/functions) rather than replacing them. If Terraform’s built-in functions better fit your requirements, they should be your choice.

To use the Assert provider, declare it as a `required_provider` in the `terraform {}` block:

```
terraform {
  required_version = ">= 1.8.0"
  required_providers {
    assert = {
      source  = "bschaatsbergen/assert"
      version = "0.9.3"
    }
  }
}
```
You use the functions with a special syntax: `provider::assert::`. For instance, to check if an HTTP status code falls within the success range, use the `http_success` function and call it using `provider::assert::http_success(data.http.example.status_code)`.

Let's see how to use these functions to validate input variables.

#### Input variable validation

Terraform variables can have their default values overridden using CLI flags, `.tfvars` files, and environment variables. To ensure that any set value is within a required range of values, you can specify custom validation rules for a particular variable by adding a `validation` block within a `variable`. The `validation` block requires you to set a `condition` argument, which produces an error message If the condition evaluates to `false`. 

Using the Assert provider, the example below validates whether the value passed to the disk volume size variable is between 20GB and 40GB.

```
variable "disk_volume_size" {
  type = number
  validation {
    condition     = provider::assert::between(20, 40, var.disk_volume_size)
    error_message = "Disk volume size must be between 20 and 40 GB"
  }
}
```
Without the Terraform Assert provider, you would need to create an "or" condition that references the `disk_volume_size` variable twice. While the condition validates the same criteria, it uses a less intuitive and readable expression:

```
condition = var.disk_volume_size >= 20 || var.disk_volume_size <= 40
```
You can also use the `cidr` function to validate whether the provided value is a valid CIDR range:

```
variable "subnet_a" {
  type = string
  validation {
    condition     = provider::assert::cidr(var.subnet_a)
    error_message = "Invalid CIDR range"
  }
}
```
Use the `key` or `value` functions to verify if a key or value is present in a map:

```
variable "tags" {
  type = map(string)
  validation {
    condition     = provider::assert::key("key1", var.tags)
    error_message = "Map must contain the key 'key1'"
  }
}
```
The Assert provider offers [a wide range of functions](https://registry.terraform.io/providers/bschaatsbergen/assert/latest/docs) to help with variable validation, including numeric, IP, CIDR, JSON, YAML, Boolean, map, list, and string functions.

The recent [Terraform 1.9 release](https://www.hashicorp.com/blog/terraform-1-9-enhances-input-variable-validations) includes enhanced input variable validation, allowing cross-object references. Previously, input validation conditions could reference only the variable itself. With Terraform 1.9, conditions can now reference other input variables, data sources, and local values. This significantly expands what authors can validate and allows for even more flexibility when using the Assert provider.

Now that you have learned how to validate variables, let's investigate other Terraform features that can make your configuration more robust.

#### Custom conditions prevent problems

Besides input variable validation, Terraform supports several other custom conditions that are useful for asserting configurations, such as checks, preconditions, and postconditions.

##### Checks

[Checks](https://developer.hashicorp.com/terraform/language/checks) let you define custom conditions executed during every Terraform plan or apply, without impacting the overall status of the operation. They run as the final step of a plan or apply, after Terraform has planned or provisioned your infrastructure. Think of checks as a post-deployment monitoring capability.

Using the Assert provider, here’s an example of how to verify if a website returns a successful status code:

```
data "http" "terraform_io" {
  url = "https://www.terraform.io"
}

check "terraform_io_success" {
  assert {
    condition     = provider::assert::http_success(data.http.terraform_io.status_code)
    error_message = "${data.http.terraform_io.url} returned an unhealthy status code"
  }
}
```
Without the Assert provider, you’d have to manually maintain a list of hard-coded success status codes, which reduces readability and maintainability.

##### Preconditions and postconditions

Another type of custom condition is a [precondition or postcondition](https://developer.hashicorp.com/terraform/language/checks#resource-preconditions-and-postconditions). These function similarly to check blocks, but differ in their timing of execution: a precondition runs before a resource change is applied or planned, while a postcondition runs after. If either a precondition or postcondition fails, it blocks Terraform from executing the current operation. (If a `check` fails it does not prevent Terraform from executing an operation.)

```
data "http" "terraform_io" {
  url = "https://www.terraform.io"

  lifecycle {
    postcondition {
      condition = provider::assert::http_success(self.status_code)
      error_message = "${self.url} returned an unhealthy status code"
    }
  }
}
```
Checks and validation help you improve the runtime quality of your Terraform configuration. Here are some techniques to improve the long-term health of your configuration.

#### Continuous validation in HCP Terraform

HCP Terraform features continuous validation, a form of [health assessment](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health), allowing HCP Terraform to proactively monitor if a workspace’s configuration or modules with assertions are passing, and notify you if any assertions fail. Continuous validation evaluates preconditions, postconditions, and check blocks as part of a health assessment. We recommend using [check blocks](https://developer.hashicorp.com/terraform/language/checks) for post-apply monitoring.

The example below shows a typical use of continuous validation to detect certificate renewals before they expire. The `expired` function within the Assert provider requires an RFC3339 timestamp as its input.

```
resource "aws_acm_certificate" "example" {
  domain_name       = "example.com"
  validation_method = "DNS"

  lifecycle {
    create_before_destroy = true
  }
}

check "example_certificate_renewal" {
  assert {
    # Add 336 hours (14 days) to the expiration time, making sure we have enough time to renew the certificate
    condition     = !provider::assert::expired(timeadd(aws_acm_certificate.example.not_after, "336h"))
    error_message = "Example certificate needs to be renewed"
  }
}
```
Health assessments can be enabled for [individual workspaces](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health#enable-health-assessments) or [organization-wide](https://developer.hashicorp.com/terraform/cloud-docs/users-teams-organizations/organizations#health). To view health assessment results, including drift detection and continuous validation, go to the “Health” tab in an HCP Terraform workspace.

If you use the [HCP Terraform and Terraform Enterprise provider](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs) to manage workspace configurations, you can enable health assessments using the `assessments_enabled` argument in the [`tfe_workspace`](https://registry.terraform.io/providers/hashicorp/tfe/latest/docs/resources/workspace#assessments_enabled) resource:

```
resource "tfe_workspace" "example" {
  name                = "example"
  assessments_enabled = true

  # ... other workspace attributes
}
```
Finally, let's see how the assert provider can help simplify the process of testing Terraform modules.

#### Terraform test

The Terraform test framework allows you to ensure that Terraform configuration updates do not introduce breaking changes. By default, tests in Terraform create real infrastructure, so you can run assertions against this short-lived, test-specific infrastructure.

```
run "health_check" {
  command = apply

  assert {
    condition     = provider::assert::http_success(data.http.index.status_code)
    error_message = "${data.http.index.url} returned an unhealthy status code"
  }
}
```
Note, you can configure Terraform to not create new infrastructure by setting the `command` argument to `plan`, which lets you validate logical operations and custom conditions without deploying resources.

```
run "ebs_volume_size" {
  command = plan

  assert {
    condition     = provider::assert::between(1, 100, aws_ebs_volume.example.size)
    error_message = "EBS volume size must be between 1 and 100 GiB"
  }
}
```
Validation methods in Terraform, such as variable validation, preconditions, postconditions, and check blocks ensure the correctness and integrity of a Terraform configuration by enforcing custom conditions. For example, variable validation might prevent specifying an invalid subnet CIDR block. 

On the other hand, tests in Terraform validate the behavior and logic of the configuration, ensuring the deployed infrastructure behaves as expected.

#### Getting started with the Terraform Assert provider

The Terraform Assert provider, now available on the Terraform Registry, simplifies writing assertions, improving the reliability and integrity of your infrastructure deployments.

To learn more about the Terraform Assert provider, check out these resources:

* [Terraform Registry documentation](https://registry.terraform.io/providers/bschaatsbergen/assert/latest/docs)
* [GitHub repository](https://github.com/bschaatsbergen/terraform-provider-assert)

You can also read our [Terraform 1.8 provider-defined functions release blog post](https://www.hashicorp.com/blog/terraform-1-8-improves-extensibility-with-provider-defined-functions) to learn more about provider-defined functions. And, to learn how to leverage Terraform’s testing framework to write effective tests, see [Write Terraform tests](https://developer.hashicorp.com/terraform/tutorials/configuration-language/test) on the HashiCorp Developer site.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-1-9-enhances-input-variable-validations/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1714171194-blog-library-product-terraform-black.jpg?w=1200&h=630&fit=crop&auto=format)

Terraform 1.9 is now generally available, bringing enhancements to input variable validations, a new string templating function, and more.

HashiCorp Terraform 1.9 is now generally available, [ready for download](https://developer.hashicorp.com/terraform/downloads), and immediately available for use in [HCP Terraform](https://www.hashicorp.com/products/terraform). Terraform 1.9 includes several new features that have been highly requested by the Terraform community, along with a number of improvements to existing capabilities to enhance developer productivity.

#### Cross-object referencing for input variable validations

[Input variable validations](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#input-variable-validation), first introduced in Terraform 0.13, ensure that input variable values meet specific requirements before execution. This reduces the likelihood of provisioning errors and misconfigurations caused by invalid or unexpected user input and lets Terraform authors create more reliable code while providing clear feedback to users through custom error messages.

Previously, the condition block of an input validation could refer only to the variable itself. With Terraform 1.9, conditions can now refer to other input variables and even to other objects, such as data sources and local values, greatly expanding the kinds of scenarios that authors can validate.

The following example demonstrates a variable validation condition referencing the value of a different variable. Previously, this scenario would require a precondition block on a data source or resource later in the configuration, potentially leading to a partially completed deployment:

```
variable "create_cluster" {
  description = "Whether to create a new cluster."
  type        = bool
  default     = false
}

variable "cluster_endpoint" {
  description = "Endpoint of the existing cluster to use."
  type        = string
  default     = ""

  validation {
    condition     = var.create_cluster == false ? length(var.cluster_endpoint) > 0 : true
    error_message = "You must specify a value for cluster_endpoint if create_cluster is false."
  }
}

```

If a user attempts to execute this Terraform configuration with `create_cluster = false` and without providing a value for `cluster_endpoint`, they will encounter a validation error:

```
# terraform plan

Planning failed. Terraform encountered an error while generating this plan.

╷
│ Error: Invalid value for variable
│
│   on variables.tf line 7:
│    7: variable "cluster_endpoint" {
│     ├────────────────
│     │ var.cluster_endpoint is ""
│     │ var.create_cluster is false
│
│ You must specify a value for cluster_endpoint if create_cluster is false.
│
│ This was checked by the validation rule at variables.tf:12,3-13.

```

In the next example, a data source is used to dynamically validate the instance type supplied by a user:

```
data "aws_ec2_instance_types" "valid" {
  filter {
    name   = "current-generation"
    values = ["true"]
  }

  filter {
    name   = "processor-info.supported-architecture"
    values = ["arm64"]
  }
}

variable "instance_type" {
  description = "The EC2 instance type to provision."
  type        = string

  validation {
    condition     = contains(data.aws_ec2_instance_types.valid.instance_types, var.instance_type)
    error_message = "You must select a current-generation ARM64 instance type."
  }
}

```

This powerful new feature unlocks many new and dynamic input validation possibilities for Terraform authors to make provisioning workflows more reliable.

#### New templatestring function

Terraform 1.9 also brings a new built-in [`templatestring`](https://developer.hashicorp.com/terraform/language/functions/templatestring) function. Similar to the existing [`templatefile`](https://developer.hashicorp.com/terraform/language/functions/templatefile) function, `templatestring` is designed to render templates obtained dynamically, like from a data source result, without having to save it to a file on the local disk. The function takes two parameters: a direct reference to a named string object in the current module, and an object representing the templated variables to interpolate.

The most common use case for this function is to retrieve a template from an external location using a data source, transform it, and pass it to another resource. This example retrieves a Kubernetes resource manifest template from an HTTP location, injects some input variables and resource references, and references it in a `kubernetes_manifest` resource:

```
data "http" "manifest" {
  url = "https://git.democorp.example/repocontent/k8s-templates/ingress-template.yaml"
}

locals {
  manifest_final = templatestring(data.http.manifest.response_body, {
    APP_NAME       = var.app_name
    NAMESPACE      = kubernetes_namespace_v1.example.metadata.0.name
    SERVICE_NAME   = kubernetes_service_v1.example.metadata.0.name
    CONTAINER_PORT = var.container_port
  })
}

resource "kubernetes_manifest" "example" {
  manifest = local.manifest_final
}

```

#### Other improvements and next steps

Terraform 1.9 also brings improvements to existing features:

* Building on the cross-type refactoring feature [introduced in Terraform 1.8](https://www.hashicorp.com/blog/terraform-1-8-improves-extensibility-with-provider-defined-functions#refactor-across-resource-types), the deprecated `null_resource` type in the [hashicorp/null provider](https://registry.terraform.io/providers/hashicorp/null/latest) can now be refactored directly to the new [`terraform_data` resource type](https://developer.hashicorp.com/terraform/language/resources/terraform-data) using [`moved` blocks](https://developer.hashicorp.com/terraform/language/moved), allowing authors to seamlessly modernize their code.
* `removed` blocks can now declare provisioners that will be executed when the associated resource instances are destroyed. This is useful in cases where you want to remove the resource declaration from your configuration, but still execute the destroy-time provisioner. For example uses, see the [Removing Resources documentation](https://developer.hashicorp.com/terraform/language/resources/syntax#removing-resources).

To learn more about all of the enhancements in Terraform 1.9, review the full [Terraform 1.9 changelog](https://github.com/hashicorp/terraform/releases/tag/v1.9.0). To get started with HashiCorp Terraform:

* [Download Terraform 1.9](https://developer.hashicorp.com/terraform/downloads)
* [Sign up for a free HCP Terraform account](https://app.terraform.io/public/signup/account)
* Read the [Terraform 1.9 upgrade guide](https://developer.hashicorp.com/terraform/language/v1.9.x/upgrade-guides)
* Get hands-on with tutorials at [HashiCorp Developer](https://developer.hashicorp.com/terraform/tutorials)

As always, this release wouldn't have been possible without the great community feedback we've received via GitHub issues, HashiCorp Discuss forums, and from our customers. Thank you!

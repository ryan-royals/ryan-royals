---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-1-8-provider-functions-for-aws-google-cloud-and-kubernetes/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1712695692-share-terraform-1-8-adds-provider-functions-for-aws-google-cloud-and-kubernetes.png?w=1200&h=630&fit=crop&auto=format)

Today, we are announcing the general availability of [provider-defined functions](https://developer.hashicorp.com/terraform/plugin/framework/functions/concepts) in the AWS, Google Cloud, and Kubernetes providers in conjunction with the [HashiCorp Terraform 1.8](https://www.hashicorp.com/blog/terraform-1-8-improves-extensibility-with-provider-defined-functions) launch. This release represents yet another step forward in our unique approach to ecosystem extensibility. Provider-defined functions will allow anyone in the Terraform community to build custom functions within providers and extend the capabilities of Terraform.

#### Introducing provider-defined functions

Previously, users relied on a handful of [built-in functions](https://developer.hashicorp.com/terraform/language/functions) in the Terraform configuration language to perform a variety of tasks, including numeric calculations, string manipulations, collection transformations, validations, and other operations. However, the Terraform community needed more capabilities than the built-in functions could offer. With the release of Terraform 1.8, providers can implement custom functions that you can call from the Terraform configuration. The schema for a function is defined within the provider's schema using the Terraform provider plugin framework.

To use a function, declare the provider as a required\_provider in the `terraform{}` block:

```
terraform {
  required_version = ">= 1.8.0"
  required_providers {
    time = {
      source  = "hashicorp/local"
      version = "2.5.1"
    }
  }
}
```
Provider-defined functions can perform multiple tasks, including:

* Transforming existing data
* Parsing combined data into individual, referenceable components
* Building combined data from individual components
* Simplifying validations and assertions

To access a provider-defined function, reference the `provider::` namespace with the local name of the Terraform Provider. For example, you can use the `direxists` function by including `provider::local::direxists()` in your Terraform configuration.

Below you’ll find several examples of new provider-defined functions in the officially supported AWS, Google Cloud, and Kubernetes providers.

#### Terraform AWS provider

The [5.40](https://github.com/hashicorp/terraform-provider-aws/releases/tag/v5.40.0) release of the [Terraform AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest) includes its first provider-defined functions to parse and build Amazon Resource Names (ARNs), simplifying Terraform configurations where ARN manipulation is required. The [`arn_parse`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/functions/arn_parse) provider-defined function is used to parse an ARN and return an object of individual referenceable components, such as a region or account identifier. For example, to get the AWS account ID from an [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/) repository, use the `arn_parse` function to retrieve the account ID and set it as an output:

```
# create an ECR repository
resource "aws_ecr_repository" "hashicups" {
  name = "hashicups"
  
  image_scanning_configuration {
    scan_on_push = true
  }
}

# output the account ID of the ECR repository
output "hashicups_ecr_repository_account_id" {
  value = provider::aws::arn_parse(aws_ecr_repository.hashicups.arn).account_id
}

```
Running `terraform apply` against the above configuration outputs the AWS Account ID:

```
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.

Outputs:

hashicups_ecr_repository_account_id = "751192555662"

```

Without the `arn_parse` function, you would need to define and test a combination of built-in Terraform functions to split the ARN and reference the proper index or define a regular expression to match on a substring. The function handles the parsing for you in a concise manner so that you do not have to worry about doing this yourself.

The AWS provider also includes a new [`arn_build`](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/functions/arn_build) function that builds an ARN from individual attributes and returns it as a string. This provider-defined function can create an ARN that you cannot reference from another resource. For example, you may want to allow another account to pull images from your ECR repository. The `arn_build` function below constructs an ARN for an IAM policy using an account ID: 

```
# allow another account to pull from the ECR repository
data "aws_iam_policy_document" "cross_account_pull_ecr" {
  statement {
    sid    = "AllowCrossAccountPull"
    effect = "Allow"

    principals {
      type = "AWS"

      identifiers = [
        provider::aws::arn_build("aws", "iam", "", var.cross_account_id, "root"),
      ]
    }

    actions = [
      "ecr:BatchGetImage",
      "ecr:GetDownloadUrlForLayer",
    ]
  }
}
```
The `arn_build` function helps to guide and simplify the process of combining substrings to form an ARN, and it improves readability compared to using string interpolation. Without it, you'd have to look up the exact ARN structure in the AWS documentation and manually test it.

#### Terraform Google Cloud provider

The [5.23](https://github.com/hashicorp/terraform-provider-google/blob/main/CHANGELOG.md#5230-apr-1-2024) release of the [Terraform Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) adds a simplified way to get regions, zones, names, and projects from the IDs of resources that aren’t managed by your Terraform configuration. Provider-defined functions can now help parse Google IDs when adding an IAM binding to a resource that’s managed outside of Terraform:

```
resource "google_cloud_run_service_iam_member" "example_run_invoker_jane" {
  member   = "user:jane@example.com"
  role     = "run.invoker"
  service  = provider::google::name_from_id(var.example_cloud_run_service_id)
  location = provider::google::location_from_id(var.example_cloud_run_service_id)
  project  = provider::google::project_from_id(var.example_cloud_run_service_id)
}
```
The Google Cloud provider also includes a new `region_from_zone` provider-defined function that helps obtain region names from a given zone (e.g. “us-west1” from “us-west1-a”). This simple string processing could be achieved in multiple ways using Terraform’s built-in functions previously, but the new function simplifies the process:

```
locals {
  zone = “us-central1-a”
  
  # ways to derive the region “us-central1” using built-in functions
  region_1 = join("-", slice(split("-", local.zone), 0, 2))
  region_2 = substr(local.zone, 0, length(local.zone)-2)

  # our new region_from_zone function makes this easier!
  region_3 = provider::google::region_from_zone(local.zone)
}
```
#### Terraform Kubernetes provider

The 2.28 release of the [Terraform Kubernetes provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs) includes provider-defined functions for encoding and decoding Kubernetes manifests into Terraform, making it easier for practitioners to work with the [`kubernetes_manifest`](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/manifest) resource.

Users that have a Kubernetes manifest in YAML format can use the `manifest_decode` function to convert it into a Terraform object. The example below shows how to use the `manifest_decode` function by referring to a Kubernetes manifest in YAML format embedded in the Terraform configuration:

```
locals {
  manifest = <
```
If you prefer to decode a YAML file instead of using an embedded YAML format, you can do so by combining the built-in `file` function with the `manifest_decode` function.

```
$ cat manifest.yaml
---
kind: Namespace
apiVersion: v1
metadata:
  name: test
  labels:
    name: test
```

```
resource "kubernetes_manifest" "example" {
  manifest = provider::kubernetes::manifest_decode(file("${path.module}/manifest.yaml"))
}
```
If your manifest YAML contains multiple Kubernetes resources, you may use the manifest*decode*multi function to decode them into a list which can then be used with the `for_each` attribute on the `kubernetes_manifest` resource:

```
$ cat manifest.yaml
---
kind: Namespace
apiVersion: v1
metadata:
  name: test-1
  labels:
    name: test-1
---
kind: Namespace
apiVersion: v1
metadata:
  name: test-2
  labels:
    name: test-2

```

```
resource "kubernetes_manifest" "example" {
  for_each = {
    for m in provider::kubernetes::manifest_decode_multi(file("${path.module}/manifest.yaml"))):
    m.metadata.name => m
  }
  manifest = each.value
}
```
#### Getting started with provider-defined functions

Provider-defined functions allow Terraform configurations to become more expressive and readable by declaring practitioner intent and reducing complex, repetitive expressions. To learn about all of the new launch-day provider-defined functions, please review the documentation and changelogs of the aforementioned providers:

* [Terraform AWS provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
* [Terraform Google provider](https://registry.terraform.io/providers/hashicorp/google/latest)
* [Terraform Kubernetes provider](https://registry.terraform.io/providers/hashicorp/kubernetes/latest)

Review our [Terraform Plugin Framework documentation](https://developer.hashicorp.com/terraform/plugin/framework/functions) to learn more about how provider-defined functions work and how you can make your own. We are thankful to our partners and community members for their valuable contributions to the HashiCorp Terraform ecosystem.

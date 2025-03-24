---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/testing-hashi-corp-terraform/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1705080764-share-testing-hashicorp-terraform.png?w=1200&h=630&fit=crop&auto=format)

Learn testing strategies for Terraform modules and configuration, and learn how to run tests against infrastructure.

How do you know if you can run `terraform apply` to your infrastructure without negatively affecting critical business applications? You can run `terraform validate` and `terraform plan` to check your configuration, but will that be enough? Whether you’ve updated some HashiCorp Terraform configuration or a new version of a [module](https://developer.hashicorp.com/terraform/tutorials/modules/module?utm_offer=ARTICLE_PAGE&utm_source=WEBSITE&utm_medium=WEB_BLOG), you want to catch errors quickly before you apply any changes to production infrastructure.

In this post, I’ll discuss some testing strategies for HashiCorp Terraform configuration and modules so that you can `terraform apply` with greater confidence. As a HashiCorp Developer Advocate, I’ve compiled some advice to help Terraform users learn how infrastructure tests fit into their organization’s development practices, the differences in testing modules versus configuration, and approaches to manage the cost of testing.

I included a few testing examples with [Terraform’s native testing framework](https://developer.hashicorp.com/terraform/cli/test). No matter which tool you use, you can generalize the approaches outlined in this post to your overall infrastructure testing strategy. In addition to the testing tools and approaches in this post, you can find other perspectives and examples in the references at the end.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#the-testing-pyramid)The testing pyramid

In theory, you might decide to align your infrastructure testing strategy with the test pyramid, which groups tests by type, scope, and granularity. The testing pyramid suggests that engineers write fewer tests in the categories at the top of the pyramid, and more tests in the categories at the bottom. Higher-level tests in the pyramid take more time to run and cost more due to the higher number of resources you have to configure and create.

![Test pyramid for infrastructure testing](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1614617558-terraformtestingpyramid.png&w=3840&q=75)
In reality, your tests may not perfectly align with the pyramid shape. The pyramid offers a common framework to describe what scope a test can cover to verify configuration and infrastructure resources. I’ll start at the bottom of the pyramid with unit tests and work my way up the pyramid to end-to-end tests. Manual testing involves spot-checking infrastructure for functionality and can have a high cost in time and effort.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#linting-and-formatting)Linting and formatting

While not on the test pyramid, you often encounter tests to verify the hygiene of your Terraform configuration. Use `terraform fmt -check` and `terraform validate` to format and validate the correctness of your Terraform configuration.

When you collaborate on Terraform, you may consider testing the Terraform configuration for a set of standards and best practices. Build or use a linting tool to analyze your Terraform configuration for specific best practices and patterns. For example, a linter can verify that your teammate defines a Terraform variable for an instance type instead of hard-coding the value.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#unit-tests)Unit tests

At the bottom of the pyramid, unit tests verify individual resources and configurations for expected values. They should answer the question, “Does my configuration or plan contain the correct metadata?” Traditionally, unit tests should run independently, without external resources or API calls.

For additional test coverage, you can use any programming language or testing tool to parse the Terraform configuration in HashiCorp Configuration Language (HCL) or JSON and check for statically defined parameters, such as provider attributes with defaults or hard-coded values. However, none of these tests verify correct variable interpolation, list iteration, or other configuration logic. As a result, I usually write additional unit tests to parse the plan representation instead of the Terraform configuration.

Configuration parsing does not require active infrastructure resources or authentication to an infrastructure provider. However, unit tests against a Terraform plan require Terraform to authenticate to your infrastructure provider and make comparisons. These types of tests overlap with security testing done via [policy as code](https://www.hashicorp.com/blog/why-policy-as-code) because you check attributes in Terraform configuration for the correct values.

For example, your Terraform module parses the IP address from an AWS instance’s [DNS name](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance#private_dns) and outputs a list of IP addresses to a local file. At a glance, you don’t know if it correctly replaces the hyphens and retrieves the IP address information.

```
variable "services" {
  type = map(object({
    node = string
    kind = string
  }))
  description = "List of services and their metadata"
}

variable "service_kind" {
  type        = string
  description = "Service kind to search"
}

locals {
  ip_addresses = toset([
    for service, service_data in var.services :
    replace(replace(split(".", service_data.node)[0], "ip-", ""), "-", ".") if service_data.kind == var.service_kind
  ])
}

resource "local_file" "ip_addresses" {
  content  = jsonencode(local.ip_addresses)
  filename = "./${var.service_kind}.hcl"
}

```

You could pass an example set of services and run `terraform plan` to manually check that your module retrieves only the TCP services and outputs their IP addresses. However, as you or your team adds to this module, you may break the module’s ability to retrieve the correct services and IP addresses. Writing unit tests ensures that the logic of searching for services based on `kind` and retrieving their IP addresses remains functional throughout a module’s lifecycle.

This example uses two sets of unit tests written in `terraform test` to check the logic generating the service’s IP addresses for each service kind. The first set of tests verify the file contents will have two IP addresses for TCP services, while the second set of tests check that the file contents will have one IP address for the HTTP service:

```
variables {
  services = {
    "service_0" = {
      kind = "tcp"
      node = "ip-10-0-0-0"
    },
    "service_1" = {
      kind = "http"
      node = "ip-10-0-0-1"
    },
    "service_2" = {
      kind = "tcp"
      node = "ip-10-0-0-2"
    },
  }
}

run "get_tcp_services" {
  variables {
    service_kind = "tcp"
  }

  command = plan

  assert {
    condition     = jsondecode(local_file.ip_addresses.content) == ["10.0.0.0", "10.0.0.2"]
    error_message = "Parsed `tcp` services should return 2 IP addresses, 10.0.0.0 and 10.0.0.2"
  }

  assert {
    condition     = local_file.ip_addresses.filename == "./tcp.hcl"
    error_message = "Filename should include service kind `tcp`"
  }
}

run "get_http_services" {
  variables {
    service_kind = "http"
  }

  command = plan

  assert {
    condition     = jsondecode(local_file.ip_addresses.content) == ["10.0.0.1"]
    error_message = "Parsed `http` services should return 1 IP address, 10.0.0.1"
  }

  assert {
    condition     = local_file.ip_addresses.filename == "./http.hcl"
    error_message = "Filename should include service kind `http`"
  }
}

```

I set some mock values for a set of services in the `services` variable. The tests include `command = plan` to check attributes in the Terraform plan without applying any changes. As a result, the unit tests do not create the local file defined in the module.

The example demonstrates positive testing, where I test the input works as expected. Terraform’s testing framework also supports negative testing, where you might expect a validation to fail for an incorrect input. Use the `[expect\_failures](https://developer.hashicorp.com/terraform/language/tests#expecting-failures)` attribute to capture the error.

If you do not want to use the native testing framework in Terraform, you can use HashiCorp Sentinel, a programming language, or your configuration testing tool of choice to parse the plan representation in JSON and verify your Terraform logic.

Besides testing attributes in the Terraform plan, unit tests can validate:

* Number of resources or attributes generated by [`for_each`](https://developer.hashicorp.com/terraform/tutorials/configuration-language/for-each) or [`count`](https://developer.hashicorp.com/terraform/tutorials/configuration-language/count)
* Values generated by [`for` expressions](https://developer.hashicorp.com/terraform/language/expressions/for)
* Values generated by [built-in functions](https://developer.hashicorp.com/terraform/language/functions)
* Dependencies between modules
* Values associated with interpolated values
* Expected variables or outputs marked as sensitive

If you wish to unit test infrastructure by simulating a `terraform apply` without creating resources, you can choose to use mocks. Terraform 1.7 includes a [test mocking framework](https://www.hashicorp.com/blog/terraform-1-7-adds-test-mocking-and-config-driven-remove), which you can use to mock providers and resources. The test mocking framework allows you to test your modules without connecting to a cloud service provider API. You can also use community tools that mock cloud service provider APIs. However, beware that not all mocks accurately reflect the behavior and configuration of their target API.

Overall, unit tests run very quickly and provide rapid feedback. As an author of a Terraform module or configuration, you can use unit tests to communicate the expected values of configuration to other collaborators in your team and organization. Since unit tests run independently of infrastructure resources, they have a virtually zero cost to run frequently.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#contract-tests)Contract tests

At the next level from the bottom of the pyramid, contract tests check that a configuration using a Terraform module passes properly formatted inputs. Contract tests answer the question, “Does the expected input to the module match what I think I should pass to it?”

Contract tests ensure that the contract between a Terraform configuration’s expected inputs to a module and the module’s actual inputs has not been broken. Most contract testing in Terraform helps the module *consumer* by communicating how the author expects someone to use their module. If you expect someone to use your module in a specific way, use a combination of [input variable validations, preconditions, and postconditions](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#preconditions-and-postconditions) to validate the combination of inputs and surface the errors.

For example, use a custom input variable validation rule to ensure that an AWS load balancer’s listener rule receives a valid integer range for its priority:

```
variable "listener_rule_priority" {
 type        = number
 default     = 1
 description = "Priority of listener rule between 1 to 50000"
 validation {
   condition     = var.listener_rule_priority > 0 && var.listener_rule_priority < 50000
   error_message = "The priority of listener_rule must be between 1 to 50000."
 }
}

```

As a part of input validation, you can use Terraform’s rich language syntax to validate variables with an [object structure](https://developer.hashicorp.com/terraform/language/expressions/type-constraints#structural-types) to enforce that the module receives the correct fields. This module example uses a map to represent a service object and its expected attributes:

```
variable "services" {
  type = map(object({
    node = string
    kind = string
  }))
  description = "List of services and their metadata"
}

```

In addition to custom validation rules, you can use [preconditions and postconditions](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#preconditions-and-postconditions) to verify specific resource attributes defined by the module consumer. For example, you cannot use a validation rule to check if the address blocks overlap. Instead, use a precondition to verify that your IP addresses do not overlap with networks in HashiCorp Cloud Platform (HCP) and your AWS account:

```
resource "hcp_hvn" "main" {
  hvn_id         = var.name
  cloud_provider = "aws"
  region         = local.hcp_region
  cidr_block     = var.hcp_cidr_block

  lifecycle {
    precondition {
      condition     = var.hcp_cidr_block != var.vpc_cidr_block
      error_message = "HCP HVN must not overlap with VPC CIDR block"
    }
  }

}

```

Contract tests catch misconfigurations in modules before applying them to live infrastructure resources. You can use them to check for correct identifier formats, naming standards, attribute types (such as private or public networks), and value constraints such as character limits or password requirements.

If you do not want to use custom conditions in Terraform, you can use HashiCorp Sentinel, a programming language, or your configuration testing tool of choice. Maintain these contract tests in the module repository and pull them into each Terraform configuration that uses the module using a CI framework. When someone references the module in their configuration and pushes a change to version control, the contract tests run against the plan representation before you apply.

Unit and contract tests may require extra time and effort to build, but they allow you to catch configuration errors *before* running `terraform apply`. For larger, more complex configurations with many resources, you should not manually check individual parameters. Instead, use unit and contract tests to quickly automate the verification of important configurations and set a foundation for collaboration across teams and organizations. Lower-level tests communicate system knowledge and expectations to teams that need to maintain and update Terraform configuration.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#integration-tests)Integration tests

With lower-level tests, you do not need to create external resources to run them, but the top half of the pyramid includes tests that require active infrastructure resources to run properly. Integration tests check that a configuration using a Terraform module passes properly formatted inputs. They answer the question, “Does this module or configuration create the resources successfully?” A `terraform apply` offers limited integration testing because it creates and configures resources while managing dependencies. You should write additional tests to check for configuration parameters on the active resource.

In my example, I add a new `terraform test` to apply the configuration and create the file. Then, I verify that the file exists on my filesystem. The integration test creates the file using a `terraform apply` and removes the file after issuing a `terraform destroy`.

```
run "check_file" {
  variables {
    service_kind = "tcp"
  }

  command = apply

  assert {
    condition     = fileexists("${var.service_kind}.hcl")
    error_message = "File `${var.service_kind}.hcl` does not exist"
  }

}

```

Should you verify every parameter that Terraform configures on a resource? You could, but it may not be the best use of your time and effort. Terraform providers include [acceptance tests](https://developer.hashicorp.com/terraform/plugin/framework/acctests) that resources properly create, update, and delete with the right configuration values. Instead, use integration tests to verify that Terraform outputs include the correct values or number of resources. They also test infrastructure configuration that can only be verified after a `terraform apply`, such as invalid configurations, nonconformant passwords, or results of `for_each` iteration.

When choosing an integration testing framework outside of `terraform test`, consider the existing integrations and languages within your organization. Integration tests help you determine whether or not to update your module version and ensure they run without errors.

Since you have to set up and tear down the resources, you will find that integration tests can take 15 minutes or more to complete, depending on the resource. As a result, implement as much unit and contract testing as possible to fail quickly on wrong configurations instead of waiting for resources to create and delete.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#end-to-end-tests)End-to-end tests

After you apply your Terraform changes to production, you need to know whether or not you’ve affected end-user functionality. End-to-end tests answer the question, “Can someone use the infrastructure system successfully?”

For example, application developers and operators should still be able to retrieve a secret from HashiCorp Vault after you upgrade the version. End-to-end tests can verify that changes did not break expected functionality. To check that you’ve upgraded Vault properly, you can create an example secret, retrieve the secret, and delete it from the cluster.

I usually write an end-to-end test using a [Terraform check](https://developer.hashicorp.com/terraform/language/checks) to verify that any updates I make to a HashiCorp Cloud Platform (HCP) Vault cluster return a healthy, unsealed status:

```
check "hcp_vault_status" {

 data "http" "vault_health" {
   url = "${hcp_vault_cluster.main.vault_public_endpoint_url}/v1/sys/health"
 }

 assert {
   condition     = data.http.vault_health.status_code == 200 || data.http.vault_health.status_code == 473
   error_message = "${data.http.vault_health.url} returned an unhealthy status code"
 }

}

```

Besides a `check` block, you can write end-to-end tests in any programming language or testing framework. This usually includes an API call to check an endpoint after creating infrastructure. End-to-end tests usually depend on an entire system, including networks, compute clusters, load balancers, and more. As a result, these tests usually run against long-lived development or production environments.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#testing-terraform-modules)Testing Terraform modules

When you test Terraform modules, you want enough verification to ensure a new, stable release of the module for use across your organization. To ensure sufficient test coverage, write unit, contract, and integration tests for modules.

A module delivery pipeline starts with a `terraform plan` and then runs unit tests (and if applicable, contract tests) to verify the expected Terraform resources and configurations. Then, run `terraform apply` and the integration tests to check that the module can still run without errors. After running integration tests, destroy the resources and release a new module version.

![Pipeline for Terraform module testing](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1705090874-module_testing.png&w=3840&q=75)
Pipeline for Terraform module testing

The [Terraform Cloud private registry](https://developer.hashicorp.com/terraform/cloud-docs/registry/test) offers a branch-based publishing workflow that includes automated testing. If you use `terraform test` for your modules, the private registry automatically runs those tests before releasing a module.

When testing modules, consider the cost and test coverage of module tests. Conduct module tests in a different project or account so that you can independently track the cost of your module testing and ensure module resources do not overwrite environments. On occasion, you can omit integration tests because of their high financial and time cost. Spinning up databases and clusters can take half an hour or more. When you’re constantly pushing changes, you might even create multiple test instances.

To manage the cost, run integration tests after merging feature branches and select the minimum number of resources you need to test the module. If possible, avoid creating entire systems. Module testing applies mostly to immutable resources because of its create and delete sequence. The tests cannot accurately represent the end state of brownfield (existing) resources because they do not test updates. As a result, it provides confidence in the module’s successful usage but not necessarily in applying module updates to live infrastructure environments.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#testing-terraform-configuration)Testing Terraform configuration

Compared to modules, Terraform configuration applied to environments should include end-to-end tests to check for end-user functionality of infrastructure resources. Write unit, integration, and end-to-end tests for configuration of active environments.

The unit tests do not need to cover the configuration in modules. Instead, focus on unit testing any configuration not associated with modules. Integration tests can check that changes successfully run in a long-lived development environment, and end-to-end tests verify the environment’s initial functionality.

If you use feature branching, merge your changes and apply them to a production environment. In production, run end-to-end tests against the system to confirm system availability.

![Pipeline for Terraform configuration testing](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1705090944-configuration_testing.png&w=3840&q=75)
Pipeline for Terraform configuration testing

Failed changes to active environments will affect critical business systems. In its ideal form, a long-running development environment that accurately mimics production can help you catch potential problems. From a practical standpoint, you may not always have a development environment that fully replicates a production environment because of cost concerns and the difficulty of replicating user traffic. As a result, you usually run a scaled-down version of production to save money.

The difference between development and production will affect the outcome of your tests, so be aware of which tests may be more important for flagging errors or disruptive to run. Even if configuration tests have less accuracy in development, they can still catch a number of errors and help you practice applying and rolling back changes before production.

#### [»](https://www.hashicorp.com/blog/testing-hashicorp-terraform#conclusion)Conclusion

Depending on your system’s cost and complexity, you can apply a variety of testing strategies to Terraform modules and configuration. While you can write tests in your programming language or testing framework of choice, you can also use the testing frameworks and constructs built into Terraform for unit, contract, integration, and end-to-end testing.

|  |  |  |
| --- | --- | --- |
| **Test type** | **Use case** | **Terraform configuration** |
| Unit test  | Modules, configuration  | `[terraform test](https://developer.hashicorp.com/terraform/language/tests)` |
| Contract test  | Modules  | [Input variable validation](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#input-variable-validation)  [Preconditions/postconditions](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#preconditions-and-postconditions)  |
| Integration test  | Modules, configuration  | `[terraform test](https://developer.hashicorp.com/terraform/language/tests)` |
| End-to-end test  | Configuration  | [Check blocks](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#checks-with-assertions) |

This post has explained the different types of tests and how you can apply them to catch errors in Terraform configurations and modules before production, and how to incorporate them into pipelines. Your Terraform testing strategy does not need to be a perfect test pyramid. At the very least, automate some tests to reduce the time you need to manually verify changes and check for errors before they reach production.

Check out our tutorial on how to [Write Terraform tests](https://developer.hashicorp.com/terraform/tutorials/configuration-language/test) to learn about writing Terraform tests for unit and integration testing and running them in the Terraform Cloud private module registry. For more information on using checks, [Use checks to validate infrastructure](https://developer.hashicorp.com/terraform/tutorials/configuration-language/checks) offers a more in-depth example. If you want to learn about writing tests for security and policy, review our documentation on [Sentinel](https://docs.hashicorp.com/sentinel/terraform).

###### More blog posts like this one

[###### Terraform AWS provider tops 3 billion downloads

HashiCorp and AWS continue to support the widespread demand for standardized infrastructure as code.](https://www.hashicorp.com/blog/terraform-aws-provider-tops-3-billion-downloads)[###### Terraform 1.9 enhances input variable validations

Terraform 1.9 is now generally available, bringing enhancements to input variable validations, a new string templating function, and more.](https://www.hashicorp.com/blog/terraform-1-9-enhances-input-variable-validations)[###### New Terraform integrations with Cisco, Dell, Red Hat, ServiceNow, and more

17 new Terraform integrations from 13 partners provide more options to automate and secure cloud infrastructure management.](https://www.hashicorp.com/blog/new-terraform-integrations-with-cisco-dell-red-hat-servicenow-and-more)

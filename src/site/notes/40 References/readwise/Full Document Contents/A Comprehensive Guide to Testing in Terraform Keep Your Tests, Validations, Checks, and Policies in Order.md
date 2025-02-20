---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/a-comprehensive-guide-to-testing-in-terraform-keep-your-tests-validations-checks-and-policies-in-order/","tags":["rw/articles"]}
---

![rw-book-cover](https://mattias.engineer/img/favicon/blue.png)

> This post discusses testing and validation for infrastructure-as-code (IaC) with **HashiCorp Terraform**. The insights and ideas presented here can surely be extended to IaC in general.
> 
> 

With the release of the new **testing framework** for Terraform 1.6 presented at HashiConf 2023 in San Francisco[1](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fn:1), there is now the possibility to test your Terraform configurations using Terraform itself.

Testing IaC has always been a pain point. If you have been using IaC for any amount of time you may know that the only true test is to run `terraform apply` and see what happens. Test frameworks for IaC come and go, some are more successful than others. My belief is that there is no mock that will ever give you enough confidence that your IaC will behave as intended[2](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fn:2). For this reason I am glad the new test framework in Terraform does exactly that, it runs `plan` and `apply` commands for you, and it creates actual infrastructure.

But wait, there is more! The new testing framework is *declarative*, meaning that you write tests using the same language that you use for the rest of your infrastructure in Terraform. There is no need to install a third-party tool to keep track of, or to learn a new language.

The new testing framework is not your only option when it comes to testing and validating your infrastructure with Terraform. Terraform 1.5 introduced the concept of **checks** together with the new `check` block. Checks allow you to validate your infrastructure outside of the usual resource lifecycle. If you are using Terraform Cloud you can even set up [continuous validations](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/health#continuous-validation) to regularly verify custom assertions. This post will not focus on Terraform Cloud, instead I will focus on what you can do with Terraform locally[3](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fn:3).

Going even further back in time, Terraform introduced **custom conditions** for validating input variables, output values, and running validation checks at given points in a resource lifecycle. This is another way to test parts of your infrastructure directly in Terraform. Custom validation of input variables allow you to check that the provided input value fulfils given constraints. These constrains could be to limit the length of a supplied string to less than ten characters, or to restrict the allowed values of a variable to a predefined list of values. Resources and data sources have the `lifecycle` block where you can add `precondition` and `postcondition` blocks to validate things before, and after, running an apply, respectively. Similarly, you can add `precondition` blocks to your `output` blocks, to validate something about the output value.

With all the above mentioned options for testing and validation you can create robust and well-tested Terraform configurations and modules.

There is a related concept to testing that you should also consider using. I am talking about **policies**, and **policy-as-code**. It does not make sense to write tests for all the properties of every resource in your modules, because most properties have no designated wrong values that you need to test for. However, there are insecure or incompliant values for properties that your organization might not allow. Besides, maybe you allow insecure property values in your development environments but not in your production environments. Instead of having to write separate test files or custom validations depending on what environment you are testing, you should instead use policies.

In this blog post I will introduce each of the concepts discussed above through examples in Terraform. I will also discuss the important question of when you should use a given approach: a test, a check, a custom condition, or a policy.

All the source code from this post is available at my GitHub repo: [github.com/mattias-fjellstrom/terraform-testing](https://github.com/mattias-fjellstrom/terraform-testing).

#### Using Terraform for testing and validation

This section will introduce each of the concepts discussed above, and in the following section I will go through two example Terraform configuration and include tests, checks, custom conditions, and policies, where appropriate.

##### CLI validation command

Let’s start at the beginning.

When you design your test and validation strategy you can choose how deep into the rabbit hole you want to go.

If you are constrained on time but would like to include basic validation of your Terraform configuration, you can use the `terraform validate` command. This command captures trivial mistakes in your configuration, like typos in resource properties and erroneous syntax in your HashiCorp Configuration Language (HCL).

During development of your Terraform configuration it is a sensible step to run `terraform validate` often[4](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fn:4). You might think that trivial mistakes like typos would be caught by your editor, but you would be surprised by how many mistakes can slip by. HashiCorp recently announced better support for editors like VS Code, so things are getting better in this area.

A good rule of thumb is that your deployment pipeline should never fail on the `terraform validate` command. You should catch these errors during development. However, your pipeline should definitely include the `terraform validate` command, because we all do make mistakes and forget things!

Note that `terraform init` also captures some basic mistakes in your configuration. This include things like using an invalid version number for a given provider.

##### Custom conditions

There are three kinds of **custom conditions** to discuss. The first custom condition is for **variable validation**.

We want to catch errors as soon as possible. If our modules include `variable` blocks, we would be naive to assume the user will only provide sensible values as input to these variables. Erroneous input values will most likely result in errors later in the plan or apply phases. The worst possible type of error is when a bad input value results in a failed apply 45 minutes into the operation.

How do we mitigate this?

The solution is to add `validation` blocks nested inside of our `variable` blocks:

```
variable "name_prefix" {
    type = string

    validation {
        condition     = length(var.name_prefix) <= 20
        error_message = "Variable length should be 20 characters or less"
    }
}

```

A `validation` block has no label, and it takes two arguments:

* A `condition` which is a boolean expression that evaluates to `true` or `false` to indicate if the validation succeeded or failed.
* An `error_message` that is presented to the user if the validation fails.

Now, let us move on to the second kind of custom condition.

We can include validations that run before or after changes are applied to a resource, or after a data source is read. We do this by including an appropriate `precondition` or `postcondition` block nested inside of a `lifecycle` block in our resource or data source.

An example of what this looks like:

```
// read an existing Azure resource group
data "azurerm_resource_group" "rg" {
  name = "rg-storage-resource-group"
}

// create a new Azure storage account in the resource group
resource "azurerm_storage_account" "stg" {
  name                     = "stsamplestorage"
  resource_group_name      = data.azurerm_resource_group.rg.name
  location                 = data.azurerm_resource_group.rg.location
  access_tier              = "Hot"
  account_replication_type = "LRS"
  account_tier             = "Standard"

  lifecycle {
    precondition {
      condition     = data.azurerm_resource_group.rg.managed_by == "terraform"
      error_message = "Resource group must be managed by Terraform!"
    }
  }
}

```

Similar to the `validation` block for variables, both the `precondition` and `postcondition` blocks takes two arguments: a `condition` and an `error_message`.

In the previous code snippet I declare a data source where I read an existing resource group from Azure (`azurerm_resource_group`). I then would like to create a new storage account in the resource group, but only if the `precondition` validation of the resource `lifecycle` passes.

In the `precondition` block I check that the `managed_by` property of the resource group is set to the value `terraform`. If the `managed_by` property has any other value, the `condition` will evaluate to false and the `precondition` fails. The operation will halt and the `error_message` is displayed to the user in the console.

The third, and last, custom condition to discuss is for **output validation**. We can add a `precondition` block nested inside of our `output` blocks. This allows us to verify something that the output depends on. This could be used to avoid outputting values from the `output` block into our state file and in our logs when the value would not be useful. Personally I think this custom condition has less obvious usecases, and I have not used it for anything myself.

The `precondition` block inside of the `output` block looks the same as for resources, it has one `condition` argument and one `error_message` argument.

An example of what a custom condition of outputs look like:

```
output "website_endpoint" {
  value = azurerm_storage_account.stg.primary_web_endpoint

  precondition {
    condition     = startswith(azurerm_storage_account.stg.primary_web_endpoint, "https://")
    error_message = "Website URL uses HTTP, you should instead configure HTTPS"
  }
}

```

This custom condition checks that a website deployed to an Azure storage account exposes a website URL starting with `https://`, and if this is not the case an error message is raised and the deployment fails.

##### Test framework

The Terraform test framework is new since Terraform 1.6. It was release a few days before HashiConf 2023 in San Francisco, and I believe it is a welcome change to Terraform.

Tests are written using HCL, so you do not need to learn a new language in order to test your IaC. Test files use the `.tftest.hcl` file ending.

By default, all test files stored in the same directory as your module, or stored in a `tests` directory, are run when you issue the new `terraform test` command. If you place your tests in a different directory you can add the `-test-directory=path/to/my/test/directory` flag to the command.

With all the necessary details out of the way, a typical setup of a simple module with tests could look like this:

```
$ tree .
.
├── main.tf
├── variables.tf
├── outputs.tf
└── tests
    ├── testfile1.tftest.hcl
    ├── testfile2.tftest.hcl
    └── testfile3.tftest.hcl

```

A test file consists of one or more `run` blocks. Each `run` block should be thought of as a test. A `run` block includes a number of arguments and blocks to configure what the test should do. Each test executes a `command`, which is either `plan` or `apply`. If you do not specify the `command` argument it defaults to `apply`.

An example of what a `run` block looks like:

```
// tests/main.tftest.hcl
run "file_contents_should_be_valid_json" {
  command = plan

  assert {
    condition     = try(jsondecode(local_file.config.content), null) != null
    error_message = "The file is not valid JSON"
  }
}

```

The `run` block label should use a descriptive name to explain what the test is about. In this case I have set the label to `file_contents_should_be_valid_json` to indicate that this tests validates that the content of a file that is produced by Terraform contains valid JSON content. The test runs a `plan` as indicated by the `command` argument. The meat of the test is in the `assert` statement. The `condition` argument evaluates to `true` or `false`, which results in the test passing or failing, respectively.

Note that you can add additional `assert` blocks to make several assertions in the same test. It is also possible to not use any `assert` block, but instead use the `expect_failures` argument where you can indicate if you expect the `plan` or `apply` to fail, and if so what will make it fail. Further down in this post I will show examples of what this looks like.

##### Checks

The concept of **checks** together with the `check` block was introduced in Terraform 1.5 and serve a purpose similar to custom validations for resources and data sources, but with one important difference. The `check` block is ideal for validations you want to make that should not stop a plan and apply from finishing. If a check fails the deployment will still continue. You will get a warning in the output indicating that the check failed.

A `check` block can include at most one scoped `data` block, and one or more `assert` blocks. Each `assert` block has a `condition` that evaluates to `true` or `false`, and an `error_message` that is displayed if the assertion fails. The purpose of the scoped `data` block is to read data about a resource, or perhaps an external website, that you want to include in the check.

Imagine that our Terraform configuration sets up a publicly available website (among other things), and we would like to check that the website responds to requests after it is set up. This is an ideal situation for a `check` block. An example of what this might look like:

```
// main.tf
module "website" {
  source = "./modules/web"

  // ... the rest of the arguments are left out for brevity
}

check "validate_website_response" {
  data "http" "static_website" {
    url = module.website.web_endpoint
  }

  assert {
    condition     = data.http.static_website.status_code == 200
    error_message = "The website returned an unhealthy status code"
  }
}

```

The main differences between `check` blocks and custom conditions for resources and data sources is that the latter is tied to the lifecycle (hence they are part of the `lifecycle` block) of the resource or data source, while `check` blocks are not. Also, `check` blocks do not fail an apply if the `assert` evaluates to false, while custom conditions for resources and data sources do.

This makes `check` blocks useful for continuous validation in Terraform Cloud. Continuous validation specifically runs the `check` blocks in your configuration on a schedule. This could be useful for basic health checks for your infrastructure.

##### Policies

Policies are closely related to tests, but they serve a different purpose.

There are two popular frameworks for **policy-as-code** that works well with Terraform, and they are both available in Terraform Cloud.

The first framework is the **Open Policy Agent (OPA)** together with its **Rego** language for policies, it has risen in popularity in recent years and is used for many types of policies. The second framework is **HashiCorp Sentinel**, which uses HCL. In this post I will use Sentinel, since it is most closely related to HashiCorp and Terraform and in my opinion it is also a little bit easier to learn.

The purpose of policies with Terraform is to validate that the changes you are introducing follow rules defined by you or your organization. These rules are most likely related to compliance or security.

An example of a Sentinel policy document is this:

```
import "tfplan/v2" as tfplan

// filter out all storage containers
containers = filter tfplan.resource_changes as _, c {
	c.type is "azurerm_storage_container"
}

// filter out containers that are created or updated
createdOrUpdated = filter containers as _, c {
	c.change.actions contains "create" or c.change.actions is ["update"]
}

// make sure each container has an access type set to private
main = rule {
	all createdOrUpdated as _, containers {
		containers.change.after.container_access_type is "private"
	}
}

```

The first time you see a Sentinel policy you might get puzzled at what it does. This post is not about explaining the syntax of Sentinel, the comments in the code snippet should be explanation enough. In essence, Sentinel takes the JSON-representation of a Terraform plan file from a `terraform plan` command, and searches for something specific in the plan, and finally evaluates the `rule` named `main` that is either `true` or `false`. If the rule evaluates to `true` the change is allowed by the policy.

In the policy example above I first apply a `filter` to find all the resources of type `azurerm_storage_container`, then I have another `filter` to find all the containers where the planned actions are `create` or `update`. Finally, I have my `rule` named `main` that checks that the `container_access_type` property is set to `private` for the containers that I have filtered out. If one or more containers has set `container_access_type` to something other than `private`, then this policy evaluation will fail, and I should not allow the change to be deployed.

The trick to learn how to write policies is to make sure you have a plan file in JSON format available, then you know what to look for and what all the fields are named. It also helps to start with an existing example and modify it to your needs.

You should run all your policies against each planned change to make sure you are not introducing anything that violates your compliance and security rules.

#### Applying testing and validation in the real world

In this section I want to go through two small sample Terraform configurations, and use the different options from above to test and validate the code. In the first sample I take on the role as a module developer, crafting a module for other developers to use. In the second sample I imagine I am part of a standalone team building infrastructure for our own applications.

##### Sample 1: Module producer

In this sample we are producers of a simple module that other teams in our organization will use in their own infrastructure. Many teams depend on our module, so we must make sure we test it thoroughly. The sample configuration might be a bit contrived, but bear with me!

The module we have produced takes three inputs, it creates a local file containing some JSON data, and it outputs the file content in base64 encoded format. This configuration file is part of a larger infrastructure where the file will be used to configure a separate system (not included in this sample). The system has constraints about the configuration file that must be respected. These constraints might be that the JSON file should be valid, it should include certain fields, and it must be at most a given size.

Our module has the following directory structure:

```
$ tree .
.
├── main.tf
├── outputs.tf
├── tests
│   └── main.tftest.hcl
└── variables.tf

1 directories, 4 files

```

The first file we will look at is `variables.tf`:

```
// variables.tf
variable "config_url" {
  type = string

  validation {
    condition     = startswith(var.config_url, "https://")
    error_message = "config_url should start with https://"
  }
}

variable "port" {
  type = number

  validation {
    condition     = var.port > 1023 && var.port <= 65535
    error_message = "Use an unprivileged port number (1024-65535)"
  }
}

variable "service_name" {
  type = string
}

```

There are three variables defined: `config_url`, `port`, and `service_name`.

Exactly what these variables mean in a larger context is out of scope but we imagine they are important! A brief description of what we do know:

* `config_url` should be a valid URL. Currently the `condition` in the `validation` block makes sure that the URL starts with `https://`. We could change this `condition` to compare the provided value with a regex describing a valid URL if we want to. For simplicity I have left the validation as it is.
* `port` should be a valid port number. The `condition` in the `validation` block checks that the user has provided un unprivileged port in the range 1024-65535.
* `service_name` is the name of a service of some kind. Currently there is no validation of this variable, this means we have no known restrictions of the value the user can supply. This is a common situation in the real world, where we might not always know what to allow or not.

Next we take a look at `main.tf`:

```
// main.tf
terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.4.0"
    }
  }
}

resource "local_file" "config" {
  filename = "config.json"
  content  = <<EOF
{
    "endpoint": "${var.config_url}",
    "port": "${var.port}",
    "service": "${var.service_name}"
}
EOF
}

```

This simple Terraform configuration specifies one required provider, the `local` provider. It creates one resource of type `local_file`. This resource is the configuration file that we are creating. The `content` argument of the file is constructed as JSON, using the three supplied variables.

Next we look at `outputs.tf`:

```
// outputs.tf
output "file_content_base64" {
  value = base64encode(local_file.config.content)

  precondition {
    condition     = length(base64encode(local_file.config.content)) < 150
    error_message = "Config file is too large."
  }
}

```

A single `output` block is defined. The `value` argument is the base64-encoded value of the file content. There is a specific restriction on the length of this base64-encoded value, it can be at most 149 characters long. Don’t ask me why, only the *system* knows. We use a `precondition` block to verify that the size restriction is fulfilled.

Could we have validated our variables in some way to avoid the `precondition` block for the output value? The problem is that the size of the JSON file depends on all three variables, and currently the `service_name` variable has no restrictions on its own. The `config_url` variable could also be almost any length. In this case it makes sense to check the size of the generated JSON as a `precondition` in the output instead.

When it comes to testing this module we should explicitly test the interface we are exposing. What is included in the interface of this module? It is the following:

* The three variables `config_url`, `port`, and `service_name`.
* The generated JSON-file `config.json`.
* The output `file_content_base64`.

These are the things that a user of our module will see and interact with.

Below I will discuss one test at a time, all the tests I show are part of the file named `tests/main.tftest.hcl`. The first test I write is for the `config_url` variable:

```
// tests/main.tftest.hcl
variables {
  config_url   = "https://example.com"
  port         = 1414
  service_name = "my-service"
}

run "bad_input_url_should_fail" {
  command = plan

  variables {
    config_url = "http://example.com"
  }

  expect_failures = [
    var.config_url
  ]
}

```

The `variables` block defined in the root of the file provides default values for all the variables. These can be overridden in each test if desired. For this test I override the `config_url` variable inside of the `run` block with a URL starting with `http://`, which I expect should not be allowed. For this particular test I am not using an `assert` block to assert something about the test outcome, instead I use the `expect_failures` argument to tell this test that I expect it to fail, and I expect that the variable named `config_url` will be the reason for the failure.

The next test is a similar test but for the variable named `port`:

```
// ... continuation of tests/main.tftest.hcl

run "bad_input_port_should_fail" {
  command = plan

  variables {
    port = 80
  }

  expect_failures = [
    var.port
  ]
}

```

This test overrides the `port` variable with a value of `80`. This is a privileged port, so I expect it will not be allowed. Once again I use the `expect_failures` argument to tell the test I expect it to fail and that the variable named `port` will be the reason for the failure. Note that to be thorough I should add a test that makes sure I can’t provide a port number larger than 65535 but I will skip it for brevity.

As discussed above there is no wrong input value for the last variable named `service_name`. So there is no good test we can write for it. However, in the next test we will use the `service_name` variable in order to make the size of the JSON content too big. This is a test for our output validation.

```
// ... continuation of tests/main.tftest.hcl

run "too_large_output_file_should_fail_deployment" {
  command = plan

  variables {
    service_name = "this-service-name-creates-a-too-big-file"
  }

  expect_failures = [
    output.file_content_base64
  ]
}

```

This test overrides the `service_name` variable with a long name, and for the third time in a row I use the `expect_failures` argument to tell the test I expect it to fail on the output named `file_content_base64`.

The last test I have added for this module concerns the validity of the content of the JSON file. When you construct a JSON file inline of your Terraform configuration like this it is easy to make mistakes. A trailing comma or a missing colon would create a broken JSON file. A good test for this is:

```
// ... continuation of tests/main.tftest.hcl

run "file_contents_should_be_valid_json" {
  command = plan

  assert {
    condition     = try(jsondecode(local_file.config.content), null) != null
    error_message = "The file is not valid JSON"
  }
}

```

This test uses the `assert` block. The `condition` argument uses the `try(...)` function. This function will select the first valid value from its list of arguments. The first argument in this function is `jsondecode(local_file.config.content)`, which encodes the string content of the file as JSON. If this encoding fails, the `try(...)` function will instead select its second argument: `null`. The `condition` argument checks that the result of `try(...)` is not equal to `null`. If it is, the assertion fails and so does the test.

To run the tests we issue the new `terraform test` command:

```
$ terraform test
tests/main.tftest.hcl... in progress
  run "bad_input_url_should_fail"... pass
  run "bad_input_port_should_fail"... pass
  run "too_large_output_file_should_fail_deployment"... pass
  run "file_contents_should_be_valid_json"... pass
tests/main.tftest.hcl... tearing down
tests/main.tftest.hcl... pass

Success! 4 passed, 0 failed.

```

To see what a failing test looks like, let’s change the `port` number in the test named `bad_input_port_should_fail` to a valid number:

```
// ... temporary change in tests/main.tftest.hcl to trigger a failing test

run "bad_input_port_should_fail" {
  command = plan

  variables {
    port = 8080
  }

  expect_failures = [
    var.port
  ]
}

```

Rerunning the tests produces the following output:

```
$ terraform test
tests/main.tftest.hcl... in progress
  run "bad_input_url_should_fail"... pass
  run "bad_input_port_should_fail"... fail
╷
│ Error: Missing expected failure
│
│   on tests/main.tftest.hcl line 27, in run "bad_input_port_should_fail":
│   27:     var.port
│
│ The checkable object, var.port, was expected to report an error but did not.
╵
  run "too_large_output_file_should_fail_deployment"... skip
  run "file_contents_should_be_valid_json"... skip
tests/main.tftest.hcl... tearing down
tests/main.tftest.hcl... fail

Failure! 1 passed, 1 failed, 2 skipped.

```

There we have it. Four simple tests to validate that the interface of our module behaves as we intend it to do. During continued development of this module we would add additional tests when it makes sense.

This module included tests and validations, but no policies. Does it make sense to talk about policies during module development? Not really. As a module developer you are not sure in what context your module will be used, so it is unlikely the policies you add would make any sense to the user of your module.

##### Sample 2: Module consumer

In this sample we put ourselves in the shoes of a module consumer. In reality we might be both a module consumer and module producer at the same time, but in this case we imagine we are writing a Terraform configuration for our own application, and we are using a module provided for us by a platform team. To have a complete example to show I will include the web module as a local module, but note that this module could be hosted in an internal Terraform registry for our organization.

The file structure of this example configuration looks like the following:

```
$ tree .
.
├── index.html
├── main.tf
├── modules
│   └── web
│       ├── main.tf
│       ├── outputs.tf
│       └── variables.tf
└── policies
    ├── policy.sentinel
    └── sentinel.hcl

4 directories, 9 files

```

I will not go into the details of the web module itself, the source code is available at the GitHub repo for this post. Our main concern is the `main.tf` file:

```
// main.tf
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.76.0"
    }
  }
}

provider "azurerm" {
  features {}
}

module "website" {
  source = "./modules/web"
  providers = {
    azurerm = azurerm
  }

  location           = "swedencentral"
  name_prefix        = "web531"
  index_file_content = file("index.html")
}

check "validate_website_response" {
  data "http" "static_website" {
    url = module.website.web_endpoint
  }

  assert {
    condition     = data.http.static_website.status_code == 200
    error_message = "${data.http.static_website.url} returned an unhealthy status code"
  }

  assert {
    condition     = data.http.static_website.response_headers["Content-Type"] == "text/html"
    error_message = "${data.http.static_website.url} returned a wrong content-type header"
  }

  assert {
    condition     = strcontains(data.http.static_website.response_body, "Hello World")
    error_message = "${data.http.static_website.url} did not respond with expected content"
  }
}

```

This configuration lists `azurerm` as a required provider. This provider is configured according to our teams specification, and then provided to the module. The `module` block takes three variables: `location`, `name_prefix`, and `index_file_content`. The website content is read from a local file `index.html`.

Apart from the module there is one large `check` block with the label `validate_website_response`. Our team has included this `check` block in order to verify a few basic things about the website we are creating. In the `check` block there is one nested `data` block that uses the `http` provider in order to send a GET request to our websites endpoint. The endpoint is read from the module output named `web_endpoint`. Following the data source there are three `assert` blocks:

* The first `assert` block checks that the website responds with a 200 OK response code. If it does not it indicates that the website is not functioning correctly.
* The second `assert` block checks that the content-type of the returned page is `text/html`. If it is not then the website will not be displayed correctly in a browser.
* The third `assert` block checks that the returned content contains the string `Hello World`. If it foes not then the right content has not been uploaded.

Appropriate `error_message` arguments are included for each `assert` block.

Notice that our directory structure does not include any tests. This is because tests are primarily for module producers, and in this case we are consuming a module. We hope that the producers of the module we are using have included tests though!

Also notice that our team have decided to use a `check` block instead of `precondition` or `postcondition` blocks. This is because our team would like to have the possibility to set up continuous checks via Terraform Cloud. The team also decided that if these simple checks fail we don’t want to halt the `terraform apply` command, because in this case the website is not business critical. Remember that `precondition` and `postcondition` validations will halt the `apply` if they fail, but `check` blocks will only report a warning.

Looking back at the directory structure for this example we notice that we have included a `policies` directory. Currently there is a single policy document in this directory:

```
// policy.sentinel
import "tfplan/v2" as tfplan

// filter out storage accounts that are created or updated
storageAccounts = filter tfplan.resource_changes as _, resourceChange {
	resourceChange.type is "azurerm_storage_account" and
		(resourceChange.change.actions contains "create" or
			resourceChange.change.actions contains "update")
}

main = rule {
	all storageAccounts as _, storageAccount {
		storageAccount.change.after.public_network_access_enabled is false
	}
}

```

This policy filters out all Azure storage accounts that are about to be created or updated, it then checks that the `public_network_access_enabled` is set to `false`. If it is not, the policy will fail. This policy should be run as part of Terraform Cloud or whatever deployment pipeline the team will be using.

To run the policy locally we have to perform the following steps:

```
$ terraform plan -out=tfplan
$ terraform show -json tfplan | jq > policies/plan.json
$ cd policies
$ sentinel apply policy.sentinel
Pass - policy.sentinel

```

#### Where to learn more

If you want to learn more about the topics presented in this post I suggest you head over to the official documentation. For your convenience I have gathered the relevant links:

#### Summary

We have seen that there are many options for testing and validating Terraform configuration, so that we can build robust modules and configurations that will stand the test of time.

The new testing framework is intended for module producers. Add tests to verify the behavior of your module interface: the variables, outputs, and any other externally visible behavior such as files.

For module consumers and general Terraform configurations there are plenty of validation options such as variable validation, output validation, lifecycle conditions in resources and data sources, as well as `check` blocks.

Let us summarize the different available options:

* We run `terraform init` and `terraform validate` to check that the HCL we are writing follows proper syntax.
* We use tests with `run` blocks to verify that our contract to our users, our module interfaces, work as intended.
* We use variable `validation` blocks to verify that the input provided by users of our modules and configurations adhere to allowed values.
* We use `precondition` and `postcondition` blocks in our resources and data sources to verify conditions before or after applying changes.
* We use `check` blocks to verify external behavior outside of resource lifecycles, and could even set up continuous validations in Terraform Cloud.
* We use policies with Sentinel or OPA to make sure the changes we are applying follow our organizations compliance and security requirements.

It will be interesting to see how the new test framework for Terraform evolves over time, and to see what tests people will be writing for their modules.

I hope this blog post has helped you starting to think about how to use tests and validations, as well as introducing policy-as-code, for your Terraform configurations!

1. Actually, it was announced a few days before the conference. Why wait when you have something good to announce? [↩︎](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fnref:1)
2. I challenge you all to tell me how a mock, or any other means of not running a real apply (or whatever term your IaC tool use) gives you confidence that your IaC will work as intended. [↩︎](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fnref:2)
3. But I will mention Terraform Cloud a few times! [↩︎](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fnref:3)
4. While you are at it, also run `terraform fmt` often. If you, like me, are using format-on-save in VS Code, then `terraform fmt` is superfluous. [↩︎](https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo#fnref:4)

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-let-s-keep-the-quality-up/","tags":["rw/articles"]}
---

![rw-book-cover](https://media.dev.to/cdn-cgi/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fvsnd4lv0t1d6f8xlviu2.png)

####  [SAP BTP and Terraform (5 Part Series)](https://dev.to/lechnerc77/series/26908)

####  Introduction

Terraform is one variant of managing Infrastructure as Code. Let us take a closer look at the the second part of the term namely at the "as-Code". What are good practices when it comes to the quality of the code when thinking about application development? Formatting and syntax checks as well as automated testing (unit and integration testing).

Shouldn't we apply the same approaches that we do when developing code for applications also when developing Terraform configurations? You can already guess what the answer is ... yes of course we should. And the cool thing is: a lot of support is available out of the box when using Terraform.

In this blog post we will walk through the different aspects that we should consider when writing Terraform configurations. We will cover the following topics:

* Code Formatting
* Code Validation
* Unit Testing
* Integration Testing

All the functionality will be demonstrated leveraging HashiCorp Terraform standard functionality using as an example the Terraform provider for SAP BTP. To automate the process, we will use GitHub Actions.

####  Code Formatting

Let us start with the very first step of ensuring the quality of the Terraform scripts - code formatting. The Terraform CLI provides a dedicated command `terraform fmt` to format the Terraform configuration files.

This command rewrites the Terraform configuration files to a canonical format and style. The good thing is that no configuration is needed as the formatting rules are predefined by Terraform itself. So no discussion in the teams how to format the code (yes I am looking at you JavaScript and the tons of options and source of infinite discussions).

So as first step to ensure the quality of the Terraform code namely a proper code formatting, run the following command:

```
terraform fmt -recursive

```

I added the `-recursive` flag to format all the files in the directory and its subdirectories. Good if you do that locally, but even better if you add it to your CI/CD pipeline assuming that changes in the Terraform scripts are done via pull requests (PR).

As an example we use GitHub Actions to ensure that whenever a pull request is created the Terraform scripts are checked for proper formatting. If this is not the case we let the pipeline fail. For that we create a GitHub Action that is triggered by a PR and basically does two things:

1. Check which directories contain changed files
2. Run the `terraform fmt` command on these directories to check if the formatting is correct

The GitHub Action workflow looks like this:

```
name: Terraform Format Check

on:
    pull_request:
      types:
        - opened
        - reopened
        - synchronize
        - ready_for_review

jobs:
    terraform-fmt:
      name: Validate Format of Terraform Files
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v4

        - name: Setup Terraform
          uses: hashicorp/setup-terraform@v3
          with:
            terraform_wrapper: false

        - name: Get changed directories
          id: changed-files
          uses: tj-actions/changed-files@v44
          with:
              dir_names: 'true'

        - name: Validate Terraform format
          if: steps.changed-files.outputs.any_changed == 'true'
          env:
            ALL_CHANGED_FILES: ${{ steps.changed-files.outputs.all_changed_files }}
          shell: bash
          run: |
              EXIT_CODE=0
              for file in ${ALL_CHANGED_FILES}; do
                echo "Checking format of $file with terraform fmt"
                terraform fmt -check -recursive "$file" || EXIT_CODE=$?
              done
              exit $EXIT_CODE

```

We use the community action `tj-actions/changed-files` to get the directories that contain changed files. The `terraform fmt` command is then run on these directories. Here we used an additional flag `-check` to check if the files are formatted correctly without formatting them.

>  **Note** - There are a few more options available for the `terraform fmt` that might come handy when executing the checks. You can find them in the [official documentation](https://developer.hashicorp.com/terraform/cli/commands/fmt).
> 
>  

The GitHub Actions workflow can be integrated in the required checks for pull requests and this way only proper formatted Terraform scripts will land in your repository. What's next? Let's look at the code validation.

####  Code Validation

Before executing a Terraform script it makes sense to statically check if the script is syntactically correct. This way we can already sort out some issues before the actual execution.

As for the formatting the Terraform CLI got us covered via the command `terraform validate`. In contrast to `terraform fmt` this command has some prerequisites before being applicable namely you must have a initialized workspace. The backend configuration can be omitted. Before executing the validation, you must therefore execute the following command in the directory where your Terraform configuration is located:

```
terraform init -backend=false

```

The `-backend=false` is needed if you have a backend configuration in place, but also doesn't do any harm in case there is no backend configuration provided. After that you can execute the validation. Use the following command to trigger the validation:

```
terraform validate

```

This will check the syntax of the Terraform scripts in the directory it is executed in and will return errors if there are any. From a automation perspective it is great that the command can return the result of the validation in a machine-readable format namely JSON by using the `-json` flag.

>  **Note** - You can find more information about the command and in particular the fields of the JSON object in the [official documentation](https://developer.hashicorp.com/terraform/cli/commands/validate).
> 
>  

Let us assume that we want to run this simple validation (without any further `jq` magic on the JSON response) in our CI/CD pipeline, i.e. just execute the validation and in case it fails, let the pipeline fail. We can do so with the following GitHub Actions workflow:

```
name: Terraform Validation Check

on:
    pull_request:
      types:
        - opened
        - reopened
        - synchronize
        - ready_for_review

jobs:
    terraform-validate:
      name: Validate Syntax of Terraform Files
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v4

        - name: Setup Terraform
          uses: hashicorp/setup-terraform@v3
          with:
            terraform_wrapper: false

        - name: Get changed directories
          id: changed-files
          uses: tj-actions/changed-files@v44
          with:
              dir_names: 'true'

        - name: Validate Terraform sytnax
          if: steps.changed-files.outputs.any_changed == 'true'
          env:
            ALL_CHANGED_FILES: ${{ steps.changed-files.outputs.all_changed_files }}
          shell: bash
          run: |
              EXIT_CODE=0
              for file in ${ALL_CHANGED_FILES}; do
                echo "Validating Terraform files in $file with terraform validate"
                cd $file
                terraform init -backend=false || EXIT_CODE=$?
                terraform validate || EXIT_CODE=$?
                rm -rf .terraform/
                cd ${{ github.workspace }}
              done
              exit $EXIT_CODE

```

As in the case of the formatting check we assume that the change is served via a PR. As before we check which directories are changed, iterate over the list of directories and execute the validation for each of the directories. In case any validation fails, the GitHub Action workflow will fail.

Cool, so now we safeguarded the quality of the Terraform scripts by ensuring that they are properly formatted and that the syntax is correct. However, there is more that can be done using [Terraforms testing framework](https://www.hashicorp.com/blog/testing-hashicorp-terraform). This framework is available since release 1.6.0 and was since then improved e.g. with [test mocking](https://www.hashicorp.com/blog/terraform-1-7-adds-test-mocking-and-config-driven-remove) in release 1.7.0.

The good thing in contrast to other Terraform testing frameworks is, that you can write the test in the same syntax that you already know i.e. the HashiCorp configuration language. This lowers the entry barrier and makes the adoption easier. Lets us take a closer look how this framework can help us improve the code quality.

####  Terraform Testing Framework

If you take a look at the original blog post about the [testing framework](https://www.hashicorp.com/blog/testing-hashicorp-terraform) by HashiCorp, you will recognize that it divides the tests into different categories that you certainly know from application development:

* Unit Tests
* Contract Tests
* Integration Tests
* End-to-End Tests

In this blog post we will focus on the categories of "Unit Tests" and "Integration Tests".

>  **Note** If you are also using Terraform modules in your company, I highly recommend to take a look at the "Contract Tests" as described in the blog post [Testing HashiCorp Terraform](https://www.hashicorp.com/blog/testing-hashicorp-terraform).
> 
>  

#####  The Basic Setup

Before we start with the testing let us first look at a basic setup. Assume we have a quite Terraform script that crates a subaccount on the SAP Business Technology Platform and assigns some entitlements to it. The configuration contains several input variables to ensure company guidelines for the naming and labeling of the subaccount. The `variables.tf` has the following layout:

```
###
# Provider configuration
###
variable "globalaccount" {
  type        = string
  description = "The subdomain of the SAP BTP global account."
}

variable "region" {
  type        = string
  description = "The region where the project account shall be created in."
  default     = "eu10"
}

###
# Subaccount setup
###
variable "project_name" {
  type        = string
  description = "The subaccount name."
  default     = "proj-1234"

  validation {
    condition     = can(regex("^[a-zA-Z0-9_\\-]{1,200}", var.project_name))
    error_message = "Provide a valid project name."
  }
}

variable "stage" {
  type        = string
  description = "The stage/tier the account will be used for."
  default     = "DEV"

  validation {
    condition     = contains(["DEV", "TST", "SBX", "PRD"], var.stage)
    error_message = "Select a valid stage for the project account."
  }
}

variable "costcenter" {
  type        = string
  description = "The cost center the account will be billed to."
  default     = "1234567890"

  validation {
    condition     = can(regex("^[0-9]{10}", var.costcenter))
    error_message = "Provide a valid cost center."
  }
}

variable "org_name" {
  type        = string
  description = "Defines to which organisation the project account shall belong to."
  default     = "B2C"

  validation {
    condition = contains(concat(
      // Cross Development
      ["B2B", "B2C", "ECOMMERCE"],
      // Internal IT
      ["PLATFORMDEV", "INTIT"],
    ), var.org_name)
    error_message = "Please select a valid org name for the project account."
  }
}

###
# Entitlements for Subaccount
###
variable "entitlements" {
  type = list(object({
    name   = string
    plan   = string
    amount = number
  }))
  description = "List of entitlements for the subaccount."
  default = [
    {
      name   = "alert-notification"
      plan   = "standard"
      amount = null
    },
    {
      name   = "SAPLaunchpad"
      plan   = "standard"
      amount = null
    },
    {
      name   = "hana-cloud"
      plan   = "hana"
      amount = null
    },
    {
      name   = "hana"
      plan   = "hdi-shared"
      amount = null
    },
    {
      name   = "sapappstudio"
      plan   = "standard-edition"
      amount = null
    }
  ]
}

```

The setup of the subaccount is given by the following `main.tf` file:

```
###
# Setup of names in accordance to the company's naming conventions
###
locals {
  project_subaccount_name   = "${var.org_name} | ${var.project_name}: CF - ${var.stage}"
  project_subaccount_domain = lower(replace("${var.org_name}-${var.project_name}-${var.stage}", " ", "-"))
  project_subaccount_cf_org = replace("${var.org_name}_${lower(var.project_name)}-${lower(var.stage)}", " ", "_")
}

###
# Creation of subaccount
###
resource "btp_subaccount" "project" {
  name      = local.project_subaccount_name
  subdomain = local.project_subaccount_domain
  region    = lower(var.region)
  labels = {
    "stage"      = ["${var.stage}"],
    "costcenter" = ["${var.costcenter}"]
  }
  usage = "NOT_USED_FOR_PRODUCTION"
}

###
# Assignment of entitlements
###
resource "btp_subaccount_entitlement" "entitlements" {
  for_each = {
    for index, entitlement in var.entitlements :
    index => entitlement
  }

  subaccount_id = btp_subaccount.project.id
  service_name  = each.value.name
  plan_name     = each.value.plan
}

```

This file translates the input variables into the right names and creates the resources. In addition we define output variables in the `outputs.tf` file:

```
output "subaccount_id" {
  value       = btp_subaccount.project.id
  description = "The ID of the project subaccount."
}

output "subaccount_name" {
  value       = btp_subaccount.project.name
  description = "The name of the project subaccount."
}

```

While this setup is quite simple, we see that some parts make sense to be tested. Let us therefore start and see how to do a Unit-Test on this configuration.

#####  Unit Tests

Unit Tests per definition should run without any dependencies like external resources or API calls. In the Terraform world that means that we can test the configuration as long as we do not need any active resources and authentication against providers. This means that everything that parses the configuration can be tested in this stage. In our setup there a two great candidates for the tests:

* The validation logic in the `variables.tf` file
* The replacement logic of the local values in the `main.tf` file

We take the recommendations from the [Terraform tutorial on testing](https://developer.hashicorp.com/terraform/tutorials/configuration-language/test) as a guidance on how to structure our code.

Assume that our Terraform configuration is located in a directory `infra` we create a new directory `tests` as a subdirectory to put in all our tests. The structure looks like this:

```
.
| - infra
|   | - main.tf
|   | - variables.tf
|   | - outputs.tf
|   | - provider.tf
|   | - ...
| - tests

```

Let us start with testing the input validation. As a first test we want to check if the the variable `costcenter` is validated as expected. We create a new file called `variables_costcenter_validation.tftest.hcl` in the `test` directory. By convention the file name must end with `.tftest.hcl` to be recognized by Terraform as a test.

As we want an isolated test without any connection to the provider we must mock the provider. To do so we add the following code to the test file:

```
mock_provider "btp" { }

```

This will make sure that we do not need to authenticate against the provider. Looking at the `variables.tf` we see that we have a mandatory parameter that we need to supply namely the `globalaccount`. As we mocked the provider, we can define any value for this variable as it will not be used. we add a variable to the file which now looks like this:

```
mock_provider "btp" { }

variables {
    globalaccount = "test"
  }

```

Now we can finally add the test itself. Terraform tests are executed in a so called `run` blocks. We add one first block which should test that a valid costcenter is provided:

```
mock_provider "btp" { }

variables {
    globalaccount = "test"
  }

run "provide_valid_costcenter" {
  command = plan
}

```

As you can see we can also specify the `command` that should be executed. The validation is already executed in the `plan` phase so we added this as `command`.  

 Next we define the valid value of a costcenter in the `run` block:

```
mock_provider "btp" {}

variables {
  globalaccount = "test"
}

run "provide_valid_costcenter" {
  command = plan

  variables {
    costcenter = "8523652147"
  }

}  

```

Finally we check if the variable is set as expected via an `assert` block that has the typical layout namely a condition and an error message if the condition is not met:

```
mock_provider "btp" {}

variables {
  globalaccount = "test"
}

run "provide_valid_costcenter" {
  command = plan

  variables {
    costcenter = "8523652147"
  }

  assert {
    condition     = var.costcenter == "8523652147"
    error_message = "Costcenter is not set correctly"
  }
}  

```

Okay, now we also want to provide an invalid value and check if an error is raised. To do so we add another `run` block but instead of an `assert` block we add an `expect_failures` block resulting in:

```
mock_provider "btp" {}

variables {
  globalaccount = "test"
}

run "provide_valid_costcenter" {
  command = plan

  variables {
    costcenter = "8523652147"
  }

  assert {
    condition     = var.costcenter == "8523652147"
    error_message = "Costcenter is not set correctly"
  }
}

run "provide_invalid_costcenter_with_letters" {
  command = plan

  variables {
    costcenter = "abc-123"
  }

  expect_failures = [
    var.costcenter
  ]
}  

```

Okay, so time to let `terraform test` do its magic. In the console we navigate to the `infra` directory and initialize the workspace:

```
terraform init -backend=false

```

Now we are set and can execute the tests:

```
terraform test

```

The output should look like this:

[![Terraform Test output of first unit test](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0o7he4vkz1n5ra8i5bj4.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F0o7he4vkz1n5ra8i5bj4.png)
This pattern can then be applied to the other validations present in the `variables.tf` file.

For the sake of exploring further let us switch to the `main.tf` file and test the local values. We want to test if the local value `project_subaccount_name` is set correctly. We create a new file called `local_project_subaccount_domain.tftest.hcl` in the `test` directory. We want to check that the local `project_subaccount_domain` has no empty spaces in it.

As before we mock the provider as we just want to test the local values and provide a dummy value for the `globalaccount` variable:

```
mock_provider "btp" {}

variables {
  globalaccount = "test"
}

```

This time we must provide all the variables that are used to construct the local value i.e. `org_name`, `project_name` and `stage`. We add the following variables to the file in a run block:

```
mock_provider "btp" {}

variables {
  globalaccount = "test"
}

run "validate_project_subaccount_domain" {
  command = plan

  variables {
    org_name     = "B2C"
    project_name = "proj 1234"
    stage        = "DEV"
  }
}

```

We intentionally keep an empty space in the `project_name` to validate the replacement. We also keep `stage` and `org_name` in capital letters to validate the transformation to lower case. Next we assert that the value for the local variable is set correctly:

```
mock_provider "btp" {}

variables {
  globalaccount = "test"
}

run "validate_project_subaccount_domain" {
  command = plan

  variables {
    org_name     = "B2C"
    project_name = "proj 1234"
    stage        = "DEV"
  }

  assert {
    condition     = local.project_subaccount_domain == "b2c-proj-1234-dev"
    error_message = "Local variable project_subaccount_domain is not transformed correctly."
  }
}

```

We can now execute the test as before:

```
terraform test

```

We get the following result:

[![Terraform test output of second unit test](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F16t86xuayov1kletl0ms.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F16t86xuayov1kletl0ms.png)
Great, we saw how we can do unit tests in an isolated way without the need to initialize the provider i.e. to authenticate against a real SAP BTP account.

As we want to execute the unit tests in a CI/CD pipeline we rename the `tests` directory to `unit-tests`. When doing so we must the testing framework explicitly to the right directory via the option `-test-directory`:

```
terraform test -test-directory=unit-tests

```

This allows us to create a GitHub Action that exclusively executes the unit tests. As the `terraform validate` command the `terraform test` command can return the test result in a machine readable format namely JSON. This can be used to further parse the test results in a CI/CD pipeline. A basic GitHub Action Workflow that executes the unit tests looks like this:

```
name: Terraform Unit Tests

on:
    pull_request:
      types:
        - opened
        - reopened
        - synchronize
        - ready_for_review
    workflow_dispatch:    

jobs:
    terraform-validate:
      name: Validate Syntax of Terraform Files
      runs-on: ubuntu-latest
      steps:
        - name: Checkout code
          uses: actions/checkout@v4

        - name: Setup Terraform
          uses: hashicorp/setup-terraform@v3
          with:
            terraform_wrapper: false

        - name: Execute Unit Tests
          shell: bash
          run: |
              cd ./infra
              terraform init -backend=false
              terraform test -test-directory=unit-tests 

```

We omitted the check for changed files in this workflow. Now let us move on to the next level of testing - the integration tests.

#####  Integration Tests

In contrast to the unit test setup, the integration test will interact with a backend and create real resources on the platform. The goal is to check if a given configuration creates a resource successfully. Be aware that this test should focus on your configuration. It makes no sense to test the provider itself with all its parameters. The test of the provider with all its parameters is done via the acceptance tests of the provider.

Keeping this in mind, we now want to write a test that the subaccount is created successfully by checking the `state` field of the newly created subaccount. We do not care about the entitlements, so we will mock the resource.

First we create a new directory `integration-tests` in the `infra` directory. In this directory we create a new file called `subaccount_creation.tftest.hcl`. As we want to test the resource for the subaccount we switch of the creation of the entitlements by adding a variable with an empty list of entitlements:

```
variables {
  entitlements = []
}

```

Next we add a run block that executes the `apply` command and provides the variable values for the subaccount:

```
variables {
  entitlements = []
}

run "test_successful_subaccount_creation" {
  command = apply

  variables {
    costcenter   = "1234567890"
    org_name     = "ECOMMERCE"
    project_name = "proj-0815"
    stage        = "TST"
    region       = "us10"
  }
}

```

With that we can now check for the state of the subaccount via a corresponding `assert` block:

```
variables {
  entitlements = []
}

run "test_successful_subaccount_creation" {
  command = apply

  variables {
    costcenter   = "1234567890"
    org_name     = "ECOMMERCE"
    project_name = "proj-0815"
    stage        = "TST"
    region       = "us10"
  }

  assert {
    condition     = resource.btp_subaccount.project.state == "OK"
    error_message = "The subaccount was not created in the expected state."
  }
}

```

Now we are good to go. In contrast to the unit test we now must provide valid values for the SAP BTP global account. We do so via the command line option `-var`. In addition, we must authenticate against the provider, which we will do by setting the corresponding environment variables for `BTP_USERNAME` and `BTP_PASSWORD`.

The command to execute the integration test finally looks like this:

```
terraform test -test-directory=integration-tests -var="globalaccount=yourgasubdomain"

```

The execution ow takes a bit longer as the subaccount is created on the SAP BTP. The final result should look like this:

[![Terraform test output of integration test](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F81pd1cyi68gc3rtysm9x.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F81pd1cyi68gc3rtysm9x.png)
The Terraform testing framework will try to remove all resources it created. Nevertheless things could go wrong and some resources might not get destroyed in the teardown of the test. This is clearly displayed in the output of the test, so you closely watch this especially when running the tests in the background via a CI/CD pipeline.

#####  Where is the code?

You find the code of the previous sections in the GitHub repository [Terraform Provider for SAP BTP - Quality Aspects](https://github.com/btp-automation-scenarios/terraform-quality).

####  Conclusion

In this blog post we learned that we can take the "as-Code" part of the "Infrastructure-as-Code" term seriously. We have seen several options how to safeguard the quality of our Terraform scripts by:

* Checking for proper formatting
* Validating the syntax of the scripts
* Adding Unit and Integration tests leveraging the Terraform testing framework

As cherry on top we can automate this in your CI/CD pipeline. The Terraform commands have been created with automation in mind and can return JSON objects that can be used for further action like automatic issue creation.

The `terraform test` command and the options of mocking resources and data sources enable a lot more than we have tried out here in this blog post. I highly recommend to take a closer look at the documentation and the blog post referenced before and play around with them. Be aware that this is a quite "young" functionality, so maybe you stumble over issues or might miss some features. If this is the case you definitely should open an issue in the corresponding [repository](https://github.com/hashicorp/terraform).

With that ... happy Terraforming and Testing!

####  [SAP BTP and Terraform (5 Part Series)](https://dev.to/lechnerc77/series/26908)

Reinvent your career. **Join DEV.**

It takes ***one minute*** and is worth it for your career.

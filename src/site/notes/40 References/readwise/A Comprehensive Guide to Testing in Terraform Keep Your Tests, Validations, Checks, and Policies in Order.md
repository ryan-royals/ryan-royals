---
{"dg-publish":true,"permalink":"/40-references/readwise/a-comprehensive-guide-to-testing-in-terraform-keep-your-tests-validations-checks-and-policies-in-order/","tags":["rw/articles"]}
---

![rw-book-cover](https://mattias.engineer/img/favicon/blue.png)
  
URL: https://mattias.engineer/posts/terraform-testing-and-validation/?mkt_tok=ODQ1LVpMRi0xOTEAAAGPci3QK6rMcySFH5kuD1iyw76fNRV2XYgAFnm6ymmeswiTB1sRRSni7ILSh_1pOE8qIzA4b3R48LO9lePo2iZZdt72i0_Bf4Hdztp-kUpwkD6gXmo
Author: mattias.engineer a blog about cloud architecture and development

## Summary

You have many options to use when it comes to testing and validating your Terraform configurations and modules. The newest addition to these options is the native Terraform testing framework. This in combination with custom conditions, check blocks, and policies allow for creating robust infrastructure-as-code. This post is a comprehensive guide to testing and validation in Terraform.

## Highlights added August 30, 2024 at 2:23 PM
>. These constrains could be to limit the length of a supplied string to less than ten characters, or to restrict the allowed values of a variable to a predefined list of values. Resources and data sources have the `lifecycle` block where you can add `precondition` and `postcondition` blocks to validate things before, and after, running an apply, respectively. Similarly, you can add `precondition` blocks to your `output` blocks, to validate something about the output value. ([View Highlight] (https://read.readwise.io/read/01hg6s3461nma2q6d635xgnarh))


>In the `precondition` block I check that the `managed_by` property of the resource group is set to the value `terraform`. If the `managed_by` property has any other value, the `condition` will evaluate to false and the `precondition` fails. The operation will halt and the `error_message` is displayed to the user in the console. ([View Highlight] (https://read.readwise.io/read/01hg6s7wjry1pcb4m7fdhsjnj5))


>Tests are written using HCL, so you do not need to learn a new language in order to test your IaC. Test files use the `.tftest.hcl` file ending.
>By default, all test files stored in the same directory as your module, or stored in a `tests` directory, are run when you issue the new `terraform test` command. If you place your tests in a different directory you can add the `-test-directory=path/to/my/test/directory` flag to the command. ([View Highlight] (https://read.readwise.io/read/01hhavh4nktk1yqeszf2qw35nm))


>A test file consists of one or more `run` blocks. Each `run` block should be thought of as a test. A `run` block includes a number of arguments and blocks to configure what the test should do. Each test executes a `command`, which is either `plan` or `apply`. If you do not specify the `command` argument it defaults to `apply`. ([View Highlight] (https://read.readwise.io/read/01hhavhexyfpgq7jkj74k09cxe))


>The concept of **checks** together with the `check` block was introduced in Terraform 1.5 and serve a purpose similar to custom validations for resources and data sources, but with one important difference. The `check` block is ideal for validations you want to make that should not stop a plan and apply from finishing. If a check fails the deployment will still continue. You will get a warning in the output indicating that the check failed. ([View Highlight] (https://read.readwise.io/read/01hhavj487c8fcc2p5h3w077s8))



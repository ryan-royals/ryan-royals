---
{"dg-publish":true,"permalink":"/40-references/readwise/keep-your-terragrunt-architecture-dry/","tags":["rw/articles"]}
---

![rw-book-cover](https://terragrunt.gruntwork.io/assets/img/terragrunt-thumbnail.png)
  
URL: https://terragrunt.gruntwork.io/docs/features/keep-your-terragrunt-architecture-dry/
Author: Terragrunt | Terraform wrapper

## Summary

Learn how to use multiple terragrunt configurations to DRY up your architecture.

## Highlights added July 17, 2024 at 11:02 AM
>To do this, we will introduce a new `env.hcl` configuration in each environment:
>└── live
>├── terragrunt.hcl
>├── _env
>│ ├── app.hcl
>│ ├── mysql.hcl
>│ └── vpc.hcl
>├── prod
>│ ├── env.hcl
>│ ├── app
>│ │ └── terragrunt.hcl
>│ ├── mysql
>│ │ └── terragrunt.hcl
>│ └── vpc
>│ └── terragrunt.hcl
>├── qa
>│ ├── env.hcl
>│ ├── app
>│ │ └── terragrunt.hcl
>│ ├── mysql
>│ │ └── terragrunt.hcl
>│ └── vpc
>│ └── terragrunt.hcl
>└── stage
>├── env.hcl
>├── app
>│ └── terragrunt.hcl
>├── mysql
>│ └── terragrunt.hcl
>└── vpc
>└── terragrunt.hcl
>The `env.hcl` configuration will look like the following:
>locals {
>env = "qa" # this will be prod in the prod folder, and stage in the stage folder.
>}
>We can then load the `env.hcl` file in the `_env/app.hcl` file to load the `env` string:
>locals {
># Load the relevant env.hcl file based on where terragrunt was invoked. This works because find_in_parent_folders
># always works at the context of the child configuration.
>env_vars = read_terragrunt_config(find_in_parent_folders("env.hcl"))
>env_name = local.env_vars.locals.env
>source_base_url = "github.com/<org>/modules.git//app"
>}
>dependency "vpc" {
>config_path = "../vpc"
>}
>dependency "mysql" {
>config_path = "../mysql"
>}
>inputs = {
>env = local.env_name
>basename = "example-app-${local.env_name}"
>vpc_id = dependency.vpc.outputs.vpc_id
>subnet_ids = dependency.vpc.outputs.subnet_ids
>mysql_endpoint = dependency.mysql.outputs.endpoint
>}
>With this configuration, `env_vars` is loaded based on which folder is being invoked. For example, when Terragrunt is invoked in the `prod/app/terragrunt.hcl` folder, `prod/env.hcl` is loaded, while `qa/env.hcl` is loaded when Terragrunt is invoked in the `qa/app/terragrunt.hcl` folder.
>Now we can clean up the child config to eliminate the `env` input variable since that is loaded in the `env.hcl` context:
>include "root" {
>path = find_in_parent_folders()
>}
>include "env" {
>path = "${get_terragrunt_dir()}/../../_env/app.hcl"
>expose = true
>}
># Construct the terraform.source attribute using the source_base_url and custom version v0.2.0
>terraform {
>source = "${include.env.locals.source_base_url}?ref=v0.2.0"
>} ([View Highlight] (https://read.readwise.io/read/01h1mvearm3zw6a5s0sct6b3yq))


># Roll out the change to the qa environment first terragrunt run-all plan --terragrunt-modules-that-include _env/app.hcl --terragrunt-working-dir qa terragrunt run-all apply --terragrunt-modules-that-include _env/app.hcl --terragrunt-working-dir qa # If the apply succeeds to qa, move on to the stage environment terragrunt run-all plan --terragrunt-modules-that-include _env/app.hcl --terragrunt-working-dir stage terragrunt run-all apply --terragrunt-modules-that-include _env/app.hcl --terragrunt-working-dir stage # And finally, prod. terragrunt run-all plan --terragrunt-modules-that-include _env/app.hcl --terragrunt-working-dir prod terragrunt run-all apply --terragrunt-modules-that-include _env/app.hcl --terragrunt-working-dir prod ([View Highlight] (https://read.readwise.io/read/01h1mvge4qc50sfzmayq9v4ctz))



---
{"dg-publish":true,"permalink":"/40-references/readwise/managing-workspaces-terraform-cli-terraform-hashi-corp-developer/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)
  
URL: https://developer.hashicorp.com/terraform/cli/workspaces
Author: State: Workspaces | Terraform | HashiCorp Developer

## Summary

Workspaces allow the use of multiple states with a single configuration directory.

## Highlights added August 30, 2024 at 2:23 PM
>Workspaces in the Terraform CLI refer to separate instances of [state data](https://developer.hashicorp.com/terraform/language/state) inside the same Terraform working directory. ([View Highlight] (https://read.readwise.io/read/01h4mwkzdbdzn5yhk5nb229zac))


>Workspaces can be helpful for specific [use cases](https://developer.hashicorp.com/terraform/cli/workspaces#use-cases), but they are not required to use the Terraform CLI. We recommend using [alternative approaches](https://developer.hashicorp.com/terraform/cli/workspaces#alternatives-to-workspaces) for complex deployments requiring separate credentials and access controls. ([View Highlight] (https://read.readwise.io/read/01h4mwmj7rs4080wgpgf7xyr0r))


>Every [initialized working directory](https://developer.hashicorp.com/terraform/cli/init) starts with one workspace named `default`. ([View Highlight] (https://read.readwise.io/read/01h4mwqs7xa345saxz482137rs))


>Use the [`terraform workspace list`](https://developer.hashicorp.com/terraform/cli/commands/workspace/list), [`terraform workspace new`](https://developer.hashicorp.com/terraform/cli/commands/workspace/new), and [`terraform workspace delete`](https://developer.hashicorp.com/terraform/cli/commands/workspace/delete) commands to manage the available workspaces in the current working directory. ([View Highlight] (https://read.readwise.io/read/01h4mwqnqn41yqk16tmdv5mgax))


>A common use for multiple workspaces is to create a parallel, distinct copy of a set of infrastructure to test a set of changes before modifying production infrastructure. ([View Highlight] (https://read.readwise.io/read/01h4mwq407dmpfc7fqzgd90st4))


>Workspaces are technically equivalent to renaming your state file. Terraform then includes a set of protections and support for remote state. ([View Highlight] (https://read.readwise.io/read/01h4mwrn3s6bbww10hj8g22s67))



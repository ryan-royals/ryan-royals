---
{"dg-publish":true,"permalink":"/40-references/readwise/style-guide-configuration-language-terraform-hashi-corp-developer/","tags":["rw/articles"]}
---

![40 References/attachments/c0fb08bec0d76da667154a80cf2860e7_MD5.jpg](/img/user/40%20References/attachments/c0fb08bec0d76da667154a80cf2860e7_MD5.jpg)
  
URL: https://developer.hashicorp.com/terraform/language/style
Author: Style Guide - Configuration Language | Terraform | HashiCorp Developer

## Summary

Terraform's configuration language offers flexibility for writing code and structuring directories. Adopting a style guide helps maintain readability and consistency. Following recommended style conventions improves code maintenance and organization.

## Highlights added August 30, 2024 at 2:23 PM
>Use `count` and `for_each` sparingly. ([View Highlight] (https://read.readwise.io/read/01hv5qypqwqfpm438fm5eeh4e9))


>Multiple environments
>We recommend that your repository's `main` branch be the source of truth for all environments. For Terraform Cloud and Terraform Enterprise users, we recommend that you use separate workspaces for each environment. For larger codebases, we recommend that you split your resources across multiple workspaces to prevent large state files and limit unintended consequences from changes. For example, you could structure your code as follows:
>.
>├── compute
>│ ├── main.tf
>│ ├── outputs.tf
>│ └── variables.tf
>├── database
>│ ├── main.tf
>│ ├── outputs.tf
>│ └── variables.tf
>└── networking
>├── main.tf
>├── outputs.tf
>└── variables.tf
>. ([View Highlight] (https://read.readwise.io/read/01hv5r4kbt7brhdmgz8f4peswf))


>If you do not use Terraform Cloud or Terraform Enterprise, we recommend that you use modules to encapsulate your configuration, and use a directory for each environment so that each one has a separate state file. The configuration in each of these directories would call the local modules, each with parameters specific to their environment. This also lets you maintain separate variable and backend configurations for each environment. ([View Highlight] (https://read.readwise.io/read/01hv5rdcrvvd8edvxt8tv90h35))



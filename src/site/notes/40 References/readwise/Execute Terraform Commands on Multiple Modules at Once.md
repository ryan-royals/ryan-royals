---
{"dg-publish":true,"permalink":"/40-references/readwise/execute-terraform-commands-on-multiple-modules-at-once/","tags":["rw/articles"]}
---

![rw-book-cover](https://terragrunt.gruntwork.io/assets/img/terragrunt-thumbnail.png)

## Full Document
[[40 References/readwise/Full Document Contents/Execute Terraform Commands on Multiple Modules at Once\|Readwise/Full Document Contents/Execute Terraform Commands on Multiple Modules at Once.md]]

## Highlights
Terragrunt will return an error indicating the dependency hasn’t been applied yet if the terraform module managed by the terragrunt config referenced in a `dependency` block has not been applied yet. This is because you cannot actually fetch outputs out of an unapplied Terraform module, even if there are no resources being created in the module. ([View Highlight] (https://read.readwise.io/read/01h1n1er6srated02phcnh0q5k))



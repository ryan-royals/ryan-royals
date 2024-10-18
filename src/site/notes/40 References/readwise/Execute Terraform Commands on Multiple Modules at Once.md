---
{"dg-publish":true,"permalink":"/40-references/readwise/execute-terraform-commands-on-multiple-modules-at-once/","tags":["rw/articles"]}
---

![40 References/attachments/28ebf92cae21c1d5609988233f4c0d58_MD5.jpg](/img/user/40%20References/attachments/28ebf92cae21c1d5609988233f4c0d58_MD5.jpg)
  
URL: https://terragrunt.gruntwork.io/docs/features/execute-terraform-commands-on-multiple-modules-at-once/#dependencies-between-modules
Author: Terragrunt | Terraform wrapper

## Summary

Learn how to avoid tedious tasks of running commands on each module separately.

## Highlights added August 30, 2024 at 2:23 PM
>Terragrunt will return an error indicating the dependency hasn’t been applied yet if the terraform module managed by the terragrunt config referenced in a `dependency` block has not been applied yet. This is because you cannot actually fetch outputs out of an unapplied Terraform module, even if there are no resources being created in the module. ([View Highlight] (https://read.readwise.io/read/01h1n1er6srated02phcnh0q5k))



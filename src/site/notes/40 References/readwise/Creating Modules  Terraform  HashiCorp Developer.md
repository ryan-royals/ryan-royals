---
{"dg-publish":true,"permalink":"/40-references/readwise/creating-modules-terraform-hashi-corp-developer/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)

## Full Document
[[40 References/readwise/Full Document Contents/Creating Modules  Terraform  HashiCorp Developer\|Readwise/Full Document Contents/Creating Modules  Terraform  HashiCorp Developer.md]]

## Highlights
We *do not* recommend writing modules that are just thin wrappers around single other resource types. If you have trouble finding a name for your module that isn't the same as the main resource type inside it, that may be a sign that your module is not creating any new abstraction and so the module is adding unnecessary complexity. Just use the resource type directly in the calling module instead. ([View Highlight] (https://read.readwise.io/read/01hbwfqyk5dhae8a7qfem4x1b6))



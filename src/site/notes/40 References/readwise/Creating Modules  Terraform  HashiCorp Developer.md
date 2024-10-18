---
{"dg-publish":true,"permalink":"/40-references/readwise/creating-modules-terraform-hashi-corp-developer/","tags":["rw/articles"]}
---

![40 References/attachments/c0fb08bec0d76da667154a80cf2860e7_MD5.jpg](/img/user/40%20References/attachments/c0fb08bec0d76da667154a80cf2860e7_MD5.jpg)
  
URL: https://developer.hashicorp.com/terraform/language/modules/develop#when-to-write-a-module
Author: Creating Modules | Terraform | HashiCorp Developer

## Summary

Modules are containers for multiple resources that are used together in a configuration. Learn when to create modules and about module structure.

## Highlights added August 30, 2024 at 2:23 PM
>We *do not* recommend writing modules that are just thin wrappers around single other resource types. If you have trouble finding a name for your module that isn't the same as the main resource type inside it, that may be a sign that your module is not creating any new abstraction and so the module is adding unnecessary complexity. Just use the resource type directly in the calling module instead. ([View Highlight] (https://read.readwise.io/read/01hbwfqyk5dhae8a7qfem4x1b6))



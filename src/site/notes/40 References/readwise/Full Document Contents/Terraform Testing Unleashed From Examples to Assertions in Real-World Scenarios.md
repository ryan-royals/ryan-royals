---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-testing-unleashed-from-examples-to-assertions-in-real-world-scenarios/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/da:true/resize:fit:1200/0*fJjTcqClbEOMCQk_)

Terraform’s [test](https://developer.hashicorp.com/terraform/cli/commands/test) command, introduced in version 1.6.0, opens up the possibility to integrate testing directly within [Terraform configurations](https://developer.hashicorp.com/terraform/language/tests). This feature allows module developers to verify functionality, ensure compatibility, and simulate different scenarios that the module might encounter.

Like in traditional software development, when writing a Unit Test you can have some code that executes before the test is executed. This is often called “Test Setup” or “Test Initialization” and it prepares the test runtime with the necessary in-memory state to execute your Unit Tests. In traditional programming, that means loading certain values into memory, creating mock objects that override very specific methods to avoid spending unnecessary time or adding unnecessary dependencies on external components.

However, in Terraform that means provisioning the pre-requisite resources that you need in order to execute your test. Just like in traditional programming, a lot of this depends on on what your module does and how you have designed its scope.

For example, if your module provisions a Virtual Machine, you would likely need to set up a Virtual Network with a subnet and some default settings to allow your virtual machine to be created.

Likewise, if your module provisions a Virtual Machine Extension, that expects to be attached to a Virtual Machine, then you would need to provision a Virtual Machine that you…

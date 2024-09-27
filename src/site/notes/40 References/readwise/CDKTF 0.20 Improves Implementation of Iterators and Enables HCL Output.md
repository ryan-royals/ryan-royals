---
{"dg-publish":true,"permalink":"/40-references/readwise/cdktf-0-20-improves-implementation-of-iterators-and-enables-hcl-output/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1704908313-share-cdktf-0-20-improves-implementation-of-iterators-and-enables-hcl-output.png?w=1200&h=630&fit=crop&auto=format)
  
URL: https://www.hashicorp.com/blog/cdktf-0-20-improves-implementation-of-iterators-and-enables-hcl-output
Author: Mutahhir Ali Hayat

## Summary

CDKTF 0.20 is released and includes improvements to iterators and enables HCL output. The new iterator support allows developers to handle more complex cases where resources are created based on data known only at runtime. The improvements include chaining iterators, complex list iterators, and support mapping to primitive values. CDKTF 0.20 also introduces the ability to output in HCL format, making it easier to read and debug the configuration. Additionally, error messages in the CDKTF package have been improved to provide more context and propose solutions.

## Highlights added August 30, 2024 at 2:23 PM
>Output HCL instead of Terraform JSON
>CDKTF synth now supports HCL as an output, in addition to the Terraform JSON which was previously supported. This makes it easier to debug the configuration that CDKTF creates, as HCL output is easier for people to read.
>Moreover, this means you can use CDKTF as a templating engine to generate a Terraform config that will then be used and edited by other teams. Finally, it means you can now use CDKTF with tooling that supports only Terraform HCL. Although Terraform Cloud’s native features, like policy evaluation and health assessments, work with JSON, other common tools, like code scanners and linters, support only HCL. ([View Highlight] (https://read.readwise.io/read/01hktj0qkkmm40st8gxjetcbqc))



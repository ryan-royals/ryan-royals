---
{"dg-publish":true,"permalink":"/40-references/readwise/the-lifecycle-meta-argument/","tags":["rw/articles"]}
---

![40 References/attachments/c0fb08bec0d76da667154a80cf2860e7_MD5.jpg](/img/user/40%20References/attachments/c0fb08bec0d76da667154a80cf2860e7_MD5.jpg)
  
URL: https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#replace_triggered_by
Author: The lifecycle Meta-Argument - Configuration Language | Terraform | HashiCorp Developer

## Summary

The meta-arguments in a lifecycle block allow you to customize resource behavior.

## Highlights added August 30, 2024 at 2:23 PM
>[`replace_triggered_by`](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#replace_triggered_by) (list of resource or attribute references) - *Added in Terraform 1.2.* Replaces the resource when any of the referenced items change. Supply a list of expressions referencing managed resources, instances, or instance attributes. When used in a resource that uses `count` or `for_each`, you can use `count.index` or `each.key` in the expression to reference specific instances of other resources that are configured with the same count or collection. ([View Highlight] (https://read.readwise.io/read/01h4nbddr97ast4wzmz7n3wcvt))


>References trigger replacement in the following conditions:
>• If the reference is to a resource with multiple instances, a plan to update or replace any instance will trigger replacement.
>• If the reference is to a single resource instance, a plan to update or replace that instance will trigger replacement.
>• If the reference is to a single attribute of a resource instance, any change to the attribute value will trigger replacement. ([View Highlight] (https://read.readwise.io/read/01h4nbdgdn1ez38akztjdfznnb))



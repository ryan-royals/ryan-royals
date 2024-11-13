---
{"dg-publish":true,"permalink":"/40-references/readwise/the-lifecycle-meta-argument/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)

## Summary

The meta-arguments in a lifecycle block allow you to customize resource behavior.

## Highlights

[`replace_triggered_by`](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#replace_triggered_by) (list of resource or attribute references) - *Added in Terraform 1.2.* Replaces the resource when any of the referenced items change. Supply a list of expressions referencing managed resources, instances, or instance attributes. When used in a resource that uses `count` or `for_each`, you can use `count.index` or `each.key` in the expression to reference specific instances of other resources that are configured with the same count or collection. ([View Highlight] (https://read.readwise.io/read/01h4nbddr97ast4wzmz7n3wcvt))


References trigger replacement in the following conditions:
• If the reference is to a resource with multiple instances, a plan to update or replace any instance will trigger replacement.
• If the reference is to a single resource instance, a plan to update or replace that instance will trigger replacement.
• If the reference is to a single attribute of a resource instance, any change to the attribute value will trigger replacement. ([View Highlight] (https://read.readwise.io/read/01h4nbdgdn1ez38akztjdfznnb))



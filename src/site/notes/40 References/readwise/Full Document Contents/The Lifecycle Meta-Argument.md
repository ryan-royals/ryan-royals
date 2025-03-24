---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/the-lifecycle-meta-argument/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)

The [Resource Behavior](https://developer.hashicorp.com/terraform/language/resources/behavior) page describes the general lifecycle for resources. Some details of that behavior can be customized using the special nested `lifecycle` block within a resource block body:

#### 

`lifecycle` is a nested block that can appear within a resource block. The `lifecycle` block and its contents are meta-arguments, available for all `resource` blocks regardless of type.

The arguments available within a `lifecycle` block are `create_before_destroy`, `prevent_destroy`, `ignore_changes`, and `replace_triggered_by`.

* [`create_before_destroy`](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#create_before_destroy) (bool) - By default, when Terraform must change a resource argument that cannot be updated in-place due to remote API limitations, Terraform will instead destroy the existing object and then create a new replacement object with the new configured arguments.

The `create_before_destroy` meta-argument changes this behavior so that the new replacement object is created *first,* and the prior object is destroyed after the replacement is created.

This is an opt-in behavior because many remote object types have unique name requirements or other constraints that must be accommodated for both a new and an old object to exist concurrently. Some resource types offer special options to append a random suffix onto each object name to avoid collisions, for example. Terraform CLI cannot automatically activate such features, so you must understand the constraints for each resource type before using `create_before_destroy` with it.

Destroy provisioners of this resource do not run if `create_before_destroy` is set to `true`. This [GitHub issue](https://github.com/hashicorp/terraform/issues/13549) contains more details.
* [`prevent_destroy`](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#prevent_destroy) (bool) - This meta-argument, when set to `true`, will cause Terraform to reject with an error any plan that would destroy the infrastructure object associated with the resource, as long as the argument remains present in the configuration.

This can be used as a measure of safety against the accidental replacement of objects that may be costly to reproduce, such as database instances. However, it will make certain configuration changes impossible to apply, and will prevent the use of the `terraform destroy` command once such objects are created, and so this option should be used sparingly.

Since this argument must be present in configuration for the protection to apply, note that this setting does not prevent the remote object from being destroyed if the `resource` block were removed from configuration entirely: in that case, the `prevent_destroy` setting is removed along with it, and so Terraform will allow the destroy operation to succeed.
* [`ignore_changes`](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#ignore_changes) (list of attribute names) - By default, Terraform detects any difference in the current settings of a real infrastructure object and plans to update the remote object to match configuration.

The `ignore_changes` feature is intended to be used when a resource is created with references to data that may change in the future, but should not affect said resource after its creation. In some rare cases, settings of a remote object are modified by processes outside of Terraform, which Terraform would then attempt to "fix" on the next run. In order to make Terraform share management responsibilities of a single object with a separate process, the `ignore_changes` meta-argument specifies resource attributes that Terraform should ignore when planning updates to the associated remote object.

The arguments corresponding to the given attribute names are considered when planning a *create* operation, but are ignored when planning an *update*. The arguments are the relative address of the attributes in the resource. Map and list elements can be referenced using index notation, like `tags["Name"]` and `list[0]` respectively.

```
    ignore_changes = [

```
Instead of a list, the special keyword `all` may be used to instruct Terraform to ignore *all* attributes, which means that Terraform can create and destroy the remote object but will never propose updates to it.

Only attributes defined by the resource type can be ignored. `ignore_changes` cannot be applied to itself or to any other meta-arguments.
* [`replace_triggered_by`](https://developer.hashicorp.com/terraform/language/meta-arguments/lifecycle#replace_triggered_by) (list of resource or attribute references) - *Added in Terraform 1.2.* Replaces the resource when any of the referenced items change. Supply a list of expressions referencing managed resources, instances, or instance attributes. When used in a resource that uses `count` or `for_each`, you can use `count.index` or `each.key` in the expression to reference specific instances of other resources that are configured with the same count or collection.

References trigger replacement in the following conditions:

	+ If the reference is to a resource with multiple instances, a plan to update or replace any instance will trigger replacement.
	+ If the reference is to a single resource instance, a plan to update or replace that instance will trigger replacement.
	+ If the reference is to a single attribute of a resource instance, any change to the attribute value will trigger replacement.You can only reference managed resources in `replace_triggered_by` expressions. This lets you modify these expressions without forcing replacement.

```
    replace_triggered_by = [

```
`replace_triggered_by` allows only resource addresses because the decision is based on the planned actions for all of the given resources. Plain values such as local values or input variables do not have planned actions of their own, but you can treat them with a resource-like lifecycle by using them with [the `terraform_data` resource type](https://developer.hashicorp.com/terraform/language/resources/terraform-data).

#### 

You can add `precondition` and `postcondition` blocks with a `lifecycle` block to specify assumptions and guarantees about how resources and data sources operate. The following examples creates a precondition that checks whether the AMI is properly configured.

```
      condition     = data.aws_ami.example.architecture == "x86_64"

```

Custom conditions can help capture assumptions, helping future maintainers understand the configuration design and intent. They also return useful information about errors earlier and in context, helping consumers more easily diagnose issues in their configurations.

Refer to [Custom Conditions](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#preconditions-and-postconditions) for more details.

#### 

The `lifecycle` settings all affect how Terraform constructs and traverses the dependency graph. As a result, only literal values can be used because the processing happens too early for arbitrary expression evaluation.

[Edit this page on GitHub](https://github.com/hashicorp/terraform/blob/main/website/docs/language/meta-arguments/lifecycle.mdx)

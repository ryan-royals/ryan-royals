---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/refactoring-terraform-hashi-corp-developer/","tags":["rw/articles"]}
---

![rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)

**Note:** Explicit refactoring declarations with `moved` blocks is available in Terraform v1.1 and later. For earlier Terraform versions or for refactoring actions too complex to express as `moved` blocks, you can use the [`terraform state mv` CLI command](https://developer.hashicorp.com/terraform/cli/commands/state/mv) as a separate step.

In shared modules and long-lived configurations, you may eventually outgrow your initial module structure and resource names. For example, you might decide that what was previously one child module makes more sense as two separate modules and move a subset of the existing resources to the new one.

Terraform compares previous state with new configuration, correlating by each module or resource's unique address. Therefore *by default* Terraform understands moving or renaming an object as an intent to destroy the object at the old address and to create a new object at the new address.

When you add `moved` blocks in your configuration to record where you've historically moved or renamed an object, Terraform treats an existing object at the old address as if it now belongs to the new address.

A `moved` block expects no labels and contains only `from` and `to` arguments:

The example above records that the resource currently known as `aws_instance.b` was known as `aws_instance.a` in a previous version of this module.

Before creating a new plan for `aws_instance.b`, Terraform first checks whether there is an existing object for `aws_instance.a` recorded in the state. If there is an existing object, Terraform renames that object to `aws_instance.b` and then proceeds with creating a plan. The resulting plan is as if the object had originally been created at `aws_instance.b`, avoiding any need to destroy it during apply.

The `from` and `to` addresses both use a special addressing syntax that allows selecting modules, resources, and resources inside child modules. Below, we describe several refactoring use-cases and the appropriate addressing syntax for each situation.

Consider this example module with a resource configuration:

```
  count = 2

```

Applying this configuration for the first time would cause Terraform to create `aws_instance.a[0]` and `aws_instance.a[1]`.

If you later choose a different name for this resource, then you can change the name label in the `resource` block and record the old name inside a `moved` block:

```
  count = 2

```

When creating the next plan for each configuration using this module, Terraform treats any existing objects belonging to `aws_instance.a` as if they had been created for `aws_instance.b`: `aws_instance.a[0]` will be treated as `aws_instance.b[0]`, and `aws_instance.a[1]` as `aws_instance.b[1]`.

New instances of the module, which *never* had an `aws_instance.a`, will ignore the `moved` block and propose to create `aws_instance.b[0]` and `aws_instance.b[1]` as normal.

Both of the addresses in this example referred to a resource as a whole, and so Terraform recognizes the move for all instances of the resource. That is, it covers both `aws_instance.a[0]` and `aws_instance.a[1]` without the need to identify each one separately.

Each resource type has a separate schema and so objects of different types are not compatible. Therefore, although you can use `moved` to change the name of a resource, you *cannot* use `moved` to change to a different resource type or to change a managed resource (a `resource` block) into a data resource (a `data` block).

Consider this example module containing a single-instance resource:

Applying this configuration would lead to Terraform creating an object bound to the address `aws_instance.a`.

Later, you use [`for_each`](https://developer.hashicorp.com/terraform/language/meta-arguments/for_each) with this resource to systematically declare multiple instances. To preserve an object that was previously associated with `aws_instance.a` alone, you must add a `moved` block to specify which instance key the object will take in the new configuration:

```
  instances = tomap({
    small = {

  to   = aws_instance.a["small"]

```

The above will keep Terraform from planning to destroy any existing object at `aws_instance.a`, treating that object instead as if it were originally created as `aws_instance.a["small"]`.

When at least one of the two addresses includes an instance key, like `["small"]` in the above example, Terraform understands both addresses as referring to specific *instances* of a resource rather than the resource as a whole. That means you can use `moved` to switch between keys and to add and remove keys as you switch between `count`, `for_each`, or neither.

The following are some other examples of valid `moved` blocks that record changes to resource instance keys in a similar way:

```
  from = aws_instance.b["small"]
  to   = aws_instance.b["tiny"]

  from = aws_instance.c[0]
  to   = aws_instance.c["small"]
  from = aws_instance.c[1]
  to   = aws_instance.c["tiny"]

  from = aws_instance.d[2]

```

**Note:** When you add `count` to an existing resource that didn't use it, Terraform automatically proposes to move the original object to instance zero, unless you write an `moved` block explicitly mentioning that resource. However, we recommend still writing out the corresponding `moved` block explicitly, to make the change clearer to future readers of the module.

You can rename a call to a module in a similar way as renaming a resource. Consider the following original module version:

```
  source = "../modules/example"

```

When applying this configuration, Terraform would prefix the addresses for any resources declared in this module with the module path `module.a`. For example, a resource `aws_instance.example` would have the full address `module.a.aws_instance.example`.

If you later choose a better name for this module call, then you can change the name label in the `module` block and record the old name inside a `moved` block:

```
  source = "../modules/example"

  from = module.a
  to   = module.b

```

When creating the next plan for each configuration using this module, Terraform will treat any existing object addresses beginning with `module.a` as if they had instead been created in `module.b`. `module.a.aws_instance.example` would be treated as `module.b.aws_instance.example`.

Both of the addresses in this example referred to a module call as a whole, and so Terraform recognizes the move for all instances of the call. If this module call used `count` or `for_each` then it would apply to all of the instances, without the need to specify each one separately.

Consider this example of a single-instance module:

```
  source = "../modules/example"

```

Applying this configuration would cause Terraform to create objects whose addresses begin with `module.a`.

In later module versions, you may need to use [`count`](https://developer.hashicorp.com/terraform/language/meta-arguments/count) with this resource to systematically declare multiple instances. To preserve an object that was previously associated with `aws_instance.a` alone, you can add a `moved` block to specify which instance key that object will take in the new configuration:

```
  source = "../modules/example"
  count  = 3

  from = module.a
  to   = module.a[2]

```

The configuration above directs Terraform to treat all objects in `module.a` as if they were originally created in `module.a[2]`. As a result, Terraform plans to create new objects only for `module.a[0]` and `module.a[1]`.

When at least one of the two addresses includes an instance key, like `[2]` in the above example, Terraform will understand both addresses as referring to specific *instances* of a module call rather than the module call as a whole. That means you can use `moved` to switch between keys and to add and remove keys as you switch between `count`, `for_each`, or neither.

For more examples of recording moves associated with instances, refer to the similar section [Enabling `count` and `for_each` For a Resource](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#enabling-count-or-for_each-for-a-resource).

### Splitting One Module into Multiple

As a module grows to support new requirements, it might eventually grow big enough to warrant splitting into two separate modules.

You can split this into two modules as follows:

To achieve this refactoring without replacing existing objects bound to the old resource addresses, you must:

1. Write module "x", copying over the two resources it should contain.
2. Write module "y", copying over the one resource it should contain.
3. Edit the original module to no longer include any of these resources, and instead to contain only shim configuration to migrate existing users.

The new modules "x" and "y" should contain only `resource` blocks:

The original module, now only a shim for backward-compatibility, calls the two new modules and indicates that the resources moved into them:

```
  source = "../modules/x"

  source = "../modules/y"

```

When an existing user of the original module upgrades to the new "shim" version, Terraform notices these three `moved` blocks and behaves as if the objects associated with the three old resource addresses were originally created inside the two new modules.

New users of this family of modules may use either the combined shim module *or* the two new modules separately. You may wish to communicate to your existing users that the old module is now deprecated and so they should use the two separate modules for any new needs.

The multi-module refactoring situation is unusual in that it violates the typical rule that a parent module sees its child module as a "closed box", unaware of exactly which resources are declared inside it. This compromise assumes that all three of these modules are maintained by the same people and distributed together in a single [module package](https://developer.hashicorp.com/terraform/language/modules/sources#modules-in-package-sub-directories).

Terraform resolves module references in `moved` blocks relative to the module instance they are defined in. For example, if the original module above were already a child module named `module.original`, the reference to `module.x.aws_instance.a` would resolve as `module.original.module.x.aws_instance.a`. A module may only make `moved` statements about its own objects and objects of its child modules.

If you need to refer to resources within a module that was called using `count` or `for_each` meta-arguments, you must specify a specific instance key to use in order to match with the new location of the resource configuration:

```
  to   = module.new[2].aws_instance.example

```

Over time, a long-lasting module may accumulate many `moved` blocks.

Removing a `moved` block is a generally breaking change because any configurations that refer to the old address will plan to delete that existing object instead of move it. We strongly recommend that you retain all historical `moved` blocks from earlier versions of your modules to preserve the upgrade path for users of any previous version.

If you do decide to remove `moved` blocks, proceed with caution. It can be safe to remove `moved` blocks when you are maintaining private modules within an organization and you are certain that all users have successfully run `terraform apply` with your new module version.

If you need to rename or move the same object twice, we recommend documenting the full history using *chained* `moved` blocks, where the new block refers to the existing block:

Recording a sequence of moves in this way allows for successful upgrades for both configurations with objects at `aws_instance.a` *and* configurations with objects at `aws_instance.b`. In both cases, Terraform treats the existing object as if it had been originally created as `aws_instance.c`.

[Edit this page on GitHub](https://github.com/hashicorp/terraform/blob/main/website/docs/language/modules/develop/refactoring.mdx)

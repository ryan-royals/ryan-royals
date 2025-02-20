---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terra-do-s-and-terra-don-ts-a-few-common-issues-with-terraform-iterables-and-how-to-avoid-them/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1024/1*RnOPBlinHbVJ00pVSyDg9g.png)

Improper iteration over resources, data sources and modules is one of the most common issues I observe when teaching Terraform. In the remainder of the article, I will refer to these objects as Terraform’s *configuration iterables,* or *iterables* in short.

In particular, most of the struggles are related to:

1. the usage of `count` vs. `for_each`
2. conditional iterable creation
3. passing information between Terraform iterables
4. module design

Fixing these issues usually requires you to refactor your code, which, depending on the size of your codebase, can be quite tedious. In this article, I will briefly describe the core issue at hand with a few simple examples, and offer some recommendations on how to avoid them.

![A collection of rocket iterables ready to Terraform distant planets](https://miro.medium.com/v2/resize:fit:700/1*RnOPBlinHbVJ00pVSyDg9g.png)A collection of rockets ready to terraform distant planets. 
### Usage of count vs. for\_each

There has already been written quite some words on the subject of `count` vs. `for_each`, and also the official Terraform documentation has a dedicated section to the usage of both meta-arguments. The gist of it: `count` was introduced before `for_each`, and is conceptually simpler, but that simplicity comes at a cost. Consider the following piece of code, in which an `aws_s3_bucket` for a list of users is configured:

```
locals {  
 users = ["Alice", "Bob", "Charlie"]  
}  
  
### Iterate with count  
resource "aws_s3_bucket" "user_bucket" {  
 count = length(local.users)  
 bucket = "working-bucket-${local.users[count.index]}"  
}  
  
### Iterate with for_each  
resource "aws_s3_bucket" "user_bucket" {  
 for_each = toset(local.users)  
 bucket = "working-bucket-${each.key}"  
}
```

Both examples look simple enough, but what happens when you swap Alice and Bob in the `users` list? In the first example, Terraform identifies each configuration by the index of the `count` object during the iteration. Terraform creates internally a mapping between that index and the configuration (which I’ve simplified in the following snippet as just the bucket name argument) associated with that index:

```
aws_s3_bucket.user_bucket[0] => "working-bucket-${local.users[0]}" // Alice  
aws_s3_bucket.user_bucket[1] => "working-bucket-${local.users[1]}" // Bob  
aws_s3_bucket.user_bucket[2] => "working-bucket-${local.users[2]}" // Charlie
```

If you change the ordering of the users in the list, the intent is still the same: you still expect to have three buckets for your three users. Terraform, however, sees that the bucket name associated with some or all of the indices has changed. And changing a bucket name triggers a recreate: it will delete the old bucket, and create a new one. Luckily the AWS provider has additional protection built in for some of the resources for which there is a risk of data loss, but not all providers are equally protective (looking at you, Azure).

In the `for_each` example, the identifier that Terraform uses is also used to configure the resource:

```
aws_s3_bucket.user_bucket["Alice"] => "working-bucket-${each.key}" // Alice  
aws_s3_bucket.user_bucket["Bob"] => "working-bucket-${each.key}" // Bob  
aws_s3_bucket.user_bucket["Charlie"] => "working-bucket-${each.key}" // Charlie
```

You can permute the user list all we want, the configuration attributes are tightly linked to the identifier of the configuration, the user name. Terraform is therefore unaware of any changes to the configuration, and does exactly what you expect it to do: nothing.

As a rule of thumb: use `for_each` by default, and `count` if and only if the resource doesn’t have any specific configuration; the usage of `count.index` to index a list is often a code smell, and you should probably use `for_each` instead.

### All or nothing: conditional creation of iterables

The one exception to this rule of thumb that I usually teach, is when there should be exactly one instance a resource, or it shouldn’t exist at all:

```
variable "requires_x" {  
 type = bool  
 default = false  
}  
  
resource "X" "Y" {  
 count = var.requires_x? 1 : 0  
}
```

Terraform's ternary operator for conditional expressions evaluates to 1 when the variable `requires_x` evaluates to `true` and to 0 when it evaluates to `false`. And when the count equals zero, nothing is created. Simple. Quite elegant.

You could also write the same logic with `for_each` as

```
variable "requires_x" {  
 type = bool  
 default = false  
}  
  
resource "X" "Y" {  
 for_each = var.requires_x? toset(["✅"]): null  
}
```

but I think few people would agree that this is better than the first example. The key is arbitrary (any utf-8 string will do), and you need the `to_set` function call, as set literals are not part of the language.

Still, the usage of `count` suffers from a similar drawback as described in the first section: what if there are additional configurable arguments in the configuration that you want to offer as a variable to the consumers of a module? Naïvely, you could pass those as additional input variables:

```
variable "requires_x" {  
 type = bool  
 default = false  
}  
  
variable "x_attributes" {  
 type = object({u = …, v = …, w = …})  
 …  
}  
  
resource "X" "Y" {  
 count = var.requires_x? 1 : 0  
 u = var.x_attributes.u  
 v = var.x_attributes.v  
 w = var.x_attribute.w  
}
```

It would work, sure, but it becomes quite cumbersome and needlessly complex for a larger number of configurable arguments.

Also, it violates another best practice: packaging related information together. Doing so will allow you to constrain information so that users of your module are less likely “to hold it wrong”. For example: users shouldn’t be able to pass the `x_attributes` variable when `requires_x` is `false`; the next snippet, which tries to validate a variable based on another variable, however, is [not supported by the language](https://github.com/hashicorp/terraform/issues/25609):

```
variable "requires_x" {  
 type = bool  
 default = false  
}  
  
variable "x_attributes" {  
 default = null  
  
 validation {  
   condition = (!var.requires_x) && (var.x_attributes != null)  
   error_message = "Attributes should not be configured when x is not required."  
 }  
  
}  
resource "X" "Y" {  
 count = var.requires_x? 1 : 0  
 z = var.x_attribute_z  
}
```

A better solution would be to ditch the conditional altogether, and use a map or object variable (or a set variable, but in the second part of the article you'll see why that also potentially has some issues), which can provide more information than just a boolean flag:

```
variable "x" {  
 default = {}  
 type = object({config=object({z=string})})  
}  
  
resource "X" "Y" {  
 for_each = var.x  
 z = each.value.z  
}
```

The variable `x` is constrained to be an object instead of a map to ensure that the module user provides exactly one configuration via the `config` attribute. Any other keys passed to the input variable `x` will be ignored. With a map type, Terraform would iterate over all keys of the map, which is useful when you have an arbitrary number `N` of configurations, but not when you want to limit them to 0 or *exactly* `N` configs (in this case `N=1`, but note that you can easily generalize this for any fixed `N`). Alternatively, you could also allow the user to pass a map as input, and add a validation to ensure there exactly `N` configurations. This has the advantage that the user is notified when they are trying to use the module incorrectly.

### Passing information between iterables

Another common scenario is an iterable which has (calculated) attributes that need to be passed to another iterable, either directly within the same module, or indirectly, through input variables of a submodule.

Let’s upgrade the first example a bit. AWS uses a global namespace for S3 bucket names, so each bucket needs to have a unique name. You can avoid name collisions by adding a random string to the bucket name, as follows:

```
locals {  
 users = toset(["Alice", "Bob", "Charlie"])  
}  
resource "random_string" "random" {  
 for_each = local.users  
 length = 8  
 special = false  
 upper = false  
}  
  
resource "aws_s3_bucket" "user_bucket" {  
 for_each = random_string.random  
 bucket = "user-bucket-${each.value.id}"  
}
```

Another way you might try to achieve the same result, is by iterating directly over the calculated ids of the `random_string` resource:

```
locals {  
 users = toset(["Alice", "Bob", "Charlie"])  
}  
resource "random_string" "random" {  
 for_each = local.users  
 length = 8  
 special = false  
 upper = false  
}  
resource "aws_s3_bucket" "user_bucket" {  
 for_each = toset([for random_string in random_string.random : random_string.id])  
 bucket = "user-bucket-${each.key}"  
}
```

When trying to apply this second example, however, you’ll get an error:

```
│ Error: Invalid for_each argument  
│   
│ on main.tf line 13, in resource "aws_s3_bucket" "user_bucket":  
│ 13: for_each = toset([for random_string in random_string.random : random_string.id])  
│ ├────────────────  
│ │ random_string.random is object with 3 attributes  
│   
│ The "for_each" set includes values derived from resource attributes that cannot be determined until apply, and so Terraform cannot determine the full set of keys that will identify the instances of  
│ this resource.  
│   
│ When working with unknown values in for_each, it's better to use a map value where the keys are defined statically in your configuration and where only the values contain apply-time results.  
│   
│ Alternatively, you could use the -target planning option to first apply only the resources that the for_each value depends on, and then apply a second time to fully converge.
```

As suggested by the error message, after a targeted apply on the `random_string`resource, the code snippet will work.

Yet, if you destroy everything and recreate it from scratch, you run into the same issue: Terraform does not know what keys to use to uniquely identify the buckets. In addition, if you do a targeted apply, and then something changes to the targeted configuration, you have to do another targeted apply, until Terraform has assured that the keys in the state are not going to change.

Targeting is discouraged by Terraform, as it can cause your infrastructure to become inconsistent. Using `terraform apply -target` routinely is a sign that the dependencies between your resources are based on calculated values, or that your state is becoming too large.

Note that Terraform gives you a recommendation on how to avoid this error: “use a map value where the keys are defined statically in your configuration and where only the values contain apply-time results.”

### Proper module design: designing modules for change

I admit, the previous code snippet probably feels like a contrived example; not many people would write the second code block if tasked with creating a variable number of uniquely named s3 buckets from scratch.

What often happens, however, is that you introduce these sorts of dependencies as your Terraform codebase grows organically, *without your being aware of it*. If the calculated value is the only configuration you need to pass to the iterable, why add more information than needed?

Iteration over calculated values can in principle be present anywhere in your codebase; the most common place I see this mistake rearing its ugly head in practice is where calculated values are passed across a module boundary, via the module's input variables.

As a module author, you should 1) be careful not to assume too much about how your users will use the module, and 2) as mentioned above, make it difficult for users to misconfigure the module by adding constraints (via the HCL type system or validations). Always consider the possibility that a set of values you iterate over could be calculated attributes. Even if you know that current usage of your module is limited to statically configured input variables, that might not always be the case in the future.

Let's rewrite the example, assuming you want to package the code that creates the buckets as a module:

```
locals {  
 users = toset(["Alice", "Bob", "Charlie"])  
}  
  
resource "random_string" "random" {  
 for_each = local.users  
 length = 8  
 special = false  
 upper = false  
}  
  
module "user_buckets" {  
  source = "./user_buckets"  
  bucket_suffixes = random_string.random  
}  
  
### Code in user_buckets/main.tf  
  
variable "bucket_suffixes" {  
  type = map(string)  
}   
  
resource "aws_s3_bucket" "user_bucket" {  
 for_each = var.bucket_suffixes  
 bucket = "user-bucket-${each.value}"  
}
```

To reiterate, you only need a single string per bucket, so as a module author you might feel tempted to ask for this information as keys in a set. Bypassing it as (an attribute of) a value in a map instead, you allow users to pass calculated values to your module, while still guaranteeing a static identification of all iterables (and hence not requiring targeted applies).

The same reasoning also applies to module outputs: if you need to output attributes from iterables that are configured via the `for_each` meta-argument, make it a habit of returning a mapping between the keys that identify those iterables and the attribute values you’d like to expose to the module’s consumers.

```
## Good: return a map   
output "bucket_arn" {  
  value = {for user, bucket in aws_s3_bucket.user_bucket: user => bucket.arn}  
}  
  
## Bad: return a list of calculated values  
output "bucket_arn" {  
  value = [ for bucket in aws_s3_bucket.user_bucket: bucket.arn]  
}
```

### Conclusion

Terraform’s configuration language HCL provides powerful primitives to avoid code repetition. But with great power comes great responsibility. You should be very careful introducing `for_each` and `count` in your module design. Assume by default that it is possible that the configuration could be the result of a calculation, and therefore not known at plan time.

The keys of your iterable configuration should be static, and transparently passed throughout the Terraform state. In particular, when the iterables are part of a module and their number and configuration are externally defined, the static keys identifying them should flow from variables to outputs.

In summary, err of the side of caution: use `for_each` over `count`; when using `for_each`, use maps over sets.

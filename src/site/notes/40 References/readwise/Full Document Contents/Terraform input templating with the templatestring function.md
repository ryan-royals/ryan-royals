---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-input-templating-with-the-templatestring-function/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn-images-1.medium.com/max/1024/1*ikuImeR6Zii8yBXTw6sPPg.jpeg)

![A bunch of code files being merged togather.](https://cdn-images-1.medium.com/max/1024/1*ikuImeR6Zii8yBXTw6sPPg.jpeg)Complex merging with templatestringThe introduction of the templatestring function in [Terraform 1.9](https://github.com/hashicorp/terraform/blob/v1.9.0/CHANGELOG.md) opens up some interesting opportunities to provide more dynamic input to Terraform modules. Here we cover the basics and a more advanced use case.

##### How does the templatestring function work?

The templatestring function accepts a templated string and a replacements dynamic as inputs. Although the replacements is of type dynamic you will see we use a map(any) in all our examples. By using standard template syntax ${placeholder\_name} in our input string we can make replacements based on the keys in the replacements parameter.

For example:

```
locals {  
  templated_string = "Hello ${world_placeholder}"  
  
  replacements = {  
    world_placeholder = "World"  
  }  
  
  final_string = templatestring(local.templated_string, local.replacements)  
}  
  
output "example" {  
  value = local.final_string  
}
```
The output of this is:

```
example = "Hello World"
```
Take note of the double-dollar $$ syntax. This is required to avoid Terraform attempting standard string interpolation. We need to escape it for these inputs. The same applies if you are using a tfvars or tfvars.json file.

Ok, you are probably thinking that is a very convoluted way to interpolate a string. Now imagine that the templated string is a resource name and that replacements includes the attributes that form your naming convention. For example:

```
variable "resource_group_name" {  
  type    = string  
  default = "rg-${service}-${environment}-${location}-${number_01}"  
}  
  
variable "service_name" {  
  type    = string  
  default = "demo"  
}  
  
variable "environment" {  
  type    = string  
  default = "prod"  
}  
  
variable "location" {  
  type    = string  
  default = "uksouth"  
}  
  
variable "number_01" {  
  type    = number  
  default = 1  
}  
  
locals {  
  resource_group_name = templatestring(var.resource_group_name, {  
    service     = var.service_name,  
    environment = var.environment,  
    location    = var.location,  
    number_01   = var.number_01  
  })  
}  
  
output "example" {  
  value = local.resource_group_name  
}
```
The output of this is:

```
example = "rg-demo-prod-uksouth-1"
```
Hopefully you can see the benefit of this is that a user can supply their own naming convention, but still use the standard inputs to define it. For example they could change the resource\_group\_name to rg-hub-$${location} and that would still work.

Now that seems more useful, but not very dynamic…

##### Dynamic inputs for template strings

We can be a bit clever with this by generating and merging maps to provide the replacements. We can also use a collection as our templated string input and iterate over that to create multiple resource names. Take a look at this example:

```
variable "resource_group_names" {  
  type = map(string)  
  default = {  
    dev  = "rg-${service}-${environment_dev}-${location}-${number_01}"  
    qa   = "rg-${service}-${environment_test}-${location}-${number_01}"  
    prd1 = "rg-${service}-${environment_prod}-${location}-${number_01}"  
    prd2 = "rg-${service}-${environment_prod}-${location}-${number_02}"  
    prd3 = "rg-${service}-${environment_prod}-${location}-${number_03}"  
  }  
}  
  
variable "service_name" {  
  type    = string  
  default = "demo"  
}  
  
variable "environments" {  
  type = map(string)  
  default = {  
    dev  = "dev"  
    test = "test"  
    prod = "prod"  
  }  
}  
  
variable "location" {  
  type    = string  
  default = "uksouth"  
}  
  
variable "seed_number" {  
  type    = number  
  default = 1  
}  
  
variable "number_padding" {  
  type    = number  
  default = 3  
}  
  
variable "total_numbers_to_create" {  
  type    = number  
  default = 10  
}  
  
locals {  
  # Create a map of numbers to be used in the replacements.  
  numbers    = range(var.seed_number, var.seed_number + var.total_numbers_to_create)  
  number_map = { for number in local.numbers : "number_${format("%02d", number)}" => format("%0${var.number_padding}d", number) }  
}  
  
locals {  
  # Rename the environments map key to match the format of the resource_group_names map.  
  environments = { for env, env_name in var.environments : "environment_${env}" => env_name }  
}  
  
locals {  
  # Form the final replacements map.  
  replacements = merge(local.number_map, local.environments, {  
    service  = var.service_name,  
    location = var.location,  
  })  
}  
  
locals {  
  # Create the final resource group names using the templatestring function  
  resource_group_names = { for key, value in var.resource_group_names : key => templatestring(value, local.replacements) }  
}  
  
output "example" {  
  value = local.resource_group_names  
}
```
The output of this is:

```
example = {  
  "dev"  = "rg-demo-dev-uksouth-001"  
  "prd1" = "rg-demo-prod-uksouth-001"  
  "prd2" = "rg-demo-prod-uksouth-002"  
  "prd3" = "rg-demo-prod-uksouth-003"  
  "qa"   = "rg-demo-test-uksouth-001"  
}
```
We can do whatever we want so long as we can merge it into a map and supply it to the replacements.

##### Templating of complex data types

So far we have only dealt with simple data types. If our template strings are of type string , list(string) , or map(string) then we can very easily replace those as we know the data structure.

So how can we handle a more complex data structure that we don’t know in advance? As you may be aware, the Terraform merge method only supports a shallow merge, it does not traverse the object tree and merge at each level. So that can’t help us here and there isn’t another other method that can traverse any object type. Nested for loops won’t help us either.

What other options do we have? As of today, we can use a bit of a trick by converting to json using jsonencode, using templatestring on the json string and then converting back to an object using jsondecode.

Here is an example:

```
variable "complex_object" {  
  type = any  
  default = {  
    resource_group_names = {  
      dev  = "rg-${service}-${environment_dev}-${location}-${number_01}"  
      qa   = "rg-${service}-${environment_test}-${location}-${number_01}"  
      prd1 = "rg-${service}-${environment_prod}-${location}-${number_01}"  
      prd2 = "rg-${service}-${environment_prod}-${location}-${number_02}"  
      prd3 = "rg-${service}-${environment_prod}-${location}-${number_03}"  
    }  
    nested_object = {  
      name                = "level-01-${service}-${environment_dev}-${location}-${number_01}"  
      custom_replacements = "level-01-custom-${custom_01}-${custom_02}-${custom_03}"  
      nested_object = {  
        name = "level-02-${service}-${environment_dev}-${location}-${number_01}"  
        nested_object = {  
          name = "level-03-${service}-${environment_dev}-${location}-${number_01}"  
          nested_object = {  
            name = "level-04-${service}-${environment_dev}-${location}-${number_01}"  
          }  
        }  
      }  
    }  
  }  
}  
  
variable "custom_replacements" {  
  type = map(any)  
  default = {  
    custom_01 = "hello"  
    custom_02 = "world"  
    custom_03 = 123  
  }  
}  
  
variable "service_name" {  
  type    = string  
  default = "demo"  
}  
  
variable "environments" {  
  type = map(string)  
  default = {  
    dev  = "dev"  
    test = "test"  
    prod = "prod"  
  }  
}  
  
variable "location" {  
  type    = string  
  default = "uksouth"  
}  
  
variable "seed_number" {  
  type    = number  
  default = 1  
}  
  
variable "number_padding" {  
  type    = number  
  default = 3  
}  
  
variable "total_numbers_to_create" {  
  type    = number  
  default = 10  
}  
  
locals {  
  # Create a map of numbers to be used in the replacements.  
  numbers    = range(var.seed_number, var.seed_number + var.total_numbers_to_create)  
  number_map = { for number in local.numbers : "number_${format("%02d", number)}" => format("%0${var.number_padding}d", number) }  
}  
  
locals {  
  # Rename the environments map key to match the format of the resource_group_names map.  
  environments = { for env, env_name in var.environments : "environment_${env}" => env_name }  
}  
  
locals {  
  # Form the final replacements map. The custom replacements are added last to the merge method so they can override any other key if desired.  
  replacements = merge(local.number_map, local.environments, {  
    service  = var.service_name,  
    location = var.location,  
  }, var.custom_replacements)  
}  
  
locals {  
  # This is the crux of the example. We are converting the complex object to a JSON string, templating it, and then converting it back to a complex object.  
  complex_object_json           = jsonencode(var.complex_object)  
  complex_object_json_templated = templatestring(local.complex_object_json, local.replacements)  
  complex_object                = jsondecode(local.complex_object_json_templated)  
  # NOTE: We are not doing this on a single line due to a bug in Terraform that causes it to fail. Try it if you don't beleive me. :)  
}  
  
output "example" {  
  value = local.complex_object  
}
```
The output of this is:

```
example = {  
  "nested_object" = {  
    "custom_replacements" = "level-01-custom-hello-world-123"  
    "name"                = "level-01-demo-dev-uksouth-001"  
    "nested_object" = {  
      "name" = "level-02-demo-dev-uksouth-001"  
      "nested_object" = {  
        "name" = "level-03-demo-dev-uksouth-001"  
        "nested_object" = {  
          "name" = "level-04-demo-dev-uksouth-001"  
        }  
      }  
    }  
  }  
  "resource_group_names" = {  
    "dev"  = "rg-demo-dev-uksouth-001"  
    "prd1" = "rg-demo-prod-uksouth-001"  
    "prd2" = "rg-demo-prod-uksouth-002"  
    "prd3" = "rg-demo-prod-uksouth-003"  
    "qa"   = "rg-demo-test-uksouth-001"  
  }  
}
```
Take note of the custom\_replacements map in that example. This allows consumers of your module to supply any values they want to template.

##### Summary

As you can see, the templatestring function provides a powerful capability that was not easy to achieve before, since you had to use templatefile (requiring IO operations) or replace to achieve anything close to this. Now we can do complex transformations in memory.

This is a really useful feature when building modules consumed by a wide audience as it enables the consumer to determine their naming conventions, etc and removes the need for them to replace common attributes of a name for each use of the module. E.g. for multi-region deployments they don’t need to care about the location for the purpose of naming as they can just use the placeholder.

##### References

* templatestring docs: <https://developer.hashicorp.com/terraform/language/functions/templatestring>
* Templating syntax: <https://developer.hashicorp.com/terraform/language/expressions/strings>
* Examples used in this post: <https://github.com/jaredfholgate/terraform-templatestring-demos>

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=a81583777ed1)

---

[Terraform input templating with the templatestring function](https://medium.com/azure-terraformer/terraform-input-templating-with-the-templatestring-function-a81583777ed1) was originally published in [Azure Terraformer](https://medium.com/azure-terraformer) on Medium, where people are continuing the conversation by highlighting and responding to this story.

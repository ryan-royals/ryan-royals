---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/alas-poor-null-provider-i-knew-him-horatio/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1024/1*tjWltjeKxx_GRBPwrv_7KA.jpeg)

**TL;DR** Stop using the [null provider](https://registry.terraform.io/providers/hashicorp/null/latest/docs), there’s no point anymore. `[terraform\_data](https://developer.hashicorp.com/terraform/language/resources/terraform-data)` can do all this and more!

![](https://miro.medium.com/v2/resize:fit:700/1*tjWltjeKxx_GRBPwrv_7KA.jpeg)
Terraform practitioners sometimes must fall back to using provisioners to do things that Terraform cannot. It’s an ugly-but-necessary solution sometimes. It looks a little like this:

```
resource "null_resource" "example" {  
  # Using triggers to force execution on resource property change  
  triggers = {  
    on_change = azurerm_foo.bar.run_provisioner_when_this_changes  
  }  
  provisioner "local-exec" {  
    command = "do something"  
  }  
}
```

However, this is yet another provider that you’ll need in your `required_providers {}` block and another dependency to manage.

However, in Terraform 1.4 we got a new built-in provider (called **terraform)** that exposes the `terraform_data {}`resource.

There are a few key use cases for this resource:

### Testing Computed Values

A really useful ability of this resource is to reflect its input into a computed output. This is very useful when testing how code would behave with values that aren’t known until after apply (computed values, etc).

```
resource "terraform_data" "foo_computed" {  
  input = "test"  
}  
  
data "foo_data" "test" {  
  foos = [terraform_data.foo_computed.output]  
}
```

In the above, we are simulating what happens if the `foo_data` data source is supplied with a value not known until after apply. It’s niche but I find this super useful!

### Replace triggered by

Sometimes you want to trigger a replacement to a resource when something external changes, this example is taken from the Hashicorp docs:

```
variable "revision" {  
  default = 1  
}  
  
resource "terraform_data" "replacement" {  
  input = var.revision  
}  
  
# This resource has no convenient attribute which forces replacement,  
# but can now be replaced by any change to the revision variable value.  
resource "example_database" "test" {  
  lifecycle {  
    replace_triggered_by = [terraform_data.replacement]  
  }  
}
```

And finally…

### Provisioners

This is the death knell for the null provider, and it’s built right in to Terraform:

```
resource "azurerm_foo" "web" {  
  # ...  
}  
  
resource "azurerm_bar" "database" {  
  # ...  
}  
  
# A use-case for terraform_data is as a do-nothing container  
# for arbitrary actions taken by a provisioner.  
resource "terraform_data" "bootstrap" {  
  triggers_replace = [  
    azurerm_foo.web.id,  
    azurerm_bar.database.id  
  ]  
  
  provisioner "local-exec" {  
    command = "bootstrap-hosts.sh"  
  }  
}
```

So, there you are — ditch the null provider, thank it for its service and put it out to pasture.

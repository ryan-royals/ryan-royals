---
{"dg-publish":true,"dg-path":"Blog Posts/TF inputs and Environments.md","permalink":"/blog-posts/tf-inputs-and-environments/","tags":["blogs"],"created":"2024-05-22","updated":"2025-11-28"}
---


## Getting the Ball Rolling

Howdy! In my previous article about [Getting Started with Terraform](https://blog.arkahna.io/getting-started-with-terraform) I talked about what Terraform is, why it's neat-o, and a small example on getting started in Azure.  
Now we are ready for the next steps, getting a Terraform Project ready to deploy to independent Dev/Test/Production environments, based off the one set of Terraform code.

A final repo of code of what we are building is [Available Here](https://github.com/arkahna/tf-environments-blog-example) if you wish to skip to the good part, or get lost on the journey. But otherwise this should be beginner friendly, and ideally use the least amount of code possible, following the mantra keeping it DRY (Don't-Repeat-Yourself).  
![Arkahna Blog - TF inputs and Environments-1716449061653.png](/img/user/10_attachments/Arkahna%20Blog%20-%20TF%20inputs%20and%20Environments-1716449061653.png)

So as quick revision, the `main.tf` is where we are going to store the bit of Terraform code that does a thing. Terraform does not care about names of files, or even the boundary of files. When you run Terraform commands, they effectively merge all of the `*.tf` files found in the directory, and builds its own Dependency Graph from there. We simply name these files as `main.tf` and `variables.tf` as it makes it easier for the human to find.

> [!info]  
> Terraform does not traverse up or down the directory tree looking for `*.tf` files, and it does not care about file names, so we use both of these constraints as tools for us to make the maintenance of the project easier.

## Variables.tf

`Variables.tf` and the `variable` block within are new to this series of blog posts, but as decently simple as they do what they say on the tin; they allow you to pass information into a Terraform module based on Environment variables, command line inputs or passing a `.tfvars` file.

> [!info]  
> Terraform has the concept of *modules*, which are close to fully fledged Terraform instances in of themselves, having their own Variables and Outputs to plug them into other modules. The top level code for Terraform is called the **Root Module**.

A `variable` is where you get to enforce what type of information is being passed into the module, for use later in the project.

```hcl
# variables.tf
variable "location" {
  description = "The location/region where the resources will be created."
  default     = "Australia East"
  type        = string
  nullable    = false
}

variable "tags" {
  description = "A object of tags to add to all resources."
  type = object({
    workload   = string
    owner      = string
    deployedBy = optional(string, "Terraform")
  })
  nullable = true
}

variable "naming" {
  description = "A object of lists used to construct the names of resources."
  type = object({
    prefix = list(string)
    suffix = list(string)
  })
  nullable = false
}
```

When declaring a `variable` block, you also give it a label that is used later in the configuration to reference this variable, which in this example we have *location, tags* and *naming*.  

`Variable` blocks are a little strange in the way that you do not have to define anything else, and it would be usable from here. There is no use case for this configuration though, and I would enforce that `description` and `type` are the minimum requirements for a block.  
`Description` is the descriptor for the variable, which is printed out to the CLI if no matching input is found, or used by tools like [terraform-docs](https://terraform-docs.io/).  
`Type` is used to define what input is expected. This can be any type that is supported by Terraform, which are categorized as *primitive*, *collection*, and *structural* types. These will be explored in the next section.  
`Default` is the default value for the variable. Whatever defined here must be valid against the `type` parameter.  
`Nullable` Is the last parameter we will cover in this post. By default, `variables` are nullable, which is Terraform for "Don't deploy anything", and is functionally different to a blank value like "". Although its not required, it is good practise to confirm if a `variable` should be `nullable` or not to avoid other users finding creative ways to break your deployment.

`Default` and `Optional()` are both ways to predefine a default option for a variable, but fill different needs. `Default` is the default for the whole variable, and in the instance of a Collection or Structural type if you are to change anything based on user input, the whole default is overwritten.  
`Optional()` is a default for a specific *value* on a *key*, so when using a Collection or Structure, the input can define other values without supplying the key that has the `optional()` value, and the default supplied by the optional will be used.


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/types-in-terraform/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





Here is a quick run through of each *type*, and how you pass inputs to the `variable` in a `.tfvars` file. These types are also used within you Terraform code in blocks such as `locals`, but those types are implied and assumed by Terraform, whilst in `variables` they are explicitly called out.

## Primitive Types

Primitive Types are the most atomic unit of input, and are used as the building blocks for more complicated Collections and Structures.

### `string`

A sequence of unicode characters. Used all the time in Terraform.  

``` hcl [2-4]
# variables.tf
variable "lettersandstuff" {
 type = string
}
```

``` hcl[2]
# dev.tfvars
lettersandstuff = "heyyyy"
```

### `number`

A number, can be fractional. Used rarely in real deployments, as Terraform is Declarative and things like sums don't always find a home when we are trying to tell a cloud platform to look like X.  

``` hcl[2-5]
# variables.tf
variable "calc_u_later" {
 type = number
}
```

``` hcl [2]
# dev.tfvars
calc_u_later = 420.69
```

### `bool`

A Boolean value (True or false). Used all the time for conditionals in deployments.

``` hcl [2-5]
# variables.tf
variable "learning_something" {
 type = bool
}
```

``` hcl [2]
# dev.tfvars
learning_something = true
```

## Collection Types

Collections are a ~~collection~~ group of the same types, used to collate information together. If you are looking to mix and match types under the same variable without nesting, that is the use case for a Structural Type.

### `list`

A ordered sequence of primitive types, which can have duplicates. Used all the time as input as it is simple to work with when we start looking at things like Loops.  

``` hcl [2-9]
# variables.tf
variable "agoodlist" {
 type = list(string)
}
variable "acomplicatedlist" {
  type = list(object({
    name = string
  }))
}
```

``` hcl[2-10]
# dev.tfvars
agoodlist = ["this", "blog", "is", "is", "is", "great"]
acomplicatedlist = [
  {
    name = "Great"
  },
  {
    name = "Awesome"
  }
]
```

### `map`

A unordered collection of values identified by a Key. Not used much as its keys are not strictly set, and Terraform is very strict about knowing keys before Plan/Apply.

```hcl [2-7]
# variables.tf
variable "pirate" {
 type = map(string)
}
```

``` hcl[2-5]
# dev.tfvars
pirate = {
 yarhar     = "fiddle dee dee",
 thisIsAKey = "thisIsAValue"
}
```

### `set`

A unordered sequence of unique values. Very rarely used as a variable, as lists are easier to work with (Since Lists are ordered, Terraform interacts with them in a simpler fashion).

```hcl[2-5]
# variables.tf
variable "agoodpun" {
 type = set(string)
}
```

``` hcl [2]
# dev.tfvars
agoodpun = ["this","blog","just","keeps","giving"]
```

## Structural Types

Structural types are similar to Collection types, but a singular Structure can have different Types all bundled together.

### `object`

A collection of named attributes, each with their own type. Used all the time by itself as a `variable`, or within a `list` as you get to define the Key up front, and know exactly what type of value you are looking up.

```hcl [2-7]
# variables.tf
variable "aobject" {
 type = object({
  name = string
  count = number
 })
}
```

```hcl [2-10]
# dev.tfvars
aobject = {
 name = "hellyeah"
 count = 20
}
```

### `tuple`

A ordered sequence of types. Each type declared must have *exactly that*. Hard to work with, not sure we have ever actually used it to have different types in any deployment. Note that `tuple` and `list` are both wrapped in square brackets `[]`, which can confuse Terraform sometimes.

``` hcl [2-5]
# variables.tf
variable "tupleware" {
 type = tuple([string, bool, number])
}
```

```hcl[2]
# dev.tfvars
["tupleCheck", false, 001]
```

## The `any` Type

For the sake of completeness, there is another type you can define being `any`. This is the same as not declaring a type on the `variable` block at all.  
I will be stern and say there is no valid use case for this type, and it is not even worth looking for exceptions or examples on when its useful, as it is almost a fundamental breach of the declarative nature of Terraform.


</div></div>


## Main.tf

```hcl
# main.tf

terraform {
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
    }
  }
  backend "azurerm" {
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = join("-", concat(var.naming.prefix, ["rg"], var.naming.suffix))
  location = var.location
}

resource "azurerm_storage_account" "st" {
  name                     = join("", concat(var.naming.prefix, ["st"], var.naming.suffix))
  resource_group_name      = azurerm_resource_group.st.name
  location                 = var.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}
```

This is the simple `main.tf` we will use in the example to explain what is going on block by block:

`terraform` and `provider` blocks are the meta information for Terraform, telling it what Providers to download, and how to configure them. Each `provider` represents a cloud environment, which in this case we are using our trusty [`azurerm` provider](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs).  
Notably in the `terraform`, we have `backend "azurerm"` defined but empty. This block is used to configure a Azure Storage Account as the state storage location, as [shown in documentation here](https://developer.hashicorp.com/terraform/language/settings/backends/azurerm). We will be configuring this block by using the `*.tfbackend` file later in the configuration.

> [!info]  
> `Backend` and `Provider` blocks authenticate separately which can be unintuitive when first trying to understand the Terraform configuration. The reasoning behind this is you could use `azurerm` for your backend, but using a `aws` provider.

The `resource` blocks show how we actually call the variables, by using the `var.` prefix and the label of the `variable` declared earlier. As when calling `resource` blocks if your `variabe` unordered type, you can use dot notation to call the key (like `azurerm.st.name`), otherwise you use square bracket notation to call element in a ordered list (like `var.list[1]`).

## .tfvars And .tfbackend

The last step in configuring the files to be ready for different environments is to start loading values into the `.tfvars` and `.tfbackend` files. Luckily these files are very simple.

```hcl
# dev.tfvars

tags = {
  workload   = "env-config"
  owner      = "someone"
  deployedBy = "Terraform"
}
naming = {
  prefix = ["dev"]
  suffix = ["aue", "config"]
}
```

The `.tfvars` file is super simple, and is just a collection of keys and values. Following the [Input Variables Precedence](https://developer.hashicorp.com/terraform/language/values/variables#variable-definition-precedence) documentation on the Terraform Docs, anything we pass here in this file will overwrite any Environment variables and defaults in the Terraform configuration.

The `.tfbackend` is another simple file that follows the same structure as the `.tfvars` file.

```hcl
# dev.tfbackend
resource_group_name  = "dev-rg-aue-tfstate" 
storage_account_name = "devrgauetfstate123647"                 
container_name       = "tfstate"                  
key                  = dev.tfstate"
```

When we pass this file later when we run `terraform init` the content of this file gets overwrites whatever is configured in the `backend "azurerm"` in the `main.tf` file.

## Executing in the Command line

> [!note]  
> For the rest of the demo, it is assumed that the CLI you are using has Terraform installed, and AzCLI installed and logged into a subscription, and a Storage Account created with its details filled into the `.tfbackend`

From here, its just simple parameters we pass to the Terraform CLI to get it to do the do.

Initialising the Project changes slightly as when you run `init`, it configures the `.terraform` folder to use the backend:

```bash
terraform init -backend-config='./variables/dev.tfbackend'
```

Once this has initialised, we are ready to use the `dev` backend for our `plan` and `apply`:

```bash
terraform plan -var-file "./variables/dev.tfvars"
terraform apply -var-file "./variables/dev.tfvars"
```

When ready to move to another environment like `uat`, the `.terraform` needs to be reconfigured to point to the next state file:

```bash
terraform init -backend-config='./variables/uat.tfbackend' -reconfigure
```

The `-reconfigure` switch tells Terraform to reconfigure the backend. The same effect can be done by deleting the `.terraform` folder, but this keeps the downloaded providers and is overall neater.

## Next Steps

With that, you should be ready to deploy to as many environments as you want, building upon Terraform configuration once and having it deployable to as many environments as you want.  
We are now close to a template that is ready for real world use in deploying actual workloads to actual places. The last missing link is CI/CD pipelines and configuring other Identities ([Like Managed Identities using OIDC](https://blog.arkahna.io/authenticating-with-azure-security-principals-explained)) to do the doing.

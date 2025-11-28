---
{"dg-publish":true,"dg-path":"Getting Started with Terraform.md","permalink":"/getting-started-with-terraform/","tags":["blogs"]}
---


## What is Infrastructure as Code

Infrastructure as Code (IaC) is a broad term used for the approach and tooling to manage infrastructure in scripts and files. This allows us to go beyond using a GUI based portal to deploy infrastructure, and instead we can parameterise and easily reproduce deployments, for doing things like deploying 10 Virtual Machines without having to click through the Portal 10 times.

At Arkahna we use IaC everywhere, for everything, all the time. An allergy to Web Portals is normal and healthy!

## So why Terraform

[Terraform]([Terraform by HashiCorp](https://www.terraform.io/)) is our tool of choice for Infrastructure as code for a few good reasons:

- **Popular** - Simply put, Terraform is the industry standard IaC tool. It is used by everyone from small business deployments to the largest enterprise applications. It is by far the most broadly used tool and is a great place to start the journey of IaC
- **Cross Platform** - Terraform has a plugin driven configuration that currently has over 300 official Providers (targeting platforms like Azure, AWS, GCP, vSphere) making the tool highly cross platform. Unlike tools like ARM / Bicep Templates or AWS CloudFormation, Terraform can be used just about anywhere without having to learn a brand new tool.
- **Simple** - Terraform uses `.tf` and `.hcl` files and functions as a *domain specific language*, meaning that it is it's own programming language. It is purpose built to deploy and manage infrastructure, and does not require any prior knowledge of other languages like Python or Typescript.
- **State Driven** - Terraform is *declarative* meaning that it does its best to make everything look like as defined in the files. It will do any Creates, Updates and Destroys (Deletions) that is sees appropriate to make the deployed infrastructure match your definition. This is apposed to other IaC languages that are *imperative*, which operate like a script and run operations from top to bottom.

## How to Read Terraform

[Terraform]([Terraform by HashiCorp](https://www.terraform.io/)) files use the [*HashiCorp Configuration Language (HCL)*]([Overview - Configuration Language | Terraform | HashiCorp Developer](https://developer.hashicorp.com/terraform/language)) syntax, and it loves blocks. Everything done in a block.

```hcl
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
    }
  }
  backend "local" {   
  }
}

provider "azurerm" {
  features {
  }
}

resource "azurerm_resource_group" "squid" {
  name     = "ark-rg-prd-workload"
  location = "australiaEast"
}

resource "azurerm_storage_account" "things" {
  name                     = "arkstprdworkload"
  resource_group_name      = azurerm_resource_group.squid.name
  location                 = azurerm_resource_group.squid.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

```

At the top of this example, we have a `terraform` and a `provider` block. These tell Terraform about where to store its state file, and what Providers to download.  
Providers represent a plugin for a cloud environment, so in this case we are telling it to use Azure.  
These two blocks are meta information for Terraform and are useful for when you are writing Terraform, but are not the key part you are typically looking for when reading Terraform.

> [!info]  
> As a tip, you would never want to use the `backend "local"` in any sort of environment, including Dev. It's good for doing local tests, but should never expect to live longer than an hour.  

Further down we have the `resource "azurerm_resource_group" "squid" {` line which block holds a lot of information that Terraform uses in its configuration, and is often the bit that is hard to digest when first learning Terraform.  
Lets breakdown the first line for the Resource Group:

`Resource` tells Terraform that this is something to deploy, as `Resource` blocks deploy stuff. Some of the other types of Blocks include: `Data`, `Locals`, `Provider`, `Variable`, `Module`.  
There are a few more meta blocks that are directly related to Terraform, but these ones are the big ones you use every day when doing things.

`"azurerm_resource_group"` actually holds two key parts of information.  
The *Azurerm* bit tells Terraform which *Provider* to use, being `azurerm` as we specified in the `provider "azurerm" {` line.  
`Resource_group` tells the *provider* what we are deploying, in this case its a Resource Group.

`"squid"` at the end of this line is a field where we name the block for tracking in Terraform. This label does not affect anything deployed, but is a meta field for Terraform.  
Later in the configuration, you can use this label and the resource type to refer to this block and its properties in a syntax like: `azurerm_resource_group.squid.location`

The stuff inside of the block is unique to the provider and the resource itself, but with that understanding of a resource block you should be able to see the trees amongst the forest and feel out what is going on.

## The Terraform Lifecycle

The next important part is actually understanding how to use Terraform, and for that we have 4 key Terraform CLI commands.  

![Arkahna Blog - Getting Started with Terraform-1705372269281.png](/img/user/10_attachments/Arkahna%20Blog%20-%20Getting%20Started%20with%20Terraform-1705372269281.png)

Terraform has a Initialise step which is done to download modules, the state file and in general prepare your working directory. All of this information gets generated and stored in a `.terraform` folder at the root of your Terraform Project.  
To initialise, you simply run `terraform init`  
Unlike Git init, this does need to be done every time you redownload your project files. This `.terraform` folder also does not get committed to Git and can instead be re initialised over and over safely.

> [!info]  
> It is not uncommon to delete this folder manually and re init if you are encountering issues.

The next part of the lifecycle looks a lot like a CI/CD lifecycle, which is not a coincidence.  
Running `terraform plan` does a Dry Run where it compares your Project files, the State file and the cloud provider you are deploying to.  
The CLI then tells you what will be Created, Updated or Destroyed.  
`terraform apply` does another Plan, but also gives you the option to proceed with the Plan, and let Terraform apply the changes.  
In a CI/CD pipeline, `terraform plan` is your Continuous Integration step, whilst `terraform apply` is the Continuous Deploy step that is conducted at the end of a successful PR.  
As a handy guide for how to predict what terraform is thinking:  
![Arkahna Blog - Getting Started with Terraform-1705372290043.png](/img/user/10_attachments/Arkahna%20Blog%20-%20Getting%20Started%20with%20Terraform-1705372290043.png)  
Lastly, we have `terraform destroy`, which deletes everything tracked in the state file.  
This command is typically executed the least, as you can live on the plan and apply wheel forever.  
Handy for at the end of a PoC or in a ephemeral environment, but not typically included as a step in CI/CD due to the danger of it.

## Cool, What's next

That is the basics! That should kick start you into starting to write Terraform and get something deploying.  
I'd suggest looking in the [Terraform docs next in the provider related to cloud environment]([Browse Providers | Terraform Registry](https://registry.terraform.io/browse/providers)) you want to deploy to. I can vouch for the [Azurerm documentation]([Docs overview | hashicorp/azurerm | Terraform | Terraform Registry](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)) being quite good at getting you started.

The above example is also a working example that you can use to get started working locally and expand from there.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/mind-the-terraform-modules/","tags":["rw/articles"]}
---

![rw-book-cover](https://media.dev.to/cdn-cgi/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz4rf81cl57gi5c53kcpk.png)

[![Cover image for # Mind the Terraform Modules](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz4rf81cl57gi5c53kcpk.png)](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz4rf81cl57gi5c53kcpk.png)[Cover image for # Mind the Terraform Modules](https://media.dev.to/cdn-cgi/image/width=1000,height=420,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fz4rf81cl57gi5c53kcpk.png)
####  [SAP BTP and Terraform (6 Part Series)](https://dev.to/lechnerc77/series/26908)

 [1 Enable Developers on SAP BTP with Terraform, GitHub Actions and Backstage](https://dev.to/lechnerc77/-enable-developers-on-sap-btp-with-terraform-github-actions-and-backstage-357e)   [2 Terraform Provider for SAP BTP - Remote State and Drift Detection](https://dev.to/lechnerc77/terraform-provider-for-sap-btp-remote-state-and-drift-detection-3pnj)   [... 2 more parts...](https://dev.to/lechnerc77/sap-btp-terraform-and-open-policy-agent-243m)   [5 Terramate this SAP BTP!](https://dev.to/lechnerc77/terramate-this-sap-btp-5a8p)   [6 # Mind the Terraform Modules](https://dev.to/lechnerc77/-mind-the-terraform-modules-3p11) 

####  Introduction

One important feature of Terraform is the ability to structure your infrastructure configuration into reusable *modules*. In this blog post I would like to give an overview about modules include digging into potential pitfalls and how to avoid them.

>  Although I am mentioning Terraform only in this blog post, the statements also apply to OpenTofu.
> 
>  

####  What are modules?

Let us start with some (maybe confusing) terminology. Formally modules are defined as "[...] containers for multiple resources that are used together." (Source: [Terraform documentation](https://developer.hashicorp.com/terraform/language/modules)). So, every collection `*.tf` files kept together in a directory is considered a module. Not what would have to come to my mind first, but that is the definition.

Based on that we can further distinguish between two types of modules:

* The *root* module
* *Child* modules

Every Terraform configuration has a *root module* that contains your Terraform configuration. That's the files that you typically write, when staring your configuration journey. From this root module you can call other modules the so called *child modules*. In contrast to the root module, a child module can be used *multiple times* in the same configuration. It can also be used *from several configurations*. This is not possible for the root module.

For the sake of keeping things simple I will use the term "module" as a reference to a child module from now.

####  Why should I use modules?

Thinking about the "as Code" aspect a module consequently represents a reusable block of configurations with an interface (the variables you define) and probably an output. This approach enables you to structure your Infrastructure as Code configurations in a well-structured. It also gives you the opportunity to adhere to the *Do Not Repeat Yourself* (DRY) principle when crafting your configurations.

Modules in Terraform represent the same approach that you would take when working with "classical" application code: you would encapsulate functionality to give your code a clear structure. If there are bits and pieces that could be used in several spots you would probably put them in reusable assets.

Besides the DRY aspect the modularization also helps you to keep your configuration code clean and readable and avoid human errors due to copy-pasting configurations all over the place (and then forgetting to apply fixes in all places). Not to forget, the usage of modules can support in ensuring compliance and governance with respect to the infrastructure configurations starting from ensuring naming conventions to the point of restricting e.g., the allowed VM sizes that you can provision via a module.

>  **Note:** Of course modules do not exempt you to safeguarding things like allowed VM sizes also on platform level like via Azure policies on Azure as somebody might not use modules and directly provision resources or not use Terraform at all.
> 
>  

While the advantages of using modules (or modularize your code) are the same as with "traditional" application code, guess what the challenges are so too. I will come to this topic in a second touching the two angles of modules namely the provider and consumer part, but first let us have a look at how modules are defined in Terraform.

####  The anatomy of a module

Following the definition of modules there is no specific keyword to define a module. However, when calling a module, you must use the keyword `module` accompanied by the name of the module in your Terraform code. In addition, you must specify the source of the module via the `source` attribute. There are several source types available like local files, Git repositories, a S3 bucket or the Terraform registry. All the supported sources are listed in the [documentation](https://developer.hashicorp.com/terraform/language/modules/sources).

Let us look at a simple example. We want to leverage a module to provision an AKS cluster on Azure. This would be quite a bit of work to stitch together all the resources manually. Luckily there is a module available for this in the [Terraform registry](https://registry.terraform.io/modules/Azure/aks/azurerm/latest). To call this module in our configuration the following code snippet would do the trick with a minimalistic configuration:

```
module "aks" {
  source              = "Azure/aks/azurerm"
  version             = "9.1.0"
  resource_group_name = "rg_my_aks_cluster" 
  }

```

This module comprises 19 resources, so obviously leveraging the module makes the code more readable and maintainable as you do not have to care about how to set them up. There are also a lot more optional parameters that you can feed into the module (more than 150 to be precise) to further tailor your AKS cluster configuration.

As you can see in the code snippet you can also specify a *version* for the module. An important topic that we will discuss in the following section when it comes to consuming modules.

Despite that the handling of modules is the same as with regular resources from a configuration perspective including meta-arguments like `depends_on` or `count`.

>  **Note** - If you are working with Azure, I want to draw your attention to the [Azure Verified Modules](https://azure.github.io/Azure-Verified-Modules/). The goal of this initiative is to provide a consolidate set of standards on how a good Infrastructure-as-Code module should look like. As it is Azure it does not only cover Terraform, but also Bicep modules. This project is not only of interest for consumption but also getting inspiration when you are building your own modules.
> 
>  

Let us look at the two angles of modules the *provider* and the *consumer*, and what we need to keep in mind for each of them.

####  Building Modules - What to consider

#####  The content of a module

When *building* a module in Terraform the aspects that we must consider are the same as when implementing a library or any re-useable chunk of code. The first point to consider is the *design* i.e. what resource combination should be contained in a module that makes the life of the user easier to provision a specific part on a cloud platform. The concrete number of resources that you combine in a module depends on your scenario. Nevertheless, avoid the following pitfalls:

* If the module comprises only one resource you should rethink if this is worth a module.
* Crafting "god modules" that contain too many resources that are covering a too huge use case or setup. As in programming *high cohesion* is the name of the game here. Bring together what logically belongs together and separate what does not.

Keep in mind that the number of resources in a module also defines its blast radius when things go sideways. With a proper design namely a reasonable combination of resources that have a clear responsibility you can limit the blast radius at least to a reasonable extent. As an extreme example it makes sense to have a module for setting up an AKS cluster and its components, but it makes in my opinion no sense to encapsulate a complete stage setup like DEV, TEST or PROD in a single module.

#####  Storage and versioning

Once you have determined the boundaries of your module put the module into a dedicated code repository (one per module would be my advice) and make use of versioning of the module via the mechanics of the code repository. The consumer of the module will want to specify a version when calling the module.

You can also push the modules to an official registry like the one of Hashicorp, but from a user perspective this is not a must. It depends on your use case and the requirements and constraints in your setup.

#####  Stick to common naming conventions

When structuring your Terraform files for your module, stick to common conventions when it comes to structure and naming i.e., have something like a `main.tf`, `variables.tf` and `outputs.tf` files (maybe with prefixes). This helps the consumer and the contributor to easily understand your module.

#####  Interface of the module

You should define reasonable input and output variables. When it comes to the input variables also make sure to use default values wherever it makes sense to make the consumer's life easier. Also make sure that the variables are properly validated. [Cross-object referencing](https://www.hashicorp.com/blog/terraform-1-9-enhances-input-variable-validations) that landed in Terraform 1.9 is something you should look at in that context.

The validations and checks can be further improved via [pre- and post-condition blocks](https://developer.hashicorp.com/terraform/language/expressions/custom-conditions#preconditions-and-postconditions). The goal when designing a module must be to make it as easy and safe for the consumer to use it.

Depending on your scenario you might also have the requirement to create resources conditionally. My advice is to make this explicit via a dedicated Boolean input variable instead of implicit derivations like "if variable X has a value and Variable Y and Z have no value then do create resource C otherwise not". Using a dedicated variable makes it also easier for the consumer to know what to expect and easier for you as provider of the module to validate the input.

#####  Write clean (Infrastructure as) Code

Although the consumer does not see you code, it should be well structured and maintainable. This will help you to maintain the module in the long run and make contributions easier. In that context you might want to look at the [dynamic blocks](https://developer.hashicorp.com/terraform/language/expressions/dynamic-blocks) that help you to get rid of repetitive code.

However, take this with caution: making the code better readable and maintainable via dynamic blocks can turn into the opposite. So do not overuse them and especially do not nest them too deep. Of course, this always depends on the scenario, but worth to keep in mind.

If you run into a situation where the nesting gets too deep, it might also be worth to look at tools that allow to generate Terraform code like [Terramate](https://terramate.io/).

#####  Documentation

Having good documentation including examples and sample use cases are a must. No difference to any other software artifact. Make it easy for your user to understand what the module does and how to use it.

#####  Testing

"With great power comes great responsibility" - as with every reusable code block this is also true for modules. You have only limited control about who uses your module where and how. Consequently, testing your modules is an important part of the process. You should use all options that Terraform provides (see e.g., this blog post about [Testing HashiCorp Terraform](https://www.hashicorp.com/blog/testing-hashicorp-terraform)) and automate the process via CI/CD pipelines.

#####  One word about local modules

You can of course also use local modules to improve the structure of your code. I would see this as a first step from a monolithic configuration to a modularized monolith. Nevertheless, the lifecycle for your configuration is still tightly coupled.

With local modules there is also no option to reuse this code in other configurations. This can be a valid step to evaluate and get an impression what might make sense to be extracted into a module but is maybe not yet the final step if you want to foster reuse.

####  Using Modules - What to consider

Let us switch perspective and put ourselves in the shoes of a consumer. Assume that we have found a module that perfectly fits our needs and follows all the best practices described above.

There is one important thing as a caller we must consider: specify the *version* of the module. This way we make a basic step towards safeguarding the setup by (hopefully) always using the same version and doing version upgrades intentionally. As mentioned before for modules from the Terraform registry this is achieved via the `version` attribute in the `module` block:

```
module "aks" {
  source              = "Azure/aks/azurerm"
  version             = "9.1.0"
  resource_group_name = "rg_my_aks_cluster" 
  }

```

If you are using a git repository you can use the `ref` argument and target a released version or (my preference) the SHA hash. I highly recommend doing this to avoid unpleasant surprises.

So, when specifying a version everything is great in terraform country, right? Right ...? Well, not perfectly. Let us dive a bit deeper into the mechanics.

Let us assume the besides the module configuration above we also have specified a provider configuration:

```
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.113.0"
    }
  }
}

```

The first step we do in our Terraform workflow is to run a `terraform init`. This command downloads the modules and provider sources and stores them in the `.terraform` directory. In the very first run it will select the newest available versions specified in your configuration that matches the given version constraint. With this information it will fill another file that landed in your file system, namely the `.terraform.lock.hcl` file:

[![Terraform file system after terraform init](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx2wmh30jizyet00pb06r.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx2wmh30jizyet00pb06r.png)[Terraform file system after terraform init](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fx2wmh30jizyet00pb06r.png)
The file is the so called [dependency lock file](https://developer.hashicorp.com/terraform/language/files/dependency-lock). It contains the checksums of the version that you downloaded. Once this lock file is there a consequent `terraform init` will always fetch the version that was downloaded before even in case that a newer version exists that fulfills the version constraints.

Taking a closer look at the lock file we see that it not only contains the version constraints, but   

 also a checksum of the downloaded version:

[![Terraform dependency lock file content](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj6x4prsir4up6212tcd6.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj6x4prsir4up6212tcd6.png)[Terraform dependency lock file content](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fj6x4prsir4up6212tcd6.png)
Besides evaluating the existing version, Terraform will execute a [checksum verification](https://developer.hashicorp.com/terraform/language/files/dependency-lock#checksum-verification) for the provider version. In case the checksum deviates for a version that exists in the lock file, Terraform will raise an error.

>  **Note:** The initial verification of the checksum is up to you. This is not covered by any built-in mechanics of Terraform. There are also scenarios where Terraform might not be capable to verify the checksum. Please refer to the [documentation](https://developer.hashicorp.com/terraform/language/files/dependency-lock#checksum-verification) for more details and the solution via [terraform providers lock](https://developer.hashicorp.com/terraform/cli/commands/providers/lock) command.
> 
>  

That's good and safeguards your setup. But wait ... what about the modules? They are also downloaded, but they are not reflected in the dependency lock file. If a module owner accidentally (or intentionally) updates a module but releases the update with the same version, this cannot be detected by Terraform at least not by the built-in functionality.

That is not so cool when it comes to secure the supply chain of your infrastructure configuration. Is there a way to mitigate this? Fortunately Terraform has an ecosystem surrounding it and there is one quite new tool that can help you here: [terrahash](https://github.com/ned1313/terrahash).

This tool fills the gap mentioned before. You can create, store, and validate the checksums for the modules that you use with the `terrahash` CLI. One word of caution before we take a closer look: `terrahash` is in its early stages (version 0.1.0 when writing this post). Basic functionalities are there, but there are certainly missing features and maybe bugs. Nevertheless, it is worth to take a look. As it is open source, you can also contribute to it.

With that in mind, let us see what this CLI can do for us.

#####  Using terrahash

The first thing that we do is execute the following command:

```
terrahash init

```

This evaluates the current configuration and generates a `.terraform.module.lock.hcl` file in analogy to the dependency lock file for the providers. The output of the command tells you exactly what it did:

[![terrahash init output](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg0b2isu012p8osp0t7q1.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg0b2isu012p8osp0t7q1.png)[terrahash init output](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fg0b2isu012p8osp0t7q1.png)
The content of the new file looks familiar:

[![terrahash dependency lock file](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh8xir0375o2mkcr89lgh.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh8xir0375o2mkcr89lgh.png)[terrahash dependency lock file](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fh8xir0375o2mkcr89lgh.png)
The file contains the checksums of the modules that you use. Looks good, now how to we validate the checksums? As this is an additional tool the checksum validation is not part of the Terraform CLI and must be triggered manually. However, in a productive setup with CI/CD pipeline this is not an issue as we can integrate this as additional pipeline step. We can trigger the check via the following command:

```
terrahash check

```

The output in a success case looks like this:

[![terrahash check output for success](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F30566dymjx6ltosr4xy8.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F30566dymjx6ltosr4xy8.png)[terrahash check output for success](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F30566dymjx6ltosr4xy8.png)
And here we go in case of an error:

[![terrahash check output for failure](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiv5csa0qznq43327fvob.png)](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiv5csa0qznq43327fvob.png)[terrahash check output for failure](https://media.dev.to/cdn-cgi/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fiv5csa0qznq43327fvob.png)
As promised this tool is a good addition to the Terraform setup when using modules and puts another piece in the puzzle of securing your infrastructure configurations with respect to unwanted version changes.

For the sake of completeness as a consumer you should of course also take of care of testing your configurations, but in contrast to a reusable module the blast radius is limited to your configuration (which might already be worse enough if you are not doing it ... nothing gets your heart rate up like accidentally destroying resources on production)

That's it from the perspective of a consumer. So let us summarize what we discussed in this blog post.

####  Summary

In general. modules are a good approach to structure your IaC configurations. As I have my background in application development is interesting to see that the "as Code" aspects heavily come into play when thinking about modules. The exact same challenges arise as with "traditional" code be it from the perspective of a provider of module and the things you must warp your head around as soon as you provide reusable (Infrastructure as) code. Fortunately, you can use the same strategies and patterns to deal with these challenges.

The same is true from a consumer perspective. Here the Terraform landscape has a gap when it comes to ensure the version integrity of the modules that you use. Luckily there is an ecosystem around Terraform and even more luckily with *terrahash* a brand-new open-source tool is available that can help you to deal with this gap.

Finally, I want to stress that although modules support you in your IaC journey towards a sustainable and maintainable setup, they are no silver bullet. You need to look at several aspects of your setup and while modules can help you with reuse, there are challenges that you will not be able to solve with them and you should also take other tools into account like e.g., [Terramate](https://terramate.io/). One further advice if you are starting your journey: always take one step at a time, work iteratively, and do not try to boil the ocean by targeting the "perfect" setup from the beginning.

With that … happy Terraforming and Terrahashing!

P.S. I am also quite sure that I missed points and best practices to describe, so feel free to add them in the comments.

####  [SAP BTP and Terraform (6 Part Series)](https://dev.to/lechnerc77/series/26908)

 [1 Enable Developers on SAP BTP with Terraform, GitHub Actions and Backstage](https://dev.to/lechnerc77/-enable-developers-on-sap-btp-with-terraform-github-actions-and-backstage-357e)   [2 Terraform Provider for SAP BTP - Remote State and Drift Detection](https://dev.to/lechnerc77/terraform-provider-for-sap-btp-remote-state-and-drift-detection-3pnj)   [...](https://dev.to/lechnerc77/sap-btp-terraform-and-open-policy-agent-243m)   [5](https://dev.to/lechnerc77/terramate-this-sap-btp-5a8p)   [6](https://dev.to/lechnerc77/-mind-the-terraform-modules-3p11)

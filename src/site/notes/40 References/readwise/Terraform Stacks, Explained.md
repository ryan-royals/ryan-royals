---
{"dg-publish":true,"permalink":"/40-references/readwise/terraform-stacks-explained/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1696883278-generic-multi-deployment-environment-example-1.png)
  
URL: https://www.hashicorp.com/blog/terraform-stacks-explained
Author: Yushuo Huang

## Summary

Terraform stacks simplify provisioning and managing resources at scale, reducing the time and overhead of managing infrastructure.

## Highlights added July 17, 2024 at 11:02 AM
>Here are the common use cases for stacks, out of the box:
>• **Deploy an entire application with components like networking, storage, and compute as a single unit without worrying about dependencies**. A stack configuration describes a full unit of infrastructure as code and can be handed to users who don’t have advanced Terraform experience, allowing them to easily stand up a complex infrastructure deployment with a single action.
>• **Deploy across multiple regions, availability zones, and cloud provider accounts without duplicating effort/code**. *Deployments* in a stack let you define multiple instances of the same configuration without needing to copy and paste configurations, or manage configurations separately. When a change is made to the stack configuration, it can be rolled out across all, some, or none of the deployments in a stack. ([View Highlight] (https://read.readwise.io/read/01hgc8fer3h18mv82edp2mzy7c))


>How do I use a Terraform stack?
>Stacks introduce a new configuration layer, which sits on top of Terraform modules and is written as code.
>Components
>The first part of this configuration layer, declared with a `.tfstack.hcl` file extension, tells Terraform what infrastructure, or components, should be part of the stack. You can compose and deploy multiple modules that share a lifecycle together using what are called *components* in a stack. Add a *component* block to this configuration for every module you'd like to include in the stack. You don’t need to rewrite any modules since components can simply leverage your existing ones.
>Deployments
>The second part of this configuration layer, which uses a `.tfdeploy.hcl` file extension, tells Terraform where and how many times to deploy the infrastructure in the stack. For each instance of the infrastructure, you add a *deployment* block with the appropriate input values and Terraform will take care of repeating that infrastructure for you. When a new version of the stack configuration is available, plans are initiated for each deployment in the stack. Once the plan is complete, you can approve the change in all, some, or none of the deployments in the stack. ([View Highlight] (https://read.readwise.io/read/01hgc80n3vg9nt94ye1m25r4pb))


>![](https://www.datocms-assets.com/2885/1700604740-tf-stacks-k8s-example.png)
>Consider an example of deploying three Kubernetes clusters, each with one or more namespaces, into three different geographies. In a stack, you would use one component to reference a module for deploying the Kubernetes cluster and another component for a module that creates a namespace in it. In order to repeat this Kubernetes cluster across three geographies, you would simply define a deployment for each geography and pass in the appropriate inputs for each, such as region identifiers. ([View Highlight] (https://read.readwise.io/read/01hgc8g9nym3xtxwqv1vm0znmf))



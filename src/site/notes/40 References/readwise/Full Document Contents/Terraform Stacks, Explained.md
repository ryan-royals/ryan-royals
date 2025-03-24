---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-stacks-explained/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1696883278-generic-multi-deployment-environment-example-1.png)

Back in October at [HashiConf 2023](https://www.hashicorp.com/blog/new-terraform-testing-and-ux-features-reduce-toil-errors-and-costs), we announced Terraform stacks, a new feature to simplify infrastructure provisioning and management at scale. This announcement has us and the broader Terraform community excited about one of the biggest changes to hit HashiCorp Terraform in recent years. While stacks are still under development, we wanted to share a few more details and answer some questions.

#### What challenges will Terraform stacks solve?

There are a number of benefits to using small modules and workspaces to build a composable infrastructure. Splitting up your Terraform code into manageable pieces helps: 

* Limit the blast radius of resource changes
* Reduce run time
* Separate management responsibilities across team boundaries
* Work around multi-step use cases such as provisioning a Kubernetes cluster

Terraform’s ability to take code, build a graph of dependencies, and turn it into infrastructure is extremely powerful. However, once you split your infrastructure across multiple Terraform configurations, the isolation between states means you must stitch together and manage dependencies yourself.

Additionally, when deploying and managing infrastructure at scale, teams usually need to provision the same infrastructure multiple times with different input values, across multiple: 

* Cloud provider accounts
* Environments (dev, staging, production)
* Regions
* Landing zones

There is not a built-in way to provision and manage the lifecycle of these instances as a single unit in Terraform today, making it difficult to manage each infrastructure root module individually.

We believe these challenges can be solved in a better and more valuable way than just wrapping Terraform with bespoke scripting and external tooling, which requires heavy lifting and is error-prone and risky to set up and manage.

#### What are Terraform stacks and what are their benefits?

Stacks are a new approach that help users automate and optimize the coordination, deployment, and lifecycle management of interdependent Terraform configurations, reducing the time and overhead of managing infrastructure. Key benefits include:

* **Simplified management**: Stacks reduce the need to manually manage cross-configuration dependencies and manually duplicate configurations for a single infrastructure deployment.
* **Improved productivity**: Stacks empower users to rapidly create and modify multiple consistent infrastructure configurations with differing inputs together, not individually, all with one simple action.

Stacks aim to be a natural next step in extending infrastructure as code to a higher layer using the same Terraform shared modules users enjoy today.

#### Common use cases for Terraform stacks

Here are the common use cases for stacks, out of the box:

* **Deploy an entire application with components like networking, storage, and compute as a single unit without worrying about dependencies**. A stack configuration describes a full unit of infrastructure as code and can be handed to users who don’t have advanced Terraform experience, allowing them to easily stand up a complex infrastructure deployment with a single action.
* **Deploy across multiple regions, availability zones, and cloud provider accounts without duplicating effort/code**. *Deployments* in a stack let you define multiple instances of the same configuration without needing to copy and paste configurations, or manage configurations separately. When a change is made to the stack configuration, it can be rolled out across all, some, or none of the deployments in a stack.

#### How do I use a Terraform stack?

Stacks introduce a new configuration layer, which sits on top of Terraform modules and is written as code. 

##### Components

The first part of this configuration layer, declared with a `.tfstack.hcl` file extension, tells Terraform what infrastructure, or components, should be part of the stack. You can compose and deploy multiple modules that share a lifecycle together using what are called *components* in a stack. Add a *component* block to this configuration for every module you'd like to include in the stack. You don’t need to rewrite any modules since components can simply leverage your existing ones.

##### Deployments

The second part of this configuration layer, which uses a `.tfdeploy.hcl` file extension, tells Terraform where and how many times to deploy the infrastructure in the stack. For each instance of the infrastructure, you add a *deployment* block with the appropriate input values and Terraform will take care of repeating that infrastructure for you. When a new version of the stack configuration is available, plans are initiated for each deployment in the stack. Once the plan is complete, you can approve the change in all, some, or none of the deployments in the stack. 

![Example:](https://www.datocms-assets.com/2885/1700604740-tf-stacks-k8s-example.png)Consider an example of deploying three Kubernetes clusters, each with one or more namespaces, into three different geographies. In a stack, you would use one component to reference a module for deploying the Kubernetes cluster and another component for a module that creates a namespace in it. In order to repeat this Kubernetes cluster across three geographies, you would simply define a deployment for each geography and pass in the appropriate inputs for each, such as region identifiers.

If you decided to add a new namespace to each of your Kubernetes clusters, it would result in plans queued across all three geographies. To test this change before propagating it to multiple geographies, you could add the namespace to the US geo first. After validating everything worked as expected, you could approve the change in the Europe geo next. You have the option to save the plan in the Asia geo for later. Having changes that are not applied in one or more deployments does not prevent new changes that are made to the stack from being planned.

#### What’s next for Terraform stacks?

At HashiConf 2023, we announced the [Terraform Cloud private preview of stacks](https://www.hashicorp.com/blog/new-terraform-testing-and-ux-features-reduce-toil-errors-and-costs#stacks-simplify-provisioning-and-managing-resources-at-scale) to generate early hands-on feedback and ensure that we develop stacks in tune with what our users need.

While our initial private preview is limited to Terraform Cloud, certain stacks functionality will be incorporated in upcoming releases of the Community edition of Terraform. As we get closer to general availability of stacks, we'll be adding stacks in Terraform Enterprise. Workspaces will continue to have their use cases and Terraform will continue to work with both workspaces and stacks.

We hope you’re as excited about stacks as we are, and appreciate your support as we transform how organizations use Terraform to further simplify infrastructure provisioning and management at scale.

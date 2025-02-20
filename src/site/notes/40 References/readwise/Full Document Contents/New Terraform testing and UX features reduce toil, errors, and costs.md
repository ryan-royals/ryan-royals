---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/new-terraform-testing-and-ux-features-reduce-toil-errors-and-costs/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1620073839-blog-library-product-terraform-cloud-tfc-black-corner-iconography.jpg)

Terraform and Terraform Cloud improve developer usability and velocity with a test framework, generated module tests, and stacks.

Today at [HashiConf](https://hashiconf.com/2023/), we are excited to announce new capabilities for HashiCorp Terraform and Terraform Cloud to improve developer velocity, code quality, and infrastructure cost management. The new Terraform and Terraform Cloud announcements include the following:

* **Terraform test framework (GA)** helps produce higher-quality modules
* **Test-integrated module publishing (beta)** streamlines the testing and publishing process
* **Generated module tests (beta)** help module authors get started in seconds
* **Enhanced editor validation in Visual Studio Code (GA)** makes it easier to find and resolve errors
* **Stacks (private preview)** simplifies infrastructure provisioning and management at scale
* **Ephemeral workspaces (GA)** help optimize infrastructure spend

#### Terraform tests help produce high-quality, reliable modules

Modules are a primary way Terraform customers standardize their infrastructure provisioning, so it is crucial to have high-quality, reliable modules. A bug in a module’s code can cause outages, compliance breaches, or open security holes — and not just once, but every time it’s reused. Without a testing framework, this quality control process can be slow and laborious — worse, sometimes testing is skipped altogether.

The Terraform community has built several excellent testing tools, but they often use full programming languages such as Ruby or Go. For a while, we’ve wanted to bring native testing to Terraform using HashiCorp Configuration Language (HCL), removing the need for context switching or additional learning.

The Terraform test framework, introduced in Terraform 1.6, gives developers easy-to-use tools to perform unit and integration testing of Terraform code. Module authors can adopt the test framework quickly because it is written in HCL and uses a structure similar to Terraform configurations. You can learn more about the Terraform test framework in the [Terraform 1.6 blog post](https://www.hashicorp.com/blog/terraform-1-6-adds-a-test-framework-for-enhanced-code-validation) and [Testing Terraform documentation](https://developer.hashicorp.com/terraform/cli/test).

To truly benefit from high-quality modules, however, organizations also need a way to control and publish them systematically. That’s why we created test-integrated module publishing for Terraform Cloud, available through the private registry. This new feature helps module authors streamline the module testing and publishing process.

First, a new branch-based publishing method in the private registry enables greater control over when and how modules are published. Unlike the current Git tag-based publishing, the branch-based method lets registry maintainers publish new module versions directly from the registry. Building on this new publishing workflow, the Terraform test framework is now directly integrated with the private registry.

Once enabled on a module, test runs will execute automatically based on version control events such as pull requests and merges, and can be initiated from the CLI or API. Just like workspace runs, tests execute remotely in a secure environment, eliminating the need for developers to handle sensitive cloud credentials on their workstation. With integrated tests and more direct control over publishing, platform teams can be confident new module versions are well-tested before making them available to downstream users.

Terraform Cloud Free users can have up to 5 test-integrated modules while Terraform Cloud Standard users can have up to 10 test-integrated modules. Customers using the Terraform Cloud Plus tier will have unlimited test-integrated modules.

For more information on test-integrated module publishing, check out our [tutorial on How to write Terraform tests](https://developer.hashicorp.com/terraform/tutorials/configuration-language/test) and the [documentation on test-integrated modules in the Terraform Cloud private registry](https://developer.hashicorp.com/terraform/cloud-docs/registry/test).

![The history of test results for a module is tracked directly in the private registry.](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1696883243-registry-tests-5.png&w=3840&q=75)The history of test results for a module is tracked directly in the private registry.
#### Generated module tests jumpstart Terraform test writing

The new test framework is designed to be easy to use, but it still takes time to learn a new framework, especially for module authors who may not know how to get started. To jumpstart that process, Terraform is using generative AI to help organizations instantly produce module tests as a starting point for module authors.

Our new generated module tests feature leverages a large language model (LLM) to auto-generate a suite of customized tests for a module within the private registry. This model is specifically trained on HCL and the Terraform test framework to help module authors begin testing their code right away.

This feature, currently in beta, is available in the private registry for Terraform Cloud Plus organizations. With the press of a button, Terraform Cloud will generate the code for one or more tests that are specifically customized to the module. Authors can copy or download the code from the UI and add it to their module repository right away, and it will be saved for later use. You can learn more in the [generated module testing documentation](https://developer.hashicorp.com/terraform/cloud-docs/registry/test#generated-module-tests).

Customer data security is very important to us, and our AI-test generation features have been built so that no customer or community module data is used for training models and module data won’t be stored with third-party vendors.

![Users can copy and paste the AI-generated test code to run the Terraform testing framework.](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1696883270-generate-tests-4.png&w=3840&q=75)
Users can copy and paste the AI-generated test code to run the Terraform testing framework.

You can also see the test-integrated module publishing and generated module tests in action:

Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/J1z7A0y2LMw?autoplay=0&mute=0&controls=1&origin=https%3A%2F%2Fwww.hashicorp.com&playsinline=1&showinfo=0&rel=0&iv_load_policy=3&modestbranding=1&enablejsapi=1&widgetid=1) 

#### Enhanced editor validation makes resolving errors easier

When writing Terraform code, either by hand or by leveraging the latest generative AI tools, errors are a fact of life. That means developers often find themselves context switching between their editor and the CLI to validate code, leading to frustration and reducing productivity.

Enhanced editor validation in the [Terraform extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=HashiCorp.terraform) automatically validates Terraform code as early as possible, creating an enhanced, integrated authoring experience by highlighting errors and providing guidance to help resolve issues quickly. Examples of these new validations include:

* Identifying missing variable declarations or required attributes
* Highlighting unexpected attributes or blocks
* Issuing warnings for deprecated attributes.

Validation errors (underlined in red) are immediately identified within the editor, without context switching.

#### Stacks simplify provisioning and managing resources at scale

Today, users can leverage a modular approach to infrastructure with Terraform, but large-scale deployment and management often remains tedious, complex, and repetitive.

For example, when provisioning multiple root modules or workspaces together, users must first understand their dependencies and manually deploy each module or workspace, one by one in the correct order. This complexity gets worse when users need to deploy the same infrastructure multiple times across multiple environments, regions, landing zones, or accounts within a cloud provider.

*Stacks*\* are a new approach that help users automate and optimize the coordination, deployment, and lifecycle management of interdependent Terraform configurations, reducing the time and overhead of managing infrastructure.

Multiple Terraform modules can be organized and deployed together in a stack using *components*, a construct that groups together different interdependent systems, such as network and database modules. Once this set of components is defined, it can be effortlessly replicated multiple times across what are known as *deployments in a stack*. This is especially useful for deploying the same infrastructure across multiple environments (e.g. staging, QA, and production) or regions. With differing input values in each deployment, users can consistently create and expand complex infrastructure with one simple action.

To learn more about stacks, [sign up for a free HashiConf virtual pass](https://hashiconf.com/2023/) to watch the Terraform and Packer roadmap session live at 1:30 p.m. ET / 10:30 a.m. PT on Wednesday, Oct. 11, or on-demand once HashiConf concludes. Stacks are currently in private preview.

\* U.S. and foreign patents pending

![Stacks eliminate the need to manually manage cross-configuration dependencies and duplicated configurations.](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1696883278-generic-multi-deployment-environment-example-1.png&w=3840&q=75)
Stacks eliminate the need to manually manage cross-configuration dependencies and duplicated configurations.

#### Ephemeral workspaces automatically optimize infrastructure spend

Back in August, HashiCorp announced the [public beta of ephemeral workspaces](https://www.hashicorp.com/blog/terraform-ephemeral-workspaces-public-beta-now-available). Today we are excited to announce the general availability of ephemeral workspaces for Terraform Cloud Plus and Terraform Enterprise. This feature lets customers schedule a time to automatically destroy non-production resources, eliminating the need for manual cleanup, streamlining infrastructure lifecycle management, and, perhaps most importantly, reducing infrastructure costs.

To learn more, please refer to the [workspace destruction and deletion documentation](https://developer.hashicorp.com/terraform/cloud-docs/workspaces/settings/deletion#automatically-destroy).

#### Get started with Terraform Cloud

As organizations look to optimize infrastructure operations and spend, Terraform is adding features to improve developer velocity, including the Terraform test framework and the test-integrated module testing workflow to produce and publish high-quality modules, along with generated module tests to jumpstart adoption. The enhanced editor validation helps resolve errors quickly without context switching. At the same time, ephemeral workspaces are helping customers cut costs with an easy way to enforce a time-to-live policy.

Together, these Terraform enhancements represent significant steps toward our goal of helping customers maximize their infrastructure investments and speed application delivery.

You can try many of these new features now. If you are new to Terraform, [sign up for HashiCorp Terraform Cloud](https://app.terraform.io/public/signup/account) and get started for free today.

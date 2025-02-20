---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-landing-zones-accelerators-for-bicep-and-terraform-announcing-general-availability/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/favicon.ico)

The Azure Landing Zones team is delighted to announce the general availability of our Azure Landing Zones Accelerators for [Bicep](https://github.com/Azure/ALZ-Bicep/wiki/Accelerator) and [Terraform](https://github.com/Azure/alz-terraform-accelerator/wiki), having both reached the version 1.0 milestone. This article will provide an overview of the accelerators and dive into the common approaches for deploying them.

We'll cover:

* What is an Azure Landing Zone?
* What are the Azure Landing Zones Accelerators?
* Why should you use an Accelerator?
* How do you use the Accelerator?
* What does the Bicep Accelerator deploy and configure?
* What does the Terraform Accelerator deploy and configure?
* Where can you learn more?
* Thank you to our collaborators!

#### What is an Azure Landing Zone?

An Azure Landing Zone serves as the cornerstone of your cloud adoption, establishing guardrails and facilitating the deployment of workloads into Azure in a secure, standardized, and scalable manner. Further details can be found in our Cloud Adtion Framework documentation under: [What is an Azure landing zone?](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/)

For the purpose of this article, you can consider the landing zone to consist of the initial setup of:

* Management groups
* Azure RBAC Roles
* Azure Policy
* Management resources, such as centralized logging and automation accounts
* Hub networking, Azure DNS, and other connectivity resources

See the green boxes in this diagram:

*Figure: Azure Landing Zones Accelerator Scope*

#### What are the Azure Landing Zones Accelerators?

The Azure Landing Zones Accelerators for [Bicep](https://github.com/Azure/ALZ-Bicep/wiki/Accelerator) and [Terraform](https://github.com/Azure/alz-terraform-accelerator/wiki) serve as automation frameworks and include corresponding documentation. Their purpose is to assist our customers and partners in swiftly deploying their Azure Landing Zone architecture by utilizing our pre-existing Azure Landing Zones [Bicep](https://github.com/Azure/ALZ-Bicep) or [Terraform](https://github.com/Azure/terraform-azurerm-caf-enterprise-scale) modules and adhering to best practices. While these accelerators are crafted to meet the requirements of 90% of users by default, they can be tailored to accommodate the specific needs of advanced scenarios.

The Accelerators follow a three phase approach:

1. Pre-requisites: Instructions to configure credentials and subscriptions.
2. Bootstrap: Automation or instructions to bootstrap managed IaC modules into Continuous Integration and Continuous Delivery Pipelines.
3. Run: Trigger the pipelines to deploy the Azure Landing Zone architecture.

The Accelerators offer support for utilizing GitHub or Azure DevOps as targets for the bootstrapping automation.

#### Why should you use an Accelerator?

The Azure Landing Zones Accelerators for Bicep and Terraform play a crucial role in minimizing the effort needed for analyzing and creating an Azure Landing Zone deployment. They offer opinionated patterns and comprehensive automation for setting up Azure Landing Zones modules, ensuring a production-ready configuration.

Before the Accelerators were available, teams invested considerable time constructing their automation for our Azure Landing Zones modules and making decisions regarding the configuration and security of Continuous Delivery. The Accelerators eliminate this overhead by offering a reusable deployment pattern.

#### How do you use the Accelerator?

The Accelerators wikis provide comprehensive documentation and quick start guides for using the Accelerators. These can be found here:

The Accelerators use a shared approach to the bootstrapping process with a common PowerShell module. The [ALZ PowerShell](https://github.com/Azure/ALZ-PowerShell-Module) module is available from the [PowerShell Gallery](https://www.powershellgallery.com/packages/ALZ/1.1.4).

The basic PowerShell to bootstrap GitHub or Azure DevOps is:

```
# Install the PowerShell Module
Install-Module -Name ALZ

# Deploy the Bootstrap for Bicep and GitHub
New-ALZEnvironment -i "bicep" -c "github"

# Deploy the Bootstrap for Bicep and Azure DevOps
New-ALZEnvironment -i "bicep" -c "azuredevops"

# Deploy the Bootstrap for Terraform and GitHub
New-ALZEnvironment -i "terraform" -c "github"

# Deploy the Bootstrap for Terraform and Azure DevOps
New-ALZEnvironment -i "terraform" -c "azuredevops"
```

#### What does the Bicep Accelerator deploy and configure?

The Azure Landing Zone Bicep Accelerator comes with a comprehensive set of instructions to guide you through the provisioning process. It assists in selecting options that are relevant to your needs and prompts you for choices within the PowerShell automation.

The Bicep Accelerator offers flexibility, allowing you to determine how you want to secure your repositories and pipelines/actions. While we provide guidance and examples, you have the freedom to choose the type of authentication that GitHub or Azure DevOps employs.

Details of what is deployed by following the Accelerator steps:

* **Microsoft Azure**  

	+ Deployment identity
* **Version Control System (GitHub or Azure DevOps)**
	+ Repositories and files
	+ Azure Pipelines/GitHub Workflows
	+ Environment Variables
	+ Branch Policies

Additionally, we provide prescription documentation for managing specific scenarios:

* Handling upgrades to newer versions of ALZ-Bicep.
* An opinionated approach to introducing a branching strategy into your CI/CD process.
* Process for incorporating modified ALZ-Bicep Modules into the Accelerator framework.

Ultimately, the documentation comprehensively guides the setup of Azure DevOps/GitHub, encompassing the configuration of the repository, pipelines, and branch policies. Furthermore, there are intentions to implement automation to streamline and reduce manual efforts. Stay tuned for future updates on this blog post as we finalize and incorporate these enhancements!

#### What does the Terraform Accelerator deploy and configure?

The Azure Landing Zones Terraform Accelerator has many options to choose from when deploying the bootstrap. You can use variables to choose between the options shown in the table below. Our default options are shown in green text, as these provide the highest level of security and leverage best practice authentication.

|  |  |  |  |
| --- | --- | --- | --- |
| **Version Control System** | **Agents / Runners** | **Networking** | **Authentication** |
| GitHub | Microsoft Hosted | Public | Workload identity federation |
| GitHub | Self Hosted | Public | Workload identity federation |
| **GitHub** | **Self Hosted** | **Private** | **Workload identity federation** |
| Azure DevOps | Microsoft Hosted | Public | Workload identity federation |
| Azure DevOps | Self Hosted | Public | Workload identity federation |
| **Azure DevOps** | **Self Hosted** | **Private** | **Workload identity federation** |
| Azure DevOps | Self Hosted | Public | Managed identity |
| Azure DevOps | Self Hosted | Private | Managed identity |

The Terraform Accelerator follows the 3 phase approach as described previously:

Details of what is deployed by the bootstrap can be found in our [documentation](https://github.com/Azure/alz-terraform-accelerator/wiki#accelerator-features), but in summary the bootstrap will deploy:

* Microsoft Azure
	+ Storage
	+ Identity
	+ Networking
	+ Self-hosted Agents / Runners
* Version Control System (GitHub or Azure DevOps)
	+ Repositories and files
	+ Pipelines / Actions
	+ Environments
	+ Approvals
	+ Branch Policies
	+ Variables

#### Where can you learn more?

The best starting point for information on the Accelerators is the documentation for [Bicep](https://github.com/Azure/ALZ-Bicep/wiki/Accelerator) and [Terraform](https://github.com/Azure/alz-terraform-accelerator/wiki).

If you encounter a question that isn't addressed there or come across an issue not covered in our FAQ or Troubleshooting guides, feel free to raise the issue in the relevant repository.

#### Thank you to our collaborators

We express our heartfelt gratitude to everyone who collaborated on the Azure Landing Zones Accelerators. The tremendous support from individuals involved in testing, offering feedback, contributing code, documentation, and ideas has been invaluable. Thank you for your dedication and contributions to the success of the Accelerators.

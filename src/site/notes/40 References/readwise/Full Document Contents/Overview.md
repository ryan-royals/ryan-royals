---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/overview/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Usage Scenarios](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/overview?view=azure-devops#usage-scenarios)
2. [Benefits](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/overview?view=azure-devops#benefits)
3. [Get Started](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/overview?view=azure-devops#get-started)

Managed DevOps Pools empowers development teams to quickly and easily spin up Azure DevOps agent pools that are tailored to a team's specific needs. Managed DevOps Pools implements security best practices, provides knobs to balance cost and performance, provides paths for the most common scenarios, and significantly reduces time spent in creating and maintaining custom pools.

Managed DevOps Pools is an evolution of Azure DevOps Virtual Machine Scale Set agent pools, simplifying custom pool creation even further, by improving scalability and reliability of custom pools. Managed DevOps Pools is a fully managed service where virtual machines or containers powering the agents live in a Microsoft Azure subscription and not in your own Azure subscription, like when using Azure DevOps Virtual Machine Scale Set agent pools. For more information, see [Microsoft Managed DevOps Pools architecture overview](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/architecture-overview?view=azure-devops).

#### Usage Scenarios

Manage DevOps Pools:

* Has more powerful agents than those available in the out-of-the-box agents
* Uses a virtual machine image that is custom tailored by you for your CI/CD workload
* Has agents in the geographical region closest to your dependencies
* Scales up and down based on your configuration
* Can maintain state of your agents up to seven days, so your builds are faster due to cache hits
* Can run long running workflows up to two days long
* Can access resources in your company network or isolate your workload to only access specific endpoints
* Can create agents that have the same software as Azure Pipelines Microsoft-hosted agents
* Can view all active agents and the status of agent provisioning and reimaging.
* Can have an additional data disk, so you don't have to use a larger SKU just to get more disk space
* Reduce your Azure cost by up to 80%, with SPOT instances (Coming by GA)
* Has container agents (Coming by GA)
* Purged problem stateful agents out of the pool (Coming by GA)
* Can fall back to another geographical region when the primary region experiences an outage (Coming by GA)

#### Benefits

Managed DevOps Pools provide the following benefits to creating, configuring, and managing Azure DevOps agent pools in the cloud:

**Time spent in Management**: Managed DevOps Pools is designed to reduce time spent in managing CI/CD infrastructure. This will free up Platform Engineering cycles or Dev Team cycles to focus on other problems.

**Team-specific Pools**: Due to the ease with which new pools can be created, Platform Engineering can very easily create multiple team-specific pools, preventing teams from noisy neighbor situations and tailoring pools to suit the needs of individual teams.

**Worry-free Self-Service**: Platform Engineering can choose to empower development teams to create their own custom pools without compromising on governance, by allowing the use of curated images and networks.

**Azure Cost**: Managed DevOps pools will help optimize your Azure cost based on your CI/CD workload's unique needs.

**Scalable**: Managed DevOps pools are scalable up to thousands of agents running simultaneously.

**Reliable**: Your developers will experience lowest amount of downtime due to the high uptimes of Managed DevOps pools.

**Security**: Your pool's agents are secured by Microsoft's best practices, and has features to further secure your pool.

#### Get Started

To start using Managed DevOps Pools, see [Get started with Managed DevOps Pools](https://learn.microsoft.com/en-us/azure/devops/managed-devops-pools/quickstart-azure-portal?view=azure-devops).

---
{"dg-publish":true,"permalink":"/40-references/readwise/about-azure-private-networking-for-git-hub-hosted-runners/","tags":["rw/articles"]}
---

![rw-book-cover](https://github.githubassets.com/images/modules/open_graph/github-logo.png)

## Full Document
[[40 References/readwise/Full Document Contents/About Azure Private Networking for GitHub-hosted Runners\|Readwise/Full Document Contents/About Azure Private Networking for GitHub-hosted Runners.md]]

## Highlights
2-64 vCPU Ubuntu and Windows runners are supported with Azure VNET. For more information on these runner types, see "[About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners#about-ubuntu-and-windows-larger-runners)."
Private networking for GitHub-hosted runners does not support static IP addresses for larger runners. You must use dynamic IP addresses, which is the default configuration for larger runners. For more information about networking for larger runners, see "[About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners#networking-for-larger-runners)." ([View Highlight] (https://read.readwise.io/read/01hty02g4kjfbtheg2zztcvb3v))


[About network communication](https://docs.github.com/en/organizations/managing-organization-settings/about-azure-private-networking-for-github-hosted-runners-in-your-organization#about-network-communication)
To facilitate communication between GitHub networks and your VNET, a GitHub-hosted runner's network interface card (NIC) deploys into your Azure VNET. ([View Highlight] (https://read.readwise.io/read/01hty02r329ghhh68yaccqpy34))


It is recommended to explicitly block all inbound connections to the runners. GitHub will never require inbound connections to these machines. ([View Highlight] (https://read.readwise.io/read/01hty03c6rcs92nwqew6e346x5))


![Diagram of the network communication architecture between GitHub networks and your private networks. The diagram describes each step in connecting GitHub-hosted runners to an Azure VNET. Each step is numbered and the numbers correspond to the numbered descriptions of the step listed below the diagram.](https://docs.github.com/assets/cb-275807/images/help/actions/actions-vnet-injected-larger-runners-architecture.png) ([View Highlight] (https://read.readwise.io/read/01hty03z6nf733hw2ea2t8bc1d))


In order to successfully deploy a NIC and join a NIC to a subnet, the GitHub Actions service maintains the following Azure role-based access control (RBAC) permissions in your Azure subscription ([View Highlight] (https://read.readwise.io/read/01hty05byapbxwtgc03smjg222))


• `GitHub.Network/operations/read`
• `GitHub.Network/networkSettings/read`
• `GitHub.Network/networkSettings/write`
• `GitHub.Network/networkSettings/delete` ([View Highlight] (https://read.readwise.io/read/01hty05m86edvdpch761ta9ynh))


The following permissions will be present on two enterprise applications in your Azure tenant. You will see the enterprise applications your Azure tenant after configuring Azure private networking.
• `GitHub CPS Network Service` id: `85c49807-809d-4249-86e7-192762525474`
• `GitHub Actions API` id: `4435c199-c3da-46b9-a61d-76de3f2c9f82` ([View Highlight] (https://read.readwise.io/read/01hty09wj5tv7rq41fs9v73mnp))


if your VNET is configured with an Azure ExpressRoute to provide access to on-premises resources (e.g. Artifactory) or connected to a VPN tunnel to provide access to other cloud-based resources, those access policies also apply to your runners. Additionally, any outbound rules applied to your VNET's network security group (NSG) also apply, giving you the ability to control outbound access for your runners. ([View Highlight] (https://read.readwise.io/read/01hty0ab8a15pm87347s3vym71))



---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/about-azure-private-networking-for-git-hub-hosted-runners/","tags":["rw/articles"]}
---

![rw-book-cover](https://github.githubassets.com/images/modules/open_graph/github-logo.png)

You can use GitHub-hosted runners in an Azure VNET. This enables you to use GitHub-managed infrastructure for CI/CD while providing you with full control over the networking policies of your runners. For more information about Azure VNET, see [What is Azure Virtual Network?](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview) in the Azure documentation.

You can connect multiple VNET subnets to GitHub.com and manage private resource access for your runners via runner groups. For more information about runner groups, see "[Controlling access to larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/controlling-access-to-larger-runners)."

Using GitHub-hosted runners within Azure VNET allows you to perform the following actions.

* Privately connect a runner to resources inside an Azure VNET without opening internet ports, including on-premises resources accessible from the Azure VNET.
* Restrict what GitHub-hosted runners can access or connect to with full control over outbound network policies.
* Monitor network logs for GitHub-hosted runners and view all connectivity to and from a runner.

2-64 vCPU Ubuntu and Windows runners are supported with Azure VNET. For more information on these runner types, see "[About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners#about-ubuntu-and-windows-larger-runners)."

Private networking for GitHub-hosted runners does not support static IP addresses for larger runners. You must use dynamic IP addresses, which is the default configuration for larger runners. For more information about networking for larger runners, see "[About larger runners](https://docs.github.com/en/actions/using-github-hosted-runners/about-larger-runners/about-larger-runners#networking-for-larger-runners)."

To facilitate communication between GitHub networks and your VNET, a GitHub-hosted runner's network interface card (NIC) deploys into your Azure VNET.

Because the NIC lives within your VNET, GitHub cannot block inbound connections. By default, Azure virtual machines will accept inbound connections from the same VNET. For more information, see [`AllowVNetInBound`](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview#allowvnetinbound) on Microsoft Learn. It is recommended to explicitly block all inbound connections to the runners. GitHub will never require inbound connections to these machines.

A NIC enables an Azure virtual machine (VM) to communicate with internet, Azure, and on-premises resources. This way, all communication is kept private within the network boundaries, and networking policies applied to the VNET also apply to the runner. For more information on how to manage a network interface, see [Change network interface settings](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-network-interface?tabs=azure-portal#change-network-interface-settings) on Microsoft Learn.

![Diagram of the network communication architecture between GitHub networks and your private networks. The diagram describes each step in connecting GitHub-hosted runners to an Azure VNET. Each step is numbered and the numbers correspond to the numbered descriptions of the step listed below the diagram.](https://docs.github.com/assets/cb-275807/images/help/actions/actions-vnet-injected-larger-runners-architecture.png)
1. A GitHub Actions workflow is triggered.
2. The GitHub Actions service creates a runner.
3. The runner service deploys the GitHub-hosted runner's network interface card (NIC) into your Azure VNET.
4. The runner agent picks up the workflow job. The GitHub Actions service queues the job.
5. The runner sends logs back to the GitHub Actions service.
6. The NIC accesses on-premise resources.

The GitHub Actions service supports a subset of all the regions that Azure provides. To facilitate communication between the GitHub Actions service and your subnet, your subnet must be in one of the following supported regions.

* `EastUs`
* `EastUs2`
* `WestUs2`
* `AustraliaEast`
* `CentralUs`
* `FranceCentral`
* `NorthEurope`
* `NorwayEast`
* `SoutheastAsia`
* `SwitzerlandNorth`
* `UkSouth`
* `WestEurope`

Azure private networking supports GPU runners in the following regions.

* `EastUs`
* `WestUs`
* `NorthCentralUs`
* `SouthCentralUs`

You may also use global virtual network peering to connect virtual networks across Azure regions. For more information, see [Virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) in the Azure documentation.

In order to successfully deploy a NIC and join a NIC to a subnet, the GitHub Actions service maintains the following Azure role-based access control (RBAC) permissions in your Azure subscription. For more information about fine-grained access management of Azure resources, see [Azure RBAC](https://learn.microsoft.com/en-us/azure/role-based-access-control/) in the Azure documentation.

* `GitHub.Network/operations/read`
* `GitHub.Network/networkSettings/read`
* `GitHub.Network/networkSettings/write`
* `GitHub.Network/networkSettings/delete`
* `Microsoft.Network/locations/operations/read`
* `Microsoft.Network/locations/operationResults/read`
* `Microsoft.Network/locations/usages/read`
* `Microsoft.Network/networkInterfaces/read`
* `Microsoft.Network/networkInterfaces/write`
* `Microsoft.Network/networkInterfaces/delete`
* `Microsoft.Network/networkInterfaces/join/action`
* `Microsoft.Network/networkSecurityGroups/join/action`
* `Microsoft.Network/networkSecurityGroups/read`
* `Microsoft.Network/publicIpAddresses/read`
* `Microsoft.Network/publicIpAddresses/write`
* `Microsoft.Network/publicIPAddresses/join/action`
* `Microsoft.Network/routeTables/join/action`
* `Microsoft.Network/virtualNetworks/read`
* `Microsoft.Network/virtualNetworks/subnets/join/action`
* `Microsoft.Network/virtualNetworks/subnets/read`
* `Microsoft.Network/virtualNetworks/subnets/write`
* `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/delete`
* `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/read`
* `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/write`
* `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/details/read`
* `Microsoft.Network/virtualNetworks/subnets/serviceAssociationLinks/validate/action`
* `Microsoft.Resources/subscriptions/resourceGroups/read`
* `Microsoft.Resources/subscriptions/resourcegroups/deployments/read`
* `Microsoft.Resources/subscriptions/resourcegroups/deployments/write`
* `Microsoft.Resources/subscriptions/resourcegroups/deployments/operations/read`
* `Microsoft.Resources/deployments/read`
* `Microsoft.Resources/deployments/write`
* `Microsoft.Resources/deployments/operationStatuses/read`

The following permissions will be present on two enterprise applications in your Azure tenant. You will see the enterprise applications your Azure tenant after configuring Azure private networking.

* `GitHub CPS Network Service` id: `85c49807-809d-4249-86e7-192762525474`
* `GitHub Actions API` id: `4435c199-c3da-46b9-a61d-76de3f2c9f82`

Because the GitHub-hosted runner's NIC is deployed into your Azure VNET, networking policies applied to the VNET also apply to the runner.

For example, if your VNET is configured with an Azure ExpressRoute to provide access to on-premises resources (e.g. Artifactory) or connected to a VPN tunnel to provide access to other cloud-based resources, those access policies also apply to your runners. Additionally, any outbound rules applied to your VNET's network security group (NSG) also apply, giving you the ability to control outbound access for your runners.

If you have enabled any network logs monitoring for your VNET, you can also monitor network traffic for your runners.

To use GitHub-hosted runners with an Azure VNET, you will need to configure your Azure resources and then create a networking configuration in GitHub.

For procedures to configure Azure private networking at the organization level, see "[Configuring private networking for GitHub-hosted runners in your organization](https://docs.github.com/en/organizations/managing-organization-settings/configuring-private-networking-for-github-hosted-runners-in-your-organization)."

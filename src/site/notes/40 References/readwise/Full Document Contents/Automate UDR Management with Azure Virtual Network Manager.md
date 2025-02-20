---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/automate-udr-management-with-azure-virtual-network-manager/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [What is UDR management?](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-user-defined-route#what-is-udr-management)
2. [How does UDR management work?](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-user-defined-route#how-does-udr-management-work)
3. [Common routing scenarios](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-user-defined-route#common-routing-scenarios)
4. [Local routing settings](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-user-defined-route#local-routing-settings)
5. [Limitations of UDR management](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-user-defined-route#limitations-of-udr-management)
6. [Next step](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-user-defined-route#next-step)

This article provides an overview of UDR management, why it's important, how it works, and common routing scenarios that you can simplify and automate using UDR management.

Important

User-defined routese management with Azure Virtual Network Manager is in public preview. Public previews are made available to you on the condition that you agree to the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/). Some features might not be supported or might have constrained capabilities. This preview version is provided without a service level agreement, and it's not recommended for production workloads.

Important

Azure Virtual Network Manager is generally available for Virtual Network Manager, hub-and-spoke connectivity configurations, and security configurations with security admin rules. Mesh connectivity configurations remain in public preview.

This preview version is provided without a service level agreement, and it's not recommended for production workloads. Certain features might not be supported or might have constrained capabilities. For more information, see [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/).

#### What is UDR management?

Azure Virtual Network Manager (AVNM) allows you to describe your desired routing behavior and orchestrate user-defined routes (UDRs) to create and maintain the desired routing behavior. User-defined routes address the need for automation and simplification in managing routing behaviors. Currently, you’d manually create User-Defined Routes (UDRs) or utilize custom scripts. However, these methods are prone to errors and overly complicated. You can utilize the Azure-managed hub in Virtual WAN. This option has certain limitations (such as the inability to customize the hub or lack of IPV6 support) not be relevant to your organization. With UDR management in your virtual network manager, you have a centralized hub for managing and maintaining routing behaviors.

#### How does UDR management work?

In virtual network manager, you create a routing configuration. Inside the configuration, you create rule collections to describe the UDRs needed for a network group (target network group). In the rule collection, route rules are used to describe the desired routing behavior for the subnets or virtual networks in the target network group. Once the configuration is created, you'll need to [deploy the configuration](https://learn.microsoft.com/en-us/azure/virtual-network-manager/concept-deployments) for it to apply to your resources. Upon deployment, all routes are stored in a route table located inside a virtual network manager-managed resource group.

Routing configurations create UDRs for you based on what the route rules specify. For example, you can specify that the spoke network group, consisting of two virtual networks, accesses the DNS service's address through a Firewall. Your network manager creates UDRs to make this routing behavior happen.

![Diagram of user-defined rules being applied to virtual networks to route DNS traffic through firewall.](https://learn.microsoft.com/en-us/azure/virtual-network-manager/media/concept-udr-management/udr-management-example.png)
##### Routing configurations

Routing configurations are the building blocks of UDR management. They're used to describe the desired routing behavior for a network group. A routing configuration consists of the following settings:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | The name of the routing configuration. |
| **Description** | The description of the routing configuration. |

##### Route collection settings

A route collection consists of the following settings:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | The name of the route collection. |
| **Local routing settings** | The local routing settings for the route collection. |
| **Enable BGP route propagation** | The BGP settings for the route collection. |
| **Target network group** | The target network group for the route collection. |
| **Route rules** | The route rules that describe the desired routing behavior for the target network group. |

![Screenshot of a configured rule collection with a routing rule.](https://learn.microsoft.com/en-us/azure/virtual-network-manager/media/how-to-deploy-user-defined-routes/rule-collection-settings.png)
##### Route rule settings

Each route rule consists of the following settings:

| **Attribute** | **Description** |
| --- | --- |
| **Name** | The name of the route rule. |
| **Destination type** |  |
| IP address | The IP address of the destination. |
| Destination IP addresses/CIDR ranges | The IP address or CIDR range of the destination. |
| Service tag | The service tag of the destination. |
| **Next hop type** |  |
| Virtual network gateway | The virtual network gateway as the next hop. |
| Virtual network | The virtual network as the next hop. |
| Internet | The Internet as the next hop. |
| Virtual appliance | The virtual appliance as the next hop. |
| **Next hop address** | The IP address of the next hop. |

![Screenshot of configured routing rule.](https://learn.microsoft.com/en-us/azure/virtual-network-manager/media/how-to-deploy-user-defined-routes/routing-rule-settings.png)
For each type of next hop, refer to [used-defined routes](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#user-defined).

##### Common destination patterns for IP Addresses

When creating route rules, you can specify the destination type and address. When you specify the destination type as an IP address, you can specify the IP address information. The following are common destination patterns: The following are common destination patterns:

| **Traffic destination** | **Description** |
| --- | --- |
| **Internet > NVA** | For traffic destined to the Internet through a network virtual appliance, enter **0.0.0.0/0** as the destination in the rule. |
| **Private traffic > NVA** | For traffic destined to the private space through a network virtual appliance, enter **192.168.0.0/16, 172.16.0.0/12, 40.0.0.0/24, 10.0.0.0/24** as the destination in the rule. These destinations are based on the RFC1918 private IP address space. |
| **Spoke network > NVA** | For traffic bound between two spoke virtual networks connecting through a network virtual appliance, enter the CIDRs of the spokes as the destination in the rule. |

##### Use Azure Firewall as the next hop

You can also easily choose an Azure Firewall as the next hop by selecting **Import Azure firewall private IP address** when creating your routing rule. The IP address of the Azure Firewall is then used as the next hop.

![Screenshot of routing rule with Azure Firewall option.](https://learn.microsoft.com/en-us/azure/virtual-network-manager/media/how-to-deploy-user-defined-routes/add-routing-rule-azure-firewall.png)
#### Common routing scenarios

Here are the common routing scenarios that you can simplify and automate by using UDR management.

| **Routing scenarios** | **Description** |
| --- | --- |
| Spoke network -> Network Virtual Appliance -> Spoke network | Use this scenario for traffic bound between two spoke virtual networks connecting through a network virtual appliance. |
| Spoke network -> Network Virtual Appliance -> Endpoint or Service in Hub network | Use this scenario for spoke network traffic for a service endpoint in a hub network connecting through a network virtual appliance. |
| Subnet -> Network Virtual Appliance -> Subnet even in the same virtual network |  |
| Spoke network -> Network Virtual Appliance -> On-premises network/internet | Use this scenario when you have Internet traffic outbound through a network virtual appliance or an on-premises location, such as hybrid network scenarios. |
| Cross-hub and spoke network via Network Virtual Appliances in each hub |  |
| hub and spoke network with Spoke network to on-premises needs to go via Network Virtual Appliance |  |
| Gateway -> Network Virtual Appliance -> Spoke network |  |

#### Local routing settings

When you create a rule collection, you define the local routing settings. The local routing settings determine how traffic is routed within the same virtual network or subnet. The following are the local routing settings:

| **Local routing setting** | **Description** |
| --- | --- |
| **Direct routing within virtual network** | Route traffic directly to the destination within the same virtual network. |
| **Direct routing within subnet** | Route traffic directly to the destination within the same subnet. |
| **Not specified** | Route traffic to the next hop specified in the route rule. |

When you select **Direct routing within virtual network** or **Direct routing within subne**t, a UDR with a virtual network next hop is created for local traffic routing within the same virtual network or subnet. However, if the destination CIDR is fully contained within the source CIDR under these selections and direct routing is selected, a UDR specifying a network appliance as the next hop won't be set up.

#### Limitations of UDR management

The following are the limitations of UDR management with Azure Virtual Network Manager:

* When conflicting routing rules exist (rules with same destination but different next hops), they aren't supported within or across rule collections that target the same virtual network or subnet.
* When you create a route rule with the same destination as an existing route in the route table, the routing rule is ignored.
* When a virtual network manager-created UDR is manually modified in the route table, the route isn't up when an empty commit is performed. Also, any update to the rule isn't reflected in the route with the same destination.
* Existing Azure services in the Hub virtual network maintain their existing limitations with respect to Route Table and UDRs.
* Azure Virtual Network Manager requires a managed resource group to store the route table. If you need to delete the resource group, deletion must happen before any new deployments are attempted for resources in the same subscription.

#### Next step

[Learn how to create user-defined routes in Azure Virtual Network Manager](https://learn.microsoft.com/en-us/azure/virtual-network-manager/how-to-create-user-defined-routes).

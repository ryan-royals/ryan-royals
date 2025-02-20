---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/configure-peering-for-an-express-route-deployment-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

[Previous](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/5-exercise-provision-expressroute-circuit/) 

* #### Design and implement Azure ExpressRoute

	+ [Introduction 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/1-introduction/)
	+ [Explore Azure ExpressRoute 22 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/2-explore/)
	+ [Design an ExpressRoute deployment 7 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/3-design-expressroute-deployment/)
	+ [Exercise: configure an ExpressRoute gateway 5 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/4-exercise-configure-expressroute-gateway/)
	+ [Exercise: provision an ExpressRoute circuit 5 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/5-exercise-provision-expressroute-circuit/)
	+ [Configure peering for an ExpressRoute deployment 10 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/6-configure-peering-for-expressroute-deployment/)
	+ [Connect an ExpressRoute circuit to a virtual network 5 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/7-connect-expressroute-circuit-virtual-network/)
	+ [Connect geographically dispersed networks with ExpressRoute global reach 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/8-connect-geographically-dispersed-networks-expressroute-global-reach/)
	+ [Improve data path performance between networks with ExpressRoute FastPath 10 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/9-improve-data-path-performance-between-networks-expressroute-fastpath/)
	+ [Troubleshoot ExpressRoute connection issues 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/10-troubleshoot-expressroute-connection-issues/)
	+ [Summary and resources 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/11-summary-resources/)

Achievements

 [Next](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/7-connect-expressroute-circuit-virtual-network/)  

 Completed 200 XP

An ExpressRoute circuit has two peering options associated with it: Azure private, and Microsoft. Each peering is configured identically on a pair of routers (in active-active or load sharing configuration) for high availability. Azure services are categorized as Azure public and Azure private to represent the IP addressing schemes.

![ExpressRoute peerings use cases](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/expressroute-peerings-31290ff8.png)
**Create Peering configuration**

* You can configure private peering and Microsoft peering for an ExpressRoute circuit. Peering's can be configured in any order you choose. However, you must make sure that you complete the configuration of each peering one at a time.
* You must have an active ExpressRoute circuit. Have the circuit enabled by your connectivity provider before you continue. To configure peering(s), the ExpressRoute circuit must be in a provisioned and enabled state.
* If you plan to use a shared key/MD5 hash, be sure to use the key on both sides of the tunnel. The limit is a maximum of 25 alphanumeric characters. Special characters are not supported.
* This only applies to circuits created with service providers offering Layer 2 connectivity services. If you are using a service provider that offers managed Layer 3 services (typically an IPVPN, like MPLS), your connectivity provider configures and manages the routing for you.

#### Choose between private peering only, Microsoft peering only, or both

The following table compares the two peering. Public peering is deprecated for new peering.

| **Features** | **Private Peering** | **Microsoft Peering** |
| --- | --- | --- |
| Max. # prefixes supported per peering | 4000 by default, 10,000 with ExpressRoute Premium | 200 |
| IP address ranges supported | Any valid IP address within your WAN. | Public IP addresses owned by you or your connectivity provider. |
| AS Number requirements | Private and public AS numbers. You must own the public AS number if you choose to use one. | Private and public AS numbers. However, you must prove ownership of public IP addresses. |
| IP protocols supported | IPv4, IPv6 (preview) | IPv4, IPv6 |
| Routing Interface IP addresses | RFC1918 and public IP addresses | Public IP addresses registered to you in routing registries. |
| MD5 Hash support | Yes | Yes |

You may enable one or more of the routing domains as part of your ExpressRoute circuit. You can choose to have all the routing domains put on the same VPN if you want to combine them into a single routing domain. The recommended configuration is that private peering is connected directly to the core network, and the public and Microsoft peering links are connected to your DMZ.

Each peering requires separate BGP sessions (one pair for each peering type). The BGP session pairs provide a highly available link. If you are connecting through layer 2 connectivity providers, you are responsible for configuring and managing routing.

Important

IPv6 support for private peering is currently in Public Preview. If you would like to connect your virtual network to an ExpressRoute circuit with IPv6-based private peering configured, please make sure that your virtual network is dual stack and follows the guidelines for [IPv6 for Azure VNet](https://learn.microsoft.com/en-us/azure/virtual-network/ipv6-overview).

#### Configure private peering

Azure compute services, namely virtual machines (IaaS) and cloud services (PaaS), that are deployed within a virtual network can be connected through the private peering domain. The private peering domain is a trusted extension of your core network into Microsoft Azure. You can set up bi-directional connectivity between your core network and Azure virtual networks (VNets). This peering lets you connect to virtual machines and cloud services directly on their private IP addresses.

You can connect more than one virtual network to the private peering domain. You can visit the [Azure Subscription and Service Limits, Quotas, and Constraints](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits) page for up-to-date information on limits.

#### Configure Microsoft peering

Microsoft 365 was created to be accessed securely and reliably via the Internet. Because of this, it is recommended to use ExpressRoute for specific scenarios.

Connectivity to Microsoft online services (Microsoft 365 and Azure PaaS services) occurs through Microsoft peering. You can enable bidirectional connectivity between your WAN and Microsoft cloud services through the Microsoft peering routing domain. You must connect to Microsoft cloud services only over public IP addresses that are owned by you or your connectivity provider and you must adhere to all the defined rules.

#### Configure route filters for Microsoft Peering

Route filters are a way to consume a subset of supported services through Microsoft peering.

Microsoft 365 services such as Exchange Online, SharePoint Online, and Skype for Business, are accessible through the Microsoft peering. When Microsoft peering gets configured in an ExpressRoute circuit, all prefixes related to these services gets advertised through the BGP sessions that are established. A BGP community value is attached to every prefix to identify the service that is offered through the prefix.

Connectivity to all Azure and Microsoft 365 services causes many prefixes to gets advertised through BGP. The large number of prefixes significantly increases the size of the route tables maintained by routers within your network. If you plan to consume only a subset of services offered through Microsoft peering, you can reduce the size of your route tables in two ways. You can:

* Filter out unwanted prefixes by applying route filters on BGP communities. Route filtering is a standard networking practice and is used commonly within many networks.
* Define route filters and apply them to your ExpressRoute circuit. A route filter is a new resource that lets you select the list of services you plan to consume through Microsoft peering. ExpressRoute routers only send the list of prefixes that belong to the services identified in the route filter.

**About route filters**

When Microsoft peering gets configured on your ExpressRoute circuit, the Microsoft Edge routers establish a pair of BGP sessions with your edge routers through your connectivity provider. No routes are advertised to your network. To enable route advertisements to your network, you must associate a route filter.

A route filter lets you identify services you want to consume through your ExpressRoute circuit's Microsoft peering. It is essentially an allowed list of all the BGP community values. Once a route filter resource gets defined and attached to an ExpressRoute circuit, all prefixes that map to the BGP community values gets advertised to your network.

To attach route filters with Microsoft 365 services, you must have authorization to consume Microsoft 365 services through ExpressRoute. If you are not authorized to consume Microsoft 365 services through ExpressRoute, the operation to attach route filters fails.

#### **Create a route filter and a filter rule**

A route filter can have only one rule, and the rule must be of type 'Allow'. This rule can have a list of BGP community values associated with it.

* Select **Create a resource** then search for Route filter as shown in the following image:

  ![Azure portal - create route filter](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/create-route-filter-4c39f8b7.png)
* Place the route filter in a resource group. Ensure the location is the same as the ExpressRoute circuit. Select **Review + create** and then **Create**.

  ![Azure portal - create route filter basics tab](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/create-route-filter-basic-ee3bf46b.png)

**Create a filter rule**

To add and update rules, select the manage rule tab for your route filter.

![Azure portal - manage route filter properties](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/manage-route-filter-25ae788c.png)
* Select the services you want to connect to from the drop-down list and save the rule when done.

  ![Azure portal - Add a route filter rule](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/add-route-filter-rule-e0f3ba9b.png)

**Attach the route filter to an ExpressRoute circuit**

* Attach the route filter to a circuit by selecting the **+ Add Circuit** button and selecting the ExpressRoute circuit from the drop-down list.

  ![Azure portal - Add a circuit to a route filter](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/add-circuit-route-filter-d47edd82.png)
* If the connectivity provider configures peering for your ExpressRoute circuit, refresh the circuit from the ExpressRoute circuit page before you select the **+ Add Circuit** button.

  ![Azure portal - Microsoft peering with provisioned status](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/refresh-express-route-circuit-e67a2d97.png)

**Common tasks**

**To get the properties of a route filter**

* You can view properties of a route filter when you open the resource in the portal.

  ![Azure portal - View Route filter properties](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/view-route-filter-89cb9a5c.png)

**To update the properties of a route filter**

You can update the list of BGP community values attached to a circuit by selecting the **Manage rule** button.

![Azure portal - Route filter manage rule](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/update-route-filter-eb52b0cd.png)
* Select the service communities you want and then select **Save**.

  ![Azure portal - Add another rule](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/add-route-filter-rules-ab446c9f.png)

**To detach a route filter from an ExpressRoute circuit**

* To detach a circuit from the route filter, right-click on the circuit and select **Disassociate**.

  ![Azure portal - dissociate rule from route filter](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/detach-route-filter-c150ae13.png)

**Clean up resources**

* You can delete a route filter by selecting the **Delete** button. Ensure the Route filter is not associate to any circuits before doing so.

  ![Azure portal - delete a rule](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/delete-route-filter-4e6da3a8.png)

#### **Reset peering**

**Sign into the Azure portal**

From a browser, go to the [Azure portal](https://portal.azure.com/), and then sign in with your Azure account.

**Reset a peering**

You can reset the Microsoft peering and the Azure private peering on an ExpressRoute circuit independently.

* Choose the circuit that you want to change.

  ![Azure portal - select ExpressRoute circuit](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/expressroute-circuit-lists-7c5d1fa6.png)
* Choose the peering configuration that you want to reset.

  ![Azure portal - select peering to reset](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/expressroute-circuit-7347c31c.png)
* Clear the **Enable Peering** check box, and then select **Save** to disable the peering configuration.

  ![Azure portal - disable peering](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/disable-peering-bb360e83.png)
* Select the **Enable Peering** check box, and then select **Save** to re-enable the peering configuration.

#### Check your knowledge

1.

An engineer wants to consume a specific set of services through Microsoft peering. Which feature should be configured?

Network Firewall.

Route filters.

You cannot consume only a subset of services.

2.

To provide connectivity to Microsoft 365 and PaaS services. Which peering service should select?

Private peering.

Public peering.

Microsoft Peering.

You must answer all questions before checking your work.

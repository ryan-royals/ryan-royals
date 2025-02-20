---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/connect-remote-resources-by-using-azure-virtual-wa-ns-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

[Previous](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/5-connect-devices-to-networks-point-to-site-vpn-connections/) 

* #### Design and implement hybrid networking

	+ [Introduction 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/1-introduction/)
	+ [Design and implement Azure VPN Gateway 24 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/2-design-implement-vpn-gateway/)
	+ [Exercise: Create and configure a virtual network gateway 10 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/3-exercise-create-configure-local-network-gateway/)
	+ [Connect networks with Site-to-site VPN connections 3 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/4-connect-networks-site-to-site-vpn-connections/)
	+ [Connect devices to networks with Point-to-site VPN connections 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/5-connect-devices-to-networks-point-to-site-vpn-connections/)
	+ [Connect remote resources by using Azure Virtual WANs 3 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/6-connect-remote-resources-by-using-azure-virtual-wans/)
	+ [Exercise: create a Virtual WAN by using the Azure portal 8 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/7-exercise-create-virtual-wan-by-using-azure-portal/)
	+ [Create a network virtual appliance (NVA) in a virtual hub 7 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/8-create-network-virtual-appliance-virtual-hub/)
	+ [Summary 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/9-summary/)

Achievements

 [Next](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/7-exercise-create-virtual-wan-by-using-azure-portal/)  

 Completed 200 XP

Today’s workforce is more distributed than ever before. Organizations are exploring options that enable their employees, partners, and customers to connect to the resources they need from wherever they are. It’s not unusual for organizations to operate across national/regional boundaries, and across time zones.

#### What is Azure Virtual WAN?

Azure Virtual WAN is a networking service that brings many networking, security, and routing functionalities together to provide a single operational interface. Some of the main features include:

* Branch connectivity (via connectivity automation from Virtual WAN Partner devices such as SD-WAN or VPN CPE).
* Site-to-site VPN connectivity.
* Remote user VPN connectivity (point-to-site).
* Private connectivity (ExpressRoute).
* Intra-cloud connectivity (transitive connectivity for virtual networks).
* VPN ExpressRoute inter-connectivity.
* Routing, Azure Firewall, and encryption for private connectivity.

The following diagram shows an organization with two Virtual WAN hubs connecting the spokes. VNets, Site-to-site and point-to-site VPNs, SD WANs, and ExpressRoute connectivity are all supported.

![Azure Virtual WAN with two regional hubs, several VNets, and multiple remote connections including Site-to-Site VPN, Point-to-Site VPN, and ExpressRoute.](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/azure-wan-regions-a420bb18.png)
To configure an end-to-end virtual WAN, you create the following resources:

* **Virtual WAN**
* **Hub**
* **Hub virtual network connection**
* **Hub-to-hub connection**
* **Hub route table**

##### Choose a Virtual WAN SKU

The virtualWAN resource represents a virtual overlay of your Azure network and is a collection of multiple resources. It contains links to all your virtual hubs that you would like to have within the virtual WAN. Virtual WANs are isolated from each other and can't contain a common hub. Virtual hubs in different virtual WANs don't communicate with each other.

There are two types of Virtual WANs: Basic and Standard. The following table shows the available configurations for each type.

| **Virtual WAN type** | **Hub type** | **Available configurations** |
| --- | --- | --- |
| Basic | Basic | Site-to-site VPN only |
| Standard | Standard | ExpressRouteUser VPN (P2S)VPN (site-to-site)Inter-hub and VNet-to-VNet transiting through the virtual hubAzure FirewallNVA in a virtual WAN |

##### Hub private address space

A virtual hub is a Microsoft-managed virtual network. The hub contains various service endpoints to enable connectivity. From your on-premises network (vpnsite), you can connect to a VPN gateway inside the virtual hub, connect ExpressRoute circuits to a virtual hub, or even connect mobile users to a point-to-site gateway in the virtual hub. The hub is the core of your network in a region. Multiple virtual hubs can be created in the same region.

The minimum address space is /24 to create a hub. If you use anything in the range from /25 to /32, it will produce an error during creation. You don't need to explicitly plan the subnet address space for the services in the virtual hub. Because Azure Virtual WAN is a managed service, it creates the appropriate subnets in the virtual hub for the different gateways/services (for example, VPN gateways, ExpressRoute gateways, User VPN point-to-site gateways, Firewall, routing, etc.).

##### Gateway scale

A hub gateway isn't the same as a virtual network gateway that you use for ExpressRoute and VPN Gateway. For example, when using Virtual WAN, you don't create a site-to-site connection from your on-premises site directly to your VNet. Instead, you create a site-to-site connection to the hub. The traffic always goes through the hub gateway. This means that your VNets don't need their own virtual network gateway. Virtual WAN lets your VNets take advantage of scaling easily through the virtual hub and the virtual hub gateway.

Gateway scale units allow you pick the aggregate throughput of the gateway in the virtual hub. Each type of gateway scale unit (site-to-site, user-vpn, and ExpressRoute) is configured separately.

##### Connect cross-tenant VNets to a Virtual WAN hub

You can use Virtual WAN to connect a VNet to a virtual hub in a different tenant. This architecture is useful if you have client workloads that must be connected to be the same network but are on different tenants. For example, as shown in the following diagram, you can connect a non-Contoso VNet (the Remote Tenant) to a Contoso virtual hub (the Parent Tenant).

![Connect a non-Contoso VNet to a Contoso virtual hub (the Parent Tenant).](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/cross-tenant-connectivity-8c970006.png)
Before you can connect a cross-tenant VNet to a Virtual WAN hub, you must have the following configuration already set up:

* A Virtual WAN and virtual hub in the parent subscription.
* A virtual network configured in a subscription in the remote tenant.
* Non-overlapping address spaces in the remote tenant and address spaces within any other VNets already connected to the parent virtual hub.

#### Virtual Hub routing

The routing capabilities in a virtual hub are provided by a router that manages all routing between gateways using Border Gateway Protocol (BGP). A virtual hub can contain multiple gateways such as a Site-to-site VPN gateway, ExpressRoute gateway, Point-to-site gateway, Azure Firewall. This router also provides transit connectivity between virtual networks that connect to a virtual hub and can support up to an aggregate throughput of 50 Gbps. These routing capabilities apply to Standard Virtual WAN customers.

To learn more about how to configure routing, see [How to configure virtual hub routing](https://learn.microsoft.com/en-us/azure/virtual-wan/how-to-virtual-hub-routing).

##### Hub route table

You can create a virtual hub route and apply the route to the virtual hub route table. You can apply multiple routes to the virtual hub route table.

#### Check your knowledge

1.

What is an Azure Virtual WAN?

Azure Virtual WAN is a collection of connectivity resources like VPNs, which enables organizations to use the Microsoft backbone.

Azure WAN describes two or more VNets connected through peering.

Azure WAN is a collection of on-premises networks connected to each other through VPNs.

2.

What is the minimum address space needed for a hub?

/24

/25

/32

You must answer all questions before checking your work.

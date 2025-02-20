---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-azure-vpn-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/open-graph-image_jaAnZEn.png)

#### In this article

1. [Why use VPN Gateway?](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#why-use-vpn-gateway)
2. [Planning and design](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#connectivity)
3. [Configuring VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#configuring)
4. [Gateway SKUs](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#gwsku)
5. [Pricing](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#pricing)
6. [What's new?](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#new)
7. [FAQ](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#faq)
8. [Next steps](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpngateways#next-steps)

Azure VPN Gateway is a service that can be used to send encrypted traffic between an Azure virtual network and on-premises locations over the public Internet. You can also use VPN Gateway to send encrypted traffic between Azure virtual networks over the Microsoft network. VPN Gateway uses a specific type of Azure virtual network gateway called a VPN gateway. Multiple connections can be created to the same VPN gateway. When you create multiple connections, all VPN tunnels share the available gateway bandwidth.

#### Why use VPN Gateway?

Here are some of the key scenarios for VPN Gateway:

* Send encrypted traffic between an Azure virtual network and on-premises locations over the public Internet. You can do this by using the following types of connections:

	+ **Site-to-site connection:** A cross-premises IPsec/IKE VPN tunnel connection between the VPN gateway and an on-premises VPN device.
	+ **Point-to-site connection:** VPN over OpenVPN, IKEv2, or SSTP. This type of connection lets you connect to your virtual network from a remote location, such as from a conference or from home.
* Send encrypted traffic between virtual networks. You can do this by using the following types of connections:

	+ **VNet-to-VNet:** An IPsec/IKE VPN tunnel connection between the VPN gateway and another Azure VPN gateway that uses a *VNet-to-VNet* connection type. This connection type is designed specifically for VNet-to-VNet connections.
	+ **Site-to-site connection:** An IPsec/IKE VPN tunnel connection between the VPN gateway and another Azure VPN gateway. This type of connection, when used in the VNet-to-VNet architecture, uses the *Site-to-site (IPsec)* connection type, which allows cross-premises connections to the gateway in addition connections between VPN gateways.
* Configure a site-to-site VPN as a secure failover path for [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction). You can do this by using:

	+ **ExpressRoute + VPN Gateway:** A combination of ExpressRoute + VPN Gateway connections (coexisting connections).
* Use site-to-site VPNs to connect to sites that aren't connected through [ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction). You can do this with:

	+ **ExpressRoute + VPN Gateway:** A combination of ExpressRoute + VPN Gateway connections (coexisting connections).

####  Planning and design

Because you can create multiple connection configurations using VPN Gateway, you need to determine which configuration best fits your needs. Point-to-site, site-to-site, and coexisting ExpressRoute/site-to-site connections all have different instructions and resource configuration requirements.

See the [VPN Gateway topology and design](https://learn.microsoft.com/en-us/azure/vpn-gateway/design) article for design topologies and links to configuration instructions. The following sections of the article highlight some of the design topologies that are most often used.

* [Site-to-site VPN connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/design#s2smulti)
* [Point-to-site VPN connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/design#P2S)
* [VNet-to-VNet VPN connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/design#V2V)

##### Planning table

The following table can help you decide the best connectivity option for your solution.

|  | **Point-to-Site** | **Site-to-Site** |
| --- | --- | --- |
| Azure Supported Services | Cloud Services and Virtual Machines | Cloud Services and Virtual Machines |
| Typical Bandwidths | Based on the gateway SKU | Typically < 10 Gbps aggregate |
| Protocols Supported | Secure Sockets Tunneling Protocol (SSTP), OpenVPN, and IPsec | IPsec |
| Routing | RouteBased (dynamic) | We support PolicyBased (static routing) and RouteBased (dynamic routing VPN) |
| Connection resiliency | active-passive or active-active | active-passive or active-active |
| Typical use case | Secure access to Azure virtual networks for remote users | Dev, test, and lab scenarios and small to medium scale production workloads for cloud services and virtual machines |
| SLA | [SLA](https://azure.microsoft.com/support/legal/sla/) | [SLA](https://azure.microsoft.com/support/legal/sla/) |
| Pricing | [Pricing](https://azure.microsoft.com/pricing/details/vpn-gateway/) | [Pricing](https://azure.microsoft.com/pricing/details/vpn-gateway/) |
| Technical Documentation | [VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/) | [VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/) |
| FAQ | [VPN Gateway FAQ](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-vpn-faq) | [VPN Gateway FAQ](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-vpn-faq) |

##### Availability Zones

VPN gateways can be deployed in Azure Availability Zones. This brings resiliency, scalability, and higher availability to virtual network gateways. Deploying gateways in Azure Availability Zones physically and logically separates gateways within a region, while protecting your on-premises network connectivity to Azure from zone-level failures. See [About zone-redundant virtual network gateways in Azure Availability Zones](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-zone-redundant-vnet-gateways).

#### Configuring VPN Gateway

A VPN gateway connection relies on multiple resources that are configured with specific settings. In some cases, resources must be configured in a certain order. The settings that you chose for each resource are critical to creating a successful connection.

For information about individual resources and settings for VPN Gateway, see [About VPN Gateway settings](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings) and [About gateway SKUs](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus). These articles contain information to help you understand gateway types, gateway SKUs, VPN types, connection types, gateway subnets, local network gateways, and various other resource settings that you might want to consider.

For design diagrams and links to configuration articles, see the [VPN Gateway topology and design](https://learn.microsoft.com/en-us/azure/vpn-gateway/design) article.

#### Gateway SKUs

When you create a virtual network gateway, you specify the gateway SKU that you want to use. Select the SKU that satisfies your requirements based on the types of workloads, throughputs, features, and SLAs. For more information about gateway SKUs, including supported features, performance tables, configuration steps, and production vs. dev-test workloads, see [About gateway SKUs](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-gateway-skus).

| **VPNGatewayGeneration** | **SKU** | **S2S/VNet-to-VNetTunnels** | **P2S SSTP Connections** | **P2S IKEv2/OpenVPN Connections** | **AggregateThroughput Benchmark** | **BGP** | **Zone-redundant** | **Supported Number of VMs in the Virtual Network** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Generation1** | **Basic** | Max. 10 | Max. 128 | Not Supported | 100 Mbps | Not Supported | No | 200 |
| **Generation1** | **VpnGw1** | Max. 30 | Max. 128 | Max. 250 | 650 Mbps | Supported | No | 450 |
| **Generation1** | **VpnGw2** | Max. 30 | Max. 128 | Max. 500 | 1 Gbps | Supported | No | 1300 |
| **Generation1** | **VpnGw3** | Max. 30 | Max. 128 | Max. 1000 | 1.25 Gbps | Supported | No | 4000 |
| **Generation1** | **VpnGw1AZ** | Max. 30 | Max. 128 | Max. 250 | 650 Mbps | Supported | Yes | 1000 |
| **Generation1** | **VpnGw2AZ** | Max. 30 | Max. 128 | Max. 500 | 1 Gbps | Supported | Yes | 2000 |
| **Generation1** | **VpnGw3AZ** | Max. 30 | Max. 128 | Max. 1000 | 1.25 Gbps | Supported | Yes | 5000 |
|  |  |  |  |  |  |  |  |  |
| **Generation2** | **VpnGw2** | Max. 30 | Max. 128 | Max. 500 | 1.25 Gbps | Supported | No | 685 |
| **Generation2** | **VpnGw3** | Max. 30 | Max. 128 | Max. 1000 | 2.5 Gbps | Supported | No | 2240 |
| **Generation2** | **VpnGw4** | Max. 100\* | Max. 128 | Max. 5000 | 5 Gbps | Supported | No | 5300 |
| **Generation2** | **VpnGw5** | Max. 100\* | Max. 128 | Max. 10000 | 10 Gbps | Supported | No | 6700 |
| **Generation2** | **VpnGw2AZ** | Max. 30 | Max. 128 | Max. 500 | 1.25 Gbps | Supported | Yes | 2000 |
| **Generation2** | **VpnGw3AZ** | Max. 30 | Max. 128 | Max. 1000 | 2.5 Gbps | Supported | Yes | 3300 |
| **Generation2** | **VpnGw4AZ** | Max. 100\* | Max. 128 | Max. 5000 | 5 Gbps | Supported | Yes | 4400 |
| **Generation2** | **VpnGw5AZ** | Max. 100\* | Max. 128 | Max. 10000 | 10 Gbps | Supported | Yes | 9000 |

(\*) If you need more than 100 S2S VPN tunnels, use [Virtual WAN](https://learn.microsoft.com/en-us/azure/virtual-wan/virtual-wan-about) instead of VPN Gateway.

#### Pricing

You pay for two things: the hourly compute costs for the virtual network gateway, and the egress data transfer from the virtual network gateway. Pricing information can be found on the [Pricing](https://azure.microsoft.com/pricing/details/vpn-gateway) page. For legacy gateway SKU pricing, see the [ExpressRoute pricing page](https://azure.microsoft.com/pricing/details/expressroute) and scroll to the **Virtual Network Gateways** section.

**Virtual network gateway compute costs**  

Each virtual network gateway has an hourly compute cost. The price is based on the gateway SKU that you specify when you create a virtual network gateway. The cost is for the gateway itself and is in addition to the data transfer that flows through the gateway. Cost of an active-active setup is the same as active-passive. For more information about gateway SKUs for VPN Gateway, see [Gateway SKUs](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings#gwsku).

**Data transfer costs**  

Data transfer costs are calculated based on egress traffic from the source virtual network gateway.

* If you're sending traffic to your on-premises VPN device, it will be charged with the Internet egress data transfer rate.
* If you're sending traffic between virtual networks in different regions, the pricing is based on the region.
* If you're sending traffic only between virtual networks that are in the same region, there are no data costs. Traffic between VNets in the same region is free.

#### What's new?

Azure VPN Gateway is updated regularly. To stay current with the latest announcements, see the [What's new?](https://learn.microsoft.com/en-us/azure/vpn-gateway/whats-new) article. The article highlights the following points of interest:

* Recent releases
* Previews underway with known limitations (if applicable)
* Known issues
* Deprecated functionality (if applicable)

You can also subscribe to the RSS feed and view the latest VPN Gateway feature updates on the [Azure Updates](https://azure.microsoft.com/updates/?category=networking&query=VPN%20Gateway) page.

#### FAQ

For frequently asked questions about VPN gateway, see the [VPN Gateway FAQ](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-vpn-faq).

#### Next steps

* [Tutorial: Create and manage a VPN Gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/tutorial-create-gateway-portal).
* [Learn module: Introduction to Azure VPN Gateway](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-vpn-gateway).
* [Learn module: Connect your on-premises network to Azure with VPN Gateway](https://learn.microsoft.com/en-us/training/modules/connect-on-premises-network-with-vpn-gateway/).
* [Subscription and service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#vpn-gateway-limits).

---
{"dg-publish":true,"dg-path":"Azure ExpressRoute.md","permalink":"/azure-express-route/","tags":["notes"]}
---


> ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider. With ExpressRoute, you can establish connections to various Microsoft cloud services, such as Microsoft Azure and Microsoft 365. Connectivity can be from an any-to-any (IP VPN) network, a point-to-point Ethernet network, or a virtual cross-connection through a connectivity provider at a colocation facility. Since ExpressRoute connections do not go over the public Internet, this approach allows ExpressRoute connections to offer more reliability, faster speeds, consistent latencies, and higher security.[^1]

## SKUs

Azure ExpressRoute is available in three different SKUs, being **Local**, **Standard**, and **Premium**.

### Local

**Local** connects you to a single Azure Region (Or regions in the same Metro). ExpressRoute Local is a more economical solution if you have a massive amount of data to transfer as you do not pay for egress data transfer (Unlike in Standard and Premium)[^2]  

### Standard

**Standard** allows you to connect to any Region, with up to *4000* prefixes for private peering, and *200* prefixes for Microsoft Peering in the route table.  

> You can connect to Microsoft in one of the peering locations and access regions within the geopolitical region.  
> For example, if you connect to Microsoft in Amsterdam through ExpressRoute, you will have access to all Microsoft cloud services hosted in Northern and Western Europe.[^3]

### Premium

**Premium** is a increased feature set on standard, with the route table limits increased to *4000* prefixes for Microsoft Peering, and *10,000* prefixes for private peering, increased number of VNets and ExpressRoute Global Reach connections, connectivity to Microsoft 365 and Global connectivity over the Microsoft core network.

> You can enable ExpressRoute Premium to extend connectivity across geopolitical boundaries. For example, if you connect to Microsoft in Amsterdam through ExpressRoute, you will have access to all Microsoft cloud services hosted in all regions across the world. You can also access services deployed in South America or Australia the same way you access North and West Europe regions. National clouds are excluded. [^3]

## Billing

Billing is based on a few configuration options:

- **Unlimited** or **Metered** Outbound data transfer. Ingress is always free.
- **ExpressRoute premium addon**.
- **Bandwidth** for the connection, which can be *50Mbps*, *100Mbps*, *200Mbps*, *1Gbps*, *2Gbps*, *5Gbps* or *10Gbps*.

## Types of Express Route

Express Route can be configured as either **Private** or **Microsoft Peering**. **Private** is configured to extend your on premises network directly into a [[30 Slipbox/Azure Virtual Network\|Virtual Network]] in Azure. **Microsoft Peering** is used to connect to Microsoft Services like [[Office 365\|Office 365]], and the Public IP Ranges for Azure Regions.  
![Azure ExpressRoute-1721605786884.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721605786884.png)

| **Features**                          | **Private Peering**                                                                        | **Microsoft Peering**                                                                    |
| ------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Max. # prefixes supported per peering | 4000 by default, 10,000 with ExpressRoute Premium                                          | 200                                                                                      |
| IP address ranges supported           | Any valid IP address within your WAN.                                                      | Public IP addresses owned by you or your connectivity provider.                          |
| AS Number requirements                | Private and public AS numbers. You must own the public AS number if you choose to use one. | Private and public AS numbers. However, you must prove ownership of public IP addresses. |
| IP protocols supported                | IPv4, IPv6 (preview)                                                                       | IPv4, IPv6                                                                               |
| Routing Interface IP addresses        | RFC1918 and public IP addresses                                                            | Public IP addresses registered to you in routing registries.                             |
| MD5 Hash support                      | Yes                                                                                        | Yes                                                                                      |

### Private Peering

> Azure compute services, namely virtual machines (IaaS) and cloud services (PaaS), that are deployed within a virtual network can be connected through the private peering domain. The private peering domain is a trusted extension of your core network into Microsoft Azure. You can set up bi-directional connectivity between your core network and Azure virtual networks (VNets). This peering lets you connect to virtual machines and cloud services directly on their private IP addresses.[^4]

### Microsoft Peering

> Connectivity to Microsoft online services (Microsoft 365 and Azure PaaS services) occurs through Microsoft peering. You can enable bidirectional connectivity between your WAN and Microsoft cloud services through the Microsoft peering routing domain. You must connect to Microsoft cloud services only over public IP addresses that are owned by you or your connectivity provider and you must adhere to all the defined rules.[^4]

## Connectivity

ExpressRoute is a [[30 Slipbox/OSI Networking Model#Layer 3 - Network\|Layer 3 Connection]] between your on-premises network and the Microsoft cloud. This connection can be an **any-to-any IPVPN**, **point-to-point Ethernet connection**, or a **virtual cross-connection via Ethernet Exchange**.  
![Azure ExpressRoute-1721177475219.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721177475219.png)

### Co-located at a Cloud exchange

> If you are co-located in a facility with a cloud exchange, you can order virtual cross-connections to the Microsoft cloud through the co-location provider’s Ethernet exchange. Co-location providers can offer either Layer 2 cross-connections, or managed Layer 3 cross-connections between your infrastructure in the co-location facility and the Microsoft cloud.[^1]

### Point-to-point Ethernet Connections

> You can connect your on-premises datacenters/offices to the Microsoft cloud through point-to-point Ethernet links. Point-to-point Ethernet providers can offer Layer 2 connections, or managed Layer 3 connections between your site and the Microsoft cloud.[^1]

### Any-to-any (IPVPN) Networks

> You can integrate your WAN with the Microsoft cloud. IPVPN providers (typically MPLS VPN) offer any-to-any connectivity between your branch offices and datacenters. The Microsoft cloud can be interconnected to your WAN to make it look just like any other branch office. WAN providers typically offer managed Layer 3 connectivity.[^1]

### Direct from ExpressRoute Sites

> You can connect directly into the Microsoft's global network at a peering location strategically distributed across the world. ExpressRoute Direct provides **dual 100 Gbps** or **10-Gbps** connectivity, which supports Active/Active connectivity at scale.[^1]

## Choosing between Provider and Direct Model

> ExpressRoute Direct gives you the ability to connect directly into Microsoft’s global network at peering locations strategically distributed around the world. ExpressRoute Direct provides dual 100 Gbps or 10-Gbps connectivity, which supports Active/Active connectivity at scale. You can work with any service provider for ExpressRoute Direct.[^1]

| **ExpressRoute using a Service Provider**                                                      | **ExpressRoute Direct**                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uses service providers to enable fast onboarding and connectivity into existing infrastructure | Requires 100 Gbps/10 Gbps infrastructure and full management of all layers                                                                                                                                                                                    |
| Integrates with hundreds of providers including Ethernet and MPLS                              | Direct/Dedicated capacity for regulated industries and massive data ingestion                                                                                                                                                                                 |
| Circuits SKUs from 50 Mbps to 10 Gbps                                                          | Customer may select a combination of the following circuit SKUs on 100-Gbps ExpressRoute Direct: 5 Gbps 10 Gbps 40 Gbps 100 Gbps Customer may select a combination of the following circuit SKUs on 10-Gbps ExpressRoute Direct: 1 Gbps 2 Gbps 5 Gbps 10 Gbps |
| Optimized for single tenant                                                                    | Optimized for single tenant with multiple business units and multiple work environments                                                                                                                                                                       |

## Route Advertisement

> When Microsoft peering gets configured on your ExpressRoute circuit, the Microsoft Edge routers establish a pair of [[30 Slipbox/Border Gateway Protocol\|Border Gateway Protocol]] (BGP) sessions with your edge routers through your connectivity provider. No routes are advertised to your network. To enable route advertisements to your network, you must associate a [[99 Inbox/Azure Route Filter\|Azure Route Filter]].  
> In order to associate a route filter:
> - You must have an active ExpressRoute circuit that has Microsoft peering provisioned.
> - Create an ExpressRoute circuit and have the circuit enabled by your connectivity provider before you continue. The ExpressRoute circuit must be in a provisioned and enabled state.
> - Create Microsoft peering if you manage the BGP session directly. Or, have your connectivity provider provision Microsoft peering for your circuit.[^1]

## Bidirectional Forwarding Detection

> ExpressRoute supports [[Bidirectional Forwarding Detection\|Bidirectional Forwarding Detection]] (BFD) both over private and Microsoft peering. When you enable BFD over ExpressRoute, you can speed up the link failure detection between Microsoft Enterprise edge (MSEE) devices and the routers that your ExpressRoute circuit gets configured (CE/PE). You can configure ExpressRoute over your edge routing devices or your Partner Edge routing devices (if you went with managed Layer 3 connection service).[^1]

> You can enable ExpressRoute circuit either by Layer 2 connections or managed Layer 3 connections. In both cases, if there are more than one Layer-2 devices in the ExpressRoute connection path, the responsibility of detecting any link failures in the path lies with the overlying BGP session.[^1]  
![Azure ExpressRoute-1721181158814.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721181158814.png)

## Configure Encryption over ExpressRoute

> This section shows you how to use Azure Virtual WAN to establish an IPsec/IKE VPN connection from your on-premises network to Azure over the private peering of an Azure ExpressRoute circuit. This technique can provide an encrypted transit between the on-premises networks and Azure virtual networks over ExpressRoute, without going over the public internet or using public IP addresses.[^1]  
![Azure ExpressRoute-1721181255378.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721181255378.png)

When using a VPN over Express route, it is important to configure the networking on both sides to weigh the VPN connection more favourably, as by default they will share the same address prefixes, and the Express Route will be priorities. In Azure to ensure that the IPsec path is preferred over the direct ExpressRoute path (without IPsec), you have two options:

- Advertise more specific prefixes on the VPN BGP session for the VPN-connected network. You can advertise a larger range that encompasses the VPN-connected network over ExpressRoute private peering, then more specific ranges in the VPN BGP session. For example, advertise 10.0.0.0/16 over ExpressRoute, and 10.0.1.0/24 over VPN.
- Advertise disjoint prefixes for VPN and ExpressRoute. If the VPN-connected network ranges are disjoint from other ExpressRoute connected networks, you can advertise the prefixes in the VPN and ExpressRoute BGP sessions, respectively. For example, advertise 10.0.0.0/24 over ExpressRoute, and 10.0.1.0/24 over VPN.

## Designing Redundancy for an ExpressRoute Deployment

Redundancy can be configured for the ExpressRoute in Azure by either **having a backup Site-to-Site connection**, or **Create a Zone redundant VNET gateway in Azure Availability Zones**.

## Virtual Network Peering

> You can link up to 10 virtual networks to a standard ExpressRoute circuit. All virtual networks must be in the same geopolitical region when using a standard ExpressRoute circuit.[^5]

> A single VNet can be linked to up to 16 ExpressRoute circuits. Use the following process to create a new connection object for each ExpressRoute circuit you are connecting to. The ExpressRoute circuits can be in the same subscription, different subscriptions, or a mix of both.[^5]

> If you enable the ExpressRoute premium add-on, you can link virtual networks outside of the geopolitical region of the ExpressRoute circuit. The premium add-on will also allow you to connect more than 10 virtual networks to your ExpressRoute circuit depending on the bandwidth chosen.[^5]

## ExpressRoute Global Reach

> You can enable ExpressRoute Global Reach to exchange data across your on-premises sites by connecting your ExpressRoute circuits. For example, if you have a private data center in California connected to an ExpressRoute circuit in Silicon Valley and another private data center in Texas connected to an ExpressRoute circuit in Dallas. With ExpressRoute Global Reach, you can connect your private data centers together through these two ExpressRoute circuits. Your cross-data-center traffic will traverse through Microsoft's network.[^3]  

![Azure ExpressRoute-1721608364354.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721608364354.png)

## ExpressRoute Fastpath

> FastPath is designed to improve the data path performance between your on-premises network and your virtual network. When enabled, FastPath sends network traffic directly to virtual machines in the virtual network, bypassing the gateway.[^6]

FastPath is available on all ExpressRoute circuits, and requires a [[30 Slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]] with either **Ultra-Performance** or **ErGw3AZ** Sku.

> While FastPath supports most configurations, it does not support the following features:
> - UDR on the gateway subnet: This UDR has no impact on the network traffic that FastPath sends directly from your on-premises network to the virtual machines in Azure virtual network.
> - VNet Peering: If you have other virtual networks peered with the one that is connected to ExpressRoute, the network traffic from your on-premises network to the other virtual networks (i.e., the so-called "Spoke" VNets) will continue to be sent to the virtual network gateway. The workaround is to connect all the virtual networks to the ExpressRoute circuit directly.
> - Basic Load Balancer: If you deploy a Basic internal load balancer in your virtual network or the Azure PaaS service you deploy in your virtual network uses a Basic internal load balancer, the network traffic from your on-premises network to the virtual IPs hosted on the Basic load balancer will be sent to the virtual network gateway. The solution is to upgrade the Basic load balancer to a Standard load balancer.
> - Private Link: If you connect to a private endpoint in your virtual network from your on-premises network, the connection will go through the virtual network gateway.[^6]

[^1]: [[40 References/readwise/Explore Azure ExpressRoute - Training\|Explore Azure ExpressRoute - Training]]
[^2]: [[40 References/readwise/FAQ - Azure ExpressRoute\|FAQ - Azure ExpressRoute]]
[^3]: [[40 References/readwise/Connect Geographically Dispersed Networks With ExpressRoute Global Reach - Training\|Connect Geographically Dispersed Networks With ExpressRoute Global Reach - Training]]
[^4]: [[40 References/readwise/Configure Peering for an ExpressRoute Deployment - Training\|Configure Peering for an ExpressRoute Deployment - Training]]
[^5]: [[40 References/readwise/Connect an ExpressRoute Circuit to a Virtual Network - Training\|Connect an ExpressRoute Circuit to a Virtual Network - Training]]
[^6]: [[40 References/readwise/Improve Data Path Performance Between Networks With ExpressRoute FastPath - Training\|Improve Data Path Performance Between Networks With ExpressRoute FastPath - Training]]

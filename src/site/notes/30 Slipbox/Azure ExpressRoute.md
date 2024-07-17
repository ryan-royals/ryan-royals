---
{"dg-publish":true,"dg-path":"Azure ExpressRoute.md","permalink":"/azure-express-route/","tags":["notes"]}
---


> ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider. With ExpressRoute, you can establish connections to various Microsoft cloud services, such as Microsoft Azure and Microsoft 365. Connectivity can be from an any-to-any (IP VPN) network, a point-to-point Ethernet network, or a virtual cross-connection through a connectivity provider at a colocation facility. Since ExpressRoute connections do not go over the public Internet, this approach allows ExpressRoute connections to offer more reliability, faster speeds, consistent latencies, and higher security.[^1]

## Types of Express Route

Express Route can be configured as either **Private** or **Microsoft Peering**. **Private** is configured to extend your on premises network directly into a [[30 Slipbox/Azure Virtual Network\|Virtual Network]] in Azure. **Microsoft Peering** is used to connect to Microsoft Services like [[Office 365\|Office 365]], and the Public IP Ranges for Azure Regions.

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

## Design Considerations

### Choose between Provider and Direct Model

> ExpressRoute Direct gives you the ability to connect directly into Microsoft’s global network at peering locations strategically distributed around the world. ExpressRoute Direct provides dual 100 Gbps or 10-Gbps connectivity, which supports Active/Active connectivity at scale. You can work with any service provider for ExpressRoute Direct.[^1]

| **ExpressRoute using a Service Provider**                                                      | **ExpressRoute Direct**                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uses service providers to enable fast onboarding and connectivity into existing infrastructure | Requires 100 Gbps/10 Gbps infrastructure and full management of all layers                                                                                                                                                                                    |
| Integrates with hundreds of providers including Ethernet and MPLS                              | Direct/Dedicated capacity for regulated industries and massive data ingestion                                                                                                                                                                                 |
| Circuits SKUs from 50 Mbps to 10 Gbps                                                          | Customer may select a combination of the following circuit SKUs on 100-Gbps ExpressRoute Direct: 5 Gbps 10 Gbps 40 Gbps 100 Gbps Customer may select a combination of the following circuit SKUs on 10-Gbps ExpressRoute Direct: 1 Gbps 2 Gbps 5 Gbps 10 Gbps |
| Optimized for single tenant                                                                    | Optimized for single tenant with multiple business units and multiple work environments                                                                                                                                                                       |

### Route Advertisement

> When Microsoft peering gets configured on your ExpressRoute circuit, the Microsoft Edge routers establish a pair of [[30 Slipbox/Border Gateway Protocol\|Border Gateway Protocol]] (BGP) sessions with your edge routers through your connectivity provider. No routes are advertised to your network. To enable route advertisements to your network, you must associate a [[Azure Route Filter\|Azure Route Filter]].  
> In order to associate a route filter:
> - You must have an active ExpressRoute circuit that has Microsoft peering provisioned.
> - Create an ExpressRoute circuit and have the circuit enabled by your connectivity provider before you continue. The ExpressRoute circuit must be in a provisioned and enabled state.
> - Create Microsoft peering if you manage the BGP session directly. Or, have your connectivity provider provision Microsoft peering for your circuit.[^1]

### Bidirectional Forwarding Detection

> ExpressRoute supports [[Bidirectional Forwarding Detection\|Bidirectional Forwarding Detection]] (BFD) both over private and Microsoft peering. When you enable BFD over ExpressRoute, you can speed up the link failure detection between Microsoft Enterprise edge (MSEE) devices and the routers that your ExpressRoute circuit gets configured (CE/PE). You can configure ExpressRoute over your edge routing devices or your Partner Edge routing devices (if you went with managed Layer 3 connection service).[^1]

> You can enable ExpressRoute circuit either by Layer 2 connections or managed Layer 3 connections. In both cases, if there are more than one Layer-2 devices in the ExpressRoute connection path, the responsibility of detecting any link failures in the path lies with the overlying BGP session.[^1]  
![Azure ExpressRoute-1721181158814.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721181158814.png)

### Configure Encryption over ExpressRoute

> This section shows you how to use Azure Virtual WAN to establish an IPsec/IKE VPN connection from your on-premises network to Azure over the private peering of an Azure ExpressRoute circuit. This technique can provide an encrypted transit between the on-premises networks and Azure virtual networks over ExpressRoute, without going over the public internet or using public IP addresses.[^1]  
![Azure ExpressRoute-1721181255378.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721181255378.png)

When using a VPN over Express route, it is important to configure the networking on both sides to weigh the VPN connection more favourably, as by default they will share the same address prefixes, and the Express Route will be priorities. In Azure to ensure that the IPsec path is preferred over the direct ExpressRoute path (without IPsec), you have two options:

- Advertise more specific prefixes on the VPN BGP session for the VPN-connected network. You can advertise a larger range that encompasses the VPN-connected network over ExpressRoute private peering, then more specific ranges in the VPN BGP session. For example, advertise 10.0.0.0/16 over ExpressRoute, and 10.0.1.0/24 over VPN.
- Advertise disjoint prefixes for VPN and ExpressRoute. If the VPN-connected network ranges are disjoint from other ExpressRoute connected networks, you can advertise the prefixes in the VPN and ExpressRoute BGP sessions, respectively. For example, advertise 10.0.0.0/24 over ExpressRoute, and 10.0.1.0/24 over VPN.

### Design Redundancy for an ExpressRoute Deployment

Redundancy can be configured for the ExpressRoute in Azure by either **having a backup Site-to-Site connection**, or **Create a Zone redundant VNET gateway in Azure Availability Zones**.

## Footnotes

[^1]: [[40 References/readwise/Explore Azure ExpressRoute - Training\|Explore Azure ExpressRoute - Training]]

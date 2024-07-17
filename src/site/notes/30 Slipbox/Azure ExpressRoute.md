---
{"dg-publish":true,"dg-path":"Azure ExpressRoute.md","permalink":"/azure-express-route/","tags":["notes"]}
---


> ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider. With ExpressRoute, you can establish connections to various Microsoft cloud services, such as Microsoft Azure and Microsoft 365. Connectivity can be from an any-to-any (IP VPN) network, a point-to-point Ethernet network, or a virtual cross-connection through a connectivity provider at a colocation facility. Since ExpressRoute connections do not go over the public Internet, this approach allows ExpressRoute connections to offer more reliability, faster speeds, consistent latencies, and higher security.[^1]

## Connectivity

ExpressRoute is a **[[30 Slipbox/OSI Networking Model#Layer 3 - Network\|Layer 3]] connection** between your on-premises network and the Microsoft cloud. This connection can be an **any-to-any IPVPN**, **point-to-point Ethernet connection**, or a **virtual cross-connection via Ethernet Exchange**.  
![Azure ExpressRoute-1721177475219.png](/img/user/40%20References/attachments/image/Azure%20ExpressRoute-1721177475219.png)

### Co-located at a Cloud exchange

> If you are co-located in a facility with a cloud exchange, you can order virtual cross-connections to the Microsoft cloud through the co-location provider’s Ethernet exchange. Co-location providers can offer either Layer 2 cross-connections, or managed Layer 3 cross-connections between your infrastructure in the co-location facility and the Microsoft cloud.[^1]

### Point-to-point Ethernet Connections

> You can connect your on-premises datacenters/offices to the Microsoft cloud through point-to-point Ethernet links. Point-to-point Ethernet providers can offer Layer 2 connections, or managed Layer 3 connections between your site and the Microsoft cloud.[^1]

### Any-to-any (IPVPN) Networks

> You can integrate your WAN with the Microsoft cloud. IPVPN providers (typically MPLS VPN) offer any-to-any connectivity between your branch offices and datacenters. The Microsoft cloud can be interconnected to your WAN to make it look just like any other branch office. WAN providers typically offer managed Layer 3 connectivity.[^1]

### Direct from ExpressRoute Sites

> You can connect directly into the Microsoft's global network at a peering location strategically distributed across the world. ExpressRoute Direct provides **dual 100 Gbps** or **10-Gbps** connectivity, which supports Active/Active connectivity at scale.[^1]

## Types of Express Route

Express Route can be configured as either **Private** or **Microsoft Peering**. **Private** is configured to extend your on premises network directly into a [[30 Slipbox/Azure Virtual Network\|Virtual Network]] in Azure. **Microsoft Peering** is used to connect to Microsoft Services like [[Office 365\|Office 365]], and the Public IP Ranges for Azure Regions.

## Footnotes

[^1]: [[40 References/readwise/Explore Azure ExpressRoute - Training\|Explore Azure ExpressRoute - Training]]

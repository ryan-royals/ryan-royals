---
{"dg-publish":true,"permalink":"/40-references/readwise/explore-azure-express-route-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

ExpressRoute enables private connections to Azure services with higher reliability and faster speeds compared to typical internet connections. It allows organizations to extend their on-premises networks securely into the Microsoft cloud. By using ExpressRoute, businesses can create fast and reliable connections for data migration, replication, disaster recovery, and high-availability strategies.

## Highlights

ExpressRoute lets you extend your on-premises networks into the Microsoft cloud over a private connection with the help of a connectivity provider. With ExpressRoute, you can establish connections to various Microsoft cloud services, such as Microsoft Azure and Microsoft 365. Connectivity can be from an any-to-any (IP VPN) network, a point-to-point Ethernet network, or a virtual cross-connection through a connectivity provider at a colocation facility. Since ExpressRoute connections do not go over the public Internet, this approach allows ExpressRoute connections to offer more reliability, faster speeds, consistent latencies, and higher security. ([View Highlight] (https://read.readwise.io/read/01j2z38smbsez5460nmqfrqtvs))


Some key benefits of ExpressRoute are:
• Layer 3 connectivity between your on-premises network and the Microsoft Cloud through a connectivity provider
• Connectivity can be from an any-to-any (IPVPN) network, a point-to-point Ethernet connection, or through a virtual cross-connection via an Ethernet exchange
• Connectivity to Microsoft cloud services across all regions in the geopolitical region
• Global connectivity to Microsoft services across all regions with the ExpressRoute premium add-on
• Built-in redundancy in every peering location for higher reliability ([View Highlight] (https://read.readwise.io/read/01j2z38pbs2xadea0gsscdv8hf))


**Co-located at a cloud exchange**
If you are co-located in a facility with a cloud exchange, you can order virtual cross-connections to the Microsoft cloud through the co-location provider’s Ethernet exchange. Co-location providers can offer either Layer 2 cross-connections, or managed Layer 3 cross-connections between your infrastructure in the co-location facility and the Microsoft cloud.
**Point-to-point Ethernet connections**
You can connect your on-premises datacenters/offices to the Microsoft cloud through point-to-point Ethernet links. Point-to-point Ethernet providers can offer Layer 2 connections, or managed Layer 3 connections between your site and the Microsoft cloud.
**Any-to-any (IPVPN) networks**
You can integrate your WAN with the Microsoft cloud. IPVPN providers (typically MPLS VPN) offer any-to-any connectivity between your branch offices and datacenters. The Microsoft cloud can be interconnected to your WAN to make it look just like any other branch office. WAN providers typically offer managed Layer 3 connectivity.
**Direct from ExpressRoute sites**
You can connect directly into the Microsoft's global network at a peering location strategically distributed across the world. ExpressRoute Direct provides dual 100 Gbps or 10-Gbps connectivity, which supports Active/Active connectivity at scale. ([View Highlight] (https://read.readwise.io/read/01j2z38cqs2m53c96rx5bvd3zd))


ExpressRoute Direct gives you the ability to connect directly into Microsoft’s global network at peering locations strategically distributed around the world. ExpressRoute Direct provides dual 100 Gbps or 10-Gbps connectivity, which supports Active/Active connectivity at scale. You can work with any service provider for ExpressRoute Direct. ([View Highlight] (https://read.readwise.io/read/01j2z5xazzp89z8jxav0bt81dq))


When Microsoft peering gets configured on your ExpressRoute circuit, the Microsoft Edge routers establish a pair of Border Gateway Protocol (BGP) sessions with your edge routers through your connectivity provider. No routes are advertised to your network. To enable route advertisements to your network, you must associate a route filter.
In order to associate a route filter:
• You must have an active ExpressRoute circuit that has Microsoft peering provisioned.
• Create an ExpressRoute circuit and have the circuit enabled by your connectivity provider before you continue. The ExpressRoute circuit must be in a provisioned and enabled state.
• Create Microsoft peering if you manage the BGP session directly. Or, have your connectivity provider provision Microsoft peering for your circuit. ([View Highlight] (https://read.readwise.io/read/01j2z60q83yzk1cjtphgxtwdrm))


ExpressRoute supports Bidirectional Forwarding Detection (BFD) both over private and Microsoft peering. When you enable BFD over ExpressRoute, you can speed up the link failure detection between Microsoft Enterprise edge (MSEE) devices and the routers that your ExpressRoute circuit gets configured (CE/PE). You can configure ExpressRoute over your edge routing devices or your Partner Edge routing devices (if you went with managed Layer 3 connection service). ([View Highlight] (https://read.readwise.io/read/01j2z66p9ag08q9k5h5gg0k7dy))


You can enable ExpressRoute circuit either by Layer 2 connections or managed Layer 3 connections. In both cases, if there are more than one Layer-2 devices in the ExpressRoute connection path, the responsibility of detecting any link failures in the path lies with the overlying BGP session. ([View Highlight] (https://read.readwise.io/read/01j2z67dx6v4awnvgfaxwmcqv9))


This section shows you how to use Azure Virtual WAN to establish an IPsec/IKE VPN connection from your on-premises network to Azure over the private peering of an Azure ExpressRoute circuit. This technique can provide an encrypted transit between the on-premises networks and Azure virtual networks over ExpressRoute, without going over the public internet or using public IP addresses. ([View Highlight] (https://read.readwise.io/read/01j2z6av7f4e0g6mt25176fbtv))



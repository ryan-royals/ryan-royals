---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/about-express-route-virtual-network-gateways/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Gateway types](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#gateway-types)
2. [Gateway SKUs](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#gwsku)
3. [Gateway subnet](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#gwsub)
4. [Virtual network gateway limitations and performance](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#virtual-network-gateway-limitations-and-performance)
5. [ExpressRoute scalable gateway (Preview)](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#expressroute-scalable-gateway-preview)
6. [VNet to VNet and VNet to Virtual WAN connectivity](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#vnet-to-vnet-and-vnet-to-virtual-wan-connectivity)
7. [FastPath](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#fastpath)
8. [Connectivity to private endpoints](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#connectivity-to-private-endpoints)
9. [REST APIs and PowerShell cmdlets](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#resources)
10. [VNet-to-VNet connectivity](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#vnet-to-vnet-connectivity)
11. [Next steps](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#next-steps)

To connect your Azure virtual network and your on-premises network using ExpressRoute, you must first create a virtual network gateway. A virtual network gateway serves two purposes: exchange IP routes between the networks and route network traffic. This article explains different gateway types, gateway SKUs, and estimated performance by SKU. This article also explains ExpressRoute [FastPath](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-about-virtual-network-gateways#fastpath), a feature that enables the network traffic from your on-premises network to bypass the virtual network gateway to improve performance.

#### Gateway types

When you create a virtual network gateway, you need to specify several settings. One of the required settings, `-GatewayType`, specifies whether the gateway is used for ExpressRoute, or VPN traffic. The two gateway types are:

* **Vpn** - To send encrypted traffic across the public Internet, you use the gateway type 'Vpn'. This type of gateway is also referred to as a VPN gateway. Site-to-Site, Point-to-Site, and VNet-to-VNet connections all use a VPN gateway.
* **ExpressRoute** - To send network traffic on a private connection, you use the gateway type 'ExpressRoute'. This type of gateway is also referred to as an ExpressRoute gateway and is used when configuring ExpressRoute.

Each virtual network can have only one virtual network gateway per gateway type. For example, you can have one virtual network gateway that uses `-GatewayType` Vpn, and one that uses `-GatewayType` ExpressRoute.

#### Gateway SKUs

When you create a virtual network gateway, you need to specify the gateway SKU that you want to use. When you select a higher gateway SKU, more CPUs and network bandwidth are allocated to the gateway, and as a result, the gateway can support higher network throughput to the virtual network.

ExpressRoute virtual network gateways can use the following SKUs:

* ERGwScale (Preview)
* Standard
* HighPerformance
* UltraPerformance
* ErGw1Az
* ErGw2Az
* ErGw3Az

If you want to upgrade your gateway to a higher capacity gateway SKU, you can use the Seamless Gateway Migration tool in either Azure portal or PowerShell. The following upgrades are supported:

* Non-Az enabled SKU on Basic IP to Non Az enabled SKU on Standard IP.
* Non-Az enabled SKU on Basic IP to Az-enabled SKU on Standard IP.
* Non-Az enabled SKU on Standard IP to Az-enabled SKU on Standard IP.

For more information, see [Migrate to an availability zone-enabled gateway](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-howto-gateway-migration-powershell).

For all other downgrade scenarios, you need to delete and recreate the gateway. Recreating a gateway incurs downtime.

#### Gateway subnet

Before you create an ExpressRoute gateway, you must create a gateway subnet. The gateway subnet contains the IP addresses that the virtual network gateway VMs and services use. When you create your virtual network gateway, gateway VMs are deployed to the gateway subnet and configured with the required ExpressRoute gateway settings. Never deploy anything else into the gateway subnet. The gateway subnet must be named 'GatewaySubnet' to work properly. Naming the gateway subnet 'GatewaySubnet' lets Azure know to deploy the virtual network gateway VMs and services into this subnet.

Note

* User-defined routes with a 0.0.0.0/0 destination and NSGs on the GatewaySubnet **are not supported**. Gateways with this configuration are blocked from being created. Gateways require access to the management controllers in order to function properly. [BGP route propagation](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#border-gateway-protocol) should be set to "Enabled" on the GatewaySubnet to ensure availability of the gateway. If BGP route propagation is set to disabled, the gateway won't function.
* Diagnostics, data path, and control path can be affected if a user-defined route overlaps with the Gateway subnet range or the gateway public IP range.

* We don't recommend deploying Azure DNS Private Resolver into a virtual network that has an ExpressRoute virtual network gateway and setting wildcard rules to direct all name resolution to a specific DNS server. Such a configuration can cause management connectivity issues.

When you create the gateway subnet, you specify the number of IP addresses that the subnet contains. The IP addresses in the gateway subnet are allocated to the gateway VMs and gateway services. Some configurations require more IP addresses than others.

When you're planning your gateway subnet size, refer to the documentation for the configuration that you're planning to create. For example, the ExpressRoute/VPN Gateway coexist configuration requires a larger gateway subnet than most other configurations. Further more, you might want to make sure your gateway subnet contains enough IP addresses to accommodate possible future configurations. We recommend that you create a gateway subnet of /27 or larger (/27, /26 etc.). If you plan on connecting 16 ExpressRoute circuits to your gateway, you **must** create a gateway subnet of /26 or larger. If you're creating a dual stack gateway subnet, we recommend that you also use an IPv6 range of /64 or larger. This set up accommodates most configurations.

The following Resource Manager PowerShell example shows a gateway subnet named GatewaySubnet. You can see the CIDR notation specifies a /27, which allows for enough IP addresses for most configurations that currently exist.

Azure PowerShell 

```
Add-AzVirtualNetworkSubnetConfig -Name 'GatewaySubnet' -AddressPrefix 10.0.3.0/27

```

Important

Network security groups (NSGs) on the gateway subnet are not supported. Associating a network security group to this subnet might cause your virtual network gateway (VPN and ExpressRoute gateways) to stop functioning as expected. For more information about network security groups, see [What is a network security group](https://learn.microsoft.com/en-us/azure/virtual-network/network-security-groups-overview)?

#### Virtual network gateway limitations and performance

##### Feature support by gateway SKU

The following table shows the features supported across each gateway types and max number of ExpressRoute circuit connections supported by each gateway SKU.

| Gateway SKU | VPN Gateway and ExpressRoute coexistence | FastPath | Max Number of Circuit Connections |
| --- | --- | --- | --- |
| **Standard SKU/ERGw1Az** | Yes | No | 4 |
| **High Perf SKU/ERGw2Az** | Yes | No | 8 |
| **Ultra Performance SKU/ErGw3Az** | Yes | Yes | 16 |
| **ErGwScale (Preview)** | Yes | Yes - minimum 10 of scale units | 4 - minimum 1 of scale unit8 - minimum of 2 scale units16 - minimum of 10 scale units |

Note

The maximum number of ExpressRoute circuits from the same peering location that can connect to the same virtual network is 4 for all gateways.

##### Estimated performances by gateway SKU

The following tables provide an overview of the different types of gateways, their respective limitations, and their expected performance metrics. These numbers are derived from the following testing conditions and represent the max support limits. Actual performance may vary, depending on how closely traffic replicates these testing conditions.

###### Testing conditions

| Gateway SKU | Traffic sent from on-premises | Number of routes advertised by gateway | Number of routes learned by gateway |
| --- | --- | --- | --- |
| **Standard/ERGw1Az** | 1 Gbps | 500 | 4000 |
| **High Performance/ERGw2Az** | 2 Gbps | 500 | 9,500 |
| **Ultra Performance/ErGw3Az** | 10 Gbps | 500 | 9,500 |
| **ErGwScale (per scale unit)** | 1 Gbps | 500 | 4,000 |

Note

ExpressRoute can facilitate up to 11,000 routes that spans virtual network address spaces, on-premises network, and any relevant virtual network peering connections. To ensure stability of your ExpressRoute connection, refrain from advertising more than 11,000 routes to ExpressRoute.

###### Performance results

This table applies to both the Azure Resource Manager and classic deployment models.

| Gateway SKU | Mega-Bits per second | Packets per second | Supported number of VMs in the virtual network 1 | Flow count limit |
| --- | --- | --- | --- | --- |
| **Standard/ERGw1Az** | 1,000 | 100,000 | 2,000 | 200,000 |
| **High Performance/ERGw2Az** | 2,000 | 200,000 | 4,500 | 400,000 |
| **Ultra Performance/ErGw3Az** | 10,000 | 1,000,000 | 11,000 | 1,000,000 |
| **ErGwScale (per scale unit)** | 1,000 | 100,000 | 2,000 | 100,000 per scale unit |

1 The values in the table are estimates and vary depending on the CPU utilization of the gateway. If the CPU utilization is high and the number of supported VMs gets exceeded, the gateway will start to drop packets.

Important

* Application performance depends on multiple factors, such as end-to-end latency, and the number of traffic flows the application opens. The numbers in the table represent the upper limit that the application can theoretically achieve in an ideal environment. Additionally, Microsoft performs routine host and OS maintenance on the ExpressRoute Virtual Network Gateway, to maintain reliability of the service. During a maintenance period, the control plane and data path capacity of the gateway is reduced.
* During a maintenance period, you may experience intermittent connectivity issues to private endpoint resources.
* ExpressRoute supports a maximum TCP and UDP packet size of 1400 bytes. Packet size larger than 1400 bytes will get fragmented.
* Azure Route Server can support up to 4000 VMs. This limit includes VMs in virtual networks that are peered. For more information, see [Azure Route Server limitations](https://learn.microsoft.com/en-us/azure/route-server/overview#route-server-limits).

##### Zone-redundant gateway SKUs

You can also deploy ExpressRoute gateways in Azure Availability Zones. This configuration physically and logically separates them into different Availability Zones, protecting your on-premises network connectivity to Azure from zone-level failures.

![Zone-redundant ExpressRoute gateway](https://learn.microsoft.com/en-gb/azure/expressroute/media/expressroute-about-virtual-network-gateways/zone-redundant.png)
Zone-redundant gateways use specific new gateway SKUs for ExpressRoute gateway.

* ErGw1AZ
* ErGw2AZ
* ErGw3AZ
* ErGwScale (Preview)

The new gateway SKUs also support other deployment options to best match your needs. When creating a virtual network gateway using the new gateway SKUs, you can deploy the gateway in a specific zone. This type of gateway is referred to as a zonal gateway. When you deploy a zonal gateway, all the instances of the gateway are deployed in the same Availability Zone.

To learn about migrating an ExpressRoute gateway, see [Gateway migration](https://learn.microsoft.com/en-gb/azure/expressroute/gateway-migration).

#### ExpressRoute scalable gateway (Preview)

The ErGwScale virtual network gateway SKU enables you to achieve 40-Gbps connectivity to VMs and Private Endpoints in the virtual network. This SKU allows you to set a minimum and maximum scale unit for the virtual network gateway infrastructure, which auto scales based on the active bandwidth or flow count. You can also set a fixed scale unit to maintain a constant connectivity at a desired bandwidth value.

##### Availability zone deployment & regional availability

ErGwScale supports both zonal and zonal-redundant deployments in Azure availability zones. For more information about these concepts, review the [Zonal and zone-redundant services](https://learn.microsoft.com/en-gb/azure/reliability/availability-zones-overview#zonal-and-zone-redundant-services) documentation.

ErGwScale is available in preview in the following regions:

* Australia East
* Brazil South
* Canada Central
* East US
* East Asia
* France Central
* Germany West Central
* India Central
* Italy North
* North Europe
* Norway East
* Sweden Central
* UAE North
* UK South
* West US 2
* West US 3

##### Autoscaling vs. fixed scale unit

The virtual network gateway infrastructure auto scales between the minimum and maximum scale unit that you configure, based on the bandwidth or flow count utilization. Scale operations might take up to 30 minutes to complete. If you want to achieve a fixed connectivity at a specific bandwidth value, you can configure a fixed scale unit by setting the minimum scale unit and the maximum scale unit to the same value.

##### Limitations

* **Basic IP**: **ErGwScale** doesn't support the **Basic IP SKU**. You need to use a **Standard IP SKU** to configure **ErGwScale**.
* **Minimum and Maximum Scale Units**: You can configure the **scale unit** for ErGwScale between **1-40**. The **minimum scale unit** can't be lower than **1** and the **maximum scale unit** can't be higher than **40**.
* **Migration Scenarios**: You can't migrate from **Standard/ErGw1Az**, **HighPerf/ErGw2Az/UltraPerf/ErGw3Az** to **ErGwScale** in the **Public preview**.

##### Pricing

ErGwScale is free of charge during public preview. For information about ExpressRoute pricing, see [Azure ExpressRoute pricing](https://azure.microsoft.com/pricing/details/expressroute/#pricing).

##### Estimated performance per scale unit

###### Supported performance per scale unit

| Scale unit | Bandwidth (Gbps) | Packets per second | Connections per second | Maximum VM connections 1 | Maximum number of flows |
| --- | --- | --- | --- | --- | --- |
| 1-10 | 1 | 100,000 | 7,000 | 2,000 | 100,000 |
| 11-40 | 1 | 100,000 | 7,000 | 1,000 | 100,000 |

###### Sample performance with scale unit

| Scale unit | Bandwidth (Gbps) | Packets per second | Connections per second | Maximum VM connections 1 | Maximum number of flows |
| --- | --- | --- | --- | --- | --- |
| 10 | 10 | 1,000,000 | 70,000 | 20,000 | 1,000,000 |
| 20 | 20 | 2,000,000 | 140,000 | 30,000 | 2,000,000 |
| 40 | 40 | 4,000,000 | 280,000 | 50,000 | 4,000,000 |

1 Maximum VM connections scale differently beyond 10 scale units. The first 10 scale units provide capacity for 2,000 VMs per scale unit. Scale units 11 and above provides 1,000 more VM capacity per scale unit.

#### VNet to VNet and VNet to Virtual WAN connectivity

By default, VNet to VNet and VNet to Virtual WAN connectivity is disabled through an ExpressRoute circuit for all gateway SKUs. To enable this connectivity, you must configure the ExpressRoute virtual network gateway to allow this traffic. For more information, see guidance about [virtual network connectivity over ExpressRoute](https://learn.microsoft.com/en-gb/azure/expressroute/virtual-network-connectivity-guidance). To enable this traffic, see [Enable VNet to VNet or VNet to Virtual WAN connectivity through ExpressRoute](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-howto-add-gateway-portal-resource-manager#enable-or-disable-vnet-to-vnet-or-vnet-to-virtual-wan-traffic-through-expressroute).

#### FastPath

ExpressRoute virtual network gateway is designed to exchange network routes and route network traffic. FastPath is designed to improve the data path performance between your on-premises network and your virtual network. When enabled, FastPath sends network traffic directly to virtual machines in the virtual network, bypassing the gateway.

For more information about FastPath, including limitations, and requirements, see [About FastPath](https://learn.microsoft.com/en-gb/azure/expressroute/about-fastpath).

#### Connectivity to private endpoints

The ExpressRoute virtual network gateway facilitates connectivity to private endpoints deployed in the same virtual network as the virtual network gateway and across virtual network peers.

Important

* The throughput and control plane capacity for connectivity to private endpoint resources may be reduced by half compared to connectivity to non-private-endpoint resources.
* During a maintenance period, you may experience intermittent connectivity issues to private endpoint resources.
* You need to ensure their on-premises configuration, including router & firewall settings, are correctly set up to ensure that packets for the IP 5-tuple transits uses a single next hop (Microsoft Enterprise Edge router - MSEE) unless there is a maintenance event. If your on-premises firewall or router configuration is causing the same IP 5-tuple to frequently switch next hops, then you will experience connectivity issues.

##### Private endpoint connectivity and planned maintenance events

Private endpoint connectivity is stateful. When a connection to a private endpoint gets established over ExpressRoute private peering, inbound, and outbound connections get routed through one of the backend instances of the gateway infrastructure. During a maintenance event, backend instances of the virtual network gateway infrastructure are rebooted one at a time, which could lead to intermittent connectivity issues.

To avoid or minimize connectivity issues with private endpoints during maintenance activities, we recommend setting the TCP time-out value to fall between 15-30 seconds on your on-premises applications. Test and configure the optimal value based on your application requirements.

#### REST APIs and PowerShell cmdlets

For more technical resources and specific syntax requirements when using REST APIs and PowerShell cmdlets for virtual network gateway configurations, see the following pages:

| **Classic** | **Resource Manager** |
| --- | --- |
| [PowerShell](https://learn.microsoft.com/en-us/powershell/module/servicemanagement/azure) | [PowerShell](https://learn.microsoft.com/en-us/powershell/module/az.network#networking) |
| [REST API](https://learn.microsoft.com/en-us/previous-versions/azure/reference/jj154113(v=azure.100)) | [REST API](https://learn.microsoft.com/en-us/rest/api/virtual-network/) |

#### VNet-to-VNet connectivity

By default, connectivity between virtual networks is enabled when you link multiple virtual networks to the same ExpressRoute circuit. Microsoft recommends not using your ExpressRoute circuit for communication between virtual networks. Instead, we recommend you to use [virtual network peering](https://learn.microsoft.com/en-gb/azure/virtual-network/virtual-network-peering-overview). For more information about why VNet-to-VNet connectivity isn't recommended over ExpressRoute, see [connectivity between virtual networks over ExpressRoute](https://learn.microsoft.com/en-gb/azure/expressroute/virtual-network-connectivity-guidance).

##### Virtual network peering

A virtual network with an ExpressRoute gateway can have virtual network peering with up to 500 other virtual networks. Virtual network peering without an ExpressRoute gateway might have a higher peering limitation.

#### Next steps

* For more information about available connection configurations, see [ExpressRoute Overview](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-introduction).
* For more information about creating ExpressRoute gateways, see [Create a virtual network gateway for ExpressRoute](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-howto-add-gateway-resource-manager).
* For more information on how to deploy ErGwScale, see [Configure a virtual network gateway for ExpressRoute using the Azure portal](https://learn.microsoft.com/en-gb/azure/expressroute/expressroute-howto-add-gateway-portal-resource-manager).
* For more information about configuring zone-redundant gateways, see [Create a zone-redundant virtual network gateway](https://learn.microsoft.com/en-gb/azure/vpn-gateway/create-zone-redundant-vnet-gateway).
* For more information about FastPath, see [About FastPath](https://learn.microsoft.com/en-gb/azure/expressroute/about-fastpath).

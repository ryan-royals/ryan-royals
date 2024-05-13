---
{"dg-publish":true,"dg-path":"Azure Virtual Network Gateway.md","permalink":"/azure-virtual-network-gateway/","tags":["notes"]}
---


Azure Virtual Network Gateway is the parent resource that can be configured to become a **ExpressRoute Gateway**, or **VPN Gateway**.

Both types of gateways require that a specific [[30 Slipbox/Azure Subnet\|Azure Subnet]] must be deployed to the [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]], with the **Exact Name** of `GatewaySubnet`.  
This subnet can be as small as /29, but it is recommended to be a /27 or larger to account for more ExpressRoute / VPN Connections.

When configuring a connection, a [[30 Slipbox/Azure Local Network Gateway\|Azure Local Network Gateway]] and a [[30 Slipbox/Azure Connection\|Azure Connection]] are configured to represent a on-premises location.

## VPN Gateway

Azure VPN Gateway is used to create a [[30 Slipbox/Virtual Private Network\|Virtual Private Network]] connections as either Point-to-Site, Site-to-Site or Vnet-to-Vnet to a [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]].

### VPN Gateway Types

VPN Gateway can be deployed as **Policy Based** or **Route Based**. This option can not be changed after the provisioning of the VPN Gateway.  
**Policy Based** can only be used with *basic* SKU and are limited to IKEv1, while **Route Based** is the option for the other SKUs and supports IKEv2.  
Microsoft recommendation is to use **Route Based**

| **Features**                      | **PolicyBased Basic VPN Gateway** | **RouteBased Basic VPN Gateway**                                       | **RouteBased Standard VPN Gateway**                                    | **RouteBased High Performance VPN Gateway**                            |
| --------------------------------- | --------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Site-to-Site connectivity (S2S)   | PolicyBased VPN configuration     | RouteBased VPN configuration                                           | RouteBased VPN configuration                                           | RouteBased VPN configuration                                           |
| Point-to-Site connectivity (P2S)  | Not supported                     | Supported (Can coexist with S2S)                                       | Supported (Can coexist with S2S)                                       | Supported (Can coexist with S2S)                                       |
| Authentication method             | Pre-shared key                    | Pre-shared key for S2S connectivity, Certificates for P2S connectivity | Pre-shared key for S2S connectivity, Certificates for P2S connectivity | Pre-shared key for S2S connectivity, Certificates for P2S connectivity |
| Maximum number of S2S connections | 1                                 | 10                                                                     | 10                                                                     | 30                                                                     |
| Maximum number of P2S connections | Not supported                     | 128                                                                    | 128                                                                    | 128                                                                    |
| Active routing support (BGP)      | Not supported                     | Not supported                                                          | Supported                                                              | Supported                                                              |

### SKUs

|**VPN Gateway Generation**|**SKU**|**S2S/VNet-to-Vnet Tunnels**|**P2S SSTP Connections**|**P2S IKEv2/OpenVPN Connections**|**Aggregate Throughput Benchmark**|**BGP**|**Zone-redundant**|
|---|---|---|---|---|---|---|---|
|Generation1|Basic|Max. 10|Max. 128|Not Supported|100 Mbps|Not Supported|No|
|Generation1|VpnGw1|Max. 30*|Max. 128|Max. 250|650 Mbps|Supported|No|
|Generation1|VpnGw2|Max. 30*|Max. 128|Max. 500|1 Gbps|Supported|No|
|Generation1|VpnGw3|Max. 30*|Max. 128|Max. 1000|1.25 Gbps|Supported|No|
|Generation1|VpnGw1AZ|Max. 30*|Max. 128|Max. 250|650 Mbps|Supported|Yes|
|Generation1|VpnGw2AZ|Max. 30*|Max. 128|Max. 500|1 Gbps|Supported|Yes|
|Generation1|VpnGw3AZ|Max. 30*|Max. 128|Max. 1000|1.25 Gbps|Supported|Yes|
|Generation2|VpnGw2|Max. 30*|Max. 128|Max. 500|1.25 Gbps|Supported|No|
|Generation2|VpnGw3|Max. 30*|Max. 128|Max. 1000|2.5 Gbps|Supported|No|
|Generation2|VpnGw4|Max. 30*|Max. 128|Max. 5000|5 Gbps|Supported|No|
|Generation2|VpnGw5|Max. 30*|Max. 128|Max. 10000|10 Gbps|Supported|No|
|Generation2|VpnGw2AZ|Max. 30*|Max. 128|Max. 500|1.25 Gbps|Supported|Yes|
|Generation2|VpnGw3AZ|Max. 30*|Max. 128|Max. 1000|2.5 Gbps|Supported|Yes|
|Generation2|VpnGw4AZ|Max. 100*|Max. 128|Max. 5000|5 Gbps|Supported|Yes|
|Generation2|VpnGw5AZ|Max. 100*|Max. 128|Max. 10000|10 Gbps|Supported|Yes|

(\*) Use Virtual WAN if you need more than 30 S2S VPN tunnels.

All the *VPN* SKUs can be actively resized at anytime, but the *Basic* SKU is a legacy SKU, and can not be resized.

### High Availability

To provide better availability for your VPN connections, there are a few options available:

- [[30 Slipbox/Azure Virtual Network Gateway#VPN Gateway Redundancy\|#VPN Gateway Redundancy]]
- [[30 Slipbox/Azure Virtual Network Gateway#Multiple on-premises VPN devices\|#Multiple on-premises VPN devices]]
- [[30 Slipbox/Azure Virtual Network Gateway#Active-active Azure VPN gateway\|#Active-active Azure VPN gateway]]
- Combination of both

#### VPN Gateway Redundancy

![Azure Virtual Network Gateway-1714955234905.png](/img/user/40%20References/attachments/image/Azure%20Virtual%20Network%20Gateway-1714955234905.png)  
Every Azure VPN Gateway consists of two instances in a Active-standby configuration. Failover to the standby instance is automatically attempted for any planned maintenance or unplanned disruption.  
Planned maintenance connectivity should typically be restored within 10-15 seconds, and unplanned disruption should be recovered in about 1-3 minutes. S2S connections should automatically reconnect, but P2S will likely need to be re initiated.

#### Multiple On-premises VPN Devices

![Azure Virtual Network Gateway-1714955592079.png](/img/user/40%20References/attachments/image/Azure%20Virtual%20Network%20Gateway-1714955592079.png)

This solution is used to create redundancy on the on-premises side of the configuration, but follows the same constraints as the [[30 Slipbox/Azure Virtual Network Gateway#VPN Gateway Redundancy\|#VPN Gateway Redundancy]] on the Azure side.  
There are some requirements and constraints:

1. You need to create multiple S2S VPN connections from your VPN devices to Azure. When you connect multiple VPN devices from the same on-premises network to Azure, you need to create one local network gateway for each VPN device, and one connection from your Azure VPN gateway to each local network gateway.
2. The local network gateways corresponding to your VPN devices must have unique public IP addresses in the GatewayIpAddress property.
3. [[30 Slipbox/Border Gateway Protocol\|BGP]] is required for this configuration. Each local network gateway representing a VPN device must have a unique BGP peer IP address specified in the Bgp PeerIpAddress property.
4. You should use BGP to advertise the same prefixes of the same on-premises network prefixes to your Azure VPN gateway, and the traffic will be forwarded through these tunnels simultaneously.
5. You must use Equal-cost multi-path routing (ECMP).
6. Each connection is counted against the maximum number of tunnels for your Azure VPN gateway, 10 for Basic and Standard SKUs, and 30 for HighPerformance SKU.

#### Active-active Azure VPN Gateway

![Azure Virtual Network Gateway-1714955747883.png](/img/user/40%20References/attachments/image/Azure%20Virtual%20Network%20Gateway-1714955747883.png)  
Note that both VPN tunnels are part of the same connection. You will still need to configure your on-premises VPN device to accept or establish two S2S VPN tunnels to those two Azure VPN gateway public IP addresses.  
Because the Azure gateway instances are in active-active configuration, the traffic from your Azure virtual network to your on-premises network will be routed through both tunnels simultaneously, even if your on-premises VPN device may favour one tunnel over the other. For a single TCP or UDP flow, Azure attempts to use the same tunnel when sending packets to your on-premises network. However, your on-premises network could use a different tunnel to send packets to Azure.

#### Dual Redundant Active-Active

![Azure Virtual Network Gateway-1714956278426.png](/img/user/40%20References/attachments/image/Azure%20Virtual%20Network%20Gateway-1714956278426.png)  
Here you create and set up the Azure VPN gateway in an active-active configuration and create two local network gateways and two connections for your two on-premises VPN devices as described above. The result is a full mesh connectivity of 4 IPsec tunnels between your Azure virtual network and your on-premises network.

### Tips and Troubleshooting

#### [[30 Slipbox/Use Azure DNS Private Resolver over Azure VPN\|Use Azure DNS Private Resolver over Azure VPN]]

#### Cant Route to Spoke from P2S

- General steps:
  - Check that the DNS Private Resolver is added to the VPN config
- If using a Azure Firewall and Forced Tunnelling:
  - Check that the routes for the VPN range on the spokes, not just a 0.0.0.0/0.
  - Check that the AzureFirewallSubnet has routes that route the subnet ranges to the Virtual Network Gateway.
  - Check that the VNG advertises the routes for the spokes.
  - Check that the Vnet peering is working.
  - Disable the Gateway Route propagation on the peering, as force tunnelling works around this.

#### Troubleshoot Azure VPN Gateway Using Diagnostic Logs

Using diagnostic logs, you can troubleshoot multiple VPN gateway related events including configuration activity, VPN Tunnel connectivity, IPsec logging, BGP route exchanges, Point to Site advanced logging.

There are several diagnostic logs you can use to help troubleshoot a problem with your VPN Gateway.

- **GatewayDiagnosticLog** - Contains diagnostic logs for gateway configuration events, primary changes, and maintenance events.
- **TunnelDiagnosticLog** - Contains tunnel state change events. Tunnel connect/disconnect events have a summarized reason for the state change if applicable.
- **RouteDiagnosticLog** - Logs changes to static routes and BGP events that occur on the gateway.
- **IKEDiagnosticLog** - Logs IKE control messages and events on the gateway.
- **P2SDiagnosticLog** - Logs point-to-site control messages and events on the gateway.

Use [[30 Slipbox/Azure Monitor\|Azure Monitor]] to analyse the data collected in the diagnostic logs.

## Express Route Gateway

### Express Route Types

#### Azure Private

Connects you to your VNET

#### Microsoft Peering

Connects you to Microsoft services like O365, as well as Public IP ranges for Azure Regions

---
{"dg-publish":true,"dg-path":"Routing in Azure.md","permalink":"/routing-in-azure/","tags":["notes"]}
---


Forget **Administrative Distance** and **Metrics**.

In Azure, these concepts are replaced by simple logic:  
**User Defined Route** over **BGP Route** over **System Route**.

## What Are the Default Routes

| Source  | Address prefixes              | Next hop type   |
| ------- | ----------------------------- | --------------- |
| Default | Unique to the virtual network | Virtual network |
| Default | 0.0.0.0/0                     | Internet        |
| Default | 10.0.0.0/8                    | None            |
| Default | 172.16.0.0/12                 | None            |
| Default | 192.168.0.0/16                | None            |
| Default | 100.64.0.0/10                 | None            |  

[^1]

 Default Route includes routes for the Address Space of a Virtual Network. Each Address Space Range gets its own route, allowing traffic to flow between subnets.

### Additional Default Routes

When declaring [[30 Slipbox/Azure Virtual Network\|Virtual Networks]], you are unable to do so if the new VNET Address Space overlaps with any VNET in the mesh of VNETS that you are trying to peer it into.

When you Peer, you can optionally add new Routes to the default routes: [^2]

| Source                  | Address prefixes                                                                         | Next hop type                 | Subnets                                            |
| ----------------------- | ---------------------------------------------------------------------------------------- | ----------------------------- | -------------------------------------------------- |
| Default                 | Unique to the virtual network                                                            | VNet Peering                  | All                                                |
| Virtual network gateway | Prefixes advertised from on-premises via BGP, or configured in the local network gateway | Virtual Network Gateway       | All                                                |
| Default                 | Multiple                                                                                 | VirtualNetworkServiceEndpoint | Only the subnet a service endpoint is enabled for. |

## BGP In Azure

[[30 Slipbox/Border Gateway Protocol\|Border Gateway Protocol]] is implemented in Azure, either managed by a [[30 Slipbox/Azure Route Server\|Azure Route Server]] or being propagated from on-premises using a [[30 Slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]].

Microsoft reserves 12076 for Azure public, Azure private, and Microsoft peering. Microsoft reserves 65515 for internal use. Virtual networks are created with the default ASN of 65515. The following ASNs are reserved by Azure or IANA:

- ASNs reserved by Azure:
    - Public ASNs: 8074, 8075, and 12076
    - Private ASNs: 65515, 65517, 65518, 65519, and 65520
- ASNs reserved by IANA:
    - 23456, 64496-64511, 65535-65551, and 429496729

Customers use either 16-bit or 32-bit ASNs.

## Designing a Azure Network

### Hub and Spoke through Firewall

When you configure VNET Peering, they typically automatically learn routes about each other. In a typical Hub and Spoke topology, the desire is to route all traffic through the [[30 Slipbox/Azure Firewall\|Azure Firewall]].

Since Default Routes Address Prefix is the Address Space for the VNET, a Route must be applied that is that specific or more specific that Next Hop is the Azure Firewall to overwrite the Default Route.

| Source  | Address prefixes                            | Next hop type                | Enabled |
| ------- | ------------------------------------------- | ---------------------------- | ------- |
| Default | Unique to the virtual network (10.0.1.0/24) | Virtual Network              | true    |
| User Defined | 0.0.0.0/0                                   | Virtual Appliance (10.0.0.4) | true    |
| Default | 10.0.0.0/24                                 | Virtual Network              | false   |
| User Defined | 10.0.0.0/24                                 | Virtual Appliance (10.0.0.4) | true        |  

*Assume this is for a Spoke Subnet in the 10.0.1.0/24 Address Space, and Hub Address Space is 10.0.0.0/24*

The firewall egresses traffic through the *AzureFirewallSubnet*, which has the learned routes of each spoke.

### VPN / Express Route through Firewall

#### GatewaySubnet

When using a [[30 Slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]], you must put a Route Table on the *GatewaySubnet* that has routes for the Hub and each Spoke to use the Firewall, but you can not add a **0.0.0.0/0** route to this subnet.

| Source  | Address prefixes                            | Next hop type                | Enabled |
| ------- | ------------------------------------------- | ---------------------------- | ------- |
| Default | Unique to the virtual network (10.0.0.0/24) | Virtual Network              | false   |
| User Defined | 10.0.0.0/24                                   | Virtual Appliance (10.0.0.4) | true    |
| Default | 10.0.1.0/24                                 | Virtual Network              | false   |
| User Defined | 10.0.1.0/24                                 | Virtual Appliance (10.0.0.4) | true    |  

*Assume this is for a Hub Subnet in the 10.0.0.0/24 Address Space, and Spoke Address Space is 10.0.1.0/24*

#### Spoke Virtual Networks

When using a Azure Virtual Network Gateway to advertise routes for on premises, if the traffic is to first go through the Azure Firewall, you must overwrite the Additional Default Routes to stop traffic going from Spoke direct to VNG.

| Source                  | Address prefixes                            | Next hop type                | Enabled |
| ----------------------- | ------------------------------------------- | ---------------------------- | ------- |
| Default                 | Unique to the virtual network (10.0.1.0/24) | Virtual Network              | true    |
| User Defined            | 0.0.0.0/0                                   | Virtual Appliance (10.0.0.4) | true    |
| Default                 | 10.0.0.0/24                                 | Virtual Network              | false   |
| User Defined            | 10.0.0.0/24                                 | Virtual Appliance (10.0.0.4) | true    |
| Virtual Network Gateway | 192.168.0.0/24                              | Virtual Network Gateway      | false   |
| User Defined            | 192.168.0.0/24                              | Virtual Appliance (10.0.0.4) | true        |  

*Assume this is for Spoke in the 10.0.1.0/24 Address Space, Hub Address Space is 10.0.0.0/24, and On Premises Address Space is 192.168.0.0/24*

## See Also

- [[30 Slipbox/Network Routing\|Network Routing]]

## References

[^1]: [[40 References/readwise/Azure virtual network traffic routing\|Azure virtual network traffic routing]]
[^2]: [[40 References/readwise/Azure virtual network traffic routing\|Azure virtual network traffic routing]]

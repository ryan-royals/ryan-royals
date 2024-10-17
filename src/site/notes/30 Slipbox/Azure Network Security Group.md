---
{"dg-publish":true,"dg-path":"Azure Network Security Group.md","permalink":"/azure-network-security-group/","tags":["notes"]}
---


A Network Security Group (NSG) in Azure allows you to filter network traffic to and from Azure resources in an Azure virtual network. A network security group contains security rules that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources. For each rule, you can specify source and destination, port, and protocol.  
[^1]  
NSG's can also be used to target [[30 Slipbox/Azure Application Security Groups\|Azure Application Security Groups]], which allows for the targeting of NICS bundled as a application, rather than targeting a set of IP addresses.

## NSG Security Rules

A network security group contains zero, or as many rules as desired, within Azure subscription limits. Each rule specifies the following properties:

- **Name** - Must be a unique name within the network security group.
- **Priority** - Can be any number between 100 and 4096. Rules are processed in priority order, with lower numbers processed before higher numbers, because lower numbers have higher priority. Once traffic matches a rule, processing stops. As a result, any rules that exist with lower priorities (higher numbers) that have the same attributes as rules with higher priorities aren't processed.
- **Source or destination** - Can be set to Any, or an individual IP address, or classless inter-domain routing (CIDR) block (10.0.0.0/24, for example), service tag, or application security group.
- **Protocol** - Can be TCP, UDP, ICMP, ESP, AH, or Any.
- **Direction** - Can be configured to apply to inbound, or outbound traffic.
- **Port range** - Can be specified either as an individual port or range of ports. For example, you could specify 80 or 10000-10005. Specifying ranges enables you to create fewer security rules.
- **Action** - Can be set to Allow or deny.

The firewall evaluates network security group security rules by priority, using the 5-tuple information (source, source port, destination, destination port, and protocol) to either allow or deny the traffic.  
[^1]

## Default Security Rules

Azure creates the following default rules in each network security group that you create:

|**Direction**|**Name**|**Priority**|**Source**|**Source Ports**|**Destination**|**Destination Ports**|**Protocol**|**Access**|
|---|---|---|---|---|---|---|---|---|
|Inbound|`AllowVNetInBound`|65000|`VirtualNetwork`|0-65535|`VirtualNetwork`|0-65535|Any|Allow|
|Inbound|`AllowAzureLoadBalancerInBound`|65001|`AzureLoadBalancer`|0-65535|0.0.0.0/0|0-65535|Any|Allow|
|Inbound|`DenyAllInbound`|65500|0.0.0.0/0|0-65535|0.0.0.0/0|0-65535|Any|Deny|
|Outbound|`AllowVnetOutBound`|65000|`VirtualNetwork`|0-65535|`VirtualNetwork`|0-65535|Any|Allow|
|Outbound|`AllowInternetOutBound`|65001|0.0.0.0/0|0-65535|`Internet`|0-65535|Any|Allow|
|Outbound|`DenyAllOutBound`|65500|0.0.0.0/0|0-65535|0.0.0.0/0|0-65535|

## NSG Assignment and Precedence

Network Security Groups can be assigned to [[30 Slipbox/Azure Subnet\|Subnets]] and [[30 Slipbox/Azure Network Interface Card\|NICs]]. If both a NIC is mounted to a Subnet, and both have NSG's attached, the Subnet NSG rules are applied first for Ingress traffic, and the opposite is applied for Egress.

[^1]: [[40 References/readwise/Deploy Network Security Groups by Using the Azure Portal - Training\|Deploy Network Security Groups by Using the Azure Portal - Training]]

---
{"dg-publish":true,"permalink":"/40-references/readwise/deploy-network-security-groups-by-using-the-azure-portal-training/","tags":["rw/articles"]}
---

![40 References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg](/img/user/40%20References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/training/modules/design-implement-network-security-monitoring/5-deploy-network-security-groups-by-using-the-azure-portal
Author: wwlpublish

## Summary

A Network Security Group (NSG) in Azure filters network traffic to and from resources in a virtual network using security rules. These rules specify details like source, destination, and protocol to allow or deny traffic. Default rules are created automatically, and both inbound and outbound traffic is processed based on the association of the NSG with subnets or network interfaces.

## Highlights added October 8, 2024 at 11:45 AM
>A Network Security Group (NSG) in Azure allows you to filter network traffic to and from Azure resources in an Azure virtual network. A network security group contains security rules that allow or deny inbound network traffic to, or outbound network traffic from, several types of Azure resources. For each rule, you can specify source and destination, port, and protocol.
>NSG security rules
>A network security group contains zero, or as many rules as desired, within Azure subscription limits. Each rule specifies the following properties:
>• **Name** - Must be a unique name within the network security group.
>• **Priority** - Can be any number between 100 and 4096. Rules are processed in priority order, with lower numbers processed before higher numbers, because lower numbers have higher priority. Once traffic matches a rule, processing stops. As a result, any rules that exist with lower priorities (higher numbers) that have the same attributes as rules with higher priorities aren't processed.
>• **Source or destination** - Can be set to Any, or an individual IP address, or classless inter-domain routing (CIDR) block (10.0.0.0/24, for example), service tag, or application security group.
>• **Protocol** - Can be TCP, UDP, ICMP, ESP, AH, or Any.
>• **Direction** - Can be configured to apply to inbound, or outbound traffic.
>• **Port range** - Can be specified either as an individual port or range of ports. For example, you could specify 80 or 10000-10005. Specifying ranges enables you to create fewer security rules.
>• **Action** - Can be set to Allow or deny.
>The firewall evaluates network security group security rules by priority, using the 5-tuple information (source, source port, destination, destination port, and protocol) to either allow or deny the traffic.
>Default security rules
>Azure creates the following default rules in each network security group that you create:
>Expand table
>**Direction**
>**Name**
>**Priority**
>**Source**
>**Source Ports**
>**Destination**
>**Destination Ports**
>**Protocol**
>**Access**
>Inbound
>`AllowVNetInBound`
>65000
>`VirtualNetwork`
>0-65535
>`VirtualNetwork`
>0-65535
>Any
>Allow
>Inbound
>`AllowAzureLoadBalancerInBound`
>65001
>`AzureLoadBalancer`
>0-65535
>0.0.0.0/0
>0-65535
>Any
>Allow
>Inbound
>`DenyAllInbound`
>65500
>0.0.0.0/0
>0-65535
>0.0.0.0/0
>0-65535
>Any
>Deny
>Outbound
>`AllowVnetOutBound`
>65000
>`VirtualNetwork`
>0-65535
>`VirtualNetwork`
>0-65535
>Any
>Allow
>Outbound
>`AllowInternetOutBound`
>65001
>0.0.0.0/0
>0-65535
>`Internet`
>0-65535
>Any
>Allow
>Outbound
>`DenyAllOutBound`
>65500
>0.0.0.0/0
>0-65535
>0.0.0.0/0
>0-65535
>Any
>Deny ([View Highlight] (https://read.readwise.io/read/01j9mty8r575e5k86fhrw06bdh))



---
{"dg-publish":true,"dg-path":"Azure NAT Gateway.md","permalink":"/azure-nat-gateway/","tags":["notes"]}
---


## Azure NAT Gateway

![Azure NAT Gateway-1693824352692.png](/img/user/40%20References/attachments/Azure%20NAT%20Gateway-1693824352692.png)

Azure NAT Gateways provide a way to utilise [[Network Address Translation\|Network Address Translation]] to route outbound traffic through to the internet through a single [[30 Slipbox/Azure Public IP\|Azure Public IP]] or IP Prefix.

NAT Gateways do not allow traffic ingress, and are a controlled way to have a known IP/s to firewall for other services.

NAT Gateways replace a [[30 Slipbox/Routing in Azure#What Are the Default Routes\|subnets default route]] to the internet. This can be overwritten by [[30 Slipbox/Azure User Defined Route\|Azure User Defined Route]] (Though this pattern most likely is not practical).

Using [[Network Address Translation\|Network Address Translation]], this service can support up to 64,000 concurrent traffic flows.

### Configurations

- Multiple Subnets within the same VNET can use different NAT gateways or the same NAT gateway.
- Multiple NAT gateways cant be attached to a single subnet.
- NAT Gateways can not span multiple Virtual Networks.
- NAT Gateways can not be deployed in a [[30 Slipbox/Azure Virtual Network Gateway\|Gateway Subnet]].
- No IPv6
- Can use up to 16 IP addresses in any combination of:
	- Public IP addresses
	- Public IP prefixes
	- Public IP addresses and prefixes derived from custom IP prefixes (BYOIP), to learn more, see [Custom IP address prefix (BYOIP)](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/custom-ip-address-prefix).
	- Can be used on a [[30 Slipbox/Azure Firewall\|Azure Firewall]] subnet.

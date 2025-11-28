---
{"dg-publish":true,"permalink":"/90-slipbox/azure-subnet/","tags":["notes"]}
---


Subnets are the standard subdivision of a [[90_slipbox/Azure Virtual Network#Address Space\|Address Space]], and can be either IPv4 or IPv6.  
IPv4 Subnets can be a max size of /16, and IPv6 subnets **must be exactly** /64 in size.

5 Addresses are reserved by Azure and can not be used.  
For example, the IP address range of 192.168.1.0/24 has the following reserved addresses:

- 192.168.1.0 : Network address
- 192.168.1.1 : Reserved by Azure for the default gateway
- 192.168.1.2, 192.168.1.3 : Reserved by Azure to map the Azure DNS IPs to the VNet space
- 192.168.1.255 : Network broadcast address.

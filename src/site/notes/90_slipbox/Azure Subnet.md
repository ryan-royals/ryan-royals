---
{"dg-publish":true,"permalink":"/90-slipbox/azure-subnet/","tags":["notes"],"created":"2025-06-11T10:28:47.826+09:30","updated":"2026-03-03T09:55:32.408+10:30","dg-note-properties":{"created":"2023-09-04","modified":"2026-03-03","related":["[[Azure Virtual Network]]","[[Network Addressing]]"],"tags":"notes"}}
---


Subnets are the standard subdivision of a [[90_slipbox/Azure Virtual Network#Address Space\|Address Space]], and can be either IPv4 or IPv6.  
IPv4 Subnets can be a max size of /16, and IPv6 subnets **must be exactly** /64 in size.

5 Addresses are reserved by Azure and can not be used.  
For example, the IP address range of 192.168.1.0/24 has the following reserved addresses:

- 192.168.1.0 : Network address
- 192.168.1.1 : Reserved by Azure for the default gateway
- 192.168.1.2, 192.168.1.3 : Reserved by Azure to map the Azure DNS IPs to the VNet space
- 192.168.1.255 : Network broadcast address.

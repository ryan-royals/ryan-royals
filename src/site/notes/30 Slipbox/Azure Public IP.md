---
{"tags":["notes"],"topics":["[[Azure]]","[[Azure Public IP Address Prefix]]"],"references":["[[Configure public IP services - Training  Microsoft Learn]]"],"created":"2024-05-02","dg-publish":true,"dg-path":"Azure Public IP.md","permalink":"/azure-public-ip/","dgPassFrontmatter":true}
---


Public networks like the Internet communicate by using public IP addresses. Private networks like your Azure Virtual Network use private IP addresses, which aren't routable on public networks. To support a network that exists both in Azure and on-premises, you must configure IP addressing for both types of networks.

Public IP addresses enable Internet resources to communicate with Azure resources and enable Azure resources to communicate outbound with Internet and public-facing Azure services. A public IP address in Azure is dedicated to a specific resource, until it's unassigned by a network engineer. A resource without a public IP assigned can communicate outbound through network address translation services, where Azure dynamically assigns an available IP address that isn't dedicated to the resource.

Public Ip Addresses can be pulled from a [[30 Slipbox/Azure Public IP Address Prefix\|Public IP Address Prefix]], which is managed as its own resource.

## Types

Azure Public IP addresses can be either *static* or *dynamic* IPv4 or Ipv6 Addresses.  
*Static* Ip addresses keep the assigned number for as long as the resource exists, while *dynamic* addresses may change over the  
lifespan of a resource. A common example on when a IP may change is when a Virtual Machine is power cycled.

## SKUs

Azure Public IPs are available in 2 SKU's: *Standard* and *Basic*. General rule is that *Standard* is the standard, as most other services require standard.

| Public IP address  | **Standard**                                                                                                                                                                                                                         | **Basic**                                                                                                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Allocation method  | Static                                                                                                                                                                                                                               | For IPv4: Dynamic or Static; For IPv6: Dynamic.                                                                                                                     |
| Idle Timeout       | Have an adjustable inbound originated flow idle timeout of 4-30 minutes, with a default of 4 minutes, and fixed outbound originated flow idle timeout of 4 minutes.                                                                  | Have an adjustable inbound originated flow idle timeout of 4-30 minutes, with a default of 4 minutes, and fixed outbound originated flow idle timeout of 4 minutes. |
| Security           | Secure by default model and be closed to inbound traffic when used as a frontend. Allow traffic with network security group (NSG) is required (for example, on the NIC of a virtual machine with a Standard SKU Public IP attached). | Open by default. Network security groups are recommended but optional for restricting inbound or outbound traffic                                                   |
| Availability zones | Supported. Standard IPs can be non-zonal, zonal, or zone-redundant. Zone redundant IPs can only be created in regions where 3 availability zones are live. IPs created before zones are live won't be zone redundant.                | Not supported.                                                                                                                                                      |
| Routing preference | Supported to enable more granular control of how traffic is routed between Azure and the Internet.                                                                                                                                   | Not supported.                                                                                                                                                      |
| Global tier        | Supported via cross-region load balancers.                                                                                                                                                                                           | Not supported.                                                                                                                                                      |

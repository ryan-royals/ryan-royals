---
{"dg-publish":true,"permalink":"/40-references/readwise/configure-public-ip-services-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

## Full Document
[[40 References/readwise/Full Document Contents/Configure public IP services - Training\|Readwise/Full Document Contents/Configure public IP services - Training.md]]

## Highlights
Public networks like the Internet communicate by using public IP addresses. Private networks like your Azure Virtual Network use private IP addresses, which aren't routable on public networks. To support a network that exists both in Azure and on-premises, you must configure IP addressing for both types of networks. ([View Highlight] (https://read.readwise.io/read/01hwvyt0nq6tkqeap0wkhzqnhm))


Public IP addresses enable Internet resources to communicate with Azure resources and enable Azure resources to communicate outbound with Internet and public-facing Azure services. A public IP address in Azure is dedicated to a specific resource, until it's unassigned by a network engineer. A resource without a public IP assigned can communicate outbound through network address translation services, where Azure dynamically assigns an available IP address that isn't dedicated to the resource. ([View Highlight] (https://read.readwise.io/read/01hwvyv3rj2fggpgmgn1wdcbgz))


Public IP address **Standard** **Basic** Allocation method Static For IPv4: Dynamic or Static; For IPv6: Dynamic. Idle Timeout Have an adjustable inbound originated flow idle timeout of 4-30 minutes, with a default of 4 minutes, and fixed outbound originated flow idle timeout of 4 minutes. Have an adjustable inbound originated flow idle timeout of 4-30 minutes, with a default of 4 minutes, and fixed outbound originated flow idle timeout of 4 minutes. Security Secure by default model and be closed to inbound traffic when used as a frontend. Allow traffic with network security group (NSG) is required (for example, on the NIC of a virtual machine with a Standard SKU Public IP attached). Open by default. Network security groups are recommended but optional for restricting inbound or outbound traffic Availability zones Supported. Standard IPs can be non-zonal, zonal, or zone-redundant. Zone redundant IPs can only be created in regions where 3 availability zones are live. IPs created before zones are live won't be zone redundant. Not supported. Routing preference Supported to enable more granular control of how traffic is routed between Azure and the Internet. Not supported. Global tier Supported via cross-region load balancers. Not supported. ([View Highlight] (https://read.readwise.io/read/01hwvz353wgg630nvk6d6kkbre))



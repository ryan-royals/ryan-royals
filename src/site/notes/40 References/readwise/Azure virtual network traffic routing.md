---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-virtual-network-traffic-routing/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_mbgC5tW.png)

## Summary

Learn how Azure routes virtual network traffic, and how you can customize Azure's routing.

## Highlights

System routes
Azure automatically creates system routes and assigns the routes to each subnet in a virtual network. You can't create system routes, nor can you remove system routes, but you can override some system routes with [custom routes](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#custom-routes). Azure creates default system routes for each subnet, and adds more [optional default routes](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#optional-default-routes) to specific subnets, or every subnet, when you use specific Azure capabilities.
[](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#default)Default
Each route contains an address prefix and next hop type. When traffic leaving a subnet is sent to an IP address within the address prefix of a route, the route that contains the prefix is the route Azure uses. Learn more about [how Azure selects a route](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#how-azure-selects-a-route) when multiple routes contain the same prefixes, or overlapping prefixes. Whenever a virtual network is created, Azure automatically creates the following default system routes for each subnet within the virtual network:
Source
Address prefixes
Next hop type
Default
Unique to the virtual network
Virtual network
Default
0.0.0.0/0
Internet
Default
10.0.0.0/8
None
Default
172.16.0.0/12
None
Default
192.168.0.0/16
None
Default
100.64.0.0/10
None ([View Highlight] (https://read.readwise.io/read/01h4m7yh3ahxc4dnpb6qpnkbf0))


**Virtual network**: Routes traffic between address ranges within the [address space](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview/manage-virtual-network#add-or-remove-an-address-range) of a virtual network. Azure creates a route with an address prefix that corresponds to each address range defined within the address space of a virtual network. If the virtual network address space has multiple address ranges defined, Azure creates an individual route for each address range. Azure automatically routes traffic between subnets using the routes created for each address range. You don't need to define gateways for Azure to route traffic between subnets. Though a virtual network contains subnets, and each subnet has a defined address range, Azure doesn't create default routes for subnet address ranges. Each subnet address range is within an address range of the address space of a virtual network. ([View Highlight] (https://read.readwise.io/read/01h6tcd29ybc2qyrgr1hzq84n0))


Optional default routes
Azure adds more default system routes for different Azure capabilities, but only if you enable the capabilities. Depending on the capability, Azure adds optional default routes to either specific subnets within the virtual network, or to all subnets within a virtual network. The other system routes and next hop types that Azure may add when you enable different capabilities are:
Source
Address prefixes
Next hop type
Subnet within virtual network that route is added to
Default
Unique to the virtual network, for example: 10.1.0.0/16
VNet peering
All
Virtual network gateway
Prefixes advertised from on-premises via BGP, or configured in the local network gateway
Virtual network gateway
All
Default
Multiple
VirtualNetworkServiceEndpoint
Only the subnet a service endpoint is enabled for. ([View Highlight] (https://read.readwise.io/read/01h8mwg8xg30grp6587jtztwtt))



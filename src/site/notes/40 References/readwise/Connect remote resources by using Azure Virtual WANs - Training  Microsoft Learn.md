---
{"dg-publish":true,"permalink":"/40-references/readwise/connect-remote-resources-by-using-azure-virtual-wa-ns-training-microsoft-learn/","tags":["rw/articles"]}
---


![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

  

URL: <https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/6-connect-remote-resources-by-using-azure-virtual-wans>  
Author: wwlpublish

## Summary

Azure Virtual WAN is a networking service that connects resources for distributed workforces. It combines various networking features like VPNs and routing functionalities. Virtual hubs play a key role in connecting different networks and enabling secure communication.

## Highlights Added July 17, 2024 at 11:02 AM

> What is Azure Virtual WAN?  
> Azure Virtual WAN is a networking service that brings many networking, security, and routing functionalities together to provide a single operational interface. Some of the main features include:  
> • Branch connectivity (via connectivity automation from Virtual WAN Partner devices such as SD-WAN or VPN CPE).  
> • Site-to-site VPN connectivity.  
> • Remote user VPN connectivity (point-to-site).  
> • Private connectivity (ExpressRoute).  
> • Intra-cloud connectivity (transitive connectivity for virtual networks).  
> • VPN ExpressRoute inter-connectivity.  
> • Routing, Azure Firewall, and encryption for private connectivity.  
> The following diagram shows an organization with two Virtual WAN hubs connecting the spokes. VNets, Site-to-site and point-to-site VPNs, SD WANs, and ExpressRoute connectivity are all supported.  
> ![Azure Virtual WAN with two regional hubs, several VNets, and multiple remote connections including Site-to-Site VPN, Point-to-Site VPN, and ExpressRoute.](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/6-connect-remote-resources-by-using-azure-virtual-wans/../../wwl-azure/design-implement-hybrid-networking/media/azure-wan-regions-a420bb18.png)  
> To configure an end-to-end virtual WAN, you create the following resources:  
> • **Virtual WAN**  
> • **Hub**  
> • **Hub virtual network connection**  
> • **Hub-to-hub connection**  
> • **Hub route table** ([View Highlight] (<https://read.readwise.io/read/01hxxaa7hrf68cvvpjz23pkwx7>))

> A virtual hub is a Microsoft-managed virtual network. ([View Highlight] (<https://read.readwise.io/read/01hy4ksc8rptqg8h5kkecras37>))

> The minimum address space is /24 to create a hub. ([View Highlight] (<https://read.readwise.io/read/01hy4ksk9swgpabc5y2ep32xny>))

> You don't need to explicitly plan the subnet address space for the services in the virtual hub. Because Azure Virtual WAN is a managed service, it creates the appropriate subnets in the virtual hub for the different gateways/services (for example, VPN gateways, ExpressRoute gateways, User VPN point-to-site gateways, Firewall, routing, etc.). ([View Highlight] (<https://read.readwise.io/read/01hy4ksv3chpecqm2dht8st5az>))

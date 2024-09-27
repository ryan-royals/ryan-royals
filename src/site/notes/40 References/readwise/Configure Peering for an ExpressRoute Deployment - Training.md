---
{"dg-publish":true,"permalink":"/40-references/readwise/configure-peering-for-an-express-route-deployment-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)
  
URL: https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/6-configure-peering-for-expressroute-deployment
Author: wwlpublish

## Summary

This text explains how to configure peering for an Azure ExpressRoute deployment, focusing on private and Microsoft peering options. Each peering must be set up individually on an active ExpressRoute circuit, allowing connectivity to virtual networks or Microsoft services. Route filters can be used to manage the services accessed through Microsoft peering, reducing the size of route tables.

## Highlights added August 30, 2024 at 2:23 PM
>Azure compute services, namely virtual machines (IaaS) and cloud services (PaaS), that are deployed within a virtual network can be connected through the private peering domain. The private peering domain is a trusted extension of your core network into Microsoft Azure. You can set up bi-directional connectivity between your core network and Azure virtual networks (VNets). This peering lets you connect to virtual machines and cloud services directly on their private IP addresses. ([View Highlight] (https://read.readwise.io/read/01j3bvadzzrrm92mdpkxqrd0q9))


>Connectivity to Microsoft online services (Microsoft 365 and Azure PaaS services) occurs through Microsoft peering. You can enable bidirectional connectivity between your WAN and Microsoft cloud services through the Microsoft peering routing domain. You must connect to Microsoft cloud services only over public IP addresses that are owned by you or your connectivity provider and you must adhere to all the defined rules. ([View Highlight] (https://read.readwise.io/read/01j3bvaqntka66zfm511rg2f5g))


>When Microsoft peering gets configured on your ExpressRoute circuit, the Microsoft Edge routers establish a pair of BGP sessions with your edge routers through your connectivity provider. No routes are advertised to your network. To enable route advertisements to your network, you must associate a route filter.
>A route filter lets you identify services you want to consume through your ExpressRoute circuit's Microsoft peering. It is essentially an allowed list of all the BGP community values. Once a route filter resource gets defined and attached to an ExpressRoute circuit, all prefixes that map to the BGP community values gets advertised to your network.
>To attach route filters with Microsoft 365 services, you must have authorization to consume Microsoft 365 services through ExpressRoute. If you are not authorized to consume Microsoft 365 services through ExpressRoute, the operation to attach route filters fails. ([View Highlight] (https://read.readwise.io/read/01j3bvzqwa2a1sysf4pyj5fcht))



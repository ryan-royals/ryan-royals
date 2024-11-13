---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-azure-route-server/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

Learn how Azure Route Server can simplify routing between your network virtual appliance (NVA) and your virtual network.

## Highlights

Azure Route Server simplifies dynamic routing between your network virtual appliance (NVA) and your virtual network. It allows you to exchange routing information directly through Border Gateway Protocol (BGP) routing protocol between any NVA that supports the BGP routing protocol and the Azure Software Defined Network (SDN) in the Azure Virtual Network (VNet) without the need to manually configure or maintain route tables. Azure Route Server is a fully managed service and is configured with high availability. ([View Highlight] (https://read.readwise.io/read/01h9fv4e39ce7dtx1r6ehnf7xe))


[](https://learn.microsoft.com/en-us/azure/route-server/overview#key-benefits)Key benefits
Azure Route Server simplifies configuration, management, and deployment of your NVA in your virtual network.
• You no longer need to manually update the routing table on your NVA whenever your virtual network addresses are updated.
• You no longer need to update [User-Defined Routes](https://learn.microsoft.com/en-us/azure/route-server/overview/../virtual-network/virtual-networks-udr-overview) manually whenever your NVA announces new routes or withdraw old ones.
• You can peer multiple instances of your NVA with Azure Route Server. You can configure the BGP attributes in your NVA and, depending on your design (for example, active-active for performance or active-passive for resiliency), let Azure Route Server know which NVA instance is active or which one is passive.
• The interface between NVA and Azure Route Server is based on a common standard protocol. As long as your NVA supports BGP, you can peer it with Azure Route Server. For more information, see [Route Server supported routing protocols](https://learn.microsoft.com/en-us/azure/route-server/overview/route-server-faq#protocol).
• You can deploy Azure Route Server in any of your new or existing virtual network. ([View Highlight] (https://read.readwise.io/read/01h9fv58txj0tsph9592rt2v2v))



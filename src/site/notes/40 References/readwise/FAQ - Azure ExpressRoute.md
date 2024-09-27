---
{"dg-publish":true,"permalink":"/40-references/readwise/faq-azure-express-route/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)
  
URL: https://learn.microsoft.com/en-us/azure/expressroute/expressroute-faqs#what-is-expressroute-local
Author: duongau

## Summary

ExpressRoute is an Azure service for creating private connections between Microsoft datacenters and on-premises infrastructure. Using ExpressRoute can lead to cost savings compared to transferring data over the public Internet. You can have multiple ExpressRoute circuits with different service providers to increase connectivity options.

## Highlights added August 30, 2024 at 2:23 PM
>ExpressRoute premium is a collection of the following features:
>• Increased routing table limit from 4000 routes to 10,000 routes for private peering.
>• Increased number of VNets and ExpressRoute Global Reach connections that can be enabled on an ExpressRoute circuit (default is 10). For more information, see the [ExpressRoute Limits](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-faqs#limits) table.
>• Connectivity to Microsoft 365
>• Global connectivity over the Microsoft core network. You can now link a VNet in one geopolitical region with an ExpressRoute circuit in another region. 
>**Examples:**
>• You can link a VNet created in Europe West to an ExpressRoute circuit created in Silicon Valley.
>• On the Microsoft peering, prefixes from other geopolitical regions are advertised such that you can connect to, for example, SQL Azure in Europe West from a circuit in Silicon Valley. ([View Highlight] (https://read.readwise.io/read/01j31hy2rmjy24kkz4y2sf8r4z))


>ExpressRoute Local is a SKU of ExpressRoute circuit, in addition to the Standard SKU and the Premium SKU. A key feature of Local is that a Local circuit at an ExpressRoute peering location gives you access only to one or two Azure regions in or near the same metro. In contrast, a Standard circuit gives you access to all Azure regions in a geopolitical area and a Premium circuit to all Azure regions globally. Specifically, with a Local SKU you can only advertise routes over Microsoft and private peering from the corresponding local region of the ExpressRoute circuit. You won't receive routes for other regions different than the defined local region. ([View Highlight] (https://read.readwise.io/read/01j31hb7c9vt7drqa085ey4g07))


>While you need to pay egress data transfer for your Standard or Premium ExpressRoute circuit, you don't pay egress data transfer separately for your ExpressRoute Local circuit. In other words, the price of ExpressRoute Local includes data transfer fees. ExpressRoute Local is an economical solution if you have massive amount of data to transfer and want to have your data over a private connection to an ExpressRoute peering location near your desired Azure regions. ([View Highlight] (https://read.readwise.io/read/01j31hft44hnbdxqkp7p310n0q))



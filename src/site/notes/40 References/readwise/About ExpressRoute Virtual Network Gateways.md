---
{"dg-publish":true,"permalink":"/40-references/readwise/about-express-route-virtual-network-gateways/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

To connect your Azure virtual network to your on-premises network with ExpressRoute, you need to create a virtual network gateway that exchanges IP routes and routes traffic. There are different types of gateways and SKUs, with higher SKUs providing better performance and capacity. Additionally, you must create a gateway subnet for the gateway VMs, and you can enable features like FastPath for improved traffic handling.

## Highlights

Gateway SKU VPN Gateway and ExpressRoute coexistence FastPath Max Number of Circuit Connections **Standard SKU/ERGw1Az** Yes No 4 **High Perf SKU/ERGw2Az** Yes No 8 **Ultra Performance SKU/ErGw3Az** Yes Yes 16 **ErGwScale (Preview)** Yes Yes - minimum 10 of scale units 4 - minimum 1 of scale unit 
8 - minimum of 2 scale units 
16 - minimum of 10 scale units ([View Highlight] (https://read.readwise.io/read/01jcc4ehnpcgs79p5mfr769vsd))



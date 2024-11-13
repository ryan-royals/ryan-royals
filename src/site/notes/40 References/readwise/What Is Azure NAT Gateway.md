---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-azure-nat-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

Overview of Azure NAT Gateway features, resources, architecture, and implementation. Learn how Azure NAT Gateway works and how to use NAT gateway resources in Azure.

## Highlights

Azure NAT Gateway is a fully managed and highly resilient Network Address Translation (NAT) service. You can use Azure NAT Gateway to let all instances in a private subnet connect outbound to the internet while remaining fully private. Unsolicited inbound connections from the internet aren't permitted through a NAT gateway. Only packets arriving as response packets to an outbound connection can pass through a NAT gateway.
NAT Gateway provides dynamic SNAT port functionality to automatically scale outbound connectivity and reduce the risk of SNAT port exhaustion. ([View Highlight] (https://read.readwise.io/read/01h9fwryafshg9wsnnjh9c6tj0))


NAT gateway replaces a subnet’s default route to the internet when configured. All traffic within the 0.0.0.0/0 prefix has a next hop type to NAT gateway before connecting outbound to the internet. ([View Highlight] (https://read.readwise.io/read/01h9fwsyvq7f9sdztywz09ma08))


You can override NAT gateway as a subnet’s next hop to the internet with the creation of a custom user-defined route (UDR). ([View Highlight] (https://read.readwise.io/read/01h9fwvvkk7krjsk2ssbfq7j41))


Presence of custom UDRs for virtual appliances and ExpressRoute override NAT gateway for directing internet bound traffic (route to the 0.0.0.0/0 address prefix). ([View Highlight] (https://read.readwise.io/read/01h9fwvqdw1mthvntsfw1x1gap))



---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-a-private-endpoint-azure-private-link/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

## Full Document
[[40 References/readwise/Full Document Contents/What is a private endpoint - Azure Private Link\|Readwise/Full Document Contents/What is a private endpoint - Azure Private Link.md]]

## Highlights
A private endpoint is a network interface that uses a private IP address from your virtual network. This network interface connects you privately and securely to a service that's powered by Azure Private Link. ([View Highlight] (https://read.readwise.io/read/01h06jsfbnf0tjfs9v6afk5pbe))


• Azure Storage
• Azure Cosmos DB
• Azure SQL Database
• Your own service, using [Private Link service](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview/private-link-service-overview). ([View Highlight] (https://read.readwise.io/read/01h06jx5s5tppmr62nr65qhde9))


Private endpoints enable connectivity between the customers from the same:
• Virtual network
• Regionally peered virtual networks
• Globally peered virtual networks
• On-premises environments that use [VPN](https://azure.microsoft.com/services/vpn-gateway/) or [Express Route](https://azure.microsoft.com/services/expressroute/)
• Services that are powered by Private Link ([View Highlight] (https://read.readwise.io/read/01h06mcpmc0ghjy82yqth2cas8))


The private endpoint must be deployed in the same region and subscription as the virtual network. ([View Highlight] (https://read.readwise.io/read/01h06mcv8sp1x1batk81t8tqa6))


Multiple private endpoints can be created with the same private-link resource. For a single network using a common DNS server configuration, the recommended practice is to use a single private endpoint for a specified private-link resource. Use this practice to avoid duplicate entries or conflicts in DNS resolution. ([View Highlight] (https://read.readwise.io/read/01h06md5mdxvhcwghk7rsvdty6))


To connect to the same service over private endpoint, separate DNS settings, often configured via private DNS zones, are required ([View Highlight] (https://read.readwise.io/read/01h06measpnxx396p1qhamxzm9))



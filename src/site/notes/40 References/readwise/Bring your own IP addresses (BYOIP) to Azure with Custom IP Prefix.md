---
{"dg-publish":true,"permalink":"/40-references/readwise/bring-your-own-ip-addresses-byoip-to-azure-with-custom-ip-prefix/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2022/03/f216b134-24a6-4a59-bb9a-5e276aa67e77.webp)

## Full Document
[[40 References/readwise/Full Document Contents/Bring your own IP addresses (BYOIP) to Azure with Custom IP Prefix\|Readwise/Full Document Contents/Bring your own IP addresses (BYOIP) to Azure with Custom IP Prefix.md]]

## Highlights
Using the [Custom IP Prefix resource](https://docs.microsoft.com/azure/virtual-network/ip-services/custom-ip-address-prefix), you can now bring your own public IPv4 ranges to Azure and use them like any other Azure-owned public IP ranges. Once onboarded, these IPs can be associated with Azure resources, interact with private IPs and VNETs within Azure’s network, and reach external destinations by egressing from Microsoft’s Wide Area Network. ([View Highlight] (https://read.readwise.io/read/01hwvzwh578rhtf0p2neh3new7))


In order to bring a public IP range to use on Azure, you must own and have registered the range with a Routing Internet Registry such as [ARIN](https://www.arin.net/) or [RIPE](https://www.ripe.net/). ([View Highlight] (https://read.readwise.io/read/01hww01zksvey4wq80drje24e5))


Key takeaways
• The ability to bring your own IP addresses (BYOIP) to Azure is currently available in all regions.
• The minimum size of an onboarded range is /24 (256 IP addresses).
• Onboarded IPs are put in a Custom IP Prefix resource for management, from which Public IP Prefixes can be derived and utilized across subscriptions.
• You are not charged for the hosting or management of onboarded ranges brought to Azure. ([View Highlight] (https://read.readwise.io/read/01hwvzypt86bjhqh3h59f9tp9e))



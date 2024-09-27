---
{"dg-publish":true,"permalink":"/40-references/readwise/what-is-a-virtual-network-link-subresource-of-azure-dns-private-zones/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)
  
URL: https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links
Author: greg-lindsay

## Summary

After creating a private DNS zone in Azure, you can link a virtual network to it so that VMs in the network can access the DNS zone. The virtual network can be linked as a registration or resolution network, affecting how DNS records are managed. There are limits and considerations to keep in mind when linking virtual networks to private DNS zones in Azure.

## Highlights added August 30, 2024 at 2:23 PM
>When [creating a link](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links/private-dns-getstarted-portal#link-the-virtual-network) between a private DNS zone and a virtual network. You have the option to enable [autoregistration](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links/private-dns-autoregistration). With this setting enabled, the virtual network becomes a registration virtual network for the private DNS zone. A DNS record gets automatically created for any virtual machines you deploy in the virtual network. DNS records will also be created for virtual machines already deployed in the virtual network. ([View Highlight] (https://read.readwise.io/read/01hww1ws7r16prxw1jxk1b3a0f))



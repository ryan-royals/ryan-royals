---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-firewall-faq/","tags":["rw/articles"]}
---

# Azure Firewall FAQ

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)
  
URL: https://learn.microsoft.com/en-us/azure/firewall/firewall-faq?WT.mc_id=Portal-Microsoft_Azure_Health#is-forced-tunneling-chaining-to-a-network-virtual-appliance-supported
Author: vhorne

## Summary

FAQ for Azure Firewall. A managed, cloud-based network security service that protects your Azure Virtual Network resources.

## Highlights added July 17, 2024 at 10:55 AM
>Is forced tunneling/chaining to a Network Virtual Appliance supported?
>Forced tunneling is supported when you create a new firewall. You can't configure an existing firewall for forced tunneling. For more information, see [Azure Firewall forced tunneling](https://learn.microsoft.com/en-us/azure/firewall/firewall-faq?WT.mc_id=Portal-Microsoft_Azure_Health/forced-tunneling).
>Azure Firewall must have direct Internet connectivity. If your AzureFirewallSubnet learns a default route to your on-premises network via BGP, you must override this with a 0.0.0.0/0 UDR with the **NextHopType** value set as **Internet** to maintain direct Internet connectivity.
>If your configuration requires forced tunneling to an on-premises network and you can determine the target IP prefixes for your Internet destinations, you can configure these ranges with the on-premises network as the next hop via a user defined route on the AzureFirewallSubnet. Or, you can use BGP to define these routes. ([View Highlight] (https://read.readwise.io/read/01hce39d2nngg5anew869j1wew))



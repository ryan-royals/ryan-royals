---
{"dg-publish":true,"permalink":"/40-references/readwise/single-region-scenario-private-link-and-dns-in-azure-virtual-wan-azure-architecture-center/","tags":["rw/articles"]}
---

![40 References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg](/img/user/40%20References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/azure/architecture/guide/networking/private-link-virtual-wan-dns-single-region-workload
Author: robbag

## Summary

This article provides guidance on implementing DNS to support private endpoints in a Virtual WAN network in a single region where the virtual hub has a Firewall with DNS Proxy enabled. The solution includes implementing a virtual WAN hub extension for DNS.

## Highlights added August 30, 2024 at 2:23 PM
>Successful outcome
>The Azure Virtual Machine client can connect to the Azure Storage account via the storage account's private endpoint that is in the same virtual network, and all other access to the storage account is blocked. ([View Highlight] (https://read.readwise.io/read/01h06jkw0kc9jjjtfp3ebgef49))


>It isn't possible to link a private DNS zone that maintains the storage accounts necessary DNS records to a virtual hub. ([View Highlight] (https://read.readwise.io/read/01h06jm48mx94805x3gn1xswmy))


>You can link a private DNS zone to the workload network, so you might think that would work. Unfortunately, the [baseline architecture](https://learn.microsoft.com/en-us/azure/architecture/guide/networking/private-link-virtual-wan-dns-guide#starting-network-topology) stipulates that each connected virtual network has DNS servers configured to point to use the Azure Firewall DNS proxy. ([View Highlight] (https://read.readwise.io/read/01h06jmc30v2x8rcx54p2e99wj))


>Solution - Establish a virtual hub extension for DNS ([View Highlight] (https://read.readwise.io/read/01h06jmkrcwrfjmskw9qncfqf7))


>he DNS extension is implemented as a virtual network spoke that is peered to its regional virtual hub. It's possible to link private DNS zones to this virtual network ([View Highlight] (https://read.readwise.io/read/01h06jn2h5qv406hcfg2bqntqy))



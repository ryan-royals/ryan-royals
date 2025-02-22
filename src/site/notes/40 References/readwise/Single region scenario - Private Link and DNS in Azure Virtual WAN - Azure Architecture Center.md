---
{"dg-publish":true,"permalink":"/40-references/readwise/single-region-scenario-private-link-and-dns-in-azure-virtual-wan-azure-architecture-center/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_7lYYhOX.png)

## Full Document
[[40 References/readwise/Full Document Contents/Single region scenario - Private Link and DNS in Azure Virtual WAN - Azure Architecture Center\|Readwise/Full Document Contents/Single region scenario - Private Link and DNS in Azure Virtual WAN - Azure Architecture Center.md]]

## Highlights
Successful outcome
The Azure Virtual Machine client can connect to the Azure Storage account via the storage account's private endpoint that is in the same virtual network, and all other access to the storage account is blocked. ([View Highlight] (https://read.readwise.io/read/01h06jkw0kc9jjjtfp3ebgef49))


It isn't possible to link a private DNS zone that maintains the storage accounts necessary DNS records to a virtual hub. ([View Highlight] (https://read.readwise.io/read/01h06jm48mx94805x3gn1xswmy))


You can link a private DNS zone to the workload network, so you might think that would work. Unfortunately, the [baseline architecture](https://learn.microsoft.com/en-us/azure/architecture/guide/networking/private-link-virtual-wan-dns-guide#starting-network-topology) stipulates that each connected virtual network has DNS servers configured to point to use the Azure Firewall DNS proxy. ([View Highlight] (https://read.readwise.io/read/01h06jmc30v2x8rcx54p2e99wj))


Solution - Establish a virtual hub extension for DNS ([View Highlight] (https://read.readwise.io/read/01h06jmkrcwrfjmskw9qncfqf7))


he DNS extension is implemented as a virtual network spoke that is peered to its regional virtual hub. It's possible to link private DNS zones to this virtual network ([View Highlight] (https://read.readwise.io/read/01h06jn2h5qv406hcfg2bqntqy))



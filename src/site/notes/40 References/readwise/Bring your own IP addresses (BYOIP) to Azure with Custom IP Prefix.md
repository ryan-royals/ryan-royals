---
{"dg-publish":true,"permalink":"/40-references/readwise/bring-your-own-ip-addresses-byoip-to-azure-with-custom-ip-prefix/","tags":["rw/articles"]}
---

![40 References/attachments/8021582c92835a9f22bce018664f0554_MD5.webp](/img/user/40%20References/attachments/8021582c92835a9f22bce018664f0554_MD5.webp)
  
URL: https://azure.microsoft.com/en-us/blog/bring-your-own-ip-addresses-byoip-to-azure-with-custom-ip-prefix/
Author: Brian Lehr

## Summary

You can now bring your own public IP addresses to Azure using the Custom IP Prefix resource. This feature allows you to retain existing IP addresses and integrate them with Azure resources. Onboarding IP ranges can be done through various methods, and you are not charged for hosting the onboarded IP addresses.

## Highlights added August 30, 2024 at 2:23 PM
>Using the [Custom IP Prefix resource](https://docs.microsoft.com/azure/virtual-network/ip-services/custom-ip-address-prefix), you can now bring your own public IPv4 ranges to Azure and use them like any other Azure-owned public IP ranges. Once onboarded, these IPs can be associated with Azure resources, interact with private IPs and VNETs within Azure’s network, and reach external destinations by egressing from Microsoft’s Wide Area Network. ([View Highlight] (https://read.readwise.io/read/01hwvzwh578rhtf0p2neh3new7))


>In order to bring a public IP range to use on Azure, you must own and have registered the range with a Routing Internet Registry such as [ARIN](https://www.arin.net/) or [RIPE](https://www.ripe.net/). ([View Highlight] (https://read.readwise.io/read/01hww01zksvey4wq80drje24e5))


>Key takeaways
>• The ability to bring your own IP addresses (BYOIP) to Azure is currently available in all regions.
>• The minimum size of an onboarded range is /24 (256 IP addresses).
>• Onboarded IPs are put in a Custom IP Prefix resource for management, from which Public IP Prefixes can be derived and utilized across subscriptions.
>• You are not charged for the hosting or management of onboarded ranges brought to Azure. ([View Highlight] (https://read.readwise.io/read/01hwvzypt86bjhqh3h59f9tp9e))



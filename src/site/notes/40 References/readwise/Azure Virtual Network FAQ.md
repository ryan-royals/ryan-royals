---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-virtual-network-faq/","tags":["rw/articles"]}
---

![40 References/attachments/44982d0c5c08e08c8a1df2cdfefe5013_MD5.jpg](/img/user/40%20References/attachments/44982d0c5c08e08c8a1df2cdfefe5013_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-faq#are-there-any-restrictions-on-using-ip-addresses-within-these-subnets
Author: custom roles

## Summary

Answers to the most frequently asked questions about Microsoft Azure virtual networks.

## Highlights added August 30, 2024 at 2:23 PM
>Yes. Azure reserves the first four and last IP address for a total of 5 IP addresses within each subnet.
>For example, the IP address range of 192.168.1.0/24 has the following reserved addresses:
>• 192.168.1.0 : Network address
>• 192.168.1.1 : Reserved by Azure for the default gateway
>• 192.168.1.2, 192.168.1.3 : Reserved by Azure to map the Azure DNS IPs to the VNet space
>• 192.168.1.255 : Network broadcast address. ([View Highlight] (https://read.readwise.io/read/01h83171ffk4y7frd117bzwk55))



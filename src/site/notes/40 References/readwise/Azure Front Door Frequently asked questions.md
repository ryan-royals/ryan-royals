---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-front-door-frequently-asked-questions/","tags":["rw/articles"]}
---

![40 References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg](/img/user/40%20References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/faq
Author: duongau

## Summary

This page provides answers to frequently asked questions about Azure Front Door Standard/Premium.

## Highlights added August 30, 2024 at 2:23 PM
>[](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/faq#how-do-i-lock-down-the-access-to-my-backend-to-only-azure-front-door)How do I lock down the access to my backend to only Azure Front Door?
>The best way to lock down your application to accept traffic only from your specific Front Door instance is to publish your application via Private Endpoint. Network traffic between Front Door and the application traverses over the VNet and a Private Link on the Microsoft backbone network, eliminating exposure from the public internet.
>Learn more about the [securing origin for Front Door with Private Link](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/faq/../private-link).
>Alternative way to lock down your application to accept traffic only from your specific Front Door, you'll need to set up IP ACLs for your backend. Then restrict the traffic of your backend to the specific value of the header 'X-Azure-FDID' sent by Front Door. These steps are detailed out as below:
>• Configure IP ACLing for your backends to accept traffic from Azure Front Door's backend IP address space and Azure's infrastructure services only. Refer to the IP details below for ACLing your backend:
>• Refer *AzureFrontDoor.Backend* section in [Azure IP Ranges and Service Tags](https://www.microsoft.com/download/details.aspx?id=56519) for Front Door's backend IP address range. You can also use the service tag *AzureFrontDoor.Backend* in your [network security groups](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/faq/../../virtual-network/network-security-groups-overview#security-rules).
>• Azure's [basic infrastructure services](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/faq/../../virtual-network/network-security-groups-overview#azure-platform-considerations) through virtualized host IP addresses: `168.63.129.16` and `169.254.169.254`. ([View Highlight] (https://read.readwise.io/read/01h2s5n5c1k1xbdff9h1m2ms6r))


>• Do a GET operation on your Front Door with the API version `2020-01-01` or higher. In the API call, look for `frontdoorID` field. Filter on the incoming header '**X-Azure-FDID**' sent by Front Door to your backend with the value of the field `frontdoorID`. You can also find `Front Door ID` value under the Overview section from Front Door portal page.
>• Apply rule filtering in your backend web server to restrict traffic based on the resulting 'X-Azure-FDID' header value. ([View Highlight] (https://read.readwise.io/read/01h2w1q5kzz6tzk0p7neymnary))



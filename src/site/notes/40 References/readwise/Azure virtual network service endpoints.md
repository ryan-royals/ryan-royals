---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-virtual-network-service-endpoints/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)
  
URL: https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-service-endpoints-overview
Author: asudbring

## Summary

Learn how to enable direct access to Azure resources from a virtual network using service endpoints.

## Highlights added August 30, 2024 at 2:23 PM
>Virtual Network (VNet) service endpoint provides secure and direct connectivity to Azure services over an optimized route over the Azure backbone network ([View Highlight] (https://read.readwise.io/read/01h0eer4keb2kaax541418mkxf))


>Service endpoints are available for the following Azure services and regions. The *Microsoft.** resource is in parenthesis ([View Highlight] (https://read.readwise.io/read/01h0eermh873efqt6eq50xbep6))


>**mproved security for your Azure service resources**: VNet private address spaces can overlap. You can't use overlapping spaces to uniquely identify traffic that originates from your VNet. Service endpoints enable securing of Azure service resources to your virtual network by extending VNet identity to the service. Once you enable service endpoints in your virtual network, you can add a virtual network rule to secure the Azure service resources to your virtual network. The rule addition provides improved security by fully removing public internet access to resources and allowing traffic only from your virtual network. ([View Highlight] (https://read.readwise.io/read/01h0eet0zvywybdtyzp3x475m0))


>**Optimal routing for Azure service traffic from your virtual network**: Today, any routes in your virtual network that force internet traffic to your on-premises and/or virtual appliances also force Azure service traffic to take the same route as the internet traffic. Service endpoints provide optimal routing for Azure traffic.
>Endpoints always take service traffic directly from your virtual network to the service on the Microsoft Azure backbone network. Keeping traffic on the Azure backbone network allows you to continue auditing and monitoring outbound Internet traffic from your virtual networks, through forced-tunneling, without impacting service traffic. For more information about user-defined routes and forced-tunneling, see [Azure virtual network traffic routing](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview). ([View Highlight] (https://read.readwise.io/read/01h0eet6b611n58jxqqjv98hsf))


>**Simple to set up with less management overhead**: You no longer need reserved, public IP addresses in your virtual networks to secure Azure resources through IP firewall. There are no Network Address Translation (NAT) or gateway devices required to set up the service endpoints. You can configure service endpoints through a single selection on a subnet. There's no extra overhead to maintaining the endpoints. ([View Highlight] (https://read.readwise.io/read/01h0eet94w5fn1tjazd59evwx6))



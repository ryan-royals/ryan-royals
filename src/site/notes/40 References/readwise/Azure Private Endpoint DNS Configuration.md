---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-private-endpoint-dns-configuration/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)
  
URL: https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-dns
Author: asudbring

## Summary

Learn about Azure Private Endpoint DNS configuration.

## Highlights added August 30, 2024 at 2:23 PM
>It's important to correctly configure your DNS settings to resolve the private endpoint IP address to the fully qualified domain name (FQDN) of the connection string. ([View Highlight] (https://read.readwise.io/read/01h0efwbchgkh9gdka5xxf2p7g))


>You can use the following options to configure your DNS settings for private endpoints:
>• **Use the host file (only recommended for testing)**. You can use the host file on a virtual machine to override the DNS.
>• **Use a private DNS zone**. You can use [private DNS zones](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone) to override the DNS resolution for a private endpoint. A private DNS zone can be linked to your virtual network to resolve specific domains.
>• **Use your DNS forwarder (optional)**. You can use your DNS forwarder to override the DNS resolution for a private link resource. Create a DNS forwarding rule to use a private DNS zone on your [DNS server](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances#name-resolution-that-uses-your-own-dns-server) hosted in a virtual network. ([View Highlight] (https://read.readwise.io/read/01h0efwj1r8h528phw0j92667v))



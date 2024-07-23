---
{"dg-publish":true,"permalink":"/40-references/readwise/add-custom-dns-servers-and-set-azure-point-to-site-vpn-to-connect-automatically/","tags":["rw/articles"]}
---


![rw-book-cover](https://luke.geek.nz/images/iazure-marketplace-banner.png)

  

URL: <https://luke.geek.nz/azure/add-custom-dns-servers-and-set-azure-point-to-site-vpn-to-connect-automatically/>  
Author: Luke Murray

## Summary

The Azure Point to Site VPN will take the DNS servers from the Virtual Network, that the Gateway is peering into by default, but due to VNET Peering or custom configuration if you may want to point this to custom DNS servers.

## Highlights Added July 17, 2024 at 11:02 AM

> <name>Luke's Azure Point to Site VPN</name> <clientconfig> <!-- need to specify always on = true for the VPN to connect automatically --> <AlwaysOn>true</AlwaysOn> <!-- Add custom DNS Servers --> <dnsservers> <dnsserver>10.100.1.1</dnsserver> <dnsserver>10.100.1.2</dnsserver> </dnsservers> <!-- Add custom DNS suffixes --> <dnssuffixes> <dnssuffix>.luke.geek.nz</dnssuffix> </dnssuffixes> </clientconfig> ([View Highlight] (<https://read.readwise.io/read/01h2f9p5qkbg54wax21bjcwpbn>))

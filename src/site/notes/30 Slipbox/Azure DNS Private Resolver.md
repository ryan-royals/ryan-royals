---
{"dg-publish":true,"dg-path":"Azure DNS Private Resolver.md","permalink":"/Azure DNS Private Resolver/","tags":["notes"]}
---


## Azure DNS Private Resolver

### Overview

Azure DNS Private Resolver is used to communicate with [[30 Slipbox/Azure Private DNS Zone\|Azure Private DNS Zone]] and the [[30 Slipbox/Azure Magic IP\|Azure Magic IP]] without managing a virtual machine on the network.

Azure Private DNS Resolver is used to act as a Conditional Forwarder for DNS traffic on a Virtual Network. It is costed in a way to that it replaces having redundant Virtual Machines.

### Requirements

#### Subnet

| Configuration                  | Valid Inputs                   |
| ------------------------------ | ------------------------------ |
| Address Space                  | /24 - /28                      |
| Delegation                     | Microsoft.Network/dnsResolvers |
| Share Vnet?                    | No                             |
| Share Subnet?                  | No                             |
| Ipv6?                          | No                             |
| ExpressRoute FastPath support? | No                             |

### Use Azure DNS Private Resolver over Azure VPN


<div class="transclusion internal-embed is-loaded"><div class="markdown-embed">



### Overview

In order to access the Private DNS Resolver over a VPN connection, the `azurevpnconfig.xml` file supplied by the Virtual Network Gateway needs to be modified to include:

```XML
<clientconfig>
<!-- need to specify always on = true for the VPN to connect automatically -->
<AlwaysOn>false</AlwaysOn>
<!-- Add custom DNS Servers -->
        <dnsservers>
            <dnsserver>*IP Address from DNS Resolver*</dnsserver>
        </dnsservers>
<!-- Add custom DNS suffixes -->
        <dnssuffixes>
        <!-- <dnssuffix>.azurecr.io</dnssuffix> -->
    </dnssuffixes>
</clientconfig>
```

Note that when testing the VPN, you *will not* be able to `NSLookup` any DNS records due to the way the application interacts with the Windows network stack. Pinging the destination address will respond with the correct IP.


</div></div>


---
created: 2023-05-02
modified: 2023-08-22
tags: pkm
---

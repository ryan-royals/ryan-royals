---
{"dg-publish":true,"permalink":"/90-slipbox/azure-dns-private-resolver/","tags":["notes"]}
---

Azure DNS Private Resolver is used to communicate with [[90_slipbox/Azure Private DNS Zone\|Azure Private DNS Zone]] and the [[90_slipbox/Azure Magic IP\|Azure Magic IP]] without managing a virtual machine on the network.

Azure Private DNS Resolver is used to act as a Conditional Forwarder for DNS traffic on a Virtual Network. It is costed in a way to that it replaces having redundant Virtual Machines.

## Quick Tips

- You are charged for any and all associated inbound and outbound resolvers, even if the outbound resolver has no rules on it (and is doing nothing)

## Use Azure DNS Private Resolver over Azure VPN


<div class="transclusion internal-embed is-loaded"><a class="markdown-embed-link" href="/90-slipbox/use-azure-dns-private-resolver-over-azure-vpn/" aria-label="Open link"><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="svg-icon lucide-link"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"></path><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"></path></svg></a><div class="markdown-embed">





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


## Requirements

### Subnet

| Configuration                  | Valid Inputs                   |
| ------------------------------ | ------------------------------ |
| Address Space                  | /24 - /28                      |
| Delegation                     | Microsoft.Network/dnsResolvers |
| Share Vnet?                    | No                             |
| Share Subnet?                  | No                             |
| Ipv6?                          | No                             |
| ExpressRoute FastPath support? | No                             |

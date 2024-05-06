---
{"dg-publish":true,"dg-path":"Use Azure DNS Private Resolver over Azure VPN.md","permalink":"/use-azure-dns-private-resolver-over-azure-vpn/","tags":["notes"]}
---


## Use Azure DNS Private Resolver over Azure VPN

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

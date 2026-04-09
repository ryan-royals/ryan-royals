---
{"dg-publish":true,"permalink":"/90-slipbox/use-azure-dns-private-resolver-over-azure-vpn/","tags":["notes"],"created":"2025-06-11T10:28:48.743+09:30","updated":"2026-03-03T09:55:32.064+10:30","dg-note-properties":{"created":"2023-06-14","modified":"2026-03-03","tags":"notes","related":["[[Azure DNS Private Resolver]]","[[Azure Private DNS Zone]]","[[Azure Virtual Network Gateway]]"],"references":null}}
---


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

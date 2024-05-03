---
{"dg-publish":true,"dg-path":"Azure VPN Gateway.md","permalink":"/azure-vpn-gateway/","tags":["notes"]}
---


## Azure VPN Gateway

### Overview

Azure VPN Gateway is used to create a [[Virtual Private Network\|Virtual Private Network]] connections as either Point-to-Site, Site-to-Site or Vnet-to-Vnet. to a [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]]  
Azure VPN Gateway is a type of Virtual Network Gateway

### Use Azure Private DNS Resolver over VPN


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


### Troubleshooting

#### Cant Route to Spoke from P2S

- General steps:
  - Check that the DNS Private Resolver is added to the VPN config
- If using a Azure Firewall and Forced Tunnelling:
  - Check that the routes for the VPN range on the spokes, not just a 0.0.0.0/0.
  - Check that the AzureFirewallSubnet has routes that route the subnet ranges to the Virtual Network Gateway.
  - Check that the VNG advertises the routes for the spokes.
  - Check that the Vnet peering is working.
  - Disable the Gateway Route propagation on the peering, as force tunnelling works around this.

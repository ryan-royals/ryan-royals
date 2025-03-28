---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/add-custom-dns-servers-and-set-azure-point-to-site-vpn-to-connect-automatically/","tags":["rw/articles"]}
---

![rw-book-cover](https://luke.geek.nz/images/iazure-marketplace-banner.png)

The Azure Point to Site VPN will take the DNS servers from the Virtual Network, that the Gateway is peering into by default, but due to VNET Peering or custom configuration if you may want to point this to custom DNS servers.

To do this, you need to edit the ‘azurevpnconfig.xml’ file and reimport the VPN connection.

1. Open: azurevpnconfig.xml in your favourite editor *(ie Visual Studio Code or Notepad)*
2. Underneath the \_(which you can also change, as this is the name that users will see in Windows)\_ add: < clientconfig>.

For example:

```
  <name>Luke's Azure Point to Site VPN</name>
  <clientconfig>
 <!-- need to specify always on = true for the VPN to connect automatically --> 
 <AlwaysOn>true</AlwaysOn>
  <!-- Add custom DNS Servers --> 
           <dnsservers>
             <dnsserver>10.100.1.1</dnsserver>
             <dnsserver>10.100.1.2</dnsserver>
         </dnsservers>
<!-- Add custom DNS suffixes --> 
          <dnssuffixes>
          <dnssuffix>.luke.geek.nz</dnssuffix>
    </dnssuffixes>
</clientconfig>

```

Save your azurevpnconfig.xml and import it into the Azure VPN client.

Once the VPN has been re-established your Custom DNS settings and suffxies should take effect. If you included the this will reconnect automatically, after your first connection and after computer reboots.

If you need assistance setting up a Point to Site VPN, check out my article here: [Create Azure Point to Site VPN using Azure Active Directory authentication](https://luke.geek.nz/azure/create-azure-point-to-site-vpn-using-azure-active-directory-authentication/)

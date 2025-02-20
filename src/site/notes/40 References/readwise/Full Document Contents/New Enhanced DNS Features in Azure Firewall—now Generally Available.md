---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/new-enhanced-dns-features-in-azure-firewall-now-generally-available/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/d944b156-02e4-4e7b-94d3-94e85d72d8c7.webp)

*This post was co-authored by Adam Stuart, Technical Specialist, Azure Networking*

Custom DNS, DNS proxy, and FQDN filtering in network rules (for non-HTTP/S and non-MSSQL protocols) in Azure Firewall are now generally available. In this blog, we also share an example use-case on using DNS proxy with [Private Link](https://docs.microsoft.com/en-us/azure/private-link/private-link-overview).

Azure Firewall is a cloud-native firewall as a service (FWaaS) offering that allows you to centrally govern and log all your traffic flows using a DevOps approach. The service supports both application, NAT, and network-level filtering and is integrated with the Microsoft Threat Intelligence feed for filtering known malicious IP addresses and domains. Azure Firewall is highly available with built-in auto scaling.

#### Custom DNS support is now generally available

Since its launch in September 2018, Azure Firewall has been hardcoded to use Azure DNS to ensure the service can reliably resolve its outbound dependencies. Custom DNS allows you to configure Azure Firewall to use your own DNS server, while ensuring the firewall outbound dependencies are still resolved with Azure DNS. You may configure a single DNS server or multiple servers in Azure Firewall and Firewall Policy DNS settings.

Azure Firewall can also resolve names using [Azure Private DNS](https://docs.microsoft.com/en-us/azure/dns/private-dns-overview). The Virtual Network within which the Azure Firewall resides must be [linked](https://docs.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#link-the-virtual-network) to the Azure Private Zone.

#### DNS proxy is now generally available

With DNS proxy enabled, Azure Firewall can process and forward DNS queries from a Virtual Network(s) to your desired DNS server. This functionality is crucial and required to have reliable FQDN filtering in network rules. You can enable DNS proxy in Azure Firewall and Firewall Policy settings. To learn more about DNS proxy logs, see the [Azure Firewall log and metrics documentation](https://docs.microsoft.com/en-us/azure/firewall/logs-and-metrics).

DNS proxy configuration requires three steps:

1. Enable DNS proxy in Azure Firewall DNS settings.
2. Optionally configure your custom DNS server or use the provided default.
3. Finally, you must configure the Azure Firewall’s private IP address as a custom DNS server in your virtual network DNS server settings. This ensures DNS traffic is directed to Azure Firewall.

DNS proxy listens for requests on TCP port 53 and forwards them to Azure DNS or the custom DNS specified.

![Custom DNS and DNS Proxy settings on Azure Firewall.](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2020/11/d944b156-02e4-4e7b-94d3-94e85d72d8c7.webp)
*Figure 1. Custom DNS and DNS proxy settings on Azure Firewall.*

#### FQDN filtering in network rules now generally available

You can now use fully qualified domain names (FQDNs) in network rules based on DNS resolution in Azure Firewall and Firewall Policy. The specified FQDNs in your rule collections are translated to IP addresses based on your firewall DNS settings. This capability allows you to filter outbound traffic using FQDNs with any TCP/UDP protocol (including NTP, SSH, RDP, and more). As this capability is based on DNS resolution, it is highly recommended you enable the DNS proxy to ensure name resolution is consistent for your protected virtual machines and firewall.

*What’s the difference between FQDN filtering in **application rules** verses **network rules**?* 

FQDN filtering in application rules for HTTP/S and MSSQL is based on an application level transparent proxy. As such, it can discern between two FQDNs that are resolved to the same IP address. This is not the case with FQDN filtering in network rules, so it is always recommended you use application rules when possible.

![FQDN filtering in network rules.](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2020/11/ae523b5c-6a42-46c1-a376-fbb9cd2e641b.webp)
*Figure 2. FQDN filtering in network rules.*

#### Using Azure Firewall as a DNS proxy to enable private endpoints access from on-premises

[Azure Private Link](https://docs.microsoft.com/en-us/azure/private-link/private-link-overview) provides the ability to connect to Microsoft PaaS services, including storage accounts, app services, and more, over a private connection, using [private endpoints](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview). A private endpoint is a network interface that connects you privately and securely to a PaaS service powered by Azure Private Link. Private endpoints use a private IP address from your Virtual Network (VNet), effectively bringing the service inside your private network in the cloud. This approach provides additional security benefits as it removes the exposure and accessibility of public IP addresses of the PaaS service.

One of the big benefits of Azure Private Link is the ability to consume Microsoft PaaS services over privately addressed hybrid connections (for example, *Azure ExpressRoute Private Peering* or *Site-to-Site VPN*). However, this benefit also comes with the [challenge of forwarding DNS requests from on-premises to Azure Private DNS](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-dns#on-premises-workloads-using-a-dns-forwarder) to benefit from the automated lifecycle management of DNS records that map to your private endpoints.

Each Azure PaaS service that utilizes Private Link is given an FQDN that is mapped and stored in an Azure Private DNS zone. Requests sent to Azure DNS Private Zones go to the platform address of [168.63.129.16](https://docs.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16) that is only reachable from inside of Azure. Therefore, if the DNS request originates from on-premises (outside of Azure), there is a requirement to proxy the DNS request via a service inside of a Virtual Network.

With this general availability announcement, **Azure Firewall DNS proxy** is an option to meet this DNS forwarding requirement, applicable with a [hub-and-spoke model](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/hub-spoke). To do this, configure your on-premises DNS server to conditionally forward requests to Azure Firewall for the [required zone name](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-dns#azure-services-dns-zone-configuration). Ensure that your private DNS zone is linked to the Virtual Network within which the Azure Firewall resides. Configure Azure Firewall to use the default Azure DNS for lookups, and enable DNS proxy in Azure Firewall DNS settings. For more information about DNS proxy, visit our [DNS settings documentation](https://docs.microsoft.com/en-us/azure/firewall/dns-settings).

#### Next steps

For more information on everything we covered in this blog post, check out the following:

[Register now](https://info.microsoft.com/ww-landing-Network-Security-2020.html?ocid=AID3025106_QSG_487434) for the Azure network security digital event to learn more about Azure Firewall, and how to take a Zero Trust approach to secure your network and protect against cyber security attacks.

---
{"dg-publish":true,"permalink":"/40-references/readwise/new-enhanced-dns-features-in-azure-firewall-now-generally-available/","tags":["rw/articles"]}
---

# New Enhanced DNS Features in Azure Firewall—now Generally Available

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/d944b156-02e4-4e7b-94d3-94e85d72d8c7.webp)
  
URL: https://azure.microsoft.com/en-us/blog/new-enhanced-dns-features-in-azure-firewall-now-generally-available/
Author: Suren Jamiyanaa

## Summary

Custom DNS, DNS proxy, and FQDN filtering in network rules (for non-HTTP/S and non-MSSQL protocols) in Azure Firewall are now generally available. In this blog, we also share an example use-case on using DNS proxy with Private Link. Azure Firewall is a cloud-native firewall as a service (FWaaS) offering that allows you to centrally govern and log all your traffic flows using a DevOps approach.

## Highlights added July 17, 2024 at 10:55 AM
>DNS proxy is now generally available
>With DNS proxy enabled, Azure Firewall can process and forward DNS queries from a Virtual Network(s) to your desired DNS server. This functionality is crucial and required to have reliable FQDN filtering in network rules. You can enable DNS proxy in Azure Firewall and Firewall Policy settings. To learn more about DNS proxy logs, see the [Azure Firewall log and metrics documentation](https://docs.microsoft.com/en-us/azure/firewall/logs-and-metrics). ([View Highlight] (https://read.readwise.io/read/01h65vmq1g8cw8cyzgt5jk54ph))


>[Azure Private Link](https://docs.microsoft.com/en-us/azure/private-link/private-link-overview) provides the ability to connect to Microsoft PaaS services, including storage accounts, app services, and more, over a private connection, using [private endpoints](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-overview). A private endpoint is a network interface that connects you privately and securely to a PaaS service powered by Azure Private Link. Private endpoints use a private IP address from your Virtual Network (VNet), effectively bringing the service inside your private network in the cloud. This approach provides additional security benefits as it removes the exposure and accessibility of public IP addresses of the PaaS service. ([View Highlight] (https://read.readwise.io/read/01h65vqxbzterqae5b3zh1r49a))


>With this general availability announcement, **Azure Firewall DNS proxy** is an option to meet this DNS forwarding requirement, applicable with a [hub-and-spoke model](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/hub-spoke). To do this, configure your on-premises DNS server to conditionally forward requests to Azure Firewall for the [required zone name](https://docs.microsoft.com/en-us/azure/private-link/private-endpoint-dns#azure-services-dns-zone-configuration). Ensure that your private DNS zone is linked to the Virtual Network within which the Azure Firewall resides. Configure Azure Firewall to use the default Azure DNS for lookups, and enable DNS proxy in Azure Firewall DNS settings. For more information about DNS proxy, visit our [DNS settings documentation](https://docs.microsoft.com/en-us/azure/firewall/dns-settings). ([View Highlight] (https://read.readwise.io/read/01h65vqth0w95ynp9708tfdckd))



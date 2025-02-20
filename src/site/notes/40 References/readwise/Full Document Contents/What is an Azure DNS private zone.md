---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-an-azure-dns-private-zone/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Limits](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone#limits)
2. [Restrictions](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone#restrictions)
3. [Next steps](https://learn.microsoft.com/en-us/azure/dns/private-dns-privatednszone#next-steps)

Azure Private DNS provides a reliable, secure DNS service to manage and resolve domain names in a virtual network without the need to add a custom DNS solution. By using private DNS zones, you can use your own custom domain names rather than the Azure-provided names available today.

The records contained in a private DNS zone aren't resolvable from the Internet. DNS resolution against a private DNS zone works only from virtual networks that are linked to it.

You can link a private DNS zone to one or more virtual networks by creating [virtual network links](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links). You can also enable the [autoregistration](https://learn.microsoft.com/en-us/azure/dns/private-dns-autoregistration) feature to automatically manage the life cycle of the DNS records for the virtual machines that get deployed in a virtual network.

#### Limits

To understand how many private DNS zones you can create in a subscription and how many record sets are supported in a private DNS zone, see [Azure DNS limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-dns-limits)

#### Restrictions

* Single-label private DNS zones aren't supported. Your private DNS zone must have two or more labels. For example, contoso.com has two labels separated by a dot. A private DNS zone can have a maximum of 34 labels.
* You can't create zone delegations (NS records) in a private DNS zone. If you intend to use a child domain, you can directly create the domain as a private DNS zone. Then you can link it to the virtual network without setting up a nameserver delegation from the parent zone.
* The following list of reserved zone names are blocked from creation to prevent disruption of services:

| Public | Azure Government | Azure China |
| --- | --- | --- |
| azclient.ms | azclient.us | azclient.cn |
| azure.com | azure.us | azure.cn |
| cloudapp.net | usgovcloudapp.net | chinacloudapp.cn |
| core.windows.net | core.usgovcloudapi.net | core.chinacloudapi.cn |
| microsoft.com | microsoft.us | microsoft.cn |
| msidentity.com | msidentity.us | msidentity.cn |
| trafficmanager.net | usgovtrafficmanager.net | trafficmanager.cn |
| windows.net | usgovcloudapi.net | chinacloudapi.cn |

#### Next steps

* Learn how to create a private zone in Azure DNS by using [Azure PowerShell](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-powershell) or [Azure CLI](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-cli).
* Read about some common [private zone scenarios](https://learn.microsoft.com/en-us/azure/dns/private-dns-scenarios) that can be realized with private zones in Azure DNS.
* For common questions and answers about private zones in Azure DNS, see [Private DNS FAQ](https://learn.microsoft.com/en-us/azure/dns/dns-faq-private).

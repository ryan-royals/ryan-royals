---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-azure-private-dns/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Private zone resiliency](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview#private-zone-resiliency)
2. [Benefits](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview#benefits)
3. [Capabilities](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview#capabilities)
4. [Other considerations](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview#other-considerations)
5. [Pricing](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview#pricing)
6. [Next steps](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview#next-steps)

The Domain Name System, or DNS, is responsible for translating (or resolving) a service name to an IP address. Azure DNS is a hosting service for domains and provides naming resolution using the Microsoft Azure infrastructure. Azure DNS not only supports internet-facing DNS domains, but it also supports private DNS zones.

Azure Private DNS provides a reliable and secure DNS service for your virtual networks. Azure Private DNS manages and resolves domain names in the virtual network without the need to configure a custom DNS solution. By using private DNS zones, you can use your own custom domain name instead of the Azure-provided names during deployment. Using a custom domain name helps you tailor your virtual network architecture to best suit your organization's needs. It provides a naming resolution for virtual machines (VMs) within a virtual network and connected virtual networks. Additionally, you can configure zones names with a split-horizon view, which allows a private and a public DNS zone to share the name.

To resolve the records of a private DNS zone from your virtual network, you must link the virtual network with the zone. Linked virtual networks have full access and can resolve all DNS records published in the private zone. You can also enable autoregistration on a virtual network link. When you enable autoregistration on a virtual network link, the DNS records for the virtual machines in that virtual network are registered in the private zone. When autoregistration gets enabled, Azure DNS will update the zone record whenever a virtual machine gets created, changes its' IP address, or gets deleted.

![DNS overview](https://learn.microsoft.com/en-us/azure/dns/media/private-dns-overview/scenario.png)
Note

As a best practice, do not use a *.local* domain for your private DNS zone. Not all operating systems support this.

#### Private zone resiliency

When you create a private DNS zone, Azure stores the zone data as a global resource. This means that the private zone is not dependent on a single VNet or region. You can link the same private zone to multiple VNets in different regions. If service is interrupted in one VNet, your private zone is still available. For more information, see [Azure Private DNS zone resiliency](https://learn.microsoft.com/en-us/azure/dns/private-dns-resiliency).

#### Benefits

Azure Private DNS provides the following benefits:

* **Removes the need for custom DNS solutions**. Previously, many customers created custom DNS solutions to manage DNS zones in their virtual network. You can now manage DNS zones using the native Azure infrastructure, which removes the burden of creating and managing custom DNS solutions.
* **Use all common DNS records types**. Azure DNS supports A, AAAA, CNAME, MX, PTR, SOA, SRV, and TXT records.
* **Automatic hostname record management**. Along with hosting your custom DNS records, Azure automatically maintains hostname records for the VMs in the specified virtual networks. In this scenario, you can optimize the domain names you use without needing to create custom DNS solutions or modify applications.
* **Hostname resolution between virtual networks**. Unlike Azure-provided host names, private DNS zones can be shared between virtual networks. This capability simplifies cross-network and service-discovery scenarios, such as virtual network peering.
* **Familiar tools and user experience**. To reduce the learning curve, this service uses well-established Azure DNS tools (Azure portal, Azure PowerShell, Azure CLI, Azure Resource Manager templates, and the REST API).
* **Split-horizon DNS support**. With Azure DNS, you can create zones with the same name that resolve to different answers from within a virtual network and from the public internet. A typical scenario for split-horizon DNS is to provide a dedicated version of a service for use inside your virtual network.
* **Available in all Azure regions**. The Azure DNS private zones feature is available in all Azure regions in the Azure public cloud.

#### Capabilities

Azure Private DNS provides the following capabilities:

* **Automatic registration of virtual machines from a virtual network that's linked to a private zone with autoregistration enabled**. Virtual machines get registered to the private zone as A records pointing to their private IP addresses. When a virtual machine in a virtual network link with autoregistration enabled gets deleted, Azure DNS also automatically removes the corresponding DNS record from the linked private zone.
* **Forward DNS resolution is supported across virtual networks that are linked to the private zone**. For cross-virtual network DNS resolution, there's no explicit dependency such that the virtual networks are peered with each other. However, you might want to peer virtual networks for other scenarios (for example, HTTP traffic).
* **Reverse DNS lookup is supported within the virtual-network scope**. Reverse DNS lookup for a private IP associated to a private zone will return an FQDN that includes the host/record name and the zone name as the suffix.

#### Other considerations

Azure Private DNS has the following limitations:

* A specific virtual network can be linked to only one private zone if automatic registration of VM DNS records is enabled. You can however link multiple virtual networks to a single DNS zone.
* Reverse DNS works only for private IP space in the linked virtual network
* Reverse DNS for a private IP address in linked virtual network will return `internal.cloudapp.net` as the default suffix for the virtual machine. For virtual networks that are linked to a private zone with autoregistration enabled, reverse DNS for a private IP address returns two FQDNs: one with default the suffix `internal.cloudapp.net` and another with the private zone suffix.
* Conditional forwarding is supported using [Azure DNS Private Resolver](https://learn.microsoft.com/en-us/azure/dns/dns-private-resolver-overview). To enable resolution between Azure and on-premises networks, see [Name resolution for VMs and role instances](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-name-resolution-for-vms-and-role-instances).

#### Pricing

For pricing information, see [Azure DNS Pricing](https://azure.microsoft.com/pricing/details/dns/).

#### Next steps

* Learn how to create a private zone in Azure DNS by using [Azure PowerShell](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-powershell) or [Azure CLI](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-cli).
* Read about some common [private zone scenarios](https://learn.microsoft.com/en-us/azure/dns/private-dns-scenarios) that can be realized with private zones in Azure DNS.
* For common questions and answers about private zones in Azure DNS, see [Private DNS FAQ](https://learn.microsoft.com/en-us/azure/dns/dns-faq-private).
* Learn about DNS zones and records by visiting [DNS zones and records overview](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records).
* Learn about some of the other key [networking capabilities](https://learn.microsoft.com/en-us/azure/networking/fundamentals/networking-overview) of Azure.
* [Learn module: Introduction to Azure DNS](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-dns).

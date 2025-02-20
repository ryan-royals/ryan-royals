---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-a-virtual-network-link-subresource-of-azure-dns-private-zones/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Registration virtual network](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links#registration-virtual-network)
2. [Resolution virtual network](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links#resolution-virtual-network)
3. [Limits](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links#limits)
4. [Other considerations](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links#other-considerations)
5. [Next steps](https://learn.microsoft.com/en-us/azure/dns/private-dns-virtual-network-links#next-steps)

After you create a private DNS zone in Azure, you'll need to link a virtual network to it. Once linked, VMs hosted in that virtual network can access the private DNS zone. Every private DNS zone has a collection of virtual network link child resources. Each one of these resources represents a connection to a virtual network. A virtual network can be linked to private DNS zone as a registration or as a resolution virtual network.

#### Registration virtual network

When [creating a link](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#link-the-virtual-network) between a private DNS zone and a virtual network. You have the option to enable [autoregistration](https://learn.microsoft.com/en-us/azure/dns/private-dns-autoregistration). With this setting enabled, the virtual network becomes a registration virtual network for the private DNS zone. A DNS record gets automatically created for any virtual machines you deploy in the virtual network. DNS records will also be created for virtual machines already deployed in the virtual network.

From the virtual network perspective, private DNS zone becomes the registration zone for that virtual network. A private DNS zone can have multiple registration virtual networks. However, every virtual network can only have one registration zone associated with it.

#### Resolution virtual network

If you choose to link your virtual network with the private DNS zone without autoregistration, the virtual network is treated as a resolution virtual network only. DNS records for virtual machines deployed this virtual network won't be created automatically in the private zone. However, virtual machines deployed in the virtual network can successfully query for DNS records in the private zone. These records include manually created and auto registered records from other virtual networks linked to the private DNS zone.

One private DNS zone can have multiple resolution virtual networks and a virtual network can have multiple resolution zones associated to it.

#### Limits

To understand how many registration and resolution networks, you can link to private DNS zones see [Azure DNS Limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-dns-limits)

#### Other considerations

* Virtual networks deployed using classic deployment model isn't supported.
* You can create only one link between a private DNS zone and a virtual network.
* Each virtual network link under a private DNS zone must have unique name within the context of the private DNS zone. You can have links with same name in different private DNS zones.
* After creating a virtual network link, check the "Link Status" field of the virtual network link resource. Depending on the size of the virtual network, it can take a few minutes before the link is operation and the Link Status changes to *Completed*.
* When you delete a virtual network, all the virtual network links and autoregistered DNS records associated with it in different private DNS zones are automatically deleted.

#### Next steps

* Learn how to link a virtual network to a private DNS zone using [Azure portal](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-portal#link-the-virtual-network)
* Learn how to create a private zone in Azure DNS by using [Azure PowerShell](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-powershell) or [Azure CLI](https://learn.microsoft.com/en-us/azure/dns/private-dns-getstarted-cli).
* Read about some common [private zone scenarios](https://learn.microsoft.com/en-us/azure/dns/private-dns-scenarios) that can be realized with private zones in Azure DNS.
* For common questions and answers about private zones in Azure DNS, including specific behavior you can expect for certain kinds of operations, see [Private DNS FAQ](https://learn.microsoft.com/en-us/azure/dns/dns-faq-private).

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/bring-your-own-ip-addresses-byoip-to-azure-with-custom-ip-prefix/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2022/03/f216b134-24a6-4a59-bb9a-5e276aa67e77.webp)

When planning a potential migration of on-premises infrastructure to Azure, you may want to retain your existing public IP addresses due to your customers’ dependencies (for example, firewalls or other IP hardcoding) or to preserve an established IP reputation. Today, we are excited to announce the general availability of the ability to bring your own IP addresses (BYOIP) to Azure in all public regions. Using the [Custom IP Prefix resource](https://docs.microsoft.com/azure/virtual-network/ip-services/custom-ip-address-prefix), you can now bring your own public IPv4 ranges to Azure and use them like any other Azure-owned public IP ranges. Once onboarded, these IPs can be associated with Azure resources, interact with private IPs and VNETs within Azure’s network, and reach external destinations by egressing from Microsoft’s Wide Area Network. Read more about how bringing your IP addresses to Azure can help to speed up your cloud migration.

#### Provisioning a custom IP range

Onboarding your ranges to Azure can be done through the Azure portal, Azure PowerShell, Azure CLI, or by using Azure Resource Manager (ARM) templates. In order to bring a public IP range to use on Azure, you must own and have registered the range with a Routing Internet Registry such as [ARIN](https://www.arin.net/) or [RIPE](https://www.ripe.net/). When bringing an IP range to use on Azure, it remains under your ownership, but Microsoft is permitted to advertise it from our Wide Area Network (WAN). The ranges used for onboarding must be no smaller than a /24 (256 IP addresses) so that they will be accepted by Internet service providers. When you create a Custom IP Prefix resource for your IP range, Microsoft performs validation steps to verify your ownership of the range and its association with your Azure subscription. Each onboarded range is associated with an Azure region.

#### Using a custom IP range

Once your range has been provisioned on Azure, you have the option to assign public IP addresses from the range to resources immediately or to begin advertising the range before assigning, depending on what fits your specific use case. After the command is issued to commission a range, Microsoft will advertise it both regionally (within Azure) and globally (to the Internet). The specific region where the range was onboarded will also be [posted publicly](https://www.microsoft.com/download/details.aspx?id=53601) for geolocation providers. To assign the BYOIPs, you would create public IP prefixes (contiguous blocks of Standard SKU public IP addresses), from which you can allocate specific individual public IP addresses. Note that while an IP range is onboarded under the context of an Azure subscription, prefixes from this range can be derived from other subscriptions with appropriate permissions. Onboarded IPs can be associated with any resource that supports Standard SKU public IPs, such as virtual machines, Standard Public Load Balancers, Azure Firewalls, and more. You are not charged for maintenance and hosting of your onboarded Public IPs Prefix; you are charged only for egress bandwidth from the IPs and any attached resources.

![Illustration of the Custom IP Prefix onboarding process.](https://azure.microsoft.com/en-us/blog/wp-content/uploads/2022/03/f216b134-24a6-4a59-bb9a-5e276aa67e77.webp)
#### Key takeaways

* The ability to bring your own IP addresses (BYOIP) to Azure is currently available in all regions.
* The minimum size of an onboarded range is /24 (256 IP addresses).
* Onboarded IPs are put in a Custom IP Prefix resource for management, from which Public IP Prefixes can be derived and utilized across subscriptions.
* You are not charged for the hosting or management of onboarded ranges brought to Azure.

#### Additional resources

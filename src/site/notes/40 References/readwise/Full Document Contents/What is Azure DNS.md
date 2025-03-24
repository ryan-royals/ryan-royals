---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-azure-dns/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Reliability and performance](https://learn.microsoft.com/en-us/azure/dns/dns-overview#reliability-and-performance)
2. [Security](https://learn.microsoft.com/en-us/azure/dns/dns-overview#security)
3. [DNSSEC](https://learn.microsoft.com/en-us/azure/dns/dns-overview#dnssec)
4. [Ease of use](https://learn.microsoft.com/en-us/azure/dns/dns-overview#ease-of-use)
5. [Customizable virtual networks with private domains](https://learn.microsoft.com/en-us/azure/dns/dns-overview#customizable-virtual-networks-with-private-domains)
6. [Alias records](https://learn.microsoft.com/en-us/azure/dns/dns-overview#alias-records)
7. [Next steps](https://learn.microsoft.com/en-us/azure/dns/dns-overview#next-steps)

Azure DNS is a hosting service for DNS domains that provides name resolution by using Microsoft Azure infrastructure. By hosting your domains in Azure, you can manage your DNS records by using the same credentials, APIs, tools, and billing as your other Azure services.

You can't use Azure DNS to buy a domain name. For an annual fee, you can buy a domain name by using [App Service domains](https://learn.microsoft.com/en-us/azure/app-service/manage-custom-dns-buy-domain#buy-and-map-an-app-service-domain) or a third-party domain name registrar. Your domains then can be hosted in Azure DNS for record management. For more information, see [Delegate a domain to Azure DNS](https://learn.microsoft.com/en-us/azure/dns/dns-domain-delegation).

The following features are included with Azure DNS.

#### Reliability and performance

DNS domains in Azure DNS are hosted on Azure's global network of DNS name servers. Azure DNS uses anycast networking. Each DNS query is answered by the closest available DNS server to provide fast performance and high availability for your domain.

#### Security

Azure DNS is based on Azure Resource Manager, which provides features such as:

* [Azure role-based access control (Azure RBAC)](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) to control who has access to specific actions for your organization.
* [Activity logs](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) to monitor how a user in your organization modified a resource or to find an error when troubleshooting.
* [Resource locking](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/lock-resources) to lock a subscription, resource group, or resource. Locking prevents other users in your organization from accidentally deleting or modifying critical resources.

For more information, see [How to protect DNS zones and records](https://learn.microsoft.com/en-us/azure/dns/dns-protect-zones-recordsets).

#### DNSSEC

Azure DNS does not currently support DNSSEC. In most cases, you can reduce the need for DNSSEC by consistently using HTTPS/TLS in your applications. If DNSSEC is a critical requirement for your DNS zones, you can host these zones with third-party DNS hosting providers.

#### Ease of use

Azure DNS can manage DNS records for your Azure services and provide DNS for your external resources as well. Azure DNS is integrated in the Azure portal and uses the same credentials, support contract, and billing as your other Azure services.

DNS billing is based on the number of DNS zones hosted in Azure and on the number of DNS queries received. To learn more about pricing, see [Azure DNS pricing](https://azure.microsoft.com/pricing/details/dns/).

Your domains and records can be managed by using the Azure portal, Azure PowerShell cmdlets, and the cross-platform Azure CLI. Applications that require automated DNS management can integrate with the service by using the REST API and SDKs.

#### Customizable virtual networks with private domains

Azure DNS also supports private DNS domains. This feature allows you to use your own custom domain names in your private virtual networks rather than the Azure-provided names available today.

For more information, see [Use Azure DNS for private domains](https://learn.microsoft.com/en-us/azure/dns/private-dns-overview).

#### Alias records

Azure DNS supports alias record sets. You can use an alias record set to refer to an Azure resource, such as an Azure public IP address, an Azure Traffic Manager profile, or an Azure Content Delivery Network (CDN) endpoint. If the IP address of the underlying resource changes, the alias record set seamlessly updates itself during DNS resolution. The alias record set points to the service instance, and the service instance is associated with an IP address.

Also, you can now point your apex or naked domain to a Traffic Manager profile or CDN endpoint using an alias record. An example is contoso.com.

For more information, see [Overview of Azure DNS alias records](https://learn.microsoft.com/en-us/azure/dns/dns-alias).

#### Next steps

* To learn about DNS zones and records, see [DNS zones and records overview](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records).
* To learn how to create a zone in Azure DNS, see [Create a DNS zone](https://learn.microsoft.com/en-us/azure/dns/dns-getstarted-portal).
* For frequently asked questions about Azure DNS, see the [Azure DNS FAQ](https://learn.microsoft.com/en-us/azure/dns/dns-faq).
* [Learn module: Introduction to Azure DNS](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-dns).

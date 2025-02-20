---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-azure-private-link/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/open-graph-image_jupSUv2.png)

#### In this article

1. [Key benefits](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#key-benefits)
2. [Availability](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#availability)
3. [Logging and monitoring](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#logging-and-monitoring)
4. [Pricing](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#pricing)
5. [FAQs](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#faqs)
6. [Limits](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#limits)
7. [Service Level Agreement](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#service-level-agreement)
8. [Next steps](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview#next-steps)

Azure Private Link enables you to access Azure PaaS Services (for example, Azure Storage and SQL Database) and Azure hosted customer-owned/partner services over a [private endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview) in your virtual network.

Traffic between your virtual network and the service travels the Microsoft backbone network. Exposing your service to the public internet is no longer necessary. You can create your own [private link service](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview) in your virtual network and deliver it to your customers. Setup and consumption using Azure Private Link is consistent across Azure PaaS, customer-owned, and shared partner services.

Important

Azure Private Link is now generally available. Both Private Endpoint and Private Link service (service behind standard load balancer) are generally available. Different Azure PaaS will onboard to Azure Private Link at different schedules. See [Private Link availability](https://learn.microsoft.com/en-us/azure/private-link/availability) for an accurate status of Azure PaaS on Private Link. For known limitations, see [Private Endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview#limitations) and [Private Link Service](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview#limitations).

![Screenshot of Azure Private Link center in Azure portal.](https://learn.microsoft.com/en-us/azure/private-link/media/private-link-overview/private-link-center.png)
#### Key benefits

Azure Private Link provides the following benefits:

* **Privately access services on the Azure platform**: Connect your virtual network using private endpoints to all services that can be used as application components in Azure. Service providers can render their services in their own virtual network and consumers can access those services in their local virtual network. The Private Link platform will handle the connectivity between the consumer and services over the Azure backbone network.
* **On-premises and peered networks**: Access services running in Azure from on-premises over ExpressRoute private peering, VPN tunnels, and peered virtual networks using private endpoints. There's no need to configure ExpressRoute Microsoft peering or traverse the internet to reach the service. Private Link provides a secure way to migrate workloads to Azure.
* **Protection against data leakage**: A private endpoint is mapped to an instance of a PaaS resource instead of the entire service. Consumers can only connect to the specific resource. Access to any other resource in the service is blocked. This mechanism provides protection against data leakage risks.
* **Global reach**: Connect privately to services running in other regions. The consumer's virtual network could be in region A and it can connect to services behind Private Link in region B.
* **Extend to your own services**: Enable the same experience and functionality to render your service privately to consumers in Azure. By placing your service behind a standard Azure Load Balancer, you can enable it for Private Link. The consumer can then connect directly to your service using a private endpoint in their own virtual network. You can manage the connection requests using an approval call flow. Azure Private Link works for consumers and services belonging to different Microsoft Entra tenants.

Note

Azure Private Link, along with Azure Virtual Network, span across [Azure Availability Zones](https://learn.microsoft.com/en-us/azure/availability-zones/az-overview) and are therefore zone resilient. To provide high availability for the Azure resource using a private endpoint, ensure that resource is zone resilient.

#### Availability

For information on Azure services that support Private Link, see [Azure Private Link availability](https://learn.microsoft.com/en-us/azure/private-link/availability).

For the most up-to-date notifications, check the [Azure Private Link updates page](https://azure.microsoft.com/updates/?product=private-link).

#### Logging and monitoring

Azure Private Link has integration with Azure Monitor. This combination allows:

* Archival of logs to a storage account.
* Streaming of events to your Event Hubs.
* Azure Monitor logging.

You can access the following information on Azure Monitor:

* **Private endpoint**:

	+ Data processed by the Private Endpoint (IN/OUT)
* **Private Link service**:

	+ Data processed by the Private Link service (IN/OUT)
	+ NAT port availability

#### Pricing

For pricing details, see [Azure Private Link pricing](https://azure.microsoft.com/pricing/details/private-link/).

#### FAQs

For FAQs, see [Azure Private Link FAQs](https://learn.microsoft.com/en-us/azure/private-link/private-link-faq).

#### Limits

For limits, see [Azure Private Link limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#private-link-limits).

#### Service Level Agreement

For SLA, see [SLA for Azure Private Link](https://azure.microsoft.com/support/legal/sla/private-link/v1_0/).

#### Next steps

* [Quickstart: Create a Private Endpoint using Azure portal](https://learn.microsoft.com/en-us/azure/private-link/create-private-endpoint-portal)
* [Quickstart: Create a Private Link service by using the Azure portal](https://learn.microsoft.com/en-us/azure/private-link/create-private-link-service-portal)
* [Learn module: Introduction to Azure Private Link](https://learn.microsoft.com/en-us/training/modules/introduction-azure-private-link/)

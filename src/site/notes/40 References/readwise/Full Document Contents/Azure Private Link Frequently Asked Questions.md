---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-private-link-frequently-asked-questions/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

* **[Azure Private Endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview)**: Azure Private Endpoint is a network interface that connects you privately and securely to a service powered by Azure Private Link. You can use Private Endpoints to connect to an Azure PaaS service that supports Private Link or to your own Private Link Service.
* **[Azure Private Link Service](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview)**: Azure Private Link service is a service created by a service provider. Currently, a Private Link service can be attached to the frontend IP configuration of a Standard Load Balancer.

Traffic is sent privately using Microsoft backbone. It doesn’t traverse the internet. Azure Private Link doesn't store customer data.

* Private Endpoints grant network access to specific resources behind a given service providing granular segmentation. Traffic can reach the service resource from on premises without using public endpoints.
* A Service Endpoint remains a publicly routable IP address. A Private Endpoint is a private IP in the address space of the virtual network where the private endpoint is configured.

Multiple private link resource types support access via Private Endpoints. Resources include Azure PaaS services and your own Private Link Service. It's a one-to-many relationship.

A Private Link service receives connections from multiple Private Endpoints. A private endpoint connects to one Private Link Service.

Yes. Private Link Service need to disable network policies to function properly.

Yes. To utilize policies like User-Defined Routes and Network Security Groups, you need to enable Network policies for a subnet in a virtual network for the Private Endpoint. This setting affects all the private endpoints within the subnet.

Yes. You can have multiple Private Endpoints in same VNet or subnet. They can connect to different services.

No. You don't require a dedicated subnet for Private Endpoints. You can choose a Private Endpoint IP from any subnet from the VNet where your service is deployed.

Yes. Private endpoints can connect to Private Link services or to an Azure PaaS across Azure Active Directory tenants. Private Endpoints across tenants require a manual request approval.

Yes. Private Endpoints can connect to Azure PaaS resources across Azure regions.

When a private endpoint is created, a read-only NIC is assigned. The NIC can't be modified and will remain for the life cycle of the Private endpoint.

Private Endpoints are highly available resources with an SLA as per [SLA for Azure Private Link](https://azure.microsoft.com/support/legal/sla/private-link/v1_0/). However, since they're regional resources, any Azure region outage can affect the availability. To achieve availability if there are regional failures, multiple PEs connected to same destination resource could be deployed in different regions. This way if one region goes down, you can still route the traffic for your recovery scenarios through PE in different region to access the destination resource. For info on how the regional failures are handled on destination service side, review the service documentation on failover and recovery. Private Link traffic follows the Azure DNS resolution for the destination endpoint.

Private Endpoints are highly available resources with an SLA as per [SLA for Azure Private Link](https://azure.microsoft.com/support/legal/sla/private-link/v1_0/). Private Endpoints are zone-agnostic: an availability zone failure in the region of the Private Endpoint won't affect the availability of the Private Endpoint.

TCP and UDP traffic are only supported for a private endpoint. For more information, see [Private Link limitations](https://learn.microsoft.com/en-us/azure/private-link/private-link-service-overview#limitations).

Your service backends should be in a Virtual Network and behind a Standard Load Balancer.

You can scale your Private Link Service in a few different ways:

* Add Backend VMs to the pool behind your Standard Load Balancer
* Add an IP to the Private Link Service. We allow up to 8 IPs per Private Link Service.
* Add new Private Link Service to Standard Load Balancer. We allow up to eight Private Link Services per Standard Load Balancer.

* The NAT IP configuration ensures the source (consumer) and destination (service provider) address space don't have IP conflicts. The configuration provides source NAT for the private link traffic for the destination. The NAT IP address will show up as source IP for all packets received by your service and destination IP for all packets sent by your service. NAT IP can be chosen from any subnet in a service provider's Virtual Network.
* Each NAT IP provides 64k TCP connections (64k ports) per VM behind the Standard Load Balancer. In order to scale and add more connections, you can either add new NAT IPs or add more VMs behind the Standard Load Balancer. Doing so will scale the port availability and allow for more connections. Connections will be distributed across NAT IPs and VMs behind the Standard Load Balancer.

Yes. One Private Link Service can receive connections from multiple Private Endpoints. However one Private Endpoint can only connect to one Private Link Service.

You can control the exposure using the visibility configuration on Private Link service. Visibility supports three settings:

* **None** - Only subscriptions with role based access can locate the service.
* **Restrictive** - Only subscriptions that are approved and with role based access can locate the service.
* **All** - Everyone can locate the service.

No. Private Link Service over a Basic Load Balancer isn't supported.

No. A dedicated subnet isn't required for the Private Link Service. You can choose any subnet in your VNet where your service is deployed.

No. Azure Private Link provides this functionality for you. You aren't required to have non-overlapping address space with your customer's address space.

#### Next steps

* Learn about [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview)

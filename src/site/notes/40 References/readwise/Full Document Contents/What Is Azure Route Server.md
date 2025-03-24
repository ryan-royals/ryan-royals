---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-azure-route-server/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [How does it work?](https://learn.microsoft.com/en-us/azure/route-server/overview#how-does-it-work)
2. [Key benefits](https://learn.microsoft.com/en-us/azure/route-server/overview#key-benefits)
3. [Route Server Limits](https://learn.microsoft.com/en-us/azure/route-server/overview#route-server-limits)
4. [Pricing](https://learn.microsoft.com/en-us/azure/route-server/overview#pricing)
5. [Service Level Agreement (SLA)](https://learn.microsoft.com/en-us/azure/route-server/overview#service-level-agreement-sla)
6. [FAQ](https://learn.microsoft.com/en-us/azure/route-server/overview#faq)
7. [Next steps](https://learn.microsoft.com/en-us/azure/route-server/overview#next-steps)

Azure Route Server simplifies dynamic routing between your network virtual appliance (NVA) and your virtual network. It allows you to exchange routing information directly through Border Gateway Protocol (BGP) routing protocol between any NVA that supports the BGP routing protocol and the Azure Software Defined Network (SDN) in the Azure Virtual Network (VNet) without the need to manually configure or maintain route tables. Azure Route Server is a fully managed service and is configured with high availability.

Important

Azure Route Servers created before November 1, 2021, that don't have a public IP address associated, are deployed with the [public preview](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) offering. The public preview offering is not backed by General Availability SLA and support. To deploy Azure Route Server with the General Availability offering, and to achieve General Availability SLA and support, please delete and recreate your Route Server.

#### How does it work?

The following diagram illustrates how Azure Route Server works with an SDWAN NVA and a security NVA in a virtual network. Once you’ve established the BGP peering, Azure Route Server will receive an on-premises route (10.250.0.0/16) from the SDWAN appliance and a default route (0.0.0.0/0) from the firewall. These routes are then automatically configured on the VMs in the virtual network. As a result, all traffic destined to the on-premises network will be sent to the SDWAN appliance, while all Internet-bound traffic will be sent to the firewall. In the opposite direction, Azure Route Server will send the virtual network address (10.1.0.0/16) to both NVAs. The SDWAN appliance can propagate it further to the on-premises network.

![Diagram showing Azure Route Server configured in a virtual network.](https://learn.microsoft.com/en-us/azure/route-server/media/overview/route-server-overview.png)
#### Key benefits

Azure Route Server simplifies configuration, management, and deployment of your NVA in your virtual network.

* You no longer need to manually update the routing table on your NVA whenever your virtual network addresses are updated.
* You no longer need to update [User-Defined Routes](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview) manually whenever your NVA announces new routes or withdraw old ones.
* You can peer multiple instances of your NVA with Azure Route Server. You can configure the BGP attributes in your NVA and, depending on your design (for example, active-active for performance or active-passive for resiliency), let Azure Route Server know which NVA instance is active or which one is passive.
* The interface between NVA and Azure Route Server is based on a common standard protocol. As long as your NVA supports BGP, you can peer it with Azure Route Server. For more information, see [Route Server supported routing protocols](https://learn.microsoft.com/en-us/azure/route-server/route-server-faq#protocol).
* You can deploy Azure Route Server in any of your new or existing virtual network.

#### Route Server Limits

Azure Route Server has the following limits (per deployment).

| Resource | Limit |
| --- | --- |
| Number of BGP peers supported | 8 |
| Number of routes each BGP peer can advertise to Azure Route Server 1 | 1,000 |
| Number of VMs in the virtual network (including peered virtual networks) that Azure Route Server can support 2 | 4,000 |

1 If your NVA advertises more routes than the limit, the BGP session gets dropped.

2 The number of VMs that Azure Route Server can support isn’t a hard limit and it depends on the availability and performance of the underlying infrastructure.

Note

The total number of routes advertised from VNet address space and Route Server towards ExpressRoute circuit, when [Branch-to-branch](https://learn.microsoft.com/en-us/azure/route-server/quickstart-configure-route-server-portal#configure-route-exchange) enabled, must not exceed 1,000. For more information, see [Route advertisement limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#expressroute-limits) of ExpressRoute.

#### Pricing

For pricing details, see [Azure Route Server pricing](https://azure.microsoft.com/pricing/details/route-server/).

#### Service Level Agreement (SLA)

For service level agreement details, see [SLA for Azure Route Server](https://azure.microsoft.com/support/legal/sla/route-server/v1_0/).

#### FAQ

For frequently asked questions about Azure Route Server, see [Azure Route Server FAQ](https://learn.microsoft.com/en-us/azure/route-server/route-server-faq).

#### Next steps

* [Learn how to configure Azure Route Server](https://learn.microsoft.com/en-us/azure/route-server/quickstart-configure-route-server-powershell)
* [Learn how Azure Route Server works with Azure ExpressRoute and Azure VPN](https://learn.microsoft.com/en-us/azure/route-server/expressroute-vpn-support)
* [Learn module: Introduction to Azure Route Server](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-route-server)

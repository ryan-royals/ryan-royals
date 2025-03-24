---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/what-is-azure-application-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_ZAtUwg7.png)

#### In this article

1. [Features](https://learn.microsoft.com/en-us/azure/application-gateway/overview#features)
2. [Infrastructure](https://learn.microsoft.com/en-us/azure/application-gateway/overview#infrastructure)
3. [Pricing and SLA](https://learn.microsoft.com/en-us/azure/application-gateway/overview#pricing-and-sla)
4. [What's new](https://learn.microsoft.com/en-us/azure/application-gateway/overview#whats-new)
5. [Next steps](https://learn.microsoft.com/en-us/azure/application-gateway/overview#next-steps)

Azure Application Gateway is a web traffic load balancer that enables you to manage traffic to your web applications. Traditional load balancers operate at the transport layer (OSI layer 4 - TCP and UDP) and route traffic based on source IP address and port, to a destination IP address and port.

Application Gateway can make routing decisions based on additional attributes of an HTTP request, for example URI path or host headers. For example, you can route traffic based on the incoming URL. So if `/images` is in the incoming URL, you can route traffic to a specific set of servers (known as a pool) configured for images. If `/video` is in the URL, that traffic is routed to another pool that's optimized for videos.

![imageURLroute](https://learn.microsoft.com/en-us/azure/application-gateway/media/application-gateway-url-route-overview/figure1-720.png)
This type of routing is known as application layer (OSI layer 7) load balancing. Azure Application Gateway can do URL-based routing and more.

Note

Azure provides a suite of fully managed load-balancing solutions for your scenarios.

* If you're looking to do DNS based global routing and do **not** have requirements for Transport Layer Security (TLS) protocol termination ("SSL offload"), per-HTTP/HTTPS request or application-layer processing, review [Traffic Manager](https://learn.microsoft.com/en-us/azure/traffic-manager/traffic-manager-overview).
* If you need to optimize global routing of your web traffic and optimize top-tier end-user performance and reliability through quick global failover, see [Front Door](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview).
* To do transport layer load balancing, review [Load Balancer](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-overview).

Your end-to-end scenarios may benefit from combining these solutions as needed. For an Azure load-balancing options comparison, see [Overview of load-balancing options in Azure](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview).

#### Features

To learn about Application Gateway features, see [Azure Application Gateway features](https://learn.microsoft.com/en-us/azure/application-gateway/features).

#### Infrastructure

To learn about Application Gateway infrastructure, see [Azure Application Gateway infrastructure configuration](https://learn.microsoft.com/en-us/azure/application-gateway/configuration-infrastructure).

#### Pricing and SLA

For Application Gateway pricing information, see [Application Gateway pricing](https://azure.microsoft.com/pricing/details/application-gateway/).

For Application Gateway SLA information, see [Application Gateway SLA](https://azure.microsoft.com/support/legal/sla/application-gateway/v1_2/).

#### What's new

To learn what's new with Azure Application Gateway, see [Azure updates](https://azure.microsoft.com/updates/?category=networking&query=Application%20Gateway).

#### Next steps

Depending on your requirements and environment, you can create a test Application Gateway using either the Azure portal, Azure PowerShell, or Azure CLI.

* [Quickstart: Direct web traffic with Azure Application Gateway - Azure portal](https://learn.microsoft.com/en-us/azure/application-gateway/quick-create-portal)
* [Quickstart: Direct web traffic with Azure Application Gateway - Azure PowerShell](https://learn.microsoft.com/en-us/azure/application-gateway/quick-create-powershell)
* [Quickstart: Direct web traffic with Azure Application Gateway - Azure CLI](https://learn.microsoft.com/en-us/azure/application-gateway/quick-create-cli)
* [Learn module: Introduction to Azure Application Gateway](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-application-gateway)
* [How an application gateway works](https://learn.microsoft.com/en-us/azure/application-gateway/how-application-gateway-works)
* [Frequently asked questions about Azure Application Gateway](https://learn.microsoft.com/en-us/azure/application-gateway/application-gateway-faq)

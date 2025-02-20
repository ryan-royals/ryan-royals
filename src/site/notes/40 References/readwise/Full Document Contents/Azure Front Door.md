---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-front-door/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_iGQZ1il.png)

#### In this article

1. [Why use Azure Front Door?](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#why-use-azure-front-door)
2. [Key Benefits](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#key-benefits)
3. [How to choose between Azure Front Door tiers?](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#how-to-choose-between-azure-front-door-tiers)
4. [Where is the service available?](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#where-is-the-service-available)
5. [Pricing](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#pricing)
6. [What's new?](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#whats-new)
7. [Next steps](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview#next-steps)

Whether you’re delivering content and files or building global apps and APIs, Azure Front Door can help you deliver higher availability, lower latency, greater scale, and more secure experiences to your users wherever they are.

Azure Front Door is Microsoft’s modern cloud Content Delivery Network (CDN) that provides fast, reliable, and secure access between your users and your applications’ static and dynamic web content across the globe. Azure Front Door delivers your content using Microsoft’s global edge network with hundreds of [global and local points of presence (PoPs)](https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region) distributed around the world close to both your enterprise and consumer end users.

[![Diagram of Azure Front Door routing user traffic to endpoints.](https://learn.microsoft.com/en-us/azure/frontdoor/media/overview/front-door-overview.png)](https://learn.microsoft.com/en-us/azure/frontdoor/media/overview/front-door-overview-expanded.png#lightbox)
Note

For web workloads, we highly recommend utilizing [**Azure DDoS protection**](https://learn.microsoft.com/en-us/azure/ddos-protection/ddos-protection-overview) and a [**web application firewall**](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview) to safeguard against emerging DDoS attacks. Another option is to employ [**Azure Front Door**](https://learn.microsoft.com/en-us/azure/frontdoor/web-application-firewall) along with a web application firewall. Azure Front Door offers [**platform-level protection**](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-ddos) against network-level DDoS attacks. For more information, see [**security baseline for Azure services**](https://learn.microsoft.com/en-us/security/benchmark/azure/security-baselines-overview).

#### Why use Azure Front Door?

Azure Front Door enables internet-facing application to:

* **Build and operate modern internet-first architectures** that have dynamic, high-quality digital experiences with highly automated, secure, and reliable platforms.
* **Accelerate and deliver your app and content globally** at scale to your users wherever they're creating opportunities for you to compete, weather change, and quickly adapt to new demand and markets.
* **Intelligently secure your digital estate** against known and new threats with intelligent security that embrace a ***Zero Trust*** framework.

#### Key Benefits

##### Global delivery scale using Microsoft’s network

Scale out and improve performance of your applications and content using Microsoft’s global Cloud CDN and WAN.

* Leverage over [118 edge locations](https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region) across 100 metro cities connected to Azure using a private enterprise-grade WAN and improve latency for apps by up to 3 times.
* Accelerate application performance by using Front Door’s [anycast](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-traffic-acceleration#select-the-front-door-edge-location-for-the-request-anycast) network and [split TCP](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-traffic-acceleration#connect-to-the-front-door-edge-location-split-tcp) connections.
* Terminate SSL offload at the edge and use integrated [certificate management](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-configure-https-custom-domain).
* Natively support end-to-end IPv6 connectivity and the HTTP/2 protocol.

##### Deliver modern apps and architectures

Modernize your internet first applications on Azure with Cloud Native experiences

* Integrate with DevOps friendly command line tools across SDKs of different languages, Bicep, ARM templates, CLI and PowerShell.
* Define your own [custom domain](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-add-custom-domain) with flexible domain validation.
* Load balance and route traffic across [origins](https://learn.microsoft.com/en-us/azure/frontdoor/origin) and use intelligent [health probe](https://learn.microsoft.com/en-us/azure/frontdoor/health-probes) monitoring across apps or content hosted in Azure or anywhere.
* Integrate with other Azure services such as DNS, Web Apps, Storage and many more for domain and origin management.
* Move your routing business logic to the edge with [enhanced rules engine](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-rules-engine) capabilities including regular expressions and server variables.
* Analyze [built-in reports](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-reports) with an all-in-one dashboard for both Front Door and security patterns.
* [Monitoring your Front Door traffic in real time](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-monitor-metrics), and configure alerts that integrate with Azure Monitor.
* [Log each Front Door request](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/how-to-logs) and failed health probes.

##### Simple and cost-effective

* Unified static and dynamic delivery offered in a single tier to accelerate and scale your application through caching, SSL offload, and layer 3-4 DDoS protection.
* Free, [autorotation managed SSL certificates](https://learn.microsoft.com/en-us/azure/frontdoor/end-to-end-tls) that save time and quickly secure apps and content.
* Low entry fee and a simplified cost model that reduces billing complexity by having fewer meters needed to plan for.
* Azure to Front Door integrated egress pricing that removes the separate egress charge from Azure regions to Azure Front Door. Refer to [Azure Front Door pricing](https://azure.microsoft.com/pricing/details/frontdoor/) for more details.

##### Intelligent secure internet perimeter

* Secure applications with built-in layer 3-4 DDoS protection, seamlessly attached [Web Application Firewall (WAF)](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/afds-overview), and [Azure DNS to protect your domains](https://learn.microsoft.com/en-us/azure/frontdoor/how-to-configure-endpoints).
* Protect your applications against layer 7 DDoS attacks using WAF. For more information, see [Application DDoS protection](https://learn.microsoft.com/en-us/azure/web-application-firewall/shared/application-ddos-protection).
* Protect your applications from malicious actors with Bot manager rules based on Microsoft’s own Threat Intelligence.
* Privately connect to your backend behind Azure Front Door with [Private Link](https://learn.microsoft.com/en-us/azure/frontdoor/private-link) and embrace a zero-trust access model.
* Provide a centralized security experience for your application via Azure Policy and Azure Advisor that ensures consistent security features across apps.

#### How to choose between Azure Front Door tiers?

For a comparison of supported features in Azure Front Door, see [Tier comparison](https://learn.microsoft.com/en-us/azure/frontdoor/standard-premium/tier-comparison).

#### Where is the service available?

Azure Front Door Classic/Standard/Premium SKUs are available in Microsoft Azure (Commercial) and Azure Front Door Classic SKU is available in Microsoft Azure Government (US).

#### Pricing

For pricing information, see [Front Door Pricing](https://azure.microsoft.com/pricing/details/frontdoor/). For information about service-level agreements, See [SLA for Azure Front Door](https://azure.microsoft.com/support/legal/sla/frontdoor/v1_0/).

#### What's new?

Subscribe to the RSS feed and view the latest Azure Front Door feature updates on the [Azure Updates](https://azure.microsoft.com/updates/?category=networking&query=Azure%20Front%20Door) page.

#### Next steps

* Learn about [Azure Front Door routing architecture](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-routing-architecture)
* Learn how to [create an Azure Front Door profile](https://learn.microsoft.com/en-us/azure/frontdoor/create-front-door-portal).
* [Learn module: Introduction to Azure Front Door](https://learn.microsoft.com/en-us/training/modules/intro-to-azure-front-door/).

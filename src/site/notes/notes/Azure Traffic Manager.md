---
{"dg-publish":true,"permalink":"/notes/azure-traffic-manager/","tags":["notes"]}
---


Azure Traffic Manager is a [[notes/OSI Networking Model#Layer 7 - Application\|DNS-based (Layer 7)]] traffic load balancer. This service allows you to distribute traffic to your public facing applications across the global Azure regions. Traffic Manager also provides your public endpoints with high availability and quick responsiveness. Traffic Manager can surface Azure Endpoints, External Endpoints or Nested Endpoints (Other Traffic Manager instances).

Traffic Manager uses DNS to direct the client requests to the appropriate service endpoint based on a traffic-routing method. Traffic manager also provides health monitoring for every endpoint. The endpoint can be any Internet-facing service hosted inside or outside of Azure. Traffic Manager provides a range of traffic-routing methods and endpoint monitoring options to suit different application needs and automatic failover models. Traffic Manager is resilient to failure, including the failure of an entire Azure region.[^1]  

![Azure Traffic Manager-1722579023803.png](/img/user/attachments/image/Azure%20Traffic%20Manager-1722579023803.png)  

![Azure Traffic Manager-1722579043312.png](/img/user/attachments/image/Azure%20Traffic%20Manager-1722579043312.png)

## Key Features

**Increase application availability** - Traffic Manager delivers high availability for your critical applications by monitoring your endpoints and providing automatic failover when an endpoint goes down.  
**Improve application performance** - Azure allows you to run cloud services and websites in datacentres located around the world. Traffic Manager can improve the responsiveness of your website by directing traffic to the endpoint with the lowest latency.  
**Service maintenance without downtime** - You can have planned maintenance done on your applications without downtime. Traffic Manager can direct traffic to alternative endpoints while the maintenance is in progress.  
**Combine hybrid applications** - Traffic Manager supports external, non-Azure endpoints enabling it to be used with hybrid cloud and on-premises deployments, including the burst-to-cloud, migrate-to-cloud, and failover-to-cloud scenarios.  
**Distribute traffic for complex deployments** - Using nested Traffic Manager profiles, multiple traffic-routing methods can be combined to create sophisticated and flexible rules to scale to the needs of larger, more complex deployments.

## Traffic Routing Methods

| Routing Method | When to use                                                                                                                                                                                                                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Priority       | Select this routing method when you want to have a primary service endpoint for all traffic. You can provide multiple backup endpoints in case the primary or one of the backup endpoints is unavailable.                                                                                                                                                        |
| Weighted       | Select this routing method when you want to distribute traffic across a set of endpoints based on their weight. Set the weight the same to distribute evenly across all endpoints.                                                                                                                                                                               |
| Performance    | Select the routing method when you have endpoints in different geographic locations, and you want end users to use the "closest" endpoint for the lowest network latency.                                                                                                                                                                                        |
| Geographic     | Select this routing method to direct users to specific endpoints (Azure, External, or Nested) based on where their DNS queries originate from geographically. With this routing method, it enables you to be compliant with scenarios such as data sovereignty mandates, localization of content & user experience and measuring traffic from different regions. |
| MultiValue     | Select this routing method for Traffic Manager profiles that can only have IPv4/IPv6 addresses as endpoints. When a query is received for this profile, all healthy endpoints are returned.                                                                                                                                                                      |
| Subnet         | Select this routing method to map sets of end-user IP address ranges to a specific endpoint. When a request is received, the endpoint returned will be the one mapped for that request’s source IP address.                                                                                                                                                      |

## Nested Traffic Manager Profiles

Each Traffic Manager profile can only specify one traffic-routing method. However, you may have scenarios that require more complicated traffic routing than the routing that can be provided by a single Traffic Manager profile. In these situations, you can combine traffic routing methods by using nested Traffic Manager profiles to gain the benefits of multiple traffic-routing methods. Nested profiles enable you to override the default Traffic Manager behavior to support larger and more complex traffic-routing configurations for your application deployments.

The example and diagrams below illustrate the combining of the **Performance** and **Weighted** traffic-routing methods in nested profiles.

| Performance | ![Azure Traffic Manager-1722579455577.png](/img/user/attachments/image/Azure%20Traffic%20Manager-1722579455577.png) |
| ----------- | -------------------------------------------- |
| Weighted    | ![Azure Traffic Manager-1722579463217.png](/img/user/attachments/image/Azure%20Traffic%20Manager-1722579463217.png) |

[^1]: [Explore Azure Traffic Manager - Training](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/5-explore-azure-traffic-manager)

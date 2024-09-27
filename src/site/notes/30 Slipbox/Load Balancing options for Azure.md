---
{"dg-publish":true,"dg-path":"Load Balancing options for Azure.md","permalink":"/load-balancing-options-for-azure/","tags":["notes"]}
---


Azure provides various load balancing services that you can use to distribute your workloads across multiple computing resources, but the following are the main services:

- **[[30 Slipbox/Azure Load Balancer\|Azure Load Balancer]]** - high-performance, ultra-low-latency [[30 Slipbox/OSI Networking Model#Layer 4 - Transport\|Layer 4]] load-balancing service (inbound and outbound) for all UDP and TCP protocols. It's built to handle millions of requests per second while ensuring your solution is highly available. Azure Load Balancer is zone-redundant, ensuring high availability across Availability Zones.
- **[[30 Slipbox/Azure Traffic Manager\|Azure Traffic Manager]]** - DNS-based traffic load balancer that enables you to distribute traffic optimally to services across global Azure regions, while providing high availability and responsiveness. Because Traffic Manager is a DNS-based load-balancing service, it load-balances only at the domain level. For that reason, it can't fail over as quickly as Front Door, because of common challenges around DNS caching and systems not honouring DNS time-to-live values (TTLs).
- **[[30 Slipbox/Azure Application Gateway\|Azure Application Gateway]]** - provides application delivery controller (ADC) as a service, offering various [[30 Slipbox/OSI Networking Model#Layer 7 - Application\|Layer 7]] load-balancing capabilities. Use it to optimize web farm productivity by offloading CPU-intensive SSL termination to the gateway.
- **[[30 Slipbox/Azure Front Door\|30 Slipbox/Azure Front Door]]** - application delivery network that provides global load balancing and site acceleration service for web applications. It offers [[30 Slipbox/OSI Networking Model#Layer 7 - Application\|Layer 7]] capabilities for your application like SSL offload, path-based routing, fast failover, caching, etc. to improve performance and high-availability of your applications.[^1]

![Load Balancing options for Azure-1721690987028.png](/img/user/40%20References/attachments/image/Load%20Balancing%20options%20for%20Azure-1721690987028.png)

| Service             | Global/regional    | Recommended traffic |
| ------------------- | ------------------ | ------------------- |
| Azure Front Door    | Global             | HTTP(S)             |
| Traffic Manager     | Global             | non-HTTP(S)         |
| Application Gateway | Regional           | HTTP(S)             |
| Azure Load Balancer | Regional or Global | non-HTTP(S)         |

[^1]: [[40 References/readwise/Explore Load Balancing - Training\|Explore Load Balancing - Training]]raining]]

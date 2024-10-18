---
{"dg-publish":true,"permalink":"/40-references/readwise/design-and-implement-azure-load-balancer-using-the-azure-portal-training/","tags":["rw/articles"]}
---

![40 References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg](/img/user/40%20References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/3-design-implement-azure-load-balancer-using-azure-portal
Author: wwlpublish

## Summary

The Azure Load Balancer distributes incoming traffic to backend pool instances, which can be Azure Virtual Machines. You can create both public and internal load balancers depending on your needs, and they can be configured for high availability across different zones. To set up a load balancer, you must create it in the Azure portal, add a backend pool, set health probes, and establish load balancing rules.

## Highlights added August 30, 2024 at 2:23 PM
>**Azure Load Balancer** operates at layer 4 of the Open Systems Interconnection (OSI) model. It's the single point of contact for clients. Azure Load Balancer distributes inbound flows that arrive at the load balancer's front end to backend pool instances. These flows are according to configured load-balancing rules and health probes. The backend pool instances can be Azure Virtual Machines or instances in a virtual machine scale set. ([View Highlight] (https://read.readwise.io/read/01j3ps7skya9jwt79g94q2084k))


>Azure services that support availability zones fall into three categories:
>• Zonal services: Resources can be pinned to a specific zone. For example, virtual machines, managed disks, or standard IP addresses can be pinned to a specific zone, which allows for increased resilience by having one or more instances of resources spread across zones.
>• Zone-redundant services: Resources are replicated or distributed across zones automatically. Azure replicates the data across three zones so that a zone failure doesn't impact its availability.
>• Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages and region-wide outages. ([View Highlight] (https://read.readwise.io/read/01j3y3mqwap5sc3ftkt0j2besa))


>***Features***
>**Standard Load Balancer**
>**Basic Load Balancer**
>Backend pool size
>Supports up to 1000 instances.
>Supports up to 300 instances.
>Backend pool endpoints
>Any virtual machines or virtual machine scale sets in a single virtual network.
>Virtual machines in a single availability set or virtual machine scale set.
>Health probes
>TCP, HTTP, HTTPS
>TCP, HTTP
>Health probe down behavior
>TCP connections stay alive on an instance probe down and on all probes down.
>TCP connections stay alive on an instance probe down. All TCP connections end when all probes are down.
>Availability Zones
>Zone-redundant and zonal frontends for inbound and outbound traffic.
>Not available
>Diagnostics
>Azure Monitor multi-dimensional metrics
>[Azure Monitor logs](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-monitor-log)
>HA Ports
>Available for Internal Load Balancer
>Not available
>Secure by default
>Closed to inbound flows unless allowed by a network security group. Internal traffic from the virtual network to the internal load balancer is allowed.
>Open by default. Network security group optional.
>Outbound Rules
>Declarative outbound NAT configuration
>Not available
>TCP Reset on Idle
>Available on any rule
>Not available
>Multiple front ends
>Inbound and outbound
>Inbound only
>Management Operations
>Most operations < 30 seconds
>60-90+ seconds typical
>SLA
>[99.99%](https://azure.microsoft.com/support/legal/sla/load-balancer/v1_0/)
>Not available
>**Microsoft recommends Standard load balancer. Standalone VMs, availability sets, and virtual machine scale sets can be connected to only one SKU, never both. Load balancer and the public IP address SKU must match when you use them with public IP addresses.**
>**SKUs aren't mutable; therefore, you cannot change the SKU of an existing resource.** ([View Highlight] (https://read.readwise.io/read/01j3y4cfg59cb9fwp82pk9zder))



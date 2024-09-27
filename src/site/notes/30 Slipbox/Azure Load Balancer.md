---
{"dg-publish":true,"dg-path":"Azure Load Balancer.md","permalink":"/azure-load-balancer/","tags":["notes"]}
---

**Azure Load Balancer** operates at [[30 Slipbox/OSI Networking Model#Layer 4 - Transport\|Layer 4 of the Open Systems Interconnnection (OSI) model]]. It's the single point of contact for clients. Azure Load Balancer distributes inbound flows that arrive at the load balancer's front end to backend pool instances. These flows are according to configured load-balancing rules and health probes. The backend pool instances can be [[30 Slipbox/Azure Virtual Machine\|Azure Virtual Machines]] or instances in a [[30 Slipbox/Azure Virtual Machine Scale Set\|Azure Virtual Machine Scale Set]].[^1]

## SKUs

| ***Features***             | **Standard Load Balancer**                                                                                                                              | **Basic Load Balancer**                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Backend pool size          | Supports up to 1000 instances.                                                                                                                          | Supports up to 300 instances                                                                            |
| Backend pool endpoints     | Any Virtual machines or virtual machine scale sets in a single virtual network.                                                                         | Virtual Machines in a single availability set or virtual machine scale set.                             |
| Health Probes              | TCP, HTTP, HTTPS.                                                                                                                                       | TCP, HTTP.                                                                                              |
| Health probe down behavior | TCP connections stay alive on an instance probe down and on all probes down.                                                                            | TCP connections stay alive on an instance probe down. All TCP connections end when all probes are down. |
| Availability zones         | Zone-redundtant and Zonal frontends for inbound and outbound traffic.                                                                                   | Not available.                                                                                          |
| Diagnostics                | Azure Monitor multi-dimensional metrics.                                                                                                                | [Azure Monitor logs](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-monitor-log).  |
| HA Ports                   | Available for internal Load Balancer.                                                                                                                   | Not available.                                                                                          |
| Secure by default          | Closed to inbound flows unless allowed by a network security group. Internal traffic from the virtual network to the internal load balancer is allowed. | Open by default. Network security group optional.                                                       |
| Outbound Rules             | Declarative outbound NAT configuration.                                                                                                                 | Not available.                                                                                          |
| TCP Reset on Idle          | Available on any rule.                                                                                                                                  | Not available.                                                                                          |
| Multiple front ends        | Inbound and outbound.                                                                                                                                   | Inbound only.                                                                                           |
| Management operations      | Most operations < 30 seconds.                                                                                                                           | 60-90+ seconds typical.                                                                                 |
| SLA                        | [[30 Slipbox/Service Level Agreement\|99.99%]]                                                                                                                     | Not available.                                                                                          |

> [!note]  
> Microsoft recommends Standard load balancer. Standalone VMs, availability sets, and virtual machine scale sets can be connected to only one SKU, never both. Load balancer and the public IP address SKU must match when you use them with public IP addresses.

> [!note]  
> **SKUs aren't mutable; therefore, you cannot change the SKU of an existing resource.**  

[^1]

## Deployment Types

Azure Load Balancer can be deployed as **Public (External)** or **Internal (Private)**.

A **Public** load balancer can provide load balancing for both ingress and egress connectivity to the Internet.  
A **Private** Load balancer is load balancing private ip addresses internal to the Virtual Network and your on-premises network in a hybrid scenario.  
![Azure Load Balancer-1721973357679.png](/img/user/40%20References/attachments/image/Azure%20Load%20Balancer-1721973357679.png)  
[^2]  

## Availability Zones

Azure Load Balancer can either be **[[30 Slipbox/Zone Redundancy in Azure\|Zone Redundant or Zonal]]** . Zone Redundancy is available in the **Standard** SKU.

### Zone Redundant

![Azure Load Balancer-1722219299235.png](/img/user/40%20References/attachments/image/Azure%20Load%20Balancer-1722219299235.png)  

### Zonal

![Azure Load Balancer-1722219304986.png](/img/user/40%20References/attachments/image/Azure%20Load%20Balancer-1722219304986.png)

[^1]:[[40 References/readwise/Design and Implement Azure Load Balancer Using the Azure Portal - Training\|Design and Implement Azure Load Balancer Using the Azure Portal - Training]]raining]]
[^2]: [[40 References/readwise/Azure Load Balancer Components\|Azure Load Balancer Components]]ponents]]

---
{"dg-publish":true,"permalink":"/90-slipbox/azure-load-balancer/","tags":["notes"]}
---

**Azure Load Balancer** operates at [[90_slipbox/OSI Networking Model#Layer 4 - Transport\|Layer 4 of the Open Systems Interconnnection (OSI) model]]. It's the single point of contact for clients. Azure Load Balancer distributes inbound flows that arrive at the load balancer's front end to backend pool instances. These flows are according to configured load-balancing rules and health probes. The backend pool instances can be [[90_slipbox/Azure Virtual Machine\|Azure Virtual Machines]] or instances in a [[90_slipbox/Azure Virtual Machine Scale Set\|Azure Virtual Machine Scale Set]].[^1]

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
| SLA                        | [[90_slipbox/Service Level Agreement\|99.99%]]                                                                                                                     | Not available.                                                                                          |

> [!note]  
> Microsoft recommends Standard load balancer. Standalone VMs, availability sets, and virtual machine scale sets can be connected to only one SKU, never both. Load balancer and the public IP address SKU must match when you use them with public IP addresses.

> [!note]  
> **SKUs aren't mutable; therefore, you cannot change the SKU of an existing resource.**  

[^1]

## Deployment Types

Azure Load Balancer can be deployed as **Public (External)** or **Internal (Private)**.

A **Public** load balancer can provide load balancing for both ingress and egress connectivity to the Internet.  
A **Private** Load balancer is load balancing private ip addresses internal to the Virtual Network and your on-premises network in a hybrid scenario.  
![Azure Load Balancer-1721973357679.png](/img/user/10_attachments/Azure%20Load%20Balancer-1721973357679.png)  
[^2]  

## Availability Zones

Azure Load Balancer can either be **[[90_slipbox/Zone Redundancy in Azure\|Zone Redundant or Zonal]]** . Zone Redundancy is available in the **Standard** SKU.

### Zone Redundant

![Azure Load Balancer-1722219299235.png](/img/user/10_attachments/Azure%20Load%20Balancer-1722219299235.png)  

### Zonal

![Azure Load Balancer-1722219304986.png](/img/user/10_attachments/Azure%20Load%20Balancer-1722219304986.png)

## Outbound Connectivity and SNAT Ports

When a VM creates an outbound flow, Azure translates the source IP address to an ephemeral IP address. This translation is done via SNAT.  
If using SNAT without outbound rules via a public load balancer, SNAT ports are pre-allocated as described in the following default SNAT ports allocation table

To establish an outbound connection, an **ephemeral port** is used to provide the destination with a port on which to communicate and maintain a distinct traffic flow. When these ephemeral ports are used for SNAT, they're called **SNAT ports** (Source NAT).

By definition, every IP address has 65,535 ports. Each port can either be used for inbound or outbound connections for TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). When a public IP address is added as a frontend IP to a load balancer, 64,000 ports are eligible for SNAT.

Each port used in a load balancing or inbound NAT rule consumes a range of eight ports from the 64,000 available SNAT ports. This usage reduces the number of ports eligible for SNAT, if the same frontend IP is used for outbound connectivity. If load-balancing or inbound NAT rules consumed ports are in the same block of eight ports consumed by another rule, the rules don't require extra ports.  

When the load-balancing rules are configured to use default port allocation, or when the outbound rules have the **Use the default number of outbound ports** setting configured, SNAT ports are allocated by default based on the backend pool size. The backend will receive the number of ports defined by the table, per frontend IP, up to a maximum of 1,024 ports.  
[^3]

### Default Port Allocation Table

| Pool size (VM instances) | Default SNAT ports |
| ------------------------ | ------------------ |
| 1-50                     | 1,024              |
| 51-100                   | 512                |
| 101-200                  | 256                |
| 201-400                  | 128                |
| 401-800                  | 64                 |
| 801-1,000                | 32                 |

[^3]

## References

[^1]:[Design and Implement Azure Load Balancer Using the Azure Portal - Training](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/3-design-implement-azure-load-balancer-using-azure-portal)
[^2]: [Azure Load Balancer Components](https://learn.microsoft.com/en-us/azure/load-balancer/components)
[^3]: [Source Network Address Translation (SNAT) for outbound connections - Azure Load Balancer - Micros...](https://learn.microsoft.com/en-gb/azure/load-balancer/load-balancer-outbound-connections)

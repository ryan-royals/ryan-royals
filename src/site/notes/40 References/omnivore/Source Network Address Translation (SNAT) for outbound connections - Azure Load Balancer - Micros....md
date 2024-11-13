---
{"dg-publish":true,"permalink":"/40-references/omnivore/source-network-address-translation-snat-for-outbound-connections-azure-load-balancer-micros/","tags":["omnivore"]}
---


- Article

Certain scenarios require virtual machines or compute instances to have outbound connectivity to the internet. The frontend IPs of a public load balancer can be used to provide outbound connectivity to the internet for backend instances. This configuration uses **source network address translation (SNAT)** to translate virtual machine's private IP into the load balancer's public IP address. SNAT maps the IP address of the backend to the public IP address of your load balancer. SNAT prevents outside sources from having a direct address to the backend instances.

## Azure's Outbound Connectivity Methods

The following methods are Azure's most commonly used methods to enable outbound connectivity:

| # | Method                                                                                                                 | Type of port allocation | Production-grade?     | Rating |
| - | ---------------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------- | ------ |
| 1 | Use the frontend IP address(es) of a load balancer for outbound via outbound rules                                     | Static, explicit        | Yes, but not at scale | OK     |
| 2 | Associate a NAT gateway to the subnet                                                                                  | Dynamic, explicit       | Yes                   | Best   |
| 3 | Assign a public IP to the virtual machine                                                                              | Static, explicit        | Yes                   | OK     |
| 4 | [Default outbound access](https://learn.microsoft.com/en-gb/azure/virtual-network/ip-services/default-outbound-access) | Implicit                | No                    | Worst  |

![Diagram of Azure outbound options.](https://proxy-prod.omnivore-image-cache.app/0x0,skEZmI3ft8D674gQky47ATZj2pb2Ih-ZKEu06y3xEoIM/https://learn.microsoft.com/en-gb/azure/load-balancer/media/load-balancer-outbound-connections/outbound-options.png)

## 1\. Use the Frontend IP Address of a Load Balancer for Outbound via Outbound Rules

![Diagram public load balancer with outbound rules.](https://proxy-prod.omnivore-image-cache.app/0x0,s74MFZx-CbScVspFd3X09snS2LrS8N5SyxTohK7anQAM/https://learn.microsoft.com/en-gb/azure/load-balancer/media/load-balancer-outbound-connections/public-load-balancer-outbound.png)

Outbound rules enable you to explicitly define SNAT (source network address translation) for a standard SKU public load balancer. This configuration allows you to use the public IP or IPs of your load balancer for outbound connectivity of the backend instances.

This configuration enables:

- IP masquerading
- Simplifying your allowlists
- Reduces the number of public IP resources for deployment

With outbound rules, you have full declarative control over outbound internet connectivity. Outbound rules allow you to scale and tune this ability to your specific needs via manual port allocation. Manually allocating SNAT port based on the backend pool size and number of **frontendIPConfigurations** can help avoid SNAT exhaustion.

You can manually allocate SNAT ports either by "ports per instance" or "maximum number of backend instances". If you have virtual machines in the backend, it's recommended that you allocate ports by "ports per instance" to get maximum SNAT port usage.

Calculate ports per instance as follows:

**Number of frontend IPs \* 64K / Number of backend instances**

If you have Virtual Machine Scale Sets in the backend, it's recommended to allocate ports by "maximum number of backend instances". If more VMs are added to the backend than remaining SNAT ports allowed, scale out of Virtual Machine Scale Sets could be blocked, or the new VMs won't receive sufficient SNAT ports.

When multiple frontend IPs are configured using outbound rules, outbound connections may come from any of the frontend IPs configured to the backend instance. We do not recommend building any dependencies on which frontend IP may be selected for connections.

For more information about outbound rules, see [Outbound rules](https://learn.microsoft.com/en-gb/azure/load-balancer/outbound-rules).

## 2\. Associate a NAT Gateway to the Subnet

![Diagram of a NAT gateway and public load balancer.](https://proxy-prod.omnivore-image-cache.app/0x0,ske3COXnJF1ii618zbT1dJNC6fvIr6mkJ7iJYPMLiuKY/https://learn.microsoft.com/en-gb/azure/load-balancer/media/load-balancer-outbound-connections/nat-gateway.png)

Azure NAT Gateway simplifies outbound-only Internet connectivity for virtual networks. When configured on a subnet, all outbound connectivity uses your specified static public IP addresses. Outbound connectivity is possible without load balancer or public IP addresses directly attached to virtual machines. NAT Gateway is fully managed and highly resilient.

Using a NAT gateway is the best method for outbound connectivity. A NAT gateway is highly extensible, reliable, and doesn't have the same concerns of SNAT port exhaustion.

NAT gateway takes precedence over other outbound connectivity methods, including a load balancer, instance-level public IP addresses, and Azure Firewall.

For more information about Azure NAT Gateway, see [What is Azure NAT Gateway](https://learn.microsoft.com/en-gb/azure/virtual-network/nat-gateway/nat-overview).

## 3\. Assign a Public IP to the Virtual Machine

![Diagram of virtual machines with instance level public IP addresses.](https://proxy-prod.omnivore-image-cache.app/0x0,sV4rCmhV2OHNwJs-nLdN7Zsy_jR9LmCVDNqkbNB8h0g0/https://learn.microsoft.com/en-gb/azure/load-balancer/media/load-balancer-outbound-connections/instance-level-public-ip.png)

| Associations          | Method                                                 | IP protocols                                                                                                                                      |
| --------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Public IP on VM's NIC | SNAT (Source Network Address Translation)  isn't used. | TCP (Transmission Control Protocol)  UDP (User Datagram Protocol)  ICMP (Internet Control Message Protocol)  ESP (Encapsulating Security Payload) |

Traffic returns to the requesting client from the virtual machine's public IP address (Instance Level IP).

Azure uses the public IP assigned to the IP configuration of the instance's NIC for all outbound flows. The instance has all ephemeral ports available. It doesn't matter whether the VM is load balanced or not. This scenario takes precedence over the others, except for NAT Gateway.

A public IP assigned to a VM is a 1:1 relationship (rather than 1: many) and implemented as a stateless 1:1 NAT.

## 4\. Default Outbound Access

![Diagram of default outbound access.](https://proxy-prod.omnivore-image-cache.app/0x0,sMV3F3V2o8Y-OhDa6ja1lTzuLZctihAjMmofWU28ZxNs/https://learn.microsoft.com/en-gb/azure/load-balancer/media/load-balancer-outbound-connections/default-outbound-access.png)

In Azure, virtual machines created in a virtual network without explicit outbound connectivity defined are assigned a default outbound public IP address. This IP address enables outbound connectivity from the resources to the Internet. This access is referred to as [default outbound access](https://learn.microsoft.com/en-gb/azure/virtual-network/ip-services/default-outbound-access). This method of access is **not recommended** as it's insecure and the IP addresses are subject to change.

 Important

On September 30, 2025, default outbound access for new deployments will be retired. For more information, see the [official announcement](https://azure.microsoft.com/updates/upgrade-to-standard-sku-public-ip-addresses-in-azure-by-30-september-2025-basic-sku-will-be-retired/). It is recommended to use one the explicit forms of connectivity as shown in options 1-3 above.

### What Are SNAT Ports?

Ports are used to generate unique identifiers used to maintain distinct flows. The internet uses a five-tuple to provide this distinction.

If a port is used for inbound connections, it has a **listener** for inbound connection requests on that port. That port can't be used for outbound connections. To establish an outbound connection, an **ephemeral port** is used to provide the destination with a port on which to communicate and maintain a distinct traffic flow. When these ephemeral ports are used for SNAT, they're called **SNAT ports**.

By definition, every IP address has 65,535 ports. Each port can either be used for inbound or outbound connections for TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). When a public IP address is added as a frontend IP to a load balancer, 64,000 ports are eligible for SNAT.

Each port used in a load balancing or inbound NAT rule consumes a range of eight ports from the 64,000 available SNAT ports. This usage reduces the number of ports eligible for SNAT, if the same frontend IP is used for outbound connectivity. If load-balancing or inbound NAT rules consumed ports are in the same block of eight ports consumed by another rule, the rules don't require extra ports.

 Note

If you need to connect to any [supported Azure PaaS services](https://learn.microsoft.com/en-gb/azure/private-link/availability) like Azure Storage, Azure SQL, or Azure Cosmos DB, you can use Azure Private Link to avoid SNAT entirely. Azure Private Link sends traffic from your virtual network to Azure services over the Azure backbone network instead of over the internet.

Private Link is the recommended option over service endpoints for private access to Azure hosted services. For more information on the difference between Private Link and service endpoints, see [Compare Private Endpoints and Service Endpoints](https://learn.microsoft.com/en-gb/azure/virtual-network/vnet-integration-for-azure-services#compare-private-endpoints-and-service-endpoints).

### How Does Default SNAT Work?

When a VM creates an outbound flow, Azure translates the source IP address to an ephemeral IP address. This translation is done via SNAT.

If using SNAT without outbound rules via a public load balancer, SNAT ports are pre-allocated as described in the following default SNAT ports allocation table:

## Default Port Allocation Table

When load balancing rules are selected to use default port allocation, or outbound rules are configured with "Use the default number of outbound ports", SNAT ports are allocated by default based on the backend pool size. Backends receive the number of ports defined by the table, per frontend IP, up to a maximum of 1024 ports.

As an example, with 100 VMs in a backend pool and only one frontend IP, each VM receives 512 ports. If a second frontend IP is added, each VM receives an extra 512 ports. This means each VM is allocated a total of 1,024 ports. As a result, adding a third frontend IP will NOT increase the number of allocated SNAT ports beyond 1024 ports.

As a rule of thumb, the number of SNAT ports provided when default port allocation is applied can be computed as: MIN(# of default SNAT ports provided based on pool size \* number of frontend IPs associated with the pool, 1024)

The following table shows the SNAT port preallocations for a single frontend IP, depending on the backend pool size:

| Pool size (VM instances) | Default SNAT ports |
| ------------------------ | ------------------ |
| 1-50                     | 1,024              |
| 51-100                   | 512                |
| 101-200                  | 256                |
| 201-400                  | 128                |
| 401-800                  | 64                 |
| 801-1,000                | 32                 |

## Port Exhaustion

Every connection to the same destination IP and destination port uses a SNAT port. This connection maintains a distinct **traffic flow** from the backend instance or **client** to a **server**. This process gives the server a distinct port on which to address traffic. Without this process, the client machine is unaware of which flow a packet is part of.

Imagine having multiple browsers going to [https://www.microsoft.com](https://www.microsoft.com/), which is:

- Destination IP = 23.53.254.142
- Destination Port = 443
- Protocol = TCP

Without SNAT ports for the return traffic, the client has no way to separate one query result from another.

Outbound connections can burst. A backend instance can be allocated insufficient ports. Use **connection reuse** functionality within your application. Without **connection reuse**, the risk of SNAT **port exhaustion** is increased.

For more information about connection pooling with Azure App Service, see [Troubleshooting intermittent outbound connection errors in Azure App Service](https://learn.microsoft.com/en-gb/azure/app-service/troubleshoot-intermittent-outbound-connection-errors#avoiding-the-problem)

New outbound connections to a destination IP fail when port exhaustion occurs. Connections succeed when a port becomes available. This exhaustion occurs when the 64,000 ports from an IP address are spread thin across many backend instances. For guidance on mitigation of SNAT port exhaustion, see the [troubleshooting guide](https://learn.microsoft.com/en-gb/azure/load-balancer/troubleshoot-outbound-connection).

## Port Reuse

For TCP connections, the load balancer uses a single SNAT port for every destination IP and port. For connections to the same destination IP, a single SNAT port can be reused as long as the destination port differs. Reuse isn't possible when there already exists a connection to the same destination IP and port.

For UDP connections, the load balancer uses a **port-restricted cone NAT** algorithm, which consumes one SNAT port per destination IP, regardless of the destination port.

Individual ports can be reused for an unlimited number of connections where reuse is permitted (when the destination IP or port is different).

In the example in the following table, a backend instance with private IP 10.0.0.1 is making TCP connections to destination IPs 23.53.254.142 and 26.108.254.155, while the load balancer is configured with frontend IP address 192.0.2.0\. Because the destination IPs are different, the same SNAT port can be reused for multiple connections.

| Flow | Source tuple | Source tuple after SNAT | Destination tuple |
| ---- | ------------ | ----------------------- | ----------------- |
| 1    | 10.0.0.1:80  | 192.0.2.0:1             | 23.53.254.142:80  |
| 2    | 10.0.0.1:80  | 192.0.2.0:1             | 26.108.254.155:80 |

## Constraints

- When a connection is idle with no new packets being sent, the ports will be released after 4 – 120 minutes.
- This threshold can be configured via outbound rules.
- Each IP address provides 64,000 ports that can be used for SNAT.
- Each port can be used for both TCP and UDP connections to a destination IP address
- A UDP SNAT port is needed whether the destination port is unique or not. For every UDP connection to a destination IP, one UDP SNAT port is used.
- A TCP SNAT port can be used for multiple connections to the same destination IP provided the destination ports are different.
- SNAT exhaustion occurs when a backend instance runs out of given SNAT Ports. A load balancer can still have unused SNAT ports. If a backend instance’s used SNAT ports exceed its given SNAT ports, it's unable to establish new outbound connections.
- Fragmented packets are dropped unless outbound is through an instance level public IP on the VM's NIC.
- Secondary IP configurations of a network interface don't provide outbound communication (unless a public IP is associated to it) via a load balancer.

## Next Steps

- [Troubleshoot outbound connection failures because of SNAT exhaustion](https://learn.microsoft.com/en-gb/azure/load-balancer/troubleshoot-outbound-connection)
- [Review SNAT metrics](https://learn.microsoft.com/en-gb/azure/load-balancer/load-balancer-standard-diagnostics#how-do-i-check-my-snat-port-usage-and-allocation) and familiarize yourself with the correct way to filter, split, and view them.
- Learn how to [migrate your existing outbound connectivity method to NAT gateway](https://learn.microsoft.com/en-gb/azure/virtual-network/nat-gateway/tutorial-migrate-outbound-nat)

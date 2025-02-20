---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-load-balancer-components/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Frontend IP configuration](https://learn.microsoft.com/en-us/azure/load-balancer/components#frontend-ip-configuration-)
2. [Backend pool](https://learn.microsoft.com/en-us/azure/load-balancer/components#backend-pool)
3. [Health probes](https://learn.microsoft.com/en-us/azure/load-balancer/components#health-probes)
4. [Load Balancer rules](https://learn.microsoft.com/en-us/azure/load-balancer/components#load-balancer-rules)
5. [High Availability Ports](https://learn.microsoft.com/en-us/azure/load-balancer/components#high-availability-ports)
6. [Inbound NAT rules](https://learn.microsoft.com/en-us/azure/load-balancer/components#inbound-nat-rules)
7. [Outbound rules](https://learn.microsoft.com/en-us/azure/load-balancer/components#outbound-rules)
8. [Limitations](https://learn.microsoft.com/en-us/azure/load-balancer/components#limitations)
9. [Next step](https://learn.microsoft.com/en-us/azure/load-balancer/components#next-step)

Azure Load Balancer includes a few key components. These components can be configured in your subscription through the Azure portal, Azure CLI, Azure PowerShell, Resource Manager Templates or appropriate alternatives.

#### Frontend IP configuration

The IP address of your Azure Load Balancer. It's the point of contact for clients. These IP addresses can be either:

* **Public IP Address**
* **Private IP Address**

The nature of the IP address determines the **type** of load balancer created. Private IP address selection creates an internal load balancer. Public IP address selection creates a public load balancer.

|  | **Public load balancer** | **Internal load balancer** |
| --- | --- | --- |
| Frontend IP configuration | Public IP address | Private IP address |
| Description | A public load balancer maps the public IP and port of incoming traffic to the private IP and port of the VM. Load balancer maps traffic the other way around for the response traffic from the VM. You can distribute specific types of traffic across multiple VMs or services by applying load-balancing rules. For example, you can spread the load of web request traffic across multiple web servers. | An internal load balancer distributes traffic to resources that are inside a virtual network. Azure restricts access to the frontend IP addresses of a virtual network that are load balanced. Frontend IP addresses and virtual networks are never directly exposed to an internet endpoint, meaning an internal load balancer can't accept incoming traffic from the internet. Internal line-of-business applications run in Azure and are accessed from within Azure or from on-premises resources. |
| SKUs supported | Basic, Standard | Basic, Standard |

![Diagram depicts a load balancer directing traffic.](https://learn.microsoft.com/en-us/azure/load-balancer/media/load-balancer-overview/load-balancer.png)
Load balancer can have multiple frontend IPs. Learn more about [multiple frontends](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-multivip-overview).

#### Backend pool

The group of virtual machines or instances in a virtual machine scale set that is serving the incoming request. To scale cost-effectively to meet high volumes of incoming traffic, computing guidelines generally recommend adding more instances to the backend pool.

Load balancer instantly reconfigures itself via automatic reconfiguration when you scale instances up or down. Adding or removing VMs from the backend pool reconfigures the load balancer without other operations. The scope of the backend pool is any virtual machine in a single virtual network.

Backend pools support addition of instances via [network interface or IP addresses](https://learn.microsoft.com/en-us/azure/load-balancer/backend-pool-management). VMs do not need a public IP address in order to be attached to backend pool of a public load balancer. VMs can be attached to the backend pool of a load balancer even if they are in a stopped state. You can also configure multiple backend pools with different groups of instances to a single load balancer. By creating multiple load balancing rules, each targeting a different backend pool, you can configure traffic to distribute to different sets of backend resources based on the load balancer frontend port and protocol.

When considering how to design your backend pool, design for the least number of individual backend pool resources to optimize the length of management operations. There's no difference in data plane performance or scale.

#### Health probes

A health probe is used to determine the health status of the instances in the backend pool. During load balancer creation, configure a health probe for the load balancer to use. This health probe determines if an instance is healthy and can receive traffic.

You can define the unhealthy threshold for your health probes. When a probe fails to respond, the load balancer stops sending new connections to the unhealthy instances. A probe failure doesn't affect existing connections. The connection continues until the application:

* Ends the flow
* Idle timeout occurs
* The VM shuts down

Load balancer provides different health probe types for endpoints: TCP, HTTP, and HTTPS. [Learn more about Load Balancer Health probes](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-custom-probe-overview).

Basic load balancer doesn't support HTTPS probes. Basic load balancer closes all TCP connections (including established connections).

#### Load Balancer rules

A load balancer rule is used to define how incoming traffic is distributed to **all** the instances within the backend pool. A load-balancing rule maps a given frontend IP configuration and port to multiple backend IP addresses and ports. Load Balancer rules are for inbound traffic only.

For example, use a load balancer rule for port 80 to route traffic from your frontend IP to port 80 of your backend instances.

![Load balancer rule reference diagram](https://learn.microsoft.com/en-us/azure/load-balancer/media/load-balancer-components/lbrules.png)
*Figure: Load-Balancing rules*

#### High Availability Ports

A load balancer rule configured with **'protocol - all and port - 0'** is known as a High Availability (HA) port rule. This rule enables a single rule to load-balance all TCP and UDP flows that arrive on all ports of an internal Standard Load Balancer.

The load-balancing decision is made per flow. This action is based on the following five-tuple connection:

1. source IP address
2. source port
3. destination IP address
4. destination port
5. protocol

The HA ports load-balancing rules help you with critical scenarios, such as high availability and scale for network virtual appliances (NVAs) inside virtual networks. The feature can help when a large number of ports must be load-balanced.

![Diagram of Azure Load Balancer directing all frontend ports to three instances of all backend ports](https://learn.microsoft.com/en-us/azure/load-balancer/media/load-balancer-components/harules.png)
*Figure: HA Ports rules*

Learn more about [HA ports](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-ha-ports-overview).

#### Inbound NAT rules

An inbound NAT rule forwards incoming traffic sent to frontend IP address and port combination. The traffic is sent to a **specific** virtual machine or instance in the backend pool. Port forwarding is done by the same hash-based distribution as load balancing.

![Inbound NAT rule reference diagram](https://learn.microsoft.com/en-us/azure/load-balancer/media/load-balancer-components/inboundnatrules.png)
*Figure: Inbound NAT rules*

Inbound NAT rules in the context of Virtual Machine Scale Sets are inbound NAT pools. Learn more about [Load Balancer components and virtual machine scale set](https://learn.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-networking#azure-virtual-machine-scale-sets-with-azure-load-balancer).

#### Outbound rules

An outbound rule configures outbound Network Address Translation (NAT) for all virtual machines or instances identified by the backend pool. This rule enables instances in the backend to communicate (outbound) to the internet or other endpoints.

Learn more about [outbound connections and rules](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-outbound-connections).

Basic load balancer doesn't support outbound rules.

![Outbound rule reference diagram](https://learn.microsoft.com/en-us/azure/load-balancer/media/load-balancer-components/outbound-rules.png)
*Figure: Outbound rules*

#### Limitations

* Learn about load balancer [limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits)
* Load balancer provides load balancing and port forwarding for specific TCP or UDP protocols. Load-balancing rules and inbound NAT rules support TCP and UDP, but not other IP protocols including ICMP.
* Load Balancer backend pool can't consist of a [Private Endpoint](https://learn.microsoft.com/en-us/azure/private-link/private-endpoint-overview).
* Outbound flow from a backend VM to a frontend of an internal Load Balancer will fail.
* A load balancer rule can't span two virtual networks. All load balancer frontends and their backend instances must be in a single virtual network.
* Forwarding IP fragments isn't supported on load-balancing rules. IP fragmentation of UDP and TCP packets isn't supported on load-balancing rules.
* You can only have one Public Load Balancer (NIC based) and one internal Load Balancer (NIC based) per availability set. However, this constraint doesn't apply to IP-based load balancers.

#### Next step

[Create a public Standard load balancer](https://learn.microsoft.com/en-us/azure/load-balancer/quickstart-load-balancer-standard-public-portal)

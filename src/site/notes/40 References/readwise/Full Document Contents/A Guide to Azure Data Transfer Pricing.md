---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/a-guide-to-azure-data-transfer-pricing/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVJtcFM5Nw?revision=10)

![Icon for Microsoft rank](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/cmstNC05WEo0blc?image-dimensions=100x16&constrain-image=true)
Understanding Azure networking charges is essential for businesses aiming to manage their budgets effectively. Given the complexity of Azure networking pricing, which involves various influencing factors, the goal here is to bring a clearer understanding of the associated data transfer costs by breaking down the pricing models into the following use cases:

* VM to VM
* VM to Private Endpoint
* VM to Internal Standard Load Balancer (ILB)
* VM to Internet
* Hybrid connectivity

Please note this is a first version, with a second version to follow that will include additional scenarios.

**Disclaimer:**

* Pricing may change over time, check the public [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) for up-to-date pricing information.
* Actual pricing may vary depending on agreements, purchase dates, and currency exchange rates.
* Sign in to the [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to see pricing based on your current program/offer with Microsoft.

### 1. VM to VM

#### 1.1. VM to VM, same VNet

Data transfer within the same virtual network (VNet) is free of charge. This means that traffic between VMs within the same VNet will not incur any additional costs. [Doc](https://azure.microsoft.com/en-us/pricing/details/virtual-network/).

Data transfer across Availability Zones (AZ) is free. [Doc](https://azure.microsoft.com/en-us/updates/update-on-interavailability-zone-data-transfer-pricing/).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXNVNzlqdw?image-dimensions=750x750&revision=10)
#### 1.2. VM to VM, across VNet peering

[Azure VNet peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) enables seamless connectivity between two virtual networks, allowing resources in different VNets to communicate with each other as if they were within the same network. When data is transferred between VNets, charges apply for both ingress and egress data. [Doc](https://azure.microsoft.com/en-us/pricing/details/virtual-network/):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVA3b2w0NA?image-dimensions=750x750&revision=10)
##### VM to VM, across VNet peering, same region

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWhxQlN3OA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LTJ2NzBGNQ?image-dimensions=750x750&revision=10)
##### VM to VM, across Global VNet peering

Azure regions are grouped into 3 Zones (distinct from Avaialbility Zones within a specific Azure region). The pricing for Global VNet Peering is based on that geographic structure. Data transfer between VNets in different zones incurs outbound and inbound data transfer rates for the respective zones.

When data is transferred from a VNet in Zone 1 to a VNet in Zone 2, outbound data transfer rates for Zone 1 and inbound data transfer rates for Zone 2 will be applicable. [Doc](https://azure.microsoft.com/en-us/pricing/details/virtual-network/).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXhRaWFieg?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXJlQ2pUUw?image-dimensions=750x750&revision=10)
#### 1.3. VM to VM, through Network Virtual Appliance (NVA)

Data transfer through an NVA involves charges for both ingress and egress data, depending on the volume of data processed.

When an NVA is in the path, such as for spoke VNet to spoke VNet connectivity via an NVA (firewall...) in the hub VNet, it incurs VM to VM pricing twice.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWVIWmd5VA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LTUyZzYzVQ?image-dimensions=750x750&revision=10)
The table above reflects only data transfer charges and does not include NVA/Azure Firewall processing costs.

### 2. VM to Private Endpoint (PE)

Private Endpoint pricing includes charges for the provisioned resource and data transfer costs based on traffic direction. For instance, writing to a Storage Account through a Private Endpoint incurs outbound data charges, while reading incurs inbound data charges. [Doc](https://azure.microsoft.com/en-us/pricing/details/private-link/):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXJraDR4aA?image-dimensions=750x750&revision=10)
#### 2.1. VM to PE, same VNet

Since data transfer within a VNet is free, charges are only applied for data processing through the Private Endpoint.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUd0VGM0Ng?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWMzMGxMWQ?image-dimensions=750x750&revision=10)
Cross-region traffic will incur additional costs if the Storage Account and the Private Endpoint are located in different regions.

#### 2.2. VM to PE, across VNet peering

Accessing Private Endpoints from a peered network **incurs only Private Link Premium charges**, with no peering fees. [Doc](https://azure.microsoft.com/en-us/pricing/details/private-link/).

##### VM to PE, across VNet peering, same region

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWlJT0xXdA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVY2MDljZg?image-dimensions=750x750&revision=10)
##### VM to PE, across VNet peering, PE region != SA region

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVd2aVpBQQ?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWJCWlI1dA?image-dimensions=750x750&revision=10)
#### 2.3. VM to PE, through NVA

When an NVA is in the path, such as for spoke VNet to spoke VNet connectivity via a firewall in the hub VNet, it incurs VM to VM charges between the VM and the NVA. However, as per the PE pricing model, there are no charges between the NVA and the PE.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXBRUlRDcg?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUlHOUhTVQ?image-dimensions=750x750&revision=10)
The table above reflects only data transfer charges and does not include NVA/Azure Firewall processing costs.

### 3. VM to Internal Load Balancer (ILB)

Azure Standard Load Balancer pricing is based on **the number of load balancing rules** as well as **the volume of data processed**. [Doc](https://azure.microsoft.com/en-us/pricing/details/load-balancer/):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LTAycEhSaQ?image-dimensions=750x750&revision=10)
#### 3.1. VM to ILB, same VNet

Data transfer within the same virtual network (VNet) is free. However, the data processed by the ILB is charged based on its volume and on the number load balancing rules implemented. Only the inbound traffic is processed by the ILB (and charged), the return traffic goes direct from the backend to the source VM (free of charge).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVVRRlJURg?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUluUzJ1OQ?image-dimensions=750x750&revision=10)
#### 3.2. VM to ILB, across VNet peering

In addition to the Load Balancer costs, data transfer charges between VNets apply for both ingress and egress.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUxlZ2ppZA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWJTbEtuTA?image-dimensions=750x750&revision=10)
#### 3.3. VM to ILB, through NVA

When an NVA is in the path, such as for spoke VNet to spoke VNet connectivity via a firewall in the hub VNet, it incurs VM to VM charges between the VM and the NVA and VM to ILB charges between the NVA and the ILB/backend resource.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LTU1V1ZEMw?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVdpOEp5bw?image-dimensions=750x750&revision=10)
The table above reflects only data transfer charges and does not include NVA/Azure Firewall processing costs.

### 4. VM to internet

#### 4.1. Data transfer and inter-region pricing model

Bandwidth refers to data moving in and out of Azure data centers, as well as data moving between Azure data centers; other transfers are explicitly covered by the Content Delivery Network, ExpressRoute pricing, or Peering. [Doc](https://azure.microsoft.com/en-us/pricing/details/bandwidth/):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUhjNnBISA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LW1YTWRFbw?image-dimensions=750x750&revision=10)
#### 4.2. Routing Preference in Azure and internet egress pricing model

When creating a public IP in Azure, Azure Routing Preference allows you to choose how your traffic routes between Azure and the Internet. You can select either the Microsoft Global Network or the public internet for routing your traffic. [Doc](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/routing-preference-overview):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUtlUHlybQ?image-dimensions=450x450&revision=10)
See how this choice can impact the performance and reliability of network traffic:

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWppOFBPTA?image-dimensions=750x750&revision=10)
By selecting a Routing Preference set *to Microsoft network*, ingress traffic enters the Microsoft network closest to the user, and egress traffic exits the network closest to the user, minimizing travel on the public internet (“Cold Potato” routing).

On the contrary, setting the Routing Preference to *internet*, ingress traffic enters the Microsoft network closest to the hosted service region. Transit ISP networks are used to route traffic, travel on the Microsoft Global Network is minimized (“Hot Potato” routing).

Bandwidth pricing for internet egress, [Doc](https://azure.microsoft.com/en-us/pricing/details/bandwidth/):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVhJQVJsUQ?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVM4NDJoMw?image-dimensions=750x750&revision=10)
#### 4.3. VM to internet, direct

Data transferred out of Azure to the internet incurs charges, while data transferred into Azure is free of charge. [Doc](https://azure.microsoft.com/en-us/pricing/details/bandwidth/).

It is important to note that default outbound access for VMs in Azure will be retired on September 30 2025, migration to an explicit outbound internet connectivity method is recommended. [Doc](https://azure.microsoft.com/en-gb/updates?id=default-outbound-access-for-vms-in-azure-will-be-retired-transition-to-a-new-method-of-internet-access).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUtYSXpVbw?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXZ2anBjZQ?image-dimensions=750x750&revision=10)
#### 4.4. VM to internet, with a public IP

Here a standard public IP is explicitly associated to a VM NIC, that incurs additional costs. Like in the previous scenario, data transferred out of Azure to the internet incurs charges, while data transferred into Azure is free of charge. [Doc](https://azure.microsoft.com/en-us/pricing/details/bandwidth/).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUQxeU0zOA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVpiMGtZVg?image-dimensions=750x750&revision=10)
#### 4.5. VM to internet, with NAT Gateway

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LTczb3IxUg?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LTJvWTBVWg?image-dimensions=750x750&revision=10)
In addition to the previous costs, data transfer through a NAT Gateway involves charges for both the data processed and the NAT Gateway itself, [Doc](https://azure.microsoft.com/en-us/pricing/details/azure-nat-gateway/?msockid=119137044b2f6af20b15228e4a686bcb):

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWVzMkVNdA?image-dimensions=750x750&revision=10)
### 5. Hybrid connectivity

Hybrid connectivity involves connecting on-premises networks to Azure VNets.

The pricing model includes charges for data transfer between the on-premises network and Azure, as well as any additional costs for using Network Virtual Appliances (NVAs) or Azure Firewalls in the hub VNet.

#### 5.1. H&S Hybrid connectivity without firewall inspection in the hub

For an inbound flow, from the ExpressRoute Gateway to a spoke VNet, VNet peering charges are applied once on the spoke inbound. There are no charges on the hub outbound.

For an outbound flow, from a spoke VNet to an ER branch, VNet peering charges are applied once, outbound of the spoke only. There are no charges on the hub inbound. [Doc](https://techcommunity.microsoft.com/blog/azurenetworkingblog/expressroute-fastpath-for-udrs-and-vnet-peering/4171115).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LVJzNEF5Tg?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LXNTNXYxMw?image-dimensions=750x750&revision=10)
The table above does not include ExpressRoute connectivity related costs.

####  5.2. H&S Hybrid connectivity with firewall inspection in the hub

Since traffic transits and is inspected via a firewall in the hub VNet (Azure Firewall or 3P firewall NVA), the previous concepts do not apply.

“Standard” inter-VNet VM-to-VM charges apply between the FW and the destination VM : inbound and outbound on both directions. Once outbound from the source VNet (Hub or Spoke), once inbound on the destination VNet (Spoke or Hub).

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUpkcTNieA?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWNubkhHUg?image-dimensions=750x750&revision=10)
The table above reflects only data transfer charges within Azure and does not include NVA/Azure Firewall processing costs nor the costs related to ExpressRoute connectivity.

#### 5.3. H&S Hybrid connectivity via a 3rd party connectivity NVA (SDWAN or IPSec)

Standard inter-VNet VM-to-VM charges apply between the NVA and the destination VM: inbound and outbound on both directions, both in the Hub VNet and in the Spoke VNet.

#### 5.4. vWAN scenarios

VNet peering is charged only from the point of view of the spoke – see [examples](https://learn.microsoft.com/en-us/azure/virtual-wan/pricing-concepts) and [vWAN pricing components](https://azure.microsoft.com/en-us/pricing/details/virtual-wan/).

### Next steps with cost management

To optimize cost management, Azure offers tools for monitoring and analyzing network charges. [Azure Cost Management and Billing](https://learn.microsoft.com/en-us/azure/cost-management-billing/cost-management-billing-overview) allows you to track and allocate costs across various services and resources, ensuring transparency and control over your expenses.

![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LUZDaDdoSw?image-dimensions=750x750&revision=10)
![](https://techcommunity.microsoft.com/t5/s/gxcuf89792/images/bS00Mzc0NTM4LWpYZ2pWcg?image-dimensions=750x750&revision=10)
By leveraging these tools, businesses can gain a deeper understanding of their network costs and make informed decisions to optimize their Azure spending.

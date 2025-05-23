---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/scale-snat-ports-with-azure-nat-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Associate a NAT gateway with an Azure Firewall subnet - Azure PowerShell](https://learn.microsoft.com/en-us/azure/firewall/integrate-with-nat-gateway#associate-a-nat-gateway-with-an-azure-firewall-subnet---azure-powershell)
2. [Associate a NAT gateway with an Azure Firewall subnet - Azure CLI](https://learn.microsoft.com/en-us/azure/firewall/integrate-with-nat-gateway#associate-a-nat-gateway-with-an-azure-firewall-subnet---azure-cli)
3. [Next steps](https://learn.microsoft.com/en-us/azure/firewall/integrate-with-nat-gateway#next-steps)

Azure Firewall provides 2,496 SNAT ports per public IP address configured per backend virtual machine scale set instance (Minimum of 2 instances), and you can associate up to [250 public IP addresses](https://learn.microsoft.com/en-us/azure/firewall/deploy-multi-public-ip-powershell). Depending on your architecture and traffic patterns, you might need more than the 1,248,000 available SNAT ports with this configuration. For example, when you use it to protect large [Azure Virtual Desktop deployments](https://learn.microsoft.com/en-us/azure/firewall/protect-azure-virtual-desktop) that integrate with Microsoft 365 Apps.

One of the challenges with using a large number of public IP addresses is when there are downstream IP address filtering requirements. Azure Firewall randomly selects the source public IP address to use for a connection, so you need to allow all public IP addresses associated with it. Even if you use [Public IP address prefixes](https://learn.microsoft.com/en-us/azure/virtual-network/ip-services/public-ip-address-prefix) and you need to associate 250 public IP addresses to meet your outbound SNAT port requirements, you still need to create and allow 16 public IP address prefixes.

A better option to scale and dynamically allocate outbound SNAT ports is to use an [Azure NAT Gateway](https://learn.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-overview). It provides 64,512 SNAT ports per public IP address and supports up to 16 public IP addresses. This effectively provides up to 1,032,192 outbound SNAT ports. Azure NAT Gateway also [dynamically allocates SNAT ports](https://learn.microsoft.com/en-us/azure/nat-gateway/nat-gateway-resource#nat-gateway-dynamically-allocates-snat-ports) on a subnet level, so all the SNAT ports provided by its associated IP addresses is available on demand to provide outbound connectivity.

When a NAT gateway resource is associated with an Azure Firewall subnet, all outbound Internet traffic automatically uses the public IP address of the NAT gateway. There’s no need to configure [User Defined Routes](https://learn.microsoft.com/en-us/azure/virtual-network/tutorial-create-route-table-portal). Response traffic to an outbound flow also passes through NAT gateway. If there are multiple IP addresses associated with the NAT gateway, the IP address is randomly selected. It isn't possible to specify what address to use.

There’s no double NAT with this architecture. Azure Firewall instances send the traffic to NAT gateway using their private IP address rather than Azure Firewall public IP address.

Note

Deploying NAT gateway with a [zone redundant firewall](https://learn.microsoft.com/en-us/azure/firewall/deploy-availability-zone-powershell) is not recommended deployment option, as the NAT gateway does not support zonal deployment at this time. In order to use NAT gateway with Azure Firewall, a zonal Firewall deployment is required.

In addition, Azure NAT Gateway integration is not currently supported in secured virtual hub network (vWAN) architectures. You must deploy using a hub virtual network architecture. For detailed guidance on integrating NAT gateway with Azure Firewall in a hub and spoke network architecture refer to the [NAT gateway and Azure Firewall integration tutorial](https://learn.microsoft.com/en-us/azure/virtual-network/nat-gateway/tutorial-hub-spoke-nat-firewall). For more information about Azure Firewall architecture options, see [What are the Azure Firewall Manager architecture options?](https://learn.microsoft.com/en-us/azure/firewall-manager/vhubs-and-vnets).

#### Associate a NAT gateway with an Azure Firewall subnet - Azure PowerShell

The following example creates and attaches a NAT gateway with an Azure Firewall subnet using Azure PowerShell.

Azure PowerShell 

```
# Create public IP addresses
New-AzPublicIpAddress -Name public-ip-1 -ResourceGroupName nat-rg -Sku Standard -AllocationMethod Static -Location 'South Central US'
New-AzPublicIpAddress -Name public-ip-2 -ResourceGroupName nat-rg -Sku Standard -AllocationMethod Static -Location 'South Central US'

# Create NAT gateway
$PublicIPAddress1 = Get-AzPublicIpAddress -Name public-ip-1 -ResourceGroupName nat-rg
$PublicIPAddress2 = Get-AzPublicIpAddress -Name public-ip-2 -ResourceGroupName nat-rg
New-AzNatGateway -Name firewall-nat -ResourceGroupName nat-rg -PublicIpAddress $PublicIPAddress1,$PublicIPAddress2 -Location 'South Central US' -Sku Standard

# Associate NAT gateway to subnet
$virtualNetwork = Get-AzVirtualNetwork -Name nat-vnet -ResourceGroupName nat-rg
$natGateway = Get-AzNatGateway -Name firewall-nat -ResourceGroupName nat-rg
$firewallSubnet = $virtualNetwork.subnets | Where-Object -Property Name -eq AzureFirewallSubnet
$firewallSubnet.NatGateway = $natGateway
$virtualNetwork | Set-AzVirtualNetwork

```

#### Associate a NAT gateway with an Azure Firewall subnet - Azure CLI

The following example creates and attaches a NAT gateway with an Azure Firewall subnet using Azure CLI.

Azure CLI 

```
# Create public IP addresses
az network public-ip create --name public-ip-1 --resource-group nat-rg --sku standard
az network public-ip create --name public-ip-2 --resource-group nat-rg --sku standard

# Create NAT gateway
az network nat gateway create --name firewall-nat --resource-group nat-rg --public-ip-addresses public-ip-1 public-ip-2

# Associate NAT gateway to subnet
az network vnet subnet update --name AzureFirewallSubnet --vnet-name nat-vnet --resource-group nat-rg --nat-gateway firewall-nat

```

#### Next steps

* For more information, see [Scale Azure Firewall SNAT ports with NAT Gateway for large workloads](https://azure.microsoft.com/blog/scale-azure-firewall-snat-ports-with-nat-gateway-for-large-workloads/).
* [Design virtual networks with NAT gateway](https://learn.microsoft.com/en-us/azure/virtual-network/nat-gateway/nat-gateway-resource)
* [Integrate NAT gateway with Azure Firewall in a hub and spoke network](https://learn.microsoft.com/en-us/azure/virtual-network/nat-gateway/tutorial-hub-spoke-nat-firewall)

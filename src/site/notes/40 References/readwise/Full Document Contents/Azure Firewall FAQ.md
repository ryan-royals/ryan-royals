---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-firewall-faq/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

Azure Firewall is a managed, cloud-based network security service that protects your Azure Virtual Network resources. It's a fully stateful firewall-as-a-service with built-in high availability and unrestricted cloud scalability. You can centrally create, enforce, and log application and network connectivity policies across subscriptions and virtual networks.

To learn about Azure Firewall features, see [Azure Firewall features](https://learn.microsoft.com/en-us/azure/firewall/features).

You can deploy Azure Firewall on any virtual network, but customers typically deploy it on a central virtual network and peer other virtual networks to it in a hub-and-spoke model. You can then set the default route from the peered virtual networks to point to this central firewall virtual network. Global VNet peering is supported, but it isn't recommended because of potential performance and latency issues across regions. For best performance, deploy one firewall per region.

The advantage of this model is the ability to centrally exert control on multiple spoke VNETs across different subscriptions. There are also cost savings as you don't need to deploy a firewall in each VNet separately. The cost savings should be measured versus the associate peering cost based on the customer traffic patterns.

You can set up Azure Firewall by using the Azure portal, PowerShell, REST API, or by using templates. See [Tutorial: Deploy and configure Azure Firewall using the Azure portal](https://learn.microsoft.com/en-us/azure/firewall/tutorial-firewall-deploy-portal) for step-by-step instructions.

Azure Firewall supports rules and rule collections. A rule collection is a set of rules that share the same order and priority. Rule collections are executed in order of their priority. Network rule collections are higher priority than application rule collections, and all rules are terminating.

There are three types of rule collections:

* *Application rules*: Configure fully qualified domain names (FQDNs) that can be accessed from a Virtual Network.
* *Network rules*: Configure rules that contain source addresses, protocols, destination ports, and destination addresses.
* *NAT rules*: Configure DNAT rules to allow incoming Internet connections.

Azure Firewall supports inbound and outbound filtering. Inbound protection is typically used for non-HTTP protocols like RDP, SSH, and FTP protocols. For inbound HTTP and HTTPS protection, use a web application firewall such as [Azure Web Application Firewall (WAF)](https://learn.microsoft.com/en-us/azure/web-application-firewall/overview) or the TLS offload and deep packet inspection capabilities of [Azure Firewall Premium](https://learn.microsoft.com/en-us/azure/firewall/premium-features).

Azure Firewall is integrated with Azure Monitor for viewing and analyzing firewall logs. Logs can be sent to Log Analytics, Azure Storage, or Event Hubs. They can be analyzed in Log Analytics or by different tools such as Excel and Power BI. For more information, see [Tutorial: Monitor Azure Firewall logs](https://learn.microsoft.com/en-us/azure/firewall/firewall-diagnostics).

Azure Firewall is a managed, cloud-based network security service that protects your virtual network resources. It's a fully stateful firewall as a service with built-in high availability and unrestricted cloud scalability. It is pre-integrated with third-party security as a service (SECaaS) providers to provide advanced security for your virtual network and branch Internet connections. To learn more about Azure network security, see [Azure network security](https://learn.microsoft.com/en-us/azure/networking/security/).

The Web Application Firewall (WAF) is a feature of Application Gateway that provides centralized inbound protection of your web applications from common exploits and vulnerabilities. Azure Firewall provides inbound protection for non-HTTP/S protocols (for example, RDP, SSH, FTP), outbound network-level protection for all ports and protocols, and application-level protection for outbound HTTP/S.

The Azure Firewall service complements network security group functionality. Together, they provide better "defense-in-depth" network security. Network security groups provide distributed network layer traffic filtering to limit traffic to resources within virtual networks in each subscription. Azure Firewall is a fully stateful, centralized network firewall as-a-service, which provides network- and application-level protection across different subscriptions and virtual networks.

Azure Firewall is a managed service with multiple protection layers, including platform protection with NIC level NSGs (not viewable). Subnet level NSGs aren't required on the AzureFirewallSubnet, and are disabled to ensure no service interruption.

For secure access to PaaS services, we recommend service endpoints. You can choose to enable service endpoints in the Azure Firewall subnet and disable them on the connected spoke virtual networks. This way you benefit from both features: service endpoint security and central logging for all traffic.

See [Azure Firewall Pricing](https://azure.microsoft.com/pricing/details/azure-firewall/).

You can use Azure PowerShell *deallocate* and *allocate* methods. For a firewall configured for forced tunneling, the procedure is slightly different.

For example, for a firewall NOT configured for forced tunneling:

Azure PowerShell 

```
# Stop an existing firewall

$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "RG Name"
$azfw.Deallocate()
Set-AzFirewall -AzureFirewall $azfw

```

Azure PowerShell 

```
# Start the firewall

$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "RG Name"
$vnet = Get-AzVirtualNetwork -ResourceGroupName "RG Name" -Name "VNet Name"
$publicip1 = Get-AzPublicIpAddress -Name "Public IP1 Name" -ResourceGroupName "RG Name"
$publicip2 = Get-AzPublicIpAddress -Name "Public IP2 Name" -ResourceGroupName "RG Name"
$azfw.Allocate($vnet,@($publicip1,$publicip2))

Set-AzFirewall -AzureFirewall $azfw

```

For a firewall configured for forced tunneling, stopping is the same. But starting requires the management public IP to be re-associated back to the firewall:

Azure PowerShell 

```
# Stop an existing firewall

$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "RG Name"
$azfw.Deallocate()
Set-AzFirewall -AzureFirewall $azfw

```

Azure PowerShell 

```
# Start the firewall

$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "RG Name"
$vnet = Get-AzVirtualNetwork -ResourceGroupName "RG Name" -Name "VNet Name"
$pip= Get-AzPublicIpAddress -ResourceGroupName "RG Name" -Name "azfwpublicip"
$mgmtPip2 = Get-AzPublicIpAddress -ResourceGroupName "RG Name" -Name "mgmtpip"
$azfw.Allocate($vnet, $pip, $mgmtPip2)
$azfw | Set-AzFirewall

```

For a firewall in a secured virtual hub architecture, stopping is the same but starting must use the virtual hub ID:

Azure PowerShell 

```
# Stop and existing firewall

$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "RG Name"
$azfw.Deallocate()
Set-AzFirewall -AzureFirewall $azfw

```

Azure PowerShell 

```
# Start the firewall

$virtualhub = get-azvirtualhub -ResourceGroupName "RG name of vHUB" -name "vHUB name"
$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "Azfw RG Name"
$azfw.Allocate($virtualhub.Id)
$azfw | Set-AzFirewall

```

When you allocate and deallocate, [firewall billing](https://azure.microsoft.com/pricing/details/azure-firewall) stops and starts accordingly.

Note

You must reallocate a firewall and public IP to the original resource group and subscription.

The recommendation is to configure availability zones during the initial firewall deployment. However, in some cases it is possible to change availability zones after deployment. The prerequisites are:

* The firewall is deployed in a VNet. It is not supported with firewalls deployed in a secured virtual hub.
* The firewall's region [supports availability zones](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-service-support).
* All attached public IP addresses are deployed with availability zones. In the properties page of each public IP address, ensure the **availability zones** field exists and is configured with the same zones you configured for the firewall.

Reconfiguring availability zones can only be done when you restart the firewall. After you allocate the firewall, and right before starting the firewall with `Set-AzFirewall`, use the following Azure PowerShell to modify the firewall's **Zones** property:

Azure PowerShell 

```
$azfw = Get-AzFirewall -Name "FW Name" -ResourceGroupName "RG Name"
$vnet = Get-AzVirtualNetwork -ResourceGroupName "RG Name" -Name "VNet Name"
$pip= Get-AzPublicIpAddress -ResourceGroupName "RG Name" -Name "azfwpublicip"
$mgmtPip2 = Get-AzPublicIpAddress -ResourceGroupName "RG Name" -Name "mgmtpip"
$azfw.Allocate($vnet, $pip, $mgmtPip2)
$azFw.Zones=1,2,3
$azfw | Set-AzFirewall

```

For Azure Firewall service limits, see [Azure subscription and service limits, quotas, and constraints](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-firewall-limits).

Yes, you can use Azure Firewall in a hub virtual network to route and filter traffic between two spoke virtual network. Subnets in each of the spoke virtual networks must have a UDR pointing to the Azure Firewall as a default gateway for this scenario to work properly.

Yes. However, configuring the UDRs to redirect traffic between subnets in the same VNET requires additional attention. While using the VNET address range as a target prefix for the UDR is sufficient, this also routes all traffic from one machine to another machine in the same subnet through the Azure Firewall instance. To avoid this, include a route for the subnet in the UDR with a next hop type of **VNET**. Managing these routes might be cumbersome and prone to error. The recommended method for internal network segmentation is to use Network Security Groups, which don't require UDRs.

Azure Firewall doesn't SNAT when the destination IP address is a private IP range per [IANA RFC 1918](https://tools.ietf.org/html/rfc1918). If your organization uses a public IP address range for private networks, Azure Firewall SNATs the traffic to one of the firewall private IP addresses in AzureFirewallSubnet. You can configure Azure Firewall to **not** SNAT your public IP address range. For more information, see [Azure Firewall SNAT private IP address ranges](https://learn.microsoft.com/en-us/azure/firewall/snat-private-range).

In addition, traffic processed by application rules are always SNAT-ed. If you want to see the original source IP address in your logs for FQDN traffic, you can use network rules with the destination FQDN.

Forced tunneling is supported when you create a new firewall. You can't configure an existing firewall for forced tunneling. For more information, see [Azure Firewall forced tunneling](https://learn.microsoft.com/en-us/azure/firewall/forced-tunneling).

Azure Firewall must have direct Internet connectivity. If your AzureFirewallSubnet learns a default route to your on-premises network via BGP, you must override this with a 0.0.0.0/0 UDR with the **NextHopType** value set as **Internet** to maintain direct Internet connectivity.

If your configuration requires forced tunneling to an on-premises network and you can determine the target IP prefixes for your Internet destinations, you can configure these ranges with the on-premises network as the next hop via a user defined route on the AzureFirewallSubnet. Or, you can use BGP to define these routes.

Yes. The firewall, VNet, and the public IP address all must be in the same resource group.

No. NAT rules implicitly add a corresponding network rule to allow the translated traffic. You can override this behavior by explicitly adding a network rule collection with deny rules that match the translated traffic. To learn more about Azure Firewall rule processing logic, see [Azure Firewall rule processing logic](https://learn.microsoft.com/en-us/azure/firewall/rule-processing).

* **URL** - Asterisks work when placed on the right-most or left-most side. If it is on the left, it can't be part of the FQDN.
* **FQDN** - Asterisks work when placed on the left-most side.
* **GENERAL** - Asterisks on the left-most side mean literally *anything* to the left will match, meaning multiple subdomains and/or potentially unwanted domain name variations will be matched - see examples below.

Examples:

| Type | Rule | Supported? | Positive examples |
| --- | --- | --- | --- |
| TargetURL | `www.contoso.com` | Yes | `www.contoso.com``www.contoso.com/` |
| TargetURL | `*.contoso.com` | Yes | `any.contoso.com/``sub1.any.contoso.com` |
| TargetURL | `*contoso.com` | Yes | `example.anycontoso.com``sub1.example.contoso.com``contoso.com`Warning: this usage of wildcard will also allow potentially undesired/risky variations such as `th3re4lcontoso.com` - use with caution. |
| TargetURL | `www.contoso.com/test` | Yes | `www.contoso.com/test``www.contoso.com/test/``www.contoso.com/test?with_query=1` |
| TargetURL | `www.contoso.com/test/*` | Yes | `www.contoso.com/test/anything`Note: `www.contoso.com/test` will **not** match (last slash) |
| TargetURL | `www.contoso.*/test/*` | No |  |
| TargetURL | `www.contoso.com/test?example=1` | No |  |
| TargetURL | `www.contoso.*` | No |  |
| TargetURL | `www.*contoso.com` | No |  |
| TargetURL | `www.contoso.com:8080` | No |  |
| TargetURL | `*.contoso.*` | No |  |
| TargetFQDN | `www.contoso.com` | Yes | `www.contoso.com` |
| TargetFQDN | `*.contoso.com` | Yes | `any.contoso.com`Note: If you want to specifically allow `contoso.com`, you must include contoso.com in the rule. Otherwise, the connection will be dropped by default because the request will not match any rule. |
| TargetFQDN | `*contoso.com` | Yes | `example.anycontoso.com``contoso.com` |
| TargetFQDN | `www.contoso.*` | No |  |
| TargetFQDN | `*.contoso.*` | No |  |

Whenever a configuration change is applied, Azure Firewall attempts to update all its underlying backend instances. In rare cases, one of these backend instances may fail to update with the new configuration and the update process stops with a failed provisioning state. Your Azure Firewall is still operational, but the applied configuration may be in an inconsistent state, where some instances have the previous configuration where others have the updated rule set. If this happens, try updating your configuration one more time until the operation succeeds and your Firewall is in a *Succeeded* provisioning state.

Azure Firewall consists of several backend nodes in an active-active configuration. For any planned maintenance, we have connection draining logic to gracefully update nodes. Updates are planned during non-business hours for each of the Azure regions to further limit risk of disruption. For unplanned issues, we instantiate a new node to replace the failed node. Connectivity to the new node is typically reestablished within 10 seconds from the time of the failure.

For any planned maintenance, connection draining logic gracefully updates backend nodes. Azure Firewall waits 90 seconds for existing connections to close. If needed, clients can automatically re-establish connectivity to another backend node.

Yes. There's a 50 character limit for a firewall name.

Azure Firewall must provision more virtual machine instances as it scales. A /26 address space ensures that the firewall has enough IP addresses available to accommodate the scaling.

No. Azure Firewall doesn't need a subnet bigger than /26.

Azure Firewall's initial throughput capacity is 2.5 - 3 Gbps and it scales out to 30 Gbps for Standard SKU and 100 Gbps for Premium SKU. It scales out automatically based on CPU usage and throughput.

Azure Firewall gradually scales when average throughput or CPU consumption is at 60%. It starts to scale out when it reaches 60% of its maximum throughput. Maximum throughput numbers vary based on Firewall SKU and enabled features. For more information, see [Azure Firewall performance](https://learn.microsoft.com/en-us/azure/firewall/firewall-performance).

Scale out takes five to seven minutes.

When performance testing, make sure you test for at least 10 to 15 minutes, and start new connections to take advantage of newly created Firewall nodes.

When a connection has an Idle Timeout (four minutes of no activity), Azure Firewall gracefully terminates the connection by sending a TCP RST packet.

An Azure Firewall VM instance shutdown may occur during Virtual Machine Scale Set scale in (scale down) or during fleet software upgrade. In these cases, new incoming connections are load balanced to the remaining firewall instances and are not forwarded to the down firewall instance. After 45 seconds the firewall starts rejecting existing connections by sending TCP RST packets. After an additional 45 seconds the firewall VM shuts down. For more information, see [Load Balancer TCP Reset and Idle Timeout](https://learn.microsoft.com/en-us/azure/load-balancer/load-balancer-tcp-reset).

No. Azure Firewall blocks Active Directory access by default. To allow access, configure the AzureActiveDirectory service tag. For more information, see [Azure Firewall service tags](https://learn.microsoft.com/en-us/azure/firewall/service-tags).

Yes, you can use Azure PowerShell to do it:

Azure PowerShell 

```
# Add a Threat Intelligence allowlist to an Existing Azure Firewall

# Create the allowlist with both FQDN and IPAddresses
$fw = Get-AzFirewall -Name "Name_of_Firewall" -ResourceGroupName "Name_of_ResourceGroup"
$fw.ThreatIntelWhitelist = New-AzFirewallThreatIntelWhitelist `
   -FQDN @("fqdn1", "fqdn2", …) -IpAddress @("ip1", "ip2", …)

# Or Update FQDNs and IpAddresses separately
$fw = Get-AzFirewall -Name $firewallname -ResourceGroupName $RG
$fw.ThreatIntelWhitelist.IpAddresses = @($fw.ThreatIntelWhitelist.IpAddresses + $ipaddresses)
$fw.ThreatIntelWhitelist.fqdns = @($fw.ThreatIntelWhitelist.fqdns + $fqdns)

Set-AzFirewall -AzureFirewall $fw

```

A TCP ping isn't actually connecting to the target FQDN. Azure Firewall doesn't allow a connection to any target IP address/FQDN unless there is an explicit rule that allows it.

TCP ping is a unique use case where if there is no allowed rule, the Firewall itself responds to the client's TCP ping request even though the TCP ping doesn't reach the target IP address/FQDN. In this case, the event is not logged. If there is a network rule that allows access to the target IP address/FQDN, then the ping request reaches the target server and its response is relayed back to the client. This event is logged in the Network rules log.

Yes. For more information, see [Azure subscription and service limits, quotas, and constraints](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-firewall-limits)

No, moving an IP Group to another resource group isn't currently supported.

A standard behavior of a network firewall is to ensure TCP connections are kept alive and to promptly close them if there's no activity. Azure Firewall TCP Idle Timeout is four minutes. This setting isn't user configurable, but you can contact Azure Support to increase the Idle Timeout for inbound and outbound connections up to 30 minutes. Idle Timeout for east-west traffic cannot be changed.

If a period of inactivity is longer than the timeout value, there's no guarantee that the TCP or HTTP session is maintained. A common practice is to use a TCP keep-alive. This practice keeps the connection active for a longer period. For more information, see the [.NET examples](https://learn.microsoft.com/en-us/dotnet/api/system.net.servicepoint.settcpkeepalive).

Yes, but you must configure the firewall in Forced Tunneling Mode. This configuration creates a management interface with a public IP address that is used by Azure Firewall for its operations. This public IP address is for management traffic. It is used exclusively by the Azure platform and can't be used for any other purpose. The tenant data path network can be configured without a public IP address, and Internet traffic can be forced tunneled to another Firewall or completely blocked.

Azure Firewall doesn't move or store customer data out of the region it's deployed in.

Yes. For more information, see [Backup Azure Firewall and Azure Firewall Policy with Logic Apps](https://techcommunity.microsoft.com/t5/azure-network-security-blog/backup-azure-firewall-and-azure-firewall-policy-with-logic-apps/ba-p/3613928).

No, currently Azure Firewall in secured virtual hubs (vWAN) is not supported in Qatar.

Azure Firewall uses Azure Virtual Machines underneath that have a [hard limit number of connections](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-machine-network-throughput#flow-limits-and-active-connections-recommendations). The total number of flows per virtual machine is 250k.

The total limit per firewall is the virtual machine connection limit (250k) x the number of virtual machines in the firewall backend pool. Azure Firewall starts with two virtual machines and scales out based on CPU usage and throughput.

Azure Firewall currently uses TCP/UDP source ports for outbound SNAT traffic, with no idle wait time. When a TCP/UDP connection is closed, the TCP port used is immediately seen as available for upcoming connections.

As a workaround for certain architectures, you can deploy and scale with [NAT Gateway with Azure Firewall](https://learn.microsoft.com/en-us/azure/nat-gateway/tutorial-hub-spoke-nat-firewall) to provide a wider pool of SNAT ports for variability and availability.

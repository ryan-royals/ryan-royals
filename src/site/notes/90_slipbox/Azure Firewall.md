---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Firewall.md","permalink":"/slipbox-notes/azure-firewall/","tags":["notes"],"created":"2023-07-25","updated":"2025-11-27"}
---


![Azure Firewall-1728452311593.png](/img/user/10_attachments/Azure%20Firewall-1728452311593.png)  
Azure Firewall includes the following features:

- **Built-in high availability** - High availability is built in, so no extra load balancers are required and there's nothing you need to configure.
- **Unrestricted cloud scalability** - Azure Firewall can scale out as much as you need to accommodate changing network traffic flows, so you do not need to budget for your peak traffic.
- **Application FQDN filtering rules** - You can limit outbound HTTP/S traffic or Azure SQL traffic to a specified list of fully qualified domain names (FQDN) including wild cards. This feature does not require TLS termination.
- **Network traffic filtering rules** - You can centrally create allow or deny network filtering rules by source and destination IP address, port, and protocol. Azure Firewall is fully stateful, so it can distinguish legitimate packets for different types of connections. Rules are enforced and logged across multiple subscriptions and virtual networks.
- **FQDN tags** - These tags make it easy for you to allow well-known Azure service network traffic through your firewall. For example, say you want to allow Windows Update network traffic through your firewall. You create an application rule and include the Windows Update tag. Now network traffic from Windows Update can flow through your firewall.
- **Service tags** - A service tag represents a group of IP address prefixes to help minimize complexity for security rule creation. You cannot create your own service tag, nor specify which IP addresses are included within a tag. Microsoft manages the address prefixes encompassed by the service tag, and automatically updates the service tag as addresses change.
- **Threat intelligence** - Threat intelligence-based filtering (IDPS) can be enabled for your firewall to alert and deny traffic from/to known malicious IP addresses and domains. The IP addresses and domains are sourced from the Microsoft Threat Intelligence feed.
- **TLS inspection** - The firewall can decrypt outbound traffic, processes the data, then encrypt the data and sends it to the destination.
- **Outbound SNAT support** - All outbound virtual network traffic IP addresses are translated to the Azure Firewall public IP (Source Network Address Translation (SNAT)). You can identify and allow traffic originating from your virtual network to remote Internet destinations.
- **Inbound DNAT support** - Inbound Internet network traffic to your firewall public IP address is translated (Destination Network Address Translation) and filtered to the private IP addresses on your virtual networks.
- **Multiple public IP addresses** - You can associate multiple public IP addresses (up to 250) with your firewall, to enable specific DNAT and SNAT scenarios.
- **Azure Monitor logging** - All events are integrated with Azure Monitor, allowing you to archive logs to a storage account, stream events to your Event Hubs, or send them to Azure Monitor logs.
- **Forced tunneling** - You can configure Azure Firewall to route all Internet-bound traffic to a designated next hop instead of going directly to the Internet. For example, you may have an on-premises edge firewall or other network virtual appliance (NVA) to process network traffic before it is passed to the Internet.
- **Web categories** - Web categories let administrators allow or deny user access to web site categories such as gambling websites, social media websites, and others. Web categories are included in Azure Firewall Standard, but it is more fine-tuned in Azure Firewall Premium Preview. As opposed to the Web categories capability in the Standard SKU that matches the category based on an FQDN, the Premium SKU matches the category according to the entire URL for both HTTP and HTTPS traffic.
- **Certifications** - Azure Firewall is Payment Card Industry (PCI), Service Organization Controls (SOC), International Organization for Standardization (ISO), and ICSA Labs compliant.  
[^1]

When deploying Azure Firewall, you can configure it to span multiple Availability Zones for increased availability. When you configure Azure Firewall in this way your availability increases to [[90_slipbox/Service Level Agreement\|99.99%]] uptime. The [[90_slipbox/Service Level Agreement\|99.99%]] uptime SLA is offered when two or more Availability Zones are selected.

You can also associate Azure Firewall to a specific zone just for proximity reasons, using the service standard [[90_slipbox/Service Level Agreement\|99.5%]] SLA.

## Rules Processing

Azure Firewall supports NAT rules (Ingress rules), network rules (private networking), and application rules (egress to URL).  
By default Azure Firewall denies all traffic.

With Firewall Policy, rules are organized inside Rule Collections which are contained in Rule Collection Groups. Rule Collections can be of the following types:

- DNAT (Destination Network Address Translation)
- Network
- Application

You can define multiple Rule Collection types within a single Rule Collection Group, and you can define zero or more Rules in a Rule Collection, but the rules within a Rule Collection must be of the same type (i.e., DNAT, Network, or Application).

With Firewall Policy, rules are processed based on Rule Collection Group Priority and Rule Collection priority. Priority is any number between 100 (highest priority) and 65,000 (lowest priority). Highest priority Rule Collection Groups are processed first, and inside a Rule Collection Group, Rule Collections with the highest priority (i.e., the lowest number) are processed first.

**In the case of a Firewall Policy being inherited from a parent policy, Rule Collection Groups in the parent policy always takes precedence regardless of the priority of the child policy.**

Application rules are always processed after network rules, which are themselves always processed after DNAT rules regardless of Rule Collection Group or Rule Collection priority and policy inheritance.  
[^1]

## DNS Proxy

Azure Firewall can be used as a proxy for DNS, enabling it to resolve [[90_slipbox/Azure Private DNS Zone\|Azure Private DNS Zone]] entries for both in Azure and On-Premises.  
This feature requires **Standard** SKU.  
[^2]

[^1]: [Design and Implement Azure Firewall - Training](https://learn.microsoft.com/en-us/training/modules/design-implement-network-security-monitoring/6-azure-firewall)
[^2]: [New Enhanced DNS Features in Azure Firewall—now Generally Available](https://azure.microsoft.com/en-us/blog/new-enhanced-dns-features-in-azure-firewall-now-generally-available/)

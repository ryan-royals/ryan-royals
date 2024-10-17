---
{"dg-publish":true,"permalink":"/40-references/readwise/design-and-implement-azure-firewall-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)
  
URL: https://learn.microsoft.com/en-us/training/modules/design-implement-network-security-monitoring/6-azure-firewall
Author: wwlpublish

## Summary

Azure Firewall is a managed network security service that protects Azure Virtual Network resources with high availability and scalability. It includes features like application filtering, threat intelligence, and logging, allowing centralized management of network traffic rules. Deployment can be enhanced with Availability Zones for increased uptime, and it supports both inbound and outbound traffic filtering.

## Highlights added October 9, 2024 at 4:09 PM
>Azure Firewall includes the following features:
>• **Built-in high availability** - High availability is built in, so no extra load balancers are required and there's nothing you need to configure.
>• **Unrestricted cloud scalability** - Azure Firewall can scale out as much as you need to accommodate changing network traffic flows, so you do not need to budget for your peak traffic.
>• **Application FQDN filtering rules** - You can limit outbound HTTP/S traffic or Azure SQL traffic to a specified list of fully qualified domain names (FQDN) including wild cards. This feature does not require TLS termination.
>• **Network traffic filtering rules** - You can centrally create allow or deny network filtering rules by source and destination IP address, port, and protocol. Azure Firewall is fully stateful, so it can distinguish legitimate packets for different types of connections. Rules are enforced and logged across multiple subscriptions and virtual networks.
>• **FQDN tags** - These tags make it easy for you to allow well-known Azure service network traffic through your firewall. For example, say you want to allow Windows Update network traffic through your firewall. You create an application rule and include the Windows Update tag. Now network traffic from Windows Update can flow through your firewall.
>• **Service tags** - A service tag represents a group of IP address prefixes to help minimize complexity for security rule creation. You cannot create your own service tag, nor specify which IP addresses are included within a tag. Microsoft manages the address prefixes encompassed by the service tag, and automatically updates the service tag as addresses change.
>• **Threat intelligence** - Threat intelligence-based filtering (IDPS) can be enabled for your firewall to alert and deny traffic from/to known malicious IP addresses and domains. The IP addresses and domains are sourced from the Microsoft Threat Intelligence feed.
>• **TLS inspection** - The firewall can decrypt outbound traffic, processes the data, then encrypt the data and sends it to the destination.
>• **Outbound SNAT support** - All outbound virtual network traffic IP addresses are translated to the Azure Firewall public IP (Source Network Address Translation (SNAT)). You can identify and allow traffic originating from your virtual network to remote Internet destinations.
>• **Inbound DNAT support** - Inbound Internet network traffic to your firewall public IP address is translated (Destination Network Address Translation) and filtered to the private IP addresses on your virtual networks.
>• **Multiple public IP addresses** - You can associate multiple public IP addresses (up to 250) with your firewall, to enable specific DNAT and SNAT scenarios.
>• **Azure Monitor logging** - All events are integrated with Azure Monitor, allowing you to archive logs to a storage account, stream events to your Event Hubs, or send them to Azure Monitor logs.
>• **Forced tunneling** - You can configure Azure Firewall to route all Internet-bound traffic to a designated next hop instead of going directly to the Internet. For example, you may have an on-premises edge firewall or other network virtual appliance (NVA) to process network traffic before it is passed to the Internet.
>• **Web categories** - Web categories let administrators allow or deny user access to web site categories such as gambling websites, social media websites, and others. Web categories are included in Azure Firewall Standard, but it is more fine-tuned in Azure Firewall Premium Preview. As opposed to the Web categories capability in the Standard SKU that matches the category based on an FQDN, the Premium SKU matches the category according to the entire URL for both HTTP and HTTPS traffic.
>• **Certifications** - Azure Firewall is Payment Card Industry (PCI), Service Organization Controls (SOC), International Organization for Standardization (ISO), and ICSA Labs compliant. ([View Highlight] (https://read.readwise.io/read/01j9qwj8f3ahh95bvtk6qarpp0))


## Highlights added October 9, 2024 at 4:56 PM
>With Firewall Policy, rules are organized inside Rule Collections which are contained in Rule Collection Groups. Rule Collections can be of the following types:
>• DNAT (Destination Network Address Translation)
>• Network
>• Application
>You can define multiple Rule Collection types within a single Rule Collection Group, and you can define zero or more Rules in a Rule Collection, but the rules within a Rule Collection must be of the same type (i.e., DNAT, Network, or Application).
>With Firewall Policy, rules are processed based on Rule Collection Group Priority and Rule Collection priority. Priority is any number between 100 (highest priority) and 65,000 (lowest priority). Highest priority Rule Collection Groups are processed first, and inside a Rule Collection Group, Rule Collections with the highest priority (i.e., the lowest number) are processed first.
>In the case of a Firewall Policy being inherited from a parent policy, Rule Collection Groups in the parent policy always takes precedence regardless of the priority of the child policy.
>Application rules are always processed after network rules, which are themselves always processed after DNAT rules regardless of Rule Collection Group or Rule Collection priority and policy inheritance. ([View Highlight] (https://read.readwise.io/read/01j9qx5fvmphq4pbgc0h6kat0q))



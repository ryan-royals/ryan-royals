---
{"dg-publish":true,"dg-path":"Azure Traffic Analytics.md","permalink":"/azure-traffic-analytics/","tags":["notes"]}
---


Traffic Analytics is a cloud-based solution that provides visibility into user and application activity in cloud networks. Traffic Analytics analyses [[99 Inbox/Azure Network Watcher\|Azure Network Watcher]] [[99 Inbox/Azure Network Security Group Flow Logs\|Azure Network Security Group Flow Logs]] to provide insights into traffic flow in your Azure cloud and provide rich visualizations of data written to NSG flow logs.

With Traffic Analytics, you can:

- Visualize network activity across your Azure subscriptions and identify hot spots.
- Identify security threats to, and secure your network, with information such as open-ports, applications attempting internet access, and virtual machines (VM) connecting to rogue networks.
- Understand traffic flow patterns across Azure regions and the internet to optimize your network deployment for performance and capacity.
- Pinpoint network misconfigurations leading to failed connections in your network.

## How Traffic Analytics Works

Traffic analytics examines the raw NSG flow logs and captures reduced logs by aggregating common flows among the same source IP address, destination IP address, destination port, and protocol. For example, Host 1 (IP address: 10.10.10.10) communicating to Host 2 (IP address: 10.10.20.10), 100 times over a period of 1 hour using port (for example, 80) and protocol (for example, http). The reduced log has one entry, that Host 1 & Host 2 communicated 100 times over a period of 1 hour using port 80 and protocol HTTP, instead of having 100 entries. Reduced logs are enhanced with geography, security, and topology information, and then stored in a Log Analytics workspace.

The diagram below illustrates the data flow:

![40 References/attachments/583be8b186c6e647fe58be424b8214eb_MD5.jpg](/img/user/40%20References/attachments/583be8b186c6e647fe58be424b8214eb_MD5.jpg)

The key components of Traffic Analytics are:

- **Network security group (NSG)** - Contains a list of security rules that allow or deny network traffic to resources connected to an Azure Virtual Network. NSGs can be associated to subnets, individual VMs (classic), or individual network interfaces (NIC) attached to VMs (Resource Manager). For more information, see [[30 Slipbox/Azure Network Security Group\|Azure Network Security Group]] .
- **Network security group (NSG) flow logs** - Allow you to view information about ingress and egress IP traffic through a network security group. NSG flow logs are written in json format and show outbound and inbound flows on a per rule basis, the NIC the flow applies to, five-tuple information about the flow (source/destination IP address, source/destination port, and protocol), and if the traffic was allowed or denied. For more information about NSG flow logs, see [[99 Inbox/Azure Network Security Group Flow Logs\|Azure Network Security Group Flow Logs]]
- **Log Analytics** - An Azure service that collects monitoring data and stores the data in a central repository. This data can include events, performance data, or custom data provided through the Azure API. Once collected, the data is available for alerting, analysis, and export. Monitoring applications such as network performance monitor and traffic analytics are built using Azure Monitor logs as a foundation. For more information, see [[30 Slipbox/Azure Log Analytics Workspace\|Azure Log Analytics Workspace]]
- **Log Analytics workspace** - An instance of Azure Monitor logs, where the data pertaining to an Azure account, is stored. For more information about Log Analytics workspaces, see Create a Log Analytics workspace.
- **Network Watcher** - A regional service that enables you to monitor and diagnose conditions at a network scenario level in Azure. You can turn NSG flow logs on and off with Network Watcher. For more information, see [[99 Inbox/Azure Network Watcher\|Azure Network Watcher]].

To analyze traffic, you need to have an existing network watcher, or enable a network watcher in each region that you have NSGs that you want to analyze traffic for. Traffic analytics can be enabled for NSGs hosted in any of the supported regions.  
[^1]

## Footnotes

[^1]: [[40 References/omnivore/Monitor your networks using Azure network watcher - Training - Microsoft Learn\|Monitor your networks using Azure network watcher - Training - Microsoft Learn]]

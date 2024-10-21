---
{"dg-publish":true,"dg-path":"Azure Network Security Group Flow Logs.md","permalink":"/azure-network-security-group-flow-logs/","tags":["notes"]}
---


[[30 Slipbox/Azure Network Security Group\|Azure Network Security Group]]s allow or deny inbound or outbound traffic to a network interface in a VM.

NSG flow logs is a feature of [[99 Inbox/Azure Network Watcher\|Azure Network Watcher]] that allows you to log information about IP traffic flowing through an NSG. The NSG flow log capability allows you to log the source and destination IP address, port, protocol, and whether traffic was allowed or denied by an NSG. You can analyse logs using a variety of tools, such as Power BI and the [[99 Inbox/Azure Traffic Analytics\|Azure Traffic Analytics]] feature in [[99 Inbox/Azure Network Watcher\|Azure Network Watcher]].

Common use cases for NSG flow logs are:

- **Network Monitoring** - Identify unknown or undesired traffic. Monitor traffic levels and bandwidth consumption. Filter flow logs by IP and port to understand application behavior. Export Flow Logs to analytics and visualization tools of your choice to set up monitoring dashboards.
- **Usage monitoring and optimization** - Identify top talkers in your network. Combine with GeoIP data to identify cross-region traffic. Understand traffic growth for capacity forecasting. Use data to remove overtly restrictive traffic rules.
- **Compliance** - Use flow data to verify network isolation and compliance with enterprise access rules.
- **Network forensics and security analysis** - Analyze network flows from compromised IPs and network interfaces. Export flow logs to any SIEM or IDS tool of your choice.  
[^1]

## Footnotes

[^1]: [[40 References/omnivore/Monitor your networks using Azure network watcher - Training - Microsoft Learn\|Monitor your networks using Azure network watcher - Training - Microsoft Learn]]

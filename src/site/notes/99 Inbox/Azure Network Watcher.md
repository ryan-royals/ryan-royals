---
{"dg-publish":true,"dg-path":"Azure Network Watcher.md","permalink":"/azure-network-watcher/","tags":["notes"]}
---


Azure Network Watcher is a regional service that enables you to monitor and diagnose conditions at a network scenario level in, to, and from Azure. Scenario level monitoring enables you to diagnose problems at an end-to-end network level view. Network diagnostic and visualization tools available with Network Watcher help you understand, diagnose, and gain insights to your network in Azure. Network Watcher is enabled through the creation of a Network Watcher resource, which allows you to utilize Network Watcher capabilities. Network Watcher is designed to monitor and repair the network health of IaaS products which includes [[30 Slipbox/Azure Virtual Machine\|Azure Virtual Machine]], [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]], [[30 Slipbox/Azure Application Gateway\|Azure Application Gateway]], and [[30 Slipbox/Azure Load Balancer\|Azure Load Balancer]].

- **Automate remote network monitoring with packet capture.** Monitor and diagnose networking issues without logging in to your virtual machines (VMs) using Network Watcher. Trigger packet capture by setting alerts, and gain access to real-time performance information at the packet level. When you observe an issue, you can investigate in detail for better diagnoses.
- **Gain insight into your network traffic using flow logs. Build a deeper understanding of your network traffic pattern using Network Security Group flow logs.** Information provided by flow logs helps you gather data for compliance, auditing and monitoring your network security profile.
- **Diagnose VPN connectivity issues. Network Watcher provides you the ability to diagnose your most common VPN Gateway and Connections issues.** Allowing you, not only, to identify the issue but also to use the detailed logs created to help further investigate.  
[^1]

Tooling includes a **Network Topology** diagram generator, a tool to **Verify Ip Flow** through NSG's egress, **Next Hop** route finder, **Effective Security Rules** to see what is allowed ingress, **VPN diagnostic tools**, **Packet Capture**, and a **Connection Trouble-shooter** to run these tools to generate a report, and [[99 Inbox/Azure Network Security Group Flow Logs\|Azure Network Security Group Flow Logs]] to long term retain network usage logs.

When using the Network Watcher, a resource group is created called `NetworkWatcherRG`, with an instance for each required region named `NetowrkWatcher_*region*`

## See also

- [[99 Inbox/Azure Network Security Group Flow Logs\|Azure Network Security Group Flow Logs]]
- [[99 Inbox/Azure Connection Monitor\|Azure Connection Monitor]]
- [[99 Inbox/Azure Traffic Analytics\|Azure Traffic Analytics]]

## Footnotes

[^1]: [[40 References/omnivore/Monitor your networks using Azure network watcher - Training - Microsoft Learn\|Monitor your networks using Azure network watcher - Training - Microsoft Learn]]

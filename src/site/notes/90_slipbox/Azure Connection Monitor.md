---
{"dg-publish":true,"permalink":"/90-slipbox/azure-connection-monitor/","tags":["notes"]}
---


Connection Monitor provides unified end-to-end connection monitoring in [[90_slipbox/Azure Network Watcher\|Azure Network Watcher]]. The Connection Monitor feature supports hybrid and Azure cloud deployments. Network Watcher provides tools to monitor, diagnose, and view connectivity-related metrics for your Azure deployments.

![aefd434494c23d7a51217d35cab6563d_MD5.jpg](/img/user/10_attachments/aefd434494c23d7a51217d35cab6563d_MD5.jpg)

Here are some use cases for Connection Monitor:

- Your front-end web server VM communicates with a database server VM in a multi-tier application. You want to check network connectivity between the two VMs.
- You want VMs in the East US region to ping VMs in the Central US region, and you want to compare cross-region network latencies.
- You have multiple on-premises office sites in Seattle, Washington, and in Ashburn, Virginia. Your office sites connect to Microsoft 365 URLs. For your users of Microsoft 365 URLs, compare the latencies between Seattle and Ashburn.
- Your hybrid application needs connectivity to an Azure Storage endpoint. Your on-premises site and your Azure application connect to the same Azure Storage endpoint. You want to compare the latencies of the on-premises site to the latencies of the Azure application.
- You want to check the connectivity between your on-premises setups and the Azure VMs that host your cloud application.

Connection Monitor combines the best of two features: the Network Watcher Connection Monitor (Classic) feature and the Network Performance Monitor (NPM) Service Connectivity Monitor, ExpressRoute Monitoring, and Performance Monitoring feature.

Here are some benefits of Connection Monitor:

- Unified, intuitive experience for Azure and hybrid monitoring needs
- Cross-region, cross-workspace connectivity monitoring
- Higher probing frequencies and better visibility into network performance
- Faster alerting for your hybrid deployments
- Support for connectivity checks that are based on HTTP, TCP, and ICMP
- Metrics and Log Analytics support for both Azure and non-Azure test setups  
[^1]

## Footnotes

[^1]: [Monitor your networks using Azure network watcher - Training - Microsoft Learn](https://learn.microsoft.com/en-us/training/modules/design-implement-network-monitoring/4-monitor-networks-using-azure-network-watcher)

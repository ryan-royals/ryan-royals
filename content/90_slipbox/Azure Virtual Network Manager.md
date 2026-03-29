---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Virtual Network Manager.md","permalink":"/slipbox-notes/azure-virtual-network-manager/","tags":["notes"],"created":"2025-06-11","updated":"2025-11-28"}
---

> Significantly reduce your operational overhead with Azure Virtual Network Manager, a central management service for your virtual network resources. Easily manage your virtual network infrastructure while scaling your cloud-based workloads. Use the centralized solution to create and manage complex network topologies and network security rules globally across subscriptions.

Adds a neat overview that helps co ordinate how your VNETs are peered, assigns them intents so you can identify which VNET or Subnet is assigned to what application or scope, and manage IP addresses.  
Notably billing wise, it is ~$22AUD a month for each virtual network that is managed by Azure Virtual Network Manager and has configurations in it, and $0.30AUD per hour per active IP address managed by Azure Virtual Network Manager IP address management.  
These costings make it a hard ask for something that feels like it should be included in the platform, or can be replicated with other tooling not tied directly to Azure

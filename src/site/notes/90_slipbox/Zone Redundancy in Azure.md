---
{"dg-publish":true,"permalink":"/90-slipbox/zone-redundancy-in-azure/","tags":["notes"],"created":"2026-03-27T09:57:51.489+10:30","updated":"2026-03-27T09:57:51.489+10:30","dg-note-properties":{"tags":"notes","related":["[[Azure]]"],"created":"2024-07-29","modified":"2026-03-03"}}
---


Azure services that support availability zones fall into three categories:

- Zonal services: Resources can be pinned to a specific zone. For example, virtual machines, managed disks, or standard IP addresses can be pinned to a specific zone, which allows for increased resilience by having one or more instances of resources spread across zones.
- Zone-redundant services: Resources are replicated or distributed across zones automatically. Azure replicates the data across three zones so that a zone failure doesn't impact its availability.
- Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages and region-wide outages.  
[^1]

[^1]: [Design and Implement Azure Load Balancer Using the Azure Portal - Training](https://learn.microsoft.com/en-us/training/modules/load-balancing-non-https-traffic-azure/3-design-implement-azure-load-balancer-using-azure-portal)

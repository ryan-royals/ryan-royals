---
{"dg-publish":true,"dg-path":"Zone Redundancy in Azure.md","permalink":"/zone-redundancy-in-azure/","tags":["notes"]}
---


Azure services that support availability zones fall into three categories:

- Zonal services: Resources can be pinned to a specific zone. For example, virtual machines, managed disks, or standard IP addresses can be pinned to a specific zone, which allows for increased resilience by having one or more instances of resources spread across zones.
- Zone-redundant services: Resources are replicated or distributed across zones automatically. Azure replicates the data across three zones so that a zone failure doesn't impact its availability.
- Non-regional services: Services are always available from Azure geographies and are resilient to zone-wide outages and region-wide outages.  
[^1]

[^1]: [[40 References/readwise/Design and Implement Azure Load Balancer Using the Azure Portal - Training\|Design and Implement Azure Load Balancer Using the Azure Portal - Training]]raining]]

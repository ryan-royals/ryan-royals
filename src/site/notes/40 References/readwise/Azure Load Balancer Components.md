---
{"dg-publish":true,"permalink":"/40-references/readwise/azure-load-balancer-components/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

Azure Load Balancer has key components such as frontend IP configuration, backend pools, health probes, and load balancing rules. It helps distribute incoming traffic to virtual machines and ensures they are healthy for processing requests. Different rules and configurations allow for both public and internal load balancing based on specific needs.

## Highlights

Load Balancer rules
A load balancer rule is used to define how incoming traffic is distributed to **all** the instances within the backend pool. A load-balancing rule maps a given frontend IP configuration and port to multiple backend IP addresses and ports. Load Balancer rules are for inbound traffic only.
For example, use a load balancer rule for port 80 to route traffic from your frontend IP to port 80 of your backend instances.
![Load balancer rule reference diagram](https://learn.microsoft.com/en-us/azure/load-balancer/components/media/load-balancer-components/lbrules.png)
*Figure: Load-Balancing rules* ([View Highlight] (https://read.readwise.io/read/01j3psscffcgzegcmydah6626x))



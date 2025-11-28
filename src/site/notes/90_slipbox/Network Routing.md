---
{"dg-publish":true,"permalink":"/90-slipbox/network-routing/","tags":["notes"]}
---

Routing rules are how traffic navigates on the [[90_slipbox/OSI Networking Model#Layer 3 - Network\|Layer 3 of the OSI Networking Model]], by directing certain traffic to next hops to further along the network, when the traffic would leave the Subnet the device is on.

Routes are determined by 3 parameters: **Administrative distance**, **Metrics** and **Prefix Length**.[^1]

## Prefix Length

The longest prefix match takes precedence.

| Address prefixes | Subnet Mask   | Next hop |
| ---------------- | ------------- | -------- |
| 192.168.0.0/24   | 255.255.255.0 | 10.0.0.4 |
| 192.168.0.0/16   | 255.255.0.0   | 20.0.0.4 |
| 0.0.0.0/0        | 0.0.0.0       | 0.0.0.0  |

Traffic to **192.168.1**.2 would route to 10.0.0.4 as it has the most reserved Bits (24 Reserved Bits with a mask of 255.255.255.0, vs 16 Reserved Bits with a mask of 255.255.0.0)

Traffic to **192.168**.10.9 would route to 20.0.0.4 as it has only 1 route that applies to it.

Traffic to 172.168.0.12 would be dropped, as the only route that applies is the 0.0.0.0/0 route (Which has no Reserved Bits)

## Metrics

Metrics are used to measure which path is best to the given destination when there are multiple paths to the same destination. Each routing protocol uses a different metric.

Metrics are a calculated value based on information such as:

Path length, bandwidth, load, hop count, path cost, delay, maximum transmission unit (MTU), reliability and communications cost.[^2]

## Administrative Distance

Administrative Distance is used to compare routes based on the trustworthiness of the source router, when there is a over lap in routing protocol.[^3]

This number is assigned per defaults set on the router such as:

| Routing Protocol             | Administrative Distance |
| ---------------------------- | ----------------------- |
| Directly connected interface | 0                       |
| Static Route                 | 1                        |

## Footnotes

[^1]: [Configure Route Selection for Routers](https://www.cisco.com/c/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21.html)
[^2]: [Metrics](https://en.wikipedia.org/wiki/Metrics_(networking))
[^3]: [Administrative Distance](https://en.wikipedia.org/wiki/Administrative_distance)

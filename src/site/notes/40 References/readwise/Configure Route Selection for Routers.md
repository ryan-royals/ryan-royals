---
{"dg-publish":true,"permalink":"/40-references/readwise/configure-route-selection-for-routers/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.cisco.com/c/dam/en/us/support/docs/ip/enhanced-interior-gateway-routing-protocol-eigrp/8651-21-00.png)

## Summary

This document describes how routers work, are configured, and how to select a route for them.

## Highlights

Build the Routing Table
The main considerations when you build the routing table are:
• **Administrative distance**- This is the measure of trustworthiness of the source of the route. If a router learns about a destination from more than one routing protocol, the administrative distance is compared and the preference is given to the routes with lower administrative distance. 
• **Metrics**- This is a measure used by the routing protocol to calculate the best path to a given destination, if it learns multiple paths to the same destination. Each routing protocol uses a different metric.
• **Prefix length** ([View Highlight] (https://read.readwise.io/read/01h6tettpks8x32cjmnf2ze5nt))



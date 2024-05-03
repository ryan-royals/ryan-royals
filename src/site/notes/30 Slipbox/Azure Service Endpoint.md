---
{"dg-publish":true,"dg-path":"Azure Service Endpoint.md","permalink":"/Azure Service Endpoint/","tags":["notes"]}
---


## Azure Service Endpoint

### Overview

Azure Service Endpoints are used to optimize routing on your subnet to the service it has been configured to reach on a subnet in a [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]].

It only only offers this access to devices on the Subnet itself, and can not be used outside of the Subnet (Natively).

A key usage is to simplify routing when using [[Azure User Defined Route\|UDR's]] to stop traffic routing to a RouteAll.

---

Links: [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]], [[30 Slipbox/Azure Private Link\|Azure Private Link]]  
Tags:  
Reference: [[40 References/readwise/Virtual Network Service Endpoints\|Virtual Network Service Endpoints]]

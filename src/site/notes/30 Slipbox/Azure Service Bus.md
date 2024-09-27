---
{"dg-publish":true,"dg-path":"Azure Service Bus.md","permalink":"/azure-service-bus/","tags":["notes"]}
---


## Azure Service Bus

### Overview

Azure Service Bus is a enterprise message broker with message queues and publish-subscribe topics that utilises First in First Out (FIFO).

#### Queues

Queues are ordered and timestamped messages that can be retrieved by receivers in order

#### Topics

Topics are used to receive a message, and send to multiple receivers

### Technical Notes

- Should not be used as a backed for [[30 Slipbox/Azure SignalR\|Azure SignalR]]
- Can not be Firewalled or configured with a [[30 Slipbox/Azure Private Endpoint\|Private Endpoint]] without the Premium SKU.
- [[Shared Access Signature\|Shared Access Signature]] can be disabled at any SKU, allowing [[Role Based Access Control\|Role Based Access Control]] on Users.

---

Links: [[30 Slipbox/Azure\|Azure]]  
Tags:  
Reference:

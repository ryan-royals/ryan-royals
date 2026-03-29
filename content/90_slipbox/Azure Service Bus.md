---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Service Bus.md","permalink":"/slipbox-notes/azure-service-bus/","tags":["notes"],"created":"2023-04-27","updated":"2025-11-27"}
---


Azure Service Bus is a enterprise message broker with message queues and publish-subscribe topics that utilises First in First Out (FIFO).

## Queues

Queues are ordered and timestamped messages that can be retrieved by receivers in order

## Topics

Topics are used to receive a message, and send to multiple receivers

## Quick Notes

Service bus is not a valid backend for SignalR, it will cripple under load.  
This can be elusive, as it will work in testing but not under real load.

Can not be Firewalled or configured with a [[90_slipbox/Azure Private Endpoint\|Private Endpoint]] without the Premium SKU.

Shared Access Signature can be disabled at any SKU, allowing Role Based Access Control on Users even on Standard SKU

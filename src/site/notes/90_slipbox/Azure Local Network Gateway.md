---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Local Network Gateway.md","permalink":"/slipbox-notes/azure-local-network-gateway/","tags":["notes"],"created":"2024-05-06","updated":"2025-11-27"}
---

A Local Network Gateway is a sub resource of a [[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]], that represents a on-premises location for the used in tandem with a [[90_slipbox/Azure Connection\|Azure Connection]] resource in the creation of a [[90_slipbox/Virtual Private Network\|Virtual Private Network]] or [[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]] Connection.

The Address Space declared can be one or more [[90_slipbox/Network Addressing#What is CIDR Notation\|CIDR]] formatted subnets. If you plan to use this Local Network Gateway in a BGP-enabled connection, the minimum prefix to declare is the host address of your BP Peer IP address on your BPN device.

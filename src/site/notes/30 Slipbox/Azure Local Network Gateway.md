---
{"dg-publish":true,"dg-path":"Azure Local Network Gateway.md","permalink":"/azure-local-network-gateway/","tags":["notes"]}
---


A Local Network Gateway is a sub resource of a [[30 Slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]], that represents a on-premises location for the used in tandem with a [[30 Slipbox/Azure Connection\|Azure Connection]] resource in the creation of a [[30 Slipbox/Virtual Private Network\|Virtual Private Network]] or [[30 Slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]] Connection.

The Address Space declared can be one or more [[30 Slipbox/Network Addressing#What is CIDR Notation\|CIDR]] formatted subnets. If you plan to use this Local Network Gateway in a BGP-enabled connection, the minimum prefix to declare is the host address of your BP Peer IP address on your BPN device.

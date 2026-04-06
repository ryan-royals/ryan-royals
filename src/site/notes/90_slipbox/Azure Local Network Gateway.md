---
{"dg-publish":true,"permalink":"/90-slipbox/azure-local-network-gateway/","tags":["notes"],"created":"2026-03-27T09:57:51.488+10:30","updated":"2026-03-27T09:57:51.488+10:30","dg-note-properties":{"tags":"notes","related":["[[90_slipbox/Azure Connection\|Azure Connection]]","[[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]]"],"references":["https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/2-design-implement-vpn-gateway"],"created":"2024-05-06","modified":"2026-03-03"}}
---


A Local Network Gateway is a sub resource of a [[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]], that represents a on-premises location for the used in tandem with a [[Azure Connection]] resource in the creation of a [[90_slipbox/Virtual Private Network\|Virtual Private Network]] or [[Azure Virtual Network Gateway]] Connection.

The Address Space declared can be one or more [[90_slipbox/Network Addressing#What is CIDR Notation\|CIDR]] formatted subnets. If you plan to use this Local Network Gateway in a BGP-enabled connection, the minimum prefix to declare is the host address of your BP Peer IP address on your BPN device.

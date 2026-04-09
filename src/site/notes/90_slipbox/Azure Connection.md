---
{"dg-publish":true,"permalink":"/90-slipbox/azure-connection/","tags":["notes"],"created":"2025-06-11T10:28:47.684+09:30","updated":"2026-03-03T09:55:32.436+10:30","dg-note-properties":{"tags":"notes","related":["[[90_slipbox/Azure Local Network Gateway\|Azure Local Network Gateway]]","[[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]]"],"references":["https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/2-design-implement-vpn-gateway"],"created":"2024-05-06","modified":"2026-03-03"}}
---


A Azure Connection is a sub resource of a [[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]] that represents the association of a [[90_slipbox/Azure Virtual Network Gateway\|Azure Virtual Network Gateway]] and a [[90_slipbox/Azure Local Network Gateway\|Azure Local Network Gateway]].  
This resource holds the configuration information for the connection, including Pre Shared Key and Public IP of the On-premises router.

Azure have a validated list of standard VPN devices from device manufacturers including Cisco, Juniper, Ubiquiti, and Barracuda Networks.

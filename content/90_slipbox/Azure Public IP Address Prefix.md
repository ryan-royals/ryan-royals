---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Public IP Address Prefix.md","permalink":"/slipbox-notes/azure-public-ip-address-prefix/","tags":["notes"],"created":"2024-05-02","updated":"2025-11-28"}
---

 A Public IP Address Prefix is a contiguous range of standard SKU public IP addresses. When you create a public IP address resource, you can assign a static public IP from the prefix and associate the address to Azure resources.

## BYO-IP

A Public IP address Prefix can be a customer supplied range, that is owned outside of the Microsoft ranges with no additional cost of usage of this service.  
The minimum range onboarded is a /24, and must be registered with a Routing Internet Registry such as ARIN or RIPE.

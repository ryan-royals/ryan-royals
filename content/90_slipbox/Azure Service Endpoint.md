---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Service Endpoint.md","permalink":"/slipbox-notes/azure-service-endpoint/","tags":["notes"],"created":"2023-05-15","updated":"2025-11-27"}
---


![Azure Service Endpoint-1728517488906.png](/img/user/10_attachments/Azure%20Service%20Endpoint-1728517488906.png)  
Azure Service Endpoints are used to optimize routing on your subnet to the service it has been configured to reach on a subnet in a [[90_slipbox/Azure Virtual Network\|Azure Virtual Network]].  
It only only offers this access to devices on the Subnet itself, and can not be used outside of the Subnet (Natively).  
A key usage is to simplify routing when using Azure User Defined Route to stop traffic routing to a RouteAll.

A Service Endpoint Policy can be configured to restrict access to only the allowed Storage Accounts through the Service Endpoint.

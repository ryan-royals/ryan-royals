---
{"dg-publish":true,"dg-path":"Azure Service Endpoint.md","permalink":"/azure-service-endpoint/","tags":["notes"]}
---


![Azure Service Endpoint-1728517488906.png](/img/user/40%20References/attachments/image/Azure%20Service%20Endpoint-1728517488906.png)  
Azure Service Endpoints are used to optimize routing on your subnet to the service it has been configured to reach on a subnet in a [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]].  
It only only offers this access to devices on the Subnet itself, and can not be used outside of the Subnet (Natively).  
A key usage is to simplify routing when using [[30 Slipbox/Azure User Defined Route\|UDR's]] to stop traffic routing to a RouteAll.

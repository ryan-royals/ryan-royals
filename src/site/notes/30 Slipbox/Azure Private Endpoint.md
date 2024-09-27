---
{"dg-publish":true,"dg-path":"Azure Private Endpoint.md","permalink":"/azure-private-endpoint/","tags":["notes"]}
---


Private Endpoints allow you to connect to a service over the private network space within a [[30 Slipbox/Azure Virtual Network\|Azure Virtual Network]] without traversing the public IP's of Azure to connect to your resource. This is powered by Azure Private Link.  
They are used on services such as:

- [[30 Slipbox/Azure Storage Account\|Azure Storage Account]]
- [[30 Slipbox/Azure Cosmos DB\|Azure Cosmos DB]]
- [[30 Slipbox/Azure SQL\|Azure SQL]]
- or your own service using [[30 Slipbox/Azure Private Link\|Private Links]]

## Cost

- Endpoint = $0.016 per hour
- Ingress / Egress data Processed
  - 0-1 PB - $0.0152 per GB
  - 1-5 PB - $0.0091 per GB
  - 5+ PB - $0.0061 per GB

## Comparison to Service Endpoints

A [[30 Slipbox/Azure Service Endpoint\|Azure Service Endpoint]] is used to establish a least cost path to the destination resource from a subnet. Service Endpoints do not deploy a Private IP Address to connect to the Resource. They also can not be accessed past their allocated Subnet, and therefore can not be reached from on-premises.

## [[30 Slipbox/Connecting to a Private Endpoint\|Connecting to a Private Endpoint]]

## FAQ

- Private Endpoints work by mapping to Private DNS Zones and by having a presence on the Virtual Network
- The PDNS zone must be connected to each VNET you are connecting to it from.
- A VNET can only be connected to 1 of each type of PDNS Zone (Privatelink.blob.core.windows.net) so best practise is to centralise these zones
- In order to use the Private Endpoint, you have to be able to do a look up to the Azure Magic IP.
- You can have access to read the DNS entry for the Private Endpoint, but you can still be blocked by Firewall or NSG rules.
- Private Endpoints completely bypass other Access Control Lists on the target resource (You can have all public access disabled on Storage Account as example.)
- Private Endpoints must be in the same region as the Virtual Network, but the destination service can be in another region

---

Links: [[30 Slipbox/Azure\|Azure]], [[30 Slipbox/Private Endpoints Presentation\|Private Endpoints Presentation]]  
Tags:  
Reference:

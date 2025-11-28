---
{"dg-publish":true,"permalink":"/90-slipbox/azure-private-endpoint/","tags":["notes"]}
---


Private Endpoints allow you to connect to a service over the private network space within a [[90_slipbox/Azure Virtual Network\|Azure Virtual Network]] without traversing the public IP's of Azure to connect to your resource. This is powered by Azure Private Link.  
They are used on services such as:

- Azure Storage Account
- Azure SQL
- or your own service using [[90_slipbox/Azure Private Link\|Private Links]]

## Cost

- Endpoint = $0.016 per hour
- Ingress / Egress data Processed
  - 0-1 PB - $0.0152 per GB
  - 1-5 PB - $0.0091 per GB
  - 5+ PB - $0.0061 per GB

## Comparison to Service Endpoints

A [[90_slipbox/Azure Service Endpoint\|Azure Service Endpoint]] is used to establish a least cost path to the destination resource from a subnet. Service Endpoints do not deploy a Private IP Address to connect to the Resource. They also can not be accessed past their allocated Subnet, and therefore can not be reached from on-premises.

## Connecting to a Private Endpoint

In order to reach the Private Endpoint, the client has to be able to do a DNS lookup to find the [[90_slipbox/Azure Private DNS Zone\|Azure Private DNS Zones]]. In order to reach the Private DNS zone, you have to be on a Virtual Network that is connected to the Private DNS Zone.

Azure does this by using the [[90_slipbox/Azure Magic IP\|Azure Magic IP]] (168.63.129.16) to confirm what Virtual Network you are coming from, and then supply you the correct records.

### Connect From Virtual Network

![Pasted image 20230512124425.png](/img/user/10_attachments/Pasted%20image%2020230512124425.png)

### Connect From On-premises

![Pasted image 20230512124536.png](/img/user/10_attachments/Pasted%20image%2020230512124536.png)  
![Connecting to a Private Endpoint-1693544625288.png](/img/user/10_attachments/Connecting%20to%20a%20Private%20Endpoint-1693544625288.png)  
Using Server level forwarders in [[Active Directory\|Active Directory]] will not work, as it will always be able to resolve the Public IP of the resource you are trying to reach.  
Conditional Forwarders are used in this situation to forward a whole domain to a different DNS resolver.

### Connect Using Azure Firewall DNS

*Uses [[90_slipbox/Azure DNS Private Resolver\|Azure DNS Private Resolver]] and [[90_slipbox/Azure Firewall\|Azure Firewall]]*  
![Pasted image 20230515095640.png](/img/user/10_attachments/Pasted%20image%2020230515095640.png)

## FAQ

- Private Endpoints work by mapping to Private DNS Zones and by having a presence on the Virtual Network
- The PDNS zone must be connected to each VNET you are connecting to it from.
- A VNET can only be connected to 1 of each type of PDNS Zone (Privatelink.blob.core.windows.net) so best practise is to centralise these zones
- In order to use the Private Endpoint, you have to be able to do a look up to the Azure Magic IP.
- You can have access to read the DNS entry for the Private Endpoint, but you can still be blocked by Firewall or NSG rules.
- Private Endpoints completely bypass other Access Control Lists on the target resource (You can have all public access disabled on Storage Account as example.)
- Private Endpoints must be in the same region as the Virtual Network, but the destination service can be in another region

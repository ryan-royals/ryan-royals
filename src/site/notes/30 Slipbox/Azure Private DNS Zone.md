---
{"dg-publish":true,"dg-path":"Azure Private DNS Zone.md","permalink":"/Azure Private DNS Zone/","tags":["notes"]}
---


Azure Private DNS provides a reliable, secure DNS service to manage and resolve domain names in a virtual network without the need to add a custom DNS solution, without these DNS entries being accessible from the internet.  

## Virtual Network Link

This works by linking to one or many [[30 Slipbox/Azure Virtual Network\|Virtual Networks]], and the DNS Server on the Virtual network needs to be configured to look up against the [[30 Slipbox/Azure Magic IP\|Azure Magic IP]], either by default or by the custom DNS server.

Auto Registration can be enabled on a Link to a VNET, but each VNET can only have Auto Registration enabled once. This service allows for [[30 Slipbox/Azure Virtual Machine\|VMs]] to be discoverable on a custom domain.

It is important to note the same DNS Zone *can not* be linked to the same Virtual Network multiple times. `contoso.com` can be linked to up to 1000 Virtual Networks, but 2 instances of the `contoso.com` can not be linked to the same Virtual Network.  
Private DNS Zones can be created with the same name as long as they are in different resource groups. This is a common occurrence with [[30 Slipbox/Azure Private Link\|Private Links]], and should be considered upfront.

## Restrictions and Limitations

| Resource                                                                                      | Limit |
| --------------------------------------------------------------------------------------------- | ----- |
| Private DNS zones per subscription                                                            | 1000  |
| Record sets per private DNS zone                                                              | 25000 |
| Records per record set for private DNS zones                                                  | 20    |
| Virtual Network Links per private DNS zone                                                    | 1000  |
| Virtual Networks Links per private DNS zones with autoregistration enabled                    | 100   |
| Number of private DNS zones a virtual network can get linked to with autoregistration enabled | 1     |
| Number of private DNS zones a virtual network can get linked                                  | 1000  |

Private DNS Zones must consist of at least 2 labels (`contoso.com,` not `contoso`), and up to a max of 34 labels.

You can not create zone delegations (NS Records) in a private DNS Zone. This can be accomplished by creating another Private DNS Zone with the required labels.

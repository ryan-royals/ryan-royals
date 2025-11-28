---
{"dg-publish":true,"permalink":"/90-slipbox/azure-virtual-network/","tags":["notes"]}
---

Azure Virtual Networks exist on [[90_slipbox/OSI Networking Model#Layer 3 - Network\|Layer 3 of the OSI Networking Model]].  
Using Virtual Networks, resources to communicate to the internet, communicate between other resources, and communicate on premises.

All resources in a Virtual network can communicate outbound to the internet by default. *This is changing ~~at the end of 2024~~ Someday*.

## DNS

The default DNS server on every VNET is [[90_slipbox/Azure Magic IP\|168.63.129.16]], but can be changed to any address.

## Peering

Virtual Networks can be [[90_slipbox/Peering Azure Virtual Networks\|peered together]], allowing for network topologies to be created.

### Designing a Virtual Network

#### Guiding Principals

- It is reasonable to have multiple Virtual Networks per region, per subscription.  
- Make sure the *Address Space* does not overlap with other VNets or or premises networks.
- Do you require isolation for security?

#### Address Space

Virtual Networks have a *Address Space* that is used by [[90_slipbox/Azure Subnet\|Azure Subnet]].

It is recommended to use a Address Space enumerated in [[90_slipbox/RFC 1918\|RFC 1918]].  
Following this, there are some restricted ranges that can not be used:

- 224.0.0.0/4 (Multicast)
- 255.255.255.255/32 (Broadcast)
- 127.0.0.0/8 (Loopback)
- 169.254.0.0/16 (Link-local)
- 168.63.129.16/32 ([[90_slipbox/Azure Magic IP\|Internal DNS]])

---
{"dg-publish":true,"dg-path":"Blog Posts/How to design Network Spaces and Blocks.md","permalink":"/blog-posts/how-to-design-network-spaces-and-blocks/","tags":["blogs"],"created":"2024-06-25","updated":"2025-11-28"}
---

2025-11-28:  
This is a bit old now, and I would more go:

Region > Env > Workload  
AUE > Platform > Hub 1  
AUE > Prod > Workload 1

But the planning method is the important part, I still like having spaces and blocks

---

The key problem space when it comes to designing a network is knowing what ranges are available to use. Choosing a incorrect space can have long term impact on your application, one of the largest being making you unable to peer your Vnet to a peering mesh as your address space is already used on the Hub and Spoke / Mesh elsewhere.

![How to design Network Spaces and Blocks-1719287165023.png](/img/user/10_attachments/How%20to%20design%20Network%20Spaces%20and%20Blocks-1719287165023.png)  
Figure 1: Example of unable to peer

In Figure 1, Vnet 2 and Vnet 3 share the same address space, and can not both be peered to Hub 1.

![How to design Network Spaces and Blocks-1719287179913.png](/img/user/10_attachments/How%20to%20design%20Network%20Spaces%20and%20Blocks-1719287179913.png)  
Figure 2: Complex example of unable to peer

In Figure 2, Vnet 3 can not peer to Vnet 1 as Vnet 3 and Vnet 2 share the same address space and Vnet 2 already exists in the peering mesh.

Considerations need to be made at the design phase to accommodate current networking and future expansion. Key considerations include:

- What are the current IP addresses being used in Azure and On Prem
    - Even if not planning on a VPN / ExpressRoute now, assume that it may happen in the future.
- How many standalone applications are going to be present now and in the future.
- What are the address space requirements for each application, and what happens if they change in the future?
- How do we know what Ip address to use next?
- How can easily define Firewall rules?

## Designing a Scalable Network

When defining a network, it is good to have a fundamental understanding on how Subnets work and divide. To start, document all the services you need to use and their networking requirements. An example is that Azure Container apps using Workload profiles requires /27 or above (smaller number) sized Subnet. If we needed 2 Workload Profiles, that would mean we need two /27's in this example. The key shorthand is that a single /26 has two /27’s within it, so we now know that our VNet needs to be at least a /26. A handy tool for visualising this is [Visual Subnet Calculator - Split/Join](https://visualsubnetcalc.com/).

Our approach to designing the network is leveraging principles put forward by Azure IPAM by using different buckets of address to make easy allocations to be used in future, and expandable for when things change. In Elements Core we use *Spaces* and *Blocks.*

### Spaces

![How to design Network Spaces and Blocks-1719287217135.png](/img/user/10_attachments/How%20to%20design%20Network%20Spaces%20and%20Blocks-1719287217135.png)  
Figure 3: An example of Spaces

| **Space**                     |
| ----------------------------- |
| **Platform -**10.0.0.0/20     |
| **Production -** 10.0.16.0/20 |
| **Dev -** 10.0.32.0/20        |

Table 1: Example of Spaces

A *Space* is the largest bucket of addresses that we define. *Spaces* are used as logic groups of Environments, such as Production, Test, UAT, Dev, Sandbox, etc. *Spaces* should not overlap with each other, and do not need to be a contiguous set of addresses (although it is reasonable to make accommodations for this up front where possible.)

In our templating, we also include *Platform* as its own *Space* as we use this to enable simple firewalling rules, where we can say Dev can communicate to Platform, but Dev can not communicate to Prod.

### Blocks

![How to design Network Spaces and Blocks-1719287228235.png](/img/user/10_attachments/How%20to%20design%20Network%20Spaces%20and%20Blocks-1719287228235.png)  
Figure 4: An Example of Spaces with Blocks

| **Space**                              | **Block**                        |
| -------------------------------------- | -------------------------------- |
| **Platform -** 10.0.0.0/20             | **Australia East -** 10.0.0.0/21 |
| **Australia South East -** 10.0.8.0/21 |                                  |
|                                        |                                  |
| **Production -** 10.0.16.0/20          | **App 1 Prod -** 10.0.16.0/23    |
| **App 2 Prod -** 10.0.18.0/23          |                                  |
|                                        |                                  |
| **Dev -** 10.0.32.0/20                 | **App 1 Dev -** 10.0.32.0/23     |
| **App 2 Dev -** 10.0.34.0/23           |                                  |

Table 2: An example of Spaces with Blocks

A *Block* is a subdivision of a *Space*, used for making further reservations, scoped more at a Application. Blocks allow us to reserve a block of addresses for a application to consume how they want, without impacting their neighbours as each *Block* can not overlap. As with *Spaces*, *Blocks* do not need to be a contiguous set of addresses, but where possible it is worth accommodating for this for simplicity.

In our templating, we have a *block* for each hub region in the Platform *Space*, which houses each Firewall, Bastion, etc. In our Environment *Spaces*, we use the application name as the key for the *Block,* to represent that applications Dev/ Test / Prod instance. Using these Blocks, we have more scoping available for us to define firewall rules, such as App 1 Dev can communicate to App 1 Prod, but App 1 Dev can not communicate to App 2 Prod.

### Virtual Networks

![How to design Network Spaces and Blocks-1719287240056.png](/img/user/10_attachments/How%20to%20design%20Network%20Spaces%20and%20Blocks-1719287240056.png)  
Figure 5: A completed example of Spaces, Blocks and Virtual Networks

| **Space**                                           | **Block**                        | **VNET**                                   | **Subnet**                                 |
| --------------------------------------------------- | -------------------------------- | ------------------------------------------ | ------------------------------------------ |
| **Platform -** 10.0.0.0/20                          | **Australia East -** 10.0.0.0/21 | **Hub 1 -** 10.0.0.0/22                    | **AzureFirewallSubnet**<br><br>10.0.0.0/26 |
| **AzureFirewallManagementSubnet**  <br>10.0.0.64/26 |                                  |                                            |                                            |
| **AzureBastionSubnet**<br><br>10.0.0.128/26         |                                  |                                            |                                            |
|                                                     |                                  |                                            |                                            |
| **Australia South East -** 10.0.8.0/21              | **Hub 2 -** 10.0.8.0/22          | **AzureFirewallSubnet**<br><br>10.0.8.0/26 |                                            |
| **AzureFirewallManagementSubnet**  <br>10.0.8.64/26 |                                  |                                            |                                            |
| **AzureBastionSubnet**<br><br>10.0.8.128/26         |                                  |                                            |                                            |
|                                                     |                                  |                                            |                                            |
| **Production -** 10.0.16.0/20                       | **App 1 Prod -** 10.0.16.0/23    | **Vnet 1 -** 10.0.16.0/24                  | **General**<br><br>10.0.16.0/26            |
|                                                     |                                  |                                            |                                            |
| **App 2 Prod -** 10.0.18.0/23                       | **Vnet 2 -** 10.0.18.0/24        | **General**<br><br>10.0.18.0/26            |                                            |
|                                                     |                                  |                                            |                                            |
| **Dev -** 10.0.32.0/20                              | **App 1 Dev -** 10.0.32.0/23     | **Vnet 1 -** 10.0.32.0/24                  | **General**<br><br>10.0.32.0/26            |
|                                                     |                                  |                                            |                                            |
| **App 2 Dev -** 10.0.34.0/23                        | **Vnet 2 -** 10.0.34.0/24        | **General**<br><br>10.0.34.0/26            |                                            |

With all the work on *Spaces* and *Blocks* up front, it is now clear what IP addresses are allocated per app, per environment. With this information, the administrator of the app can carve up the block as they see fit with as many Virtual Networks and Subnets as required, as long as they stay within their *Block*.

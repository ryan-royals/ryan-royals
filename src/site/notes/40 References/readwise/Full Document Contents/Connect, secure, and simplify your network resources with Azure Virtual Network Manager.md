---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/connect-secure-and-simplify-your-network-resources-with-azure-virtual-network-manager/","tags":["rw/articles"]}
---

![rw-book-cover](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/c22e6224-1b79-4f8c-954b-f8f96b9ba9b7.png)

Enterprise-scale management and configuration of your network resources in Azure are key to keeping costs down, reducing operational overhead, and properly connecting and securing your network presence in the cloud. **We are happy to announce [Azure Virtual Network Manager](https://azure.microsoft.com/products/virtual-network-manager/) (AVNM), your one-stop shop for managing the connectivity and security of your network resources at scale, is generally available.**

#### What is Azure Virtual Network Manager?

AVNM works through a main process of **group, configure, and deploy**. You’ll group your network resources across subscriptions, regions, and even tenants; configure the kind of connectivity and security you want among your grouped network resources; and finally, deploy those configurations onto those network groups in whichever and however many regions you’d like.

##### Common use cases

Common use cases for AVNM include the following and can be addressed by deploying AVNM’s connectivity and security admin configurations onto your defined network groups:

* Interconnected virtual networks (VNets) that communicate directly with each other.
* Central infrastructure services in a hub VNet that are shared by other VNets.
	+ Establishing direct connectivity between spoke VNets to reduce latency.
* Automatic maintenance of connectivity at scale, even with the addition of new network resources.
* Enforced standard security rules on all existing and new VNets without risk of change.
	+ Keeping flexibility for VNet owners to configure network security groups (NSGs) as needed for more specific traffic dictation.
* Application of default security rules across an entire organization to mitigate the risk of misconfiguration and security holes.
* Force-allowance of services’ traffic, such as monitoring services and program updates, to prevent accidental blocking through security rules.

##### Connectivity configuration

###### Hub and spoke topology

When you have some services in a hub VNet, such as an [Azure Firewall](https://azure.microsoft.com/products/azure-firewall) or [ExpressRoute](https://azure.microsoft.com/products/expressroute), and you need to connect several other VNets to that hub to share those services, that means you’ll have to establish connectivity between each of those spoke VNets and the hub. In the future, if you provision new VNets, you’ll also need to make sure those new VNets are correctly connected to the hub VNet.

With AVNM, you can create groups of VNets and select those groups to be connected to your desired hub VNet, and AVNM will establish all the necessary connectivity between your hub VNet and each VNet in your selected groups behind the scenes. On top of the simplicity of creating a hub and spoke topology, new VNets that match your desired conditions can be automatically added to this topology, reducing manual interference from your part.

For the time being, establishing direct connectivity between the VNets within a spoke network group is still in preview and will become generally available (GA) at a later date.

###### Mesh

If you want all of your VNets to be able to communicate with each other regionally or globally, you can build a mesh topology with AVNM’s connectivity configuration. You’ll select your desired network groups and AVNM will establish connectivity between every VNet that is a part of your selected network groups. The mesh connectivity configuration feature is still in preview and will become generally available at a later date.

###### How to implement connectivity configurations with existing environments

Let’s say you have a cross-region hub and spoke topology in Azure that you’ve set up through manual peerings. Your hub VNet has an ExpressRoute gateway and your dozens of spoke VNets are owned by various application teams.

Here are the steps you would take to implement and automate this topology using AVNM:

1. Create your network manager.
2. Create a network group for each application team’s respective VNets using Azure Policy definitions that can be conditionally based on parameters including (but not limited to) subscription, VNet tag, and VNet name.
3. Create a connectivity configuration with hub and spoke selected. Select your desired hub VNet and your network groups as the spokes.
4. By default, all connectivity established with AVNM is additive after the connectivity configuration’s deployment. If you’d like AVNM to clean up existing peerings for you, this is an option you can select; otherwise, existing connectivity can be manually cleaned up later if desired.
5. Deploy your hub and spoke connectivity configuration to your desired regions.

In just a few clicks, you’ve set up a hub and spoke topology among dozens of VNets from all application teams globally through AVNM. By defining the conditions of VNet membership for your network groups representing each application team, you’ve ensured that any newly created VNet matching those conditions will automatically be added to the corresponding network group and receive the same connectivity configuration applied onto it. Whether you choose to have AVNM delete existing peerings or not, there is no downtime to connectivity between your spoke VNets and hub VNet.

##### Security feature

AVNM currently provides you with the ability to protect your VNets at scale with security admin configurations. This type of configuration consists of security admin rules, which are high-priority security rules defined similarly to, but with precedence over NSG rules.

The security admin configuration feature is still in preview and will GA at a later date.

###### Enforcement and flexibility

With NSGs alone, widespread enforcement on VNets across several applications, teams, or even entire organizations can be tricky. Often there’s a balancing act between attempts at centralized enforcement across an organization and handing over granular, flexible control to teams. The cost of hard enforcement is higher operational overhead as admins need to manage an increasing number of NSGs. The cost of individual teams tailoring their own security rules is the risk of vulnerability as misconfiguration or opened unsafe ports is possible. Security admin rules aim to eliminate this sliding scale of choosing between enforcement and flexibility altogether by providing central governance teams with the ability to establish guardrails, while intentionally allowing traffic for individual teams to flexibly pinpoint security as needed through NSG rules.

###### Difference from NSGs

Security admin rules are similar to NSG rules in structure and input parameters, but they are not the exact same construct. Let’s boil down these differences and similarities:

|  | **TARGET AUDIENCE** | **APPLIED ON** | **EVALUATION ORDER** | **ACTION TYPES** | **PARAMETERS** |
| --- | --- | --- | --- | --- | --- |
| **SECURITY ADMIN RULES** | Network admins, central governance team | Virtual networks | Higher priority | **Allow**, **Deny**, **Always Allow** | Priority, protocol, action, source, destination |
| **NSG RULES** | Individual teams | Subnets, NICs | Lower priority, after security admin rules | **Allow**, **Deny** |

One key difference is the security admin rule’s **Allow** type. Unlike its other action types of **Deny** and **Always Allow**, if you create a security admin rule to **Allow** a certain type of traffic, then that traffic will be further evaluated by NSG rules matching that traffic. However, **Deny** and **Always Allow** security admin rules will stop the evaluation of traffic, meaning NSGs down the line will not see or handle this traffic. As a result, regardless of NSG presence, administrators can use security admin rules to protect an organization by default.

![](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/c22e6224-1b79-4f8c-954b-f8f96b9ba9b7.png)
###### Key Scenarios

###### Providing exceptions

Being able to enforce security rules throughout an organization is useful, to say the least. But one of the benefits of security admin rules that we’ve mentioned is its allowance for flexibility by teams within the organization to handle traffic differently as needed. Let’s say you’re a network administrator and you’ve enforced security admin rules to block all high-risk ports across your entire organization, but an application team 1 needs SSH traffic for a few of their resources and has requested an exception for their VNets. You’d create a network group specifically for application team 1’s VNets and create a security admin rule collection targeting only that network group-inside that rule collection, you’d create a security admin rule of action type **Allow** for inbound SSH traffic (port 22). The priority of this rule would need to be higher than the original rule you created that blocked this port across all of your organization’s resources. Effectively, you’ve now established an exception to the blocking of SSH traffic just for application team 1’s VNets, while still protecting your organization from that traffic by default.

![](https://azurecomcdn.azureedge.net/mediahandler/acomblog/media/Default/blog/14293fcd-1261-4229-b136-8ab9fe7f7be3.png)
###### Force-allowing traffic to and from monitoring services or domain controllers

Security admin rules are handy for blocking risky traffic across your organization, but they’re also useful for force-allowing traffic needed for certain services to continue running as expected. If you know that your application teams need software updates for their virtual machines, then you can create a rule collection targeting the appropriate network groups consisting of **Always Allow** security admin rules for the ports where the updates come through. This way, even if an application team misconfigures an NSG to deny traffic on a port necessary for updates, the security admin rule will ensure the traffic is delivered and doesn’t hit that conflicting NSG.

###### How to implement security admin configurations with existing environments

Let’s say you have an NSG-based security model consisting of hundreds of NSGs that are modifiable by both the central governance team and individual application teams. Your organization implemented this model originally to allow for flexibility, but there have been security vulnerabilities due to missing security rules and constant NSG modification.

Here are the steps you would take to implement and enforce organization-wide security using AVNM:

1. Create your network manager.
2. Create a network group for each application team’s respective VNets using Azure Policy definitions that can be conditionally based on parameters including (but not limited to) subscription, VNet tag, and VNet name.
3. Create a security admin configuration with a rule collection targeting all network groups. This rule collection represents the standard security rules that you’re enforcing across your entire organization.
4. Create security admin rules blocking high-risk ports. These security admin rules take precedence over NSG rules, so Deny security admin rules have no possibility of conflict with existing NSGs. Redundant or now-circumvented NSGs can be manually cleaned up if desired.
5. Deploy your security admin configuration to your desired regions.

You’ve now set up an organization-wide set of security guardrails among all of your application teams’ VNets globally through AVNM. You’ve established enforcement without sacrificing flexibility, as you’re able to create exceptions for any application team’s set of VNets. Your old NSGs still exist, but all traffic will hit your security admin rules first. You can clean up redundant or avoided NSGs, and your network resources are still protected by your security admin rules, so there is no downtime from a security standpoint.

#### Learn more about Azure Virtual Network Manager

Check out the [AVNM overview](https://azure.microsoft.com/en-us/products/virtual-network-manager/), read more about AVNM in our [public documentation set](https://learn.microsoft.com/azure/virtual-network-manager/), and deep-dive into AVNM’s security offering through our [security blog](https://techcommunity.microsoft.com/t5/azure-networking-blog/securing-your-virtual-networks-with-azure-virtual-network/ba-p/3353366).

* #### Explore

 Let us know what you think of Azure and what you would like to see in the future.
* Build your cloud computing and Azure skills with free courses by Microsoft Learn.

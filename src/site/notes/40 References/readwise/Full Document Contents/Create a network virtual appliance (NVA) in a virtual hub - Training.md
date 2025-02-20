---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/create-a-network-virtual-appliance-nva-in-a-virtual-hub-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

[Previous](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/7-exercise-create-virtual-wan-by-using-azure-portal/) 

* #### Design and implement hybrid networking

	+ [Introduction 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/1-introduction/)
	+ [Design and implement Azure VPN Gateway 24 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/2-design-implement-vpn-gateway/)
	+ [Exercise: Create and configure a virtual network gateway 10 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/3-exercise-create-configure-local-network-gateway/)
	+ [Connect networks with Site-to-site VPN connections 3 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/4-connect-networks-site-to-site-vpn-connections/)
	+ [Connect devices to networks with Point-to-site VPN connections 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/5-connect-devices-to-networks-point-to-site-vpn-connections/)
	+ [Connect remote resources by using Azure Virtual WANs 3 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/6-connect-remote-resources-by-using-azure-virtual-wans/)
	+ [Exercise: create a Virtual WAN by using the Azure portal 8 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/7-exercise-create-virtual-wan-by-using-azure-portal/)
	+ [Create a network virtual appliance (NVA) in a virtual hub 7 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/8-create-network-virtual-appliance-virtual-hub/)
	+ [Summary 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/9-summary/)

Achievements

 [Next](https://learn.microsoft.com/en-us/training/modules/design-implement-hybrid-networking/9-summary/)  

 Completed 200 XP

One of the benefits of Azure Virtual WAN is the ability to support reliable connections from many different technologies, whether Microsoft based, such as ExpressRoute or a VPN Gateway, or from a networking partner, such as Barracuda CloudGen WAN, Cisco Cloud OnRamp for Multi-Cloud, and VMware SD-WAN. These types of devices are known as network virtual appliances (NVAs); they are deployed directly into a Virtual WAN hub and have an externally facing public IP address. This capability enables customers who want to connect their branch Customer Premises Equipment (CPE) to the same brand NVA in the virtual hub to take advantage of proprietary end-to-end SD-WAN capabilities. Once VNets are connected to the virtual hub, NVAs enable transitive connectivity throughout the organization's Virtual WAN.

#### Manage an NVA in a Virtual Hub

The NVAs available in the Azure Marketplace can be deployed directly into a virtual hub and nowhere else. Each is deployed as a Managed Application, which allows Azure Virtual WAN to manage the configuration of the NVA. They cannot be deployed within an arbitrary VNet.

The following diagram shows the NVA deployment process:

![NVA deployment process.](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/nva-high-level-process-836b75d2.png)
Although each NVA offers support for different CPEs and has a slightly different user experience, they all offer a Managed Application experience through Azure Marketplace, NVA Infrastructure Unit-based capacity and billing, and Health Metrics surfaced through Azure Monitor.

#### Deploy an NVA in your Virtual Hub

To deploy an NVA in your virtual hub, you can access the Azure Marketplace through the Azure portal and select the Managed Application for the NVA partner that you need to enable connectivity for your devices. When you create an NVA in the Virtual WAN hub, like all Managed Applications, there will be two Resource Groups created in your subscription.

* **Customer Resource Group** - This will contain an application placeholder for the Managed Application. Partners can use this resource group to expose whatever customer properties they choose here.
* **Managed Resource Group** - Customers cannot configure or change resources in this resource group directly, as this is controlled by the publisher of the Managed Application. This Resource Group will contain the NetworkVirtualAppliances resource.

The NVA is configured automatically as part of the deployment process. Once the NVA has been provisioned into the virtual hub, any additional configuration must be performed via the NVA partners portal or management application. You cannot access the NVA directly.

Unlike Azure VPN Gateway configurations, you do not need to create Site resources, Site-to-Site connection resources, or point-to-site connection resources to connect your branch sites to your NVA in the Virtual WAN hub. This is all managed via the NVA partner.

You still need to create Hub-to-VNet connections to connect your Virtual WAN hub to your Azure VNets.

##### Create the Network Virtual Appliance in the hub

In this step, you will create a Network Virtual Appliance in the hub. The procedure for each NVA will be different for each NVA partner's product. For this example, we are creating a Barracuda CloudGen WAN Gateway.

1. Locate the Virtual WAN hub you created in the previous step and open it. ![screenshot of Azure Virtual WAN resource ion the Azure portal.](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/nva-hub-eec1b931.png)
2. Find the Network Virtual Appliances tile and select the Create link.
3. On the Network Virtual Appliance blade, select Barracuda CloudGen WAN, then select the Create button. ![screenshot of Network Virtual Appliance configuration blade in Azure portal](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/select-nva-0c5ab0b6.png)
4. This will take you to the Azure Marketplace offer for the Barracuda CloudGen WAN gateway. Read the terms, then select the **Create** button when you're ready. ![Azure portal screenshot of creating a Barracuda CloudGen WAN gateway](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/barracuda-create-basics-d11c3a3c.png)
5. On the Basics page you will need to provide the following information:

	* **Subscription -** Choose the subscription you used to deploy the Virtual WAN and hub.
	* **Resource Group** - Choose the same Resource Group you used to deploy the Virtual WAN and hub.
	* **Region** - Choose the same Region in which your Virtual hub resource is located.
	* **Application Name** - The Barracuda NextGen WAN is a Managed Application. Choose a name that makes it easy to identify this resource, as this is what it will be called when it appears in your subscription.
	* **Managed Resource Group** - This is the name of the Managed Resource Group in which Barracuda will deploy resources that are managed by them. The name should be pre-populated.
6. Select the Next: CloudGen WAN gateway button. ![screenshot](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-hybrid-networking/media/barracuda-cloudgen-wan-ebe559b5.png)
7. Provide the following information here:

	* **Virtual WAN Hub** - The Virtual WAN hub you want to deploy this NVA into.
	* **NVA Infrastructure Units** - Indicate the number of NVA Infrastructure Units you want to deploy this NVA with. Choose the amount of aggregate bandwidth capacity you want to provide across all of the branch sites that will be connecting to this hub through this NVA.
	* **Token** - Barracuda requires that you provide an authentication token here in order to identify yourself as a registered user of this product.

##### NVA Infrastructure Units

When you create an NVA in the Virtual WAN hub, you must choose the number of NVA Infrastructure Units you want to deploy it with. An NVA Infrastructure Unit is a unit of aggregate bandwidth capacity for an NVA in the Virtual WAN hub. An NVA Infrastructure Unit is similar to a VPN Scale Unit in terms of the way you think about capacity and sizing.

* One NVA Infrastructure Unit represents 500 Mbps of aggregate bandwidth for all branch site connections coming into this NVA.
* Azure supports from 1-80 NVA Infrastructure Units for a given NVA virtual hub deployment.
* Each partner may offer different NVA Infrastructure Unit bundles that are a subset of all supported NVA Infrastructure Unit configurations.

To learn more about deploying an NVA, see [How to create a Network Virtual Appliance in an Azure Virtual WAN hub (Preview)](https://learn.microsoft.com/en-us/azure/virtual-wan/how-to-nva-hub).

#### Check your knowledge

1.

A network engineer wants to provide VMware SD-WAN connectivity for their clients. Which Azure resource should they deploy?

Point-to-site VPN Gateway

Local network gateway

Network Virtual Appliance (NVA).

2.

Where can an NVA be deployed?

NVAs are deployed into an on-premises subnet.

NVAs are deployed directly into a Virtual WAN hub.

NVAs are deployed into a security-isolated subnet.

You must answer all questions before checking your work.

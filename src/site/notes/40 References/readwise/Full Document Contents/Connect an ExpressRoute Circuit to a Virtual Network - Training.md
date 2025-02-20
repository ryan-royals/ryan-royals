---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/connect-an-express-route-circuit-to-a-virtual-network-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

[Previous](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/6-configure-peering-for-expressroute-deployment/) 

* #### Design and implement Azure ExpressRoute

	+ [Introduction 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/1-introduction/)
	+ [Explore Azure ExpressRoute 22 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/2-explore/)
	+ [Design an ExpressRoute deployment 7 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/3-design-expressroute-deployment/)
	+ [Exercise: configure an ExpressRoute gateway 5 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/4-exercise-configure-expressroute-gateway/)
	+ [Exercise: provision an ExpressRoute circuit 5 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/5-exercise-provision-expressroute-circuit/)
	+ [Configure peering for an ExpressRoute deployment 10 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/6-configure-peering-for-expressroute-deployment/)
	+ [Connect an ExpressRoute circuit to a virtual network 5 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/7-connect-expressroute-circuit-virtual-network/)
	+ [Connect geographically dispersed networks with ExpressRoute global reach 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/8-connect-geographically-dispersed-networks-expressroute-global-reach/)
	+ [Improve data path performance between networks with ExpressRoute FastPath 10 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/9-improve-data-path-performance-between-networks-expressroute-fastpath/)
	+ [Troubleshoot ExpressRoute connection issues 6 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/10-troubleshoot-expressroute-connection-issues/)
	+ [Summary and resources 1 min : Completed](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/11-summary-resources/)

Achievements

 [Next](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/8-connect-geographically-dispersed-networks-expressroute-global-reach/)  

 Completed 100 XP

An ExpressRoute circuit represents a logical connection between your on-premises infrastructure and Microsoft cloud services through a connectivity provider. You can order multiple ExpressRoute circuits. Each circuit can be in the same or different regions and can be connected to your premises through different connectivity providers. ExpressRoute circuits do not map to any physical entities. A circuit is uniquely identified by a standard GUID called as a service key (s-key).

In the previous exercises you created an ExpressRoute Gateway and an ExpressRoute circuit. You then learned how to configure peering for an express route circuit. You will now learn how to create a connection between your ExpressRoute circuit and Azure virtual network.

#### Connect a virtual network to an ExpressRoute circuit

* You must have an active ExpressRoute circuit.
* Ensure that you have Azure private peering configured for your circuit.
* Ensure that Azure private peering gets configured and establishes BGP peering between your network and Microsoft for end-to-end connectivity.
* Ensure that you have a virtual network and a virtual network gateway created and fully provisioned. A virtual network gateway for ExpressRoute uses the GatewayType 'ExpressRoute', not VPN.
* You can link up to 10 virtual networks to a standard ExpressRoute circuit. All virtual networks must be in the same geopolitical region when using a standard ExpressRoute circuit.
* A single VNet can be linked to up to 16 ExpressRoute circuits. Use the following process to create a new connection object for each ExpressRoute circuit you are connecting to. The ExpressRoute circuits can be in the same subscription, different subscriptions, or a mix of both.
* If you enable the ExpressRoute premium add-on, you can link virtual networks outside of the geopolitical region of the ExpressRoute circuit. The premium add-on will also allow you to connect more than 10 virtual networks to your ExpressRoute circuit depending on the bandwidth chosen.
* To create the connection from the ExpressRoute circuit to the target ExpressRoute virtual network gateway, the number of address spaces advertised from the local or peered virtual networks needs to be equal to or less than **200**. Once the connection has been successfully created, you can add additional address spaces, up to 1,000, to the local or peered virtual networks.

#### Add a VPN to an ExpressRoute deployment

This section helps you configure secure encrypted connectivity between your on-premises network and your Azure virtual networks (VNets) over an ExpressRoute private connection. You can use Microsoft peering to establish a site-to-site IPsec/IKE VPN tunnel between your selected on-premises networks and Azure VNets. Configuring a secure tunnel over ExpressRoute allows for data exchange with confidentiality, anti-replay, authenticity, and integrity.

Note

When you set up site-to-site VPN over Microsoft peering, you are charged for the VPN gateway and VPN egress.

For high availability and redundancy, you can configure multiple tunnels over the two MSEE-PE pairs of an ExpressRoute circuit and enable load balancing between the tunnels.

VPN tunnels over Microsoft peering can be terminated either using VPN gateway or using an appropriate Network Virtual Appliance (NVA) available through Azure Marketplace. You can exchange routes statically or dynamically over the encrypted tunnels without exposing the route exchange to the underlying Microsoft peering. In this section, BGP (different from the BGP session used to create the Microsoft peering) is used to dynamically exchange prefixes over the encrypted tunnels.

Important

For the on-premises side, typically Microsoft peering is terminated on the DMZ and private peering is terminated on the core network zone. The two zones would be segregated using firewalls. If you are configuring Microsoft peering exclusively for enabling secure tunneling over ExpressRoute, remember to filter through only the public IPs of interest that are getting advertised via Microsoft peering.

**Steps**

* Configure Microsoft peering for your ExpressRoute circuit.
* Advertise selected Azure regional public prefixes to your on-premises network via Microsoft peering.
* Configure a VPN gateway and establish IPsec tunnels
* Configure the on-premises VPN device.
* Create the site-to-site IPsec/IKE connection.
* (Optional) Configure firewalls/filtering on the on-premises VPN device.
* Test and validate the IPsec communication over the ExpressRoute circuit.

#### Next unit: Connect geographically dispersed networks with ExpressRoute global reach

 [Continue](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/8-connect-geographically-dispersed-networks-expressroute-global-reach/)

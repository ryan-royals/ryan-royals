---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/improve-data-path-performance-between-networks-with-express-route-fast-path-training/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

[Previous](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/8-connect-geographically-dispersed-networks-expressroute-global-reach/) 

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

 [Next](https://learn.microsoft.com/en-us/training/modules/design-implement-azure-expressroute/10-troubleshoot-expressroute-connection-issues/)  

 Completed 200 XP

ExpressRoute virtual network gateway is designed to exchange network routes and route network traffic. FastPath is designed to improve the data path performance between your on-premises network and your virtual network. When enabled, FastPath sends network traffic directly to virtual machines in the virtual network, bypassing the gateway.

**Circuits**

FastPath is available on all ExpressRoute circuits.

**Gateways**

FastPath still requires a virtual network gateway to be created to exchange routes between virtual network and on-premises network.

##### Gateway requirements for ExpressRoute FastPath

To configure FastPath, the virtual network gateway must be either:

* Ultra-Performance
* ErGw3AZ

Important

If you plan to use FastPath with IPv6-based private peering over ExpressRoute, make sure to select ErGw3AZ for SKU. Note that this is only available for circuits using ExpressRoute Direct.

**Limitations**

While FastPath supports most configurations, it does not support the following features:

* UDR on the gateway subnet: This UDR has no impact on the network traffic that FastPath sends directly from your on-premises network to the virtual machines in Azure virtual network.
* VNet Peering: If you have other virtual networks peered with the one that is connected to ExpressRoute, the network traffic from your on-premises network to the other virtual networks (i.e., the so-called "Spoke" VNets) will continue to be sent to the virtual network gateway. The workaround is to connect all the virtual networks to the ExpressRoute circuit directly.
* Basic Load Balancer: If you deploy a Basic internal load balancer in your virtual network or the Azure PaaS service you deploy in your virtual network uses a Basic internal load balancer, the network traffic from your on-premises network to the virtual IPs hosted on the Basic load balancer will be sent to the virtual network gateway. The solution is to upgrade the Basic load balancer to a Standard load balancer.
* Private Link: If you connect to a private endpoint in your virtual network from your on-premises network, the connection will go through the virtual network gateway.

##### Configure ExpressRoute FastPath

To enable FastPath, connect a virtual network to an ExpressRoute circuit using the Azure portal.

This section shows you how to create a connection to link a virtual network to an Azure ExpressRoute circuit using the Azure portal. The virtual networks that you connect to your Azure ExpressRoute circuit can either be in the same subscription or be part of another subscription.

**Prerequisites**

* Review the routing requirements, and workflows before you begin configuration.
* You must have an active ExpressRoute circuit.
* Follow the instructions to create an ExpressRoute circuit and have the circuit enabled by your connectivity provider.
* Ensure that you have Azure private peering configured for your circuit.
* Ensure that Azure private peering gets configured and establishes BGP peering between your network and Microsoft for end-to-end connectivity.
* Ensure that you have a virtual network and a virtual network gateway created and fully provisioned. A virtual network gateway for ExpressRoute uses the GatewayType 'ExpressRoute', not VPN.
* You can link up to 10 virtual networks to a standard ExpressRoute circuit. All virtual networks must be in the same geopolitical region when using a standard ExpressRoute circuit.
* A single VNet can be linked to up to 16 ExpressRoute circuits. Use the following process to create a new connection object for each ExpressRoute circuit you are connecting to. The ExpressRoute circuits can be in the same subscription, different subscriptions, or a mix of both.
* If you enable the ExpressRoute premium add-on, you can link virtual networks outside of the geopolitical region of the ExpressRoute circuit. The premium add-on will also allow you to connect more than 10 virtual networks to your ExpressRoute circuit depending on the bandwidth chosen.
* To create the connection from the ExpressRoute circuit to the target ExpressRoute virtual network gateway, the number of address spaces advertised from the local or peered virtual networks needs to be equal to or less than **200**. Once the connection has been successfully created, you can add additional address spaces, up to 1,000, to the local or peered virtual networks.

**Connect a VNet to a circuit - same subscription**

Note

BGP configuration information will not appear if the layer 3 provider configured your peering. If your circuit is in a provisioned state, you should be able to create connections.

1. To create a connection Ensure that your ExpressRoute circuit and Azure private peering have been configured successfully. Your ExpressRoute circuit should look like the following image:

  ![Azure portal - ExpressRoute circuit provisioned for private peering](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/express-route-circuit-ba06fb75.png)
2. You can now start provisioning a connection to link your virtual network gateway to your ExpressRoute circuit. Select **Connection** > **Add** to open the **Add connection** page.

  ![Azure portal - Add a connection](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/add-connection-3d903613.png)
3. Enter a name for the connection and then select **Next: Settings >**.

  ![Azure portal - Create connection basics tab](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/create-connection-basic-9e210444.png)
4. Select the gateway that belongs to the virtual network that you want to link to the circuit and select **Review + create**. Then select **Create** after validation completes.

  ![Azure portal - Create connection settings tab - specify ERGW virtual network gateway](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/create-connection-settings-5e5bf3ff.png)
5. After your connection has been successfully configured, your connection object will show the information for the connection.

  ![Azure portal - verify connection i successful](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/connection-object-c2c46f5e.png)

**Administration - About circuit owners and circuit users**

The 'circuit owner' is an authorized Power User of the ExpressRoute circuit resource. The circuit owner can create authorizations that can be redeemed by 'circuit users'. Circuit users are owners of virtual network gateways that are not within the same subscription as the ExpressRoute circuit. Circuit users can redeem authorizations (one authorization per virtual network).

The circuit owner has the power to modify and revoke authorizations at any time. Revoking an authorization results in all link connections being deleted from the subscription whose access was revoked.

**Circuit owner operations**

**To create a connection authorization**

The circuit owner creates an authorization, which creates an authorization key to be used by a circuit user to connect their virtual network gateways to the ExpressRoute circuit. An authorization is valid for only one connection.

Note

Each connection requires a separate authorization.

1. In the ExpressRoute page, select **Authorizations** and then type a **name** for the authorization and select **Save**.

  ![Azure portal - configure authorization](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/authorization-ea88e96f.png)
2. Once the configuration is saved, copy the **Resource ID** and the **Authorization Key**.

  ![Azure portal - configure authorization showing resource Id and Authorization key](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/authorization-key-a8f3cdc7.png)
3. To delete a connection authorization

You can delete a connection by selecting the Delete icon for the authorization key for your connection.

![Azure portal - delete authorization key only](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/delete-authorization-key-eb398439.png)
If you want to delete the connection but retain the authorization key, you can delete the connection from the connection page of the circuit.

![Azure portal - delete connection owning circuit](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/delete-connection-owning-circuit-d3fe783f.png)
**Circuit user operations**

The circuit user needs the resource ID and an authorization key from the circuit owner.

To redeem a connection authorization

1. Select the + Create a resource button. Search for Connection and select Create.

   [![Azure portal - create new connection](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/create-new-resources.png)](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/create-new-resources.png#lightbox)
2. Make sure the Connection type is set to **ExpressRoute**. Select the Resource group and Location, then select **OK** in the Basics page.

  Note

 The location must match the virtual network gateway location you are creating the connection for.

  ![Azure portal - create connection basics tab](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/connection-basics-f709aea2.png)
3. In the **Settings** page, Select the Virtual network gateway and check the **Redeem authorization** check box. Enter the Authorization key and the Peer circuit URI and give the connection a name. Select **OK**.

  Note

 The Peer Circuit URI is the Resource ID of the ExpressRoute circuit (which you can find under the Properties Setting pane of the ExpressRoute Circuit).

  ![Azure portal - create connection settings tab](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/connection-settings-4ed83727.png)
4. Review the information in the **Summary** page and select **OK**.

  ![Azure portal - create connection summary](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/connection-summary-56e92204.png)

**Clean up resources**

1. You can delete a connection and unlink your VNet to an ExpressRoute circuit by selecting the **Delete** icon on the page for your connection.

  ![Azure portal - delete connection](https://learn.microsoft.com/en-us/training/wwl-azure/design-implement-azure-expressroute/media/delete-connection-cf82781a.png)

#### Check your knowledge

1.

How does ExpressRoute FastPath send network traffic?

Directly to virtual machines in the virtual network.

Through the gateway to Virtual machines.

Through the public internet.

2.

A network has multiple VNets peered with the VNet that is connected to ExpressRoute. How should the ExpressRoute FastPath deployment be modified?

Connect the VNet gateways to ExpressRoute FastPath.

Connect all the virtual networks to the ExpressRoute FastPath circuit directly.

Modify the VNet peering configuration.

You must answer all questions before checking your work.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/troubleshoot-an-azure-site-to-site-vpn-connection-that-cannot-connect-azure-vpn-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_EwoQvNA.png)

#### In this article

1. [Troubleshooting steps](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-troubleshoot-site-to-site-cannot-connect#troubleshooting-steps)
2. [Next steps](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-troubleshoot-site-to-site-cannot-connect#next-steps)

After you configure a site-to-site VPN connection between an on-premises network and an Azure virtual network, the VPN connection suddenly stops working and cannot be reconnected. This article provides troubleshooting steps to help you resolve this problem.

If your Azure issue is not addressed in this article, visit the Azure forums on [Microsoft Q & A and Stack Overflow](https://azure.microsoft.com/support/forums/). You can post your issue in these forums, or post to [@AzureSupport on Twitter](https://twitter.com/AzureSupport). You also can submit an Azure support request. To submit a support request, on the [Azure support](https://azure.microsoft.com/support/options/) page, select **Get support**.

#### Troubleshooting steps

To resolve the problem, first try to [reset the Azure VPN gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/reset-gateway) and reset the tunnel from the on-premises VPN device. If the problem persists, follow these steps to identify the cause of the problem.

##### Prerequisite step

Check the type of the Azure VPN gateway.

1. Go to the [Azure portal](https://portal.azure.com).
2. Check the **Overview** page of the VPN gateway for the type information.

 ![Overview of the gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/media/vpn-gateway-troubleshoot-site-to-site-cannot-connect/gatewayoverview.png)

##### Step 1. Check whether the on-premises VPN device is validated

1. Check whether you are using a [validated VPN device and operating system version](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices#devicetable). If the device is not a validated VPN device, you might have to contact the device manufacturer to see if there is a compatibility issue.
2. Make sure that the VPN device is correctly configured. For more information, see [Edit device configuration samples](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices#editing).

##### Step 2. Verify the shared key

Compare the shared key for the on-premises VPN device to the Azure Virtual Network VPN to make sure that the keys match.

To view the shared key for the Azure VPN connection, use one of the following methods:

**Azure portal**

1. Go to the VPN gateway site-to-site connection that you created.
2. In the **Settings** section, click **Shared key**.

 ![Shared key](https://learn.microsoft.com/en-us/azure/vpn-gateway/media/vpn-gateway-troubleshoot-site-to-site-cannot-connect/sharedkey.png)

**Azure PowerShell**

Note

We recommend that you use the Azure Az PowerShell module to interact with Azure. See [Install Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-azure-powershell) to get started. To learn how to migrate to the Az PowerShell module, see [Migrate Azure PowerShell from AzureRM to Az](https://learn.microsoft.com/en-us/powershell/azure/migrate-from-azurerm-to-az).

For the Azure [Resource Manager deployment model](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/deployment-models):

Azure PowerShell 

```
Get-AzVirtualNetworkGatewayConnectionSharedKey -Name <Connection name> -ResourceGroupName <Resource group name>

```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
For the classic deployment model:

Azure PowerShell 

```
Get-AzureVNetGatewayKey -VNetName -LocalNetworkSiteName

```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
##### Step 3. Verify the VPN peer IPs

* The IP definition in the **Local Network Gateway** object in Azure should match the on-premises device IP.
* The Azure gateway IP definition that is set on the on-premises device should match the Azure gateway IP.

##### Step 4. Check UDR and NSGs on the gateway subnet

Check for and remove user-defined routing (UDR) or Network Security Groups (NSGs) on the gateway subnet, and then test the result. If the problem is resolved, validate the settings that UDR or NSG applied.

##### Step 5. Check the on-premises VPN device external interface address

If the Internet-facing IP address of the VPN device is included in the **Local network** definition in Azure, you might experience sporadic disconnections.

##### Step 6. Verify that the subnets match exactly (Azure policy-based gateways)

* Verify that the virtual network address space(s) match exactly between the Azure virtual network and on-premises definitions.
* Verify that the subnets match exactly between the **Local Network Gateway** and on-premises definitions for the on-premises network.

##### Step 7. Verify the Azure gateway health probe

1. Open health probe by browsing to the following URL:

 `https://<YourVirtualNetworkGatewayIP>:8081/healthprobe`

 *For Active/Acive gateways use the following to check the second public IP:*   
 `https://<YourVirtualNetworkGatewayIP2>:8083/healthprobe`
2. Click through the certificate warning.
3. If you receive a response, the VPN gateway is considered healthy. If you don't receive a response, the gateway might not be healthy or an NSG on the gateway subnet is causing the problem. The following text is a sample response:

 XML 
```
<?xml version="1.0"?>
<string xmlns="http://schemas.microsoft.com/2003/10/Serialization/">Primary Instance: GatewayTenantWorker_IN_1 GatewayTenantVersion: 14.7.24.6</string>

```
![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)

Note

Basic SKU VPN gateways do not reply to health probe. They are not recommended for [production workloads](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-gateway-settings#workloads).

##### Step 8. Check whether the on-premises VPN device has the perfect forward secrecy feature enabled

The perfect forward secrecy feature can cause disconnection problems. If the VPN device has perfect forward secrecy enabled, disable the feature. Then update the VPN gateway IPsec policy.

Note

VPN gateways do not reply to ICMP on their local address.

#### Next steps

* [Configure a site-to-site connection to a virtual network](https://learn.microsoft.com/en-us/azure/vpn-gateway/tutorial-site-to-site-portal)
* [Configure an IPsec/IKE policy for site-to-site VPN connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-ipsecikepolicy-rm-powershell)

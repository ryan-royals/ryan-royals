---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/configure-azure-ad-tenant-and-settings-for-p2-s-vpn-connections-azure-ad-authentication-open-vpn-azure-vpn-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Azure AD tenant](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant#tenant)
2. [Create Azure AD tenant users](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant#create-azure-ad-tenant-users)
3. [Authorize the Azure VPN application](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant#authorize-the-azure-vpn-application)
4. [Configure authentication for the gateway](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant#enable-authentication)
5. [Download the Azure VPN Client profile configuration package](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant#download-the-azure-vpn-client-profile-configuration-package)
6. [Next steps](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-tenant#next-steps)

This article helps you configure your AD tenant and P2S settings for Azure AD authentication. For more information about point-to-site protocols and authentication, see [About VPN Gateway point-to-site VPN](https://learn.microsoft.com/en-us/azure/vpn-gateway/point-to-site-about). To authenticate using the Azure AD authentication type, you must include the OpenVPN tunnel type in your point-to-site configuration.

Note

Azure AD authentication is supported only for OpenVPN® protocol connections and requires the Azure VPN Client.

####  Azure AD tenant

The steps in this article require an Azure AD tenant. If you don't have an Azure AD tenant, you can create one using the steps in the [Create a new tenant](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-access-create-new-tenant) article. Note the following fields when creating your directory:

* Organizational name
* Initial domain name

#### Create Azure AD tenant users

1. Create two accounts in the newly created Azure AD tenant. For steps, see [Add or delete a new user](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/add-users-azure-active-directory).

	* Global administrator account
	* User accountThe global administrator account will be used to grant consent to the Azure VPN app registration. The user account can be used to test OpenVPN authentication.
2. Assign one of the accounts the **Global administrator** role. For steps, see [Assign administrator and non-administrator roles to users with Azure Active Directory](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-users-assign-role-azure-portal).

#### Authorize the Azure VPN application

##### Authorize the application

1. Sign in to the Azure portal as a user that is assigned the **Global administrator** role.
2. Next, grant admin consent for your organization. This allows the Azure VPN application to sign in and read user profiles. Copy and paste the URL that pertains to your deployment location in the address bar of your browser:

 Public

 
```
https://login.microsoftonline.com/common/oauth2/authorize?client_id=41b23e61-6c1e-4545-b367-cd054e0ed4b4&response_type=code&redirect_uri=https://portal.azure.com&nonce=1234&prompt=admin_consent

```
 Azure Government

 
```
https://login.microsoftonline.us/common/oauth2/authorize?client_id=51bb15d4-3a4f-4ebf-9dca-40096fe32426&response_type=code&redirect_uri=https://portal.azure.us&nonce=1234&prompt=admin_consent

```
 Microsoft Cloud Germany

 
```
https://login-us.microsoftonline.de/common/oauth2/authorize?client_id=538ee9e6-310a-468d-afef-ea97365856a9&response_type=code&redirect_uri=https://portal.microsoftazure.de&nonce=1234&prompt=admin_consent

```
 Azure China 21Vianet

 
```
https://login.chinacloudapi.cn/common/oauth2/authorize?client_id=49f817b6-84ae-4cc0-928c-73f27289b3aa&response_type=code&redirect_uri=https://portal.azure.cn&nonce=1234&prompt=admin_consent

```
  Note

 If you're using a global admin account that is not native to the Azure AD tenant to provide consent, replace "common" with the Azure AD tenant ID in the URL. You may also have to replace "common" with your tenant ID in certain other cases as well. For help with finding your tenant ID, see [How to find your Azure Active Directory tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant).
3. Select the account that has the **Global administrator** role if prompted.
4. On the **Permissions requested** page, select **Accept**.
5. Go to **Azure Active Directory**. In the left pane, click **Enterprise applications**. You'll see **Azure VPN** listed.

   [![Screenshot of the Enterprise application page showing Azure V P N listed.](https://learn.microsoft.com/en-us/azure/includes/media/vpn-gateway-vwan-azure-ad-tenant/vpn.png)](https://learn.microsoft.com/en-us/azure/includes/media/vpn-gateway-vwan-azure-ad-tenant/vpn.png#lightbox)

#### Configure authentication for the gateway

1. Locate the tenant ID of the directory that you want to use for authentication. It's listed in the properties section of the Active Directory page. For help with finding your tenant ID, see [How to find your Azure Active Directory tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant).
2. If you don't already have a functioning point-to-site environment, follow the instruction to create one. See [Create a point-to-site VPN](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-howto-point-to-site-resource-manager-portal) to create and configure a point-to-site VPN gateway.

  Important

 The Basic SKU is not supported for OpenVPN.
3. Go to the virtual network gateway. In the left pane, click **Point-to-site configuration**.

  ![Screenshot showing settings for Tunnel type, Authentication type, and Azure Active Directory settings.](https://learn.microsoft.com/en-us/azure/vpn-gateway/media/openvpn-create-azure-ad-tenant/configuration.png) 

 Configure the following values:

	* **Address pool**: client address pool
	* **Tunnel type:** OpenVPN (SSL)
	* **Authentication type**: Azure Active DirectoryFor **Azure Active Directory** values, use the following guidelines for **Tenant**, **Audience**, and **Issuer** values. Replace {AzureAD TenantID} with your tenant ID.

	* **Tenant:** TenantID for the Azure AD tenant. Enter the tenant ID that corresponds to your configuration. Make sure the Tenant URL does not have a `\` at the end.
	
	
		+ Azure Public AD: `https://login.microsoftonline.com/{AzureAD TenantID}`
		+ Azure Government AD: `https://login.microsoftonline.us/{AzureAD TenantID}`
		+ Azure Germany AD: `https://login-us.microsoftonline.de/{AzureAD TenantID}`
		+ China 21Vianet AD: `https://login.chinacloudapi.cn/{AzureAD TenantID}`
	* **Audience**: The Application ID of the "Azure VPN" Azure AD Enterprise App.
	
	
		+ Azure Public: `41b23e61-6c1e-4545-b367-cd054e0ed4b4`
		+ Azure Government: `51bb15d4-3a4f-4ebf-9dca-40096fe32426`
		+ Azure Germany: `538ee9e6-310a-468d-afef-ea97365856a9`
		+ Azure China 21Vianet: `49f817b6-84ae-4cc0-928c-73f27289b3aa`
	* **Issuer**: URL of the Secure Token Service. Include a trailing slash at the end of the **Issuer** value. Otherwise, the connection may fail.
	
	
		+ `https://sts.windows.net/{AzureAD TenantID}/`
4. Once you finish configuring settings, click **Save** at the top of the page.

#### Download the Azure VPN Client profile configuration package

In this section, you generate and download the Azure VPN Client profile configuration package. This package contains the settings that you can use to configure the Azure VPN Client profile on client computers.

1. At the top of the **Point-to-site configuration** page, click **Download VPN client**. It takes a few minutes for the client configuration package to generate.
2. Your browser indicates that a client configuration zip file is available. It's named the same name as your gateway.
3. Extract the downloaded zip file.
4. Browse to the unzipped "AzureVPN" folder.
5. Make a note of the location of the “azurevpnconfig.xml” file. The azurevpnconfig.xml contains the setting for the VPN connection. You can also distribute this file to all the users that need to connect via e-mail or other means. The user will need valid Azure AD credentials to connect successfully. For more information, see [Azure VPN client profile config files for Azure AD authentication](https://learn.microsoft.com/en-us/azure/vpn-gateway/about-vpn-profile-download).

#### Next steps

* To connect to your virtual network, you must configure the Azure VPN client on your client computers. See [Configure a VPN client for P2S VPN connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/openvpn-azure-ad-client).
* For frequently asked questions, see the **Point-to-site** section of the [VPN Gateway FAQ](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-vpn-faq#P2S).

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/microsoft-entra-joined-session-hosts-in-azure-virtual-desktop/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Known limitations](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts#known-limitations)
2. [Deploy Microsoft Entra joined VMs](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts#deploy-microsoft-entra-joined-vms)
3. [Access Microsoft Entra joined VMs](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts#access-microsoft-entra-joined-vms)
4. [User profiles](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts#user-profiles)
5. [Accessing on-premises resources](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts#accessing-on-premises-resources)
6. [Next steps](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts#next-steps)

This article will walk you through the process of deploying and accessing Microsoft Entra joined virtual machines in Azure Virtual Desktop. Microsoft Entra joined VMs remove the need to have line-of-sight from the VM to an on-premises or virtualized Active Directory Domain Controller (DC) or to deploy Microsoft Entra Domain Services. In some cases, it can remove the need for a DC entirely, simplifying the deployment and management of the environment. These VMs can also be automatically enrolled in Intune for ease of management.

#### Known limitations

The following known limitations may affect access to your on-premises or Active Directory domain-joined resources and you should consider them when deciding whether Microsoft Entra joined VMs are right for your environment.

* Azure Virtual Desktop (classic) doesn't support Microsoft Entra joined VMs.
* Microsoft Entra joined VMs don't currently support external identities, such as Microsoft Entra Business-to-Business (B2B) and Microsoft Entra Business-to-Consumer (B2C).
* Microsoft Entra joined VMs can only access [Azure Files shares](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-profile-container-azure-ad) or [Azure NetApp Files shares](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-fslogix-profile-container) for hybrid users using Microsoft Entra Kerberos for FSLogix user profiles.
* The [Remote Desktop app for Windows](https://learn.microsoft.com/en-us/azure/virtual-desktop/users/connect-microsoft-store) doesn't support Microsoft Entra joined VMs.

#### Deploy Microsoft Entra joined VMs

You can deploy Microsoft Entra joined VMs directly from the Azure portal when you [create a new host pool](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-host-pools-azure-marketplace) or [expand an existing host pool](https://learn.microsoft.com/en-us/azure/virtual-desktop/expand-existing-host-pool). To deploy a Microsoft Entra joined VM, open the **Virtual Machines** tab, then select whether to join the VM to Active Directory or Microsoft Entra ID. Selecting **Microsoft Entra ID** gives you the option to enroll VMs with Intune automatically, which lets you easily [manage your session hosts](https://learn.microsoft.com/en-us/azure/virtual-desktop/management). Keep in mind that the Microsoft Entra ID option will only join VMs to the same Microsoft Entra tenant as the subscription you're in.

Note

* Host pools should only contain VMs of the same domain join type. For example, Microsoft Entra joined VMs should only be with other Microsoft Entra joined VMs, and vice-versa.
* The VMs in the host pool must be Windows 11 or Windows 10 single-session or multi-session, version 2004 or later, or Windows Server 2022 or Windows Server 2019.

##### Assign user access to host pools

After you've created your host pool, you must assign users access to their resources. To grant access to resources, add each user to the application group. Follow the instructions in [Manage application groups](https://learn.microsoft.com/en-us/azure/virtual-desktop/manage-app-groups) to assign user access to apps and desktops. We recommend that you use user groups instead of individual users wherever possible.

For Microsoft Entra joined VMs, you'll need to do two extra things on top of the requirements for Active Directory or Microsoft Entra Domain Services-based deployments:

* Assign your users the **Virtual Machine User Login** role so they can sign in to the VMs.
* Assign administrators who need local administrative privileges the **Virtual Machine Administrator Login** role.

To grant users access to Microsoft Entra joined VMs, you must [configure role assignments for the VM](https://learn.microsoft.com/en-us/azure/active-directory/devices/howto-vm-sign-in-azure-ad-windows#configure-role-assignments-for-the-vm). You can assign the **Virtual Machine User Login** or **Virtual Machine Administrator Login** role either on the VMs, the resource group containing the VMs, or the subscription. We recommend assigning the Virtual Machine User Login role to the same user group you used for the application group at the resource group level to make it apply to all the VMs in the host pool.

#### Access Microsoft Entra joined VMs

This section explains how to access Microsoft Entra joined VMs from different Azure Virtual Desktop clients.

##### Single sign-on

For the best experience across all platforms, you should enable a single sign-on experience using Microsoft Entra authentication when accessing Microsoft Entra joined VMs. Follow the steps to [Configure single sign-on](https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-single-sign-on) to provide a seamless connection experience.

##### Connect using legacy authentication protocols

If you prefer not to enable single sign-on, you can use the following configuration to enable access to Microsoft Entra joined VMs.

**Connect using the Windows Desktop client**

The default configuration supports connections from Windows 11 or Windows 10 using the [Windows Desktop client](https://learn.microsoft.com/en-us/azure/virtual-desktop/users/connect-windows). You can use your credentials, smart card, [Windows Hello for Business certificate trust](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-hybrid-cert-trust) or [Windows Hello for Business key trust with certificates](https://learn.microsoft.com/en-us/windows/security/identity-protection/hello-for-business/hello-deployment-rdp-certs) to sign in to the session host. However, to access the session host, your local PC must meet one of the following conditions:

* The local PC is Microsoft Entra joined to the same Microsoft Entra tenant as the session host
* The local PC is Microsoft Entra hybrid joined to the same Microsoft Entra tenant as the session host
* The local PC is running Windows 11 or Windows 10, version 2004 or later, and is Microsoft Entra registered to the same Microsoft Entra tenant as the session host

If your local PC doesn't meet one of these conditions, add **targetisaadjoined:i:1** as a [custom RDP property](https://learn.microsoft.com/en-us/azure/virtual-desktop/customize-rdp-properties) to the host pool. These connections are restricted to entering user name and password credentials when signing in to the session host.

**Connect using the other clients**

To access Microsoft Entra joined VMs using the web, Android, macOS and iOS clients, you must add **targetisaadjoined:i:1** as a [custom RDP property](https://learn.microsoft.com/en-us/azure/virtual-desktop/customize-rdp-properties) to the host pool. These connections are restricted to entering user name and password credentials when signing in to the session host.

##### Enforcing Microsoft Entra multifactor authentication for Microsoft Entra joined session VMs

You can use Microsoft Entra multifactor authentication with Microsoft Entra joined VMs. Follow the steps to [Enforce Microsoft Entra multifactor authentication for Azure Virtual Desktop using Conditional Access](https://learn.microsoft.com/en-us/azure/virtual-desktop/set-up-mfa) and note the extra steps for [Microsoft Entra joined session host VMs](https://learn.microsoft.com/en-us/azure/virtual-desktop/set-up-mfa#azure-ad-joined-session-host-vms).

If you're using Microsoft Entra multifactor authentication and you don't want to restrict signing in to strong authentication methods like Windows Hello for Business, you'll need to [exclude the Azure Windows VM Sign-In app](https://learn.microsoft.com/en-us/azure/active-directory/devices/howto-vm-sign-in-azure-ad-windows#mfa-sign-in-method-required) from your Conditional Access policy.

#### User profiles

You can use FSLogix profile containers with Microsoft Entra joined VMs when you store them on Azure Files or Azure NetApp Files while using hybrid user accounts. For more information, see [Create a profile container with Azure Files and Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-profile-container-azure-ad).

#### Accessing on-premises resources

While you don't need an Active Directory to deploy or access your Microsoft Entra joined VMs, an Active Directory and line-of-sight to it are needed to access on-premises resources from those VMs. To learn more about accessing on-premises resources, see [How SSO to on-premises resources works on Microsoft Entra joined devices](https://learn.microsoft.com/en-us/azure/active-directory/devices/azuread-join-sso).

#### Next steps

Now that you've deployed some Microsoft Entra joined VMs, we recommend enabling single sign-on before connecting with a supported Azure Virtual Desktop client to test it as part of a user session. To learn more, check out these articles:

* [Configure single sign-on](https://learn.microsoft.com/en-us/azure/virtual-desktop/configure-single-sign-on)
* [Create a profile container with Azure Files and Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-profile-container-azure-ad)
* [Connect with the Windows Desktop client](https://learn.microsoft.com/en-us/azure/virtual-desktop/users/connect-windows)
* [Connect with the web client](https://learn.microsoft.com/en-us/azure/virtual-desktop/users/connect-web)
* [Troubleshoot connections to Microsoft Entra joined VMs](https://learn.microsoft.com/en-us/azure/virtual-desktop/troubleshoot-azure-ad-connections)
* [Create a profile container with Azure NetApp Files](https://learn.microsoft.com/en-us/azure/virtual-desktop/create-fslogix-profile-container)

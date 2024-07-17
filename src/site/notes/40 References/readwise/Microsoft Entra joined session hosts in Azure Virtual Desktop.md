---
{"dg-publish":true,"permalink":"/40-references/readwise/microsoft-entra-joined-session-hosts-in-azure-virtual-desktop/","tags":["rw/articles"]}
---

# Microsoft Entra joined session hosts in Azure Virtual Desktop

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)
  
URL: https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts
Author: Heidilohr

## Summary

This article explains how to deploy and manage Microsoft Entra joined virtual machines in Azure Virtual Desktop. Microsoft Entra joined VMs simplify deployment by eliminating the need for Active Directory on-premises, and they can be easily managed with Intune. Access to on-premises resources may be limited, and specific configurations are required for user access and authentication.

## Highlights added July 17, 2024 at 10:55 AM
>• Microsoft Entra joined VMs can only access [Azure Files shares](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts/create-profile-container-azure-ad) or [Azure NetApp Files shares](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts/create-fslogix-profile-container) for hybrid users using Microsoft Entra Kerberos for FSLogix user profiles.
>• The [Remote Desktop app for Windows](https://learn.microsoft.com/en-us/azure/virtual-desktop/azure-ad-joined-session-hosts/users/connect-microsoft-store) doesn't support Microsoft Entra joined VMs. ([View Highlight] (https://read.readwise.io/read/01hvqamm4j2gfjps18m1htpjmy))


>. To deploy a Microsoft Entra joined VM, open the **Virtual Machines** tab, then select whether to join the VM to Active Directory or Microsoft Entra ID ([View Highlight] (https://read.readwise.io/read/01hvqdexghf1fk96rp4qcyaedz))



---
{"dg-publish":true,"permalink":"/40-references/readwise/best-practice-recommendations-for-managed-system-identities-microsoft-entra/","tags":["rw/articles"]}
---

![40 References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg](/img/user/40%20References/attachments/be6ec1dc11499f9537329d089643e21f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/managed-identity-best-practice-recommendations
Author: barclayn

## Summary

Recommendations on when to use user-assigned versus system-assigned managed identities

## Highlights added August 30, 2024 at 2:23 PM
>Using Azure AD **groups** for granting access to services is a great way to simplify the authorization process. The idea is simple – grant permissions to a group and add identities to the group so that they inherit the same permissions. This is a well-established pattern from various on-premises systems and works well when the identities represent users. Another option to control authorization in Azure AD is by using [App Roles](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/managed-identity-best-practice-recommendations/../develop/howto-add-app-roles-in-apps), which allows you to declare **roles** that are specific to an app (rather than groups, which are a global concept in the directory). You can then [assign app roles to managed identities](https://learn.microsoft.com/en-us/azure/active-directory/managed-identities-azure-resources/managed-identity-best-practice-recommendations/how-to-assign-app-role-managed-identity-powershell) (as well as users or groups). ([View Highlight] (https://read.readwise.io/read/01h9mjkk3s4k8mmxh5czp1nw0w))



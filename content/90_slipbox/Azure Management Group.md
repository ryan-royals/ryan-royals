---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Management Group.md","permalink":"/slipbox-notes/azure-management-group/","tags":["notes"],"created":"2023-05-26","updated":"2025-11-28"}
---


Azure Management Groups are used to apply hierarchical [[90_slipbox/Azure Policy\|Policy]], and Role Based Access Control (RBAC) to Azure Subscriptions  
A subscription can only be a part of a single management group, but a management group can have many children.

A single Entra ID can have up to 10,000 management groups, with six levels of complexity, not including the Root Management Group.  
The Root Management is referred to as the *Tenant root group*, and its management group id is addressed by the Azure AD Tenant ID.

Addressing Management groups is done by:  
`/providers/Microsoft.Mangement/managementGroups/{Management-Group-ID}`

Reference: [Organize your resources with management groups - Azure Governance - Azure governance](https://learn.microsoft.com/en-us/azure/governance/management-groups/overview)

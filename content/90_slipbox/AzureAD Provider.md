---
{"dg-publish":true,"dg-path":"Slipbox Notes/AzureAD Provider.md","permalink":"/slipbox-notes/azure-ad-provider/","tags":["notes"],"created":"2023-09-06","updated":"2025-11-28"}
---


## Errors Creating Groups with `assignable_to_role`

 > GroupsClient.BaseClient.Post(): unexpected status 403 with OData error: Authorization_RequestDenied: Insufficient privileges to complete the operation.

The runner needs both `RoleManagement.ReadWrite.Directory` and `Directory.ReadWrite.All` permissions.

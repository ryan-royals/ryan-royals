---
{"dg-publish":true,"permalink":"/90-slipbox/azure-ad-provider/","tags":["notes"],"created":"2025-06-11T10:28:47.854+09:30","updated":"2026-06-11T09:30:38.354+09:30","dg-note-properties":{"created":"2023-09-06","modified":"2026-06-11","related":["[[Terraform]]"],"tags":"notes"}}
---


## Errors Creating Groups with `assignable_to_role`

 > GroupsClient.BaseClient.Post(): unexpected status 403 with OData error: Authorization_RequestDenied: Insufficient privileges to complete the operation.

The runner needs both `RoleManagement.ReadWrite.Directory` and `Directory.ReadWrite.All` permissions.

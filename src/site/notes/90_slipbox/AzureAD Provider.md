---
{"dg-publish":true,"permalink":"/90-slipbox/azure-ad-provider/","tags":["notes"],"created":"2025-06-11T10:28:47.854+09:30","updated":"2026-03-03T09:55:32.400+10:30","dg-note-properties":{"tags":"notes","related":["[[Terraform]]"],"created":"2023-09-06","modified":"2026-03-03"}}
---


## Errors Creating Groups with `assignable_to_role`

 > GroupsClient.BaseClient.Post(): unexpected status 403 with OData error: Authorization_RequestDenied: Insufficient privileges to complete the operation.

The runner needs both `RoleManagement.ReadWrite.Directory` and `Directory.ReadWrite.All` permissions.

---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Key Vault.md","permalink":"/slipbox-notes/azure-key-vault/","tags":["notes"],"created":"2023-07-25","updated":"2025-11-28"}
---


## Troubleshooting

### Secrets Constantly Recreate without Updating

Secrets being deployed by Terraform can get into a loop where they constantly recreate when using a `Data` block as the source for the `ID` parameter. If possible, instead of using a `Data` block, hard code the `ID` instead.

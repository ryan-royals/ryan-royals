---
{"dg-publish":true,"permalink":"/90-slipbox/azure-key-vault/","tags":["notes"],"created":"2026-03-27T09:57:51.494+10:30","updated":"2026-03-27T09:57:51.494+10:30","dg-note-properties":{"created":"2023-07-25","modified":"2026-03-03","tags":"notes","related":["[[Azure]]"],"references":null}}
---


## Troubleshooting

### Secrets Constantly Recreate without Updating

Secrets being deployed by Terraform can get into a loop where they constantly recreate when using a `Data` block as the source for the `ID` parameter. If possible, instead of using a `Data` block, hard code the `ID` instead.

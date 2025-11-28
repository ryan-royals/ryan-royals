---
{"dg-publish":true,"permalink":"/90-slipbox/azure-key-vault/","tags":["notes"]}
---


## Troubleshooting

### Secrets Constantly Recreate without Updating

Secrets being deployed by Terraform can get into a loop where they constantly recreate when using a `Data` block as the source for the `ID` parameter. If possible, instead of using a `Data` block, hard code the `ID` instead.

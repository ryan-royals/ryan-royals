---
{"dg-publish":true,"permalink":"/90-slipbox/azure-backup-policy-conflicts-with-tag-enforcement-on-azure-backup-rg/","tags":["today-i-learns"],"created":"2026-04-09T15:10:08.771+09:30","updated":"2026-04-09T18:13:33.898+09:30","dg-note-properties":{"tags":"today-i-learns","related":["[[90_slipbox/Azure Backup\|Azure Backup]]","[[90_slipbox/Azure Policy\|Azure Policy]]"],"created":"2026-04-09","modified":"2026-04-09"}}
---


[[Azure Backup]] auto creates a `AzureBackupRG_{region}_{N}` Resource Group, but there are no controls over the tags on this RG.  
When using a [[Azure Policy]] that enforces tagging on the RG layer, this causes backups to fail in a near silent way.  
Either creating the RG manually or removing the Azure Policy to Enforce tags are the best choice.

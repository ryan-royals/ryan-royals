---
{"dg-publish":true,"permalink":"/90-slipbox/azure-data-lake-storage-gen2/","tags":["notes"],"created":"2025-06-11","updated":"2026-03-03","dg-note-properties":{"tags":"notes","related":["[[Azure]]"],"created":"2025-06-11","modified":"2026-03-03"}}
---


## Troubleshooting

### azurerm_storage_data_lake_gen2_filesystem Wont Deploy

![azurerm_storage_data_lake_gen2_filesystem wont deploy-1712185602146.png](/img/user/10_attachments/azurerm_storage_data_lake_gen2_filesystem%20wont%20deploy-1712185602146.png)  
Errors that state that the Resource ID already exists may be a red herring. This error can occur when `public_network_access_enabled` is set to false on the `azurerm_storage_account`.

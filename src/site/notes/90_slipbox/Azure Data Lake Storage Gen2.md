---
{"dg-publish":true,"permalink":"/90-slipbox/azure-data-lake-storage-gen2/","tags":["notes"]}
---


## Troubleshooting

### azurerm_storage_data_lake_gen2_filesystem Wont Deploy

![azurerm_storage_data_lake_gen2_filesystem wont deploy-1712185602146.png](/img/user/10_attachments/azurerm_storage_data_lake_gen2_filesystem%20wont%20deploy-1712185602146.png)  
Errors that state that the Resource ID already exists may be a red herring. This error can occur when `public_network_access_enabled` is set to false on the `azurerm_storage_account`.

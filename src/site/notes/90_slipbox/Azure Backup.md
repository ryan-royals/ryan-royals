---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Backup.md","permalink":"/slipbox-notes/azure-backup/","tags":["notes"],"created":"2024-06-25","updated":"2025-11-28"}
---


## Backup failing on VM with Custom Image Deployed by Terraform

By Default, the `azurerm_virtual_machine` resource (Now depreciated), has `os_profile_windows_config`.`provision_vm_agent` set to `False`, which is not the Azure default. Without this agent, the backup will fail.  
To resolve:

1. Install Agent manually <https://github.com/Azure/WindowsVMAgent>
2. Update the `OSProfile.AllowExtensionOperations` property to `True`  

```pwsh  
$vm = Get-AzVM -ResourceGroupName <RG name> -Name <vm name>  
$vm.OSProfile.AllowExtensionOperations = $true  
$vm | Update-AzVM
```

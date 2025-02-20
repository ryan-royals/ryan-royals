---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/au-deux-access-keys-securely-locking-down-azure-storage-accounts-with-entra-id-authentication/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn-images-1.medium.com/proxy/1*TGH72Nnw24QL3iV9IOm4VA.png)

One of the big security wave items that is becoming pervasive internally at Microsoft even for the most mundane of use cases is that the antiquated, yet all too convenient, Storage account Access Keys are going the way of the dodo.

The `shared_access_key_enabled` flag will disable your ability to use the Storage Access Keys to access the Storage Account’s Data Plane. This means when you try to access anything inside the Storage Account itself you need to use Entra ID Authentication.

```
resource "azurerm_storage_account" "main" {  
  name                      = "st${random_string.storage_account_name.result}"  
  resource_group_name       = azurerm_resource_group.main.name  
  location                  = azurerm_resource_group.main.location  
  account_tier              = "Standard"  
  account_replication_type  = "LRS"  
  
  shared_access_key_enabled = false  
  
}
```

The `azurerm` provider by default uses Storage Account Access Keys to talk to the Data Plane. If you set `shared_access_key_enabled` to `false` then the next time you attempt to run Terraform Apply it will fail spectacularly like this:

```
Error: retrieving queue properties for Storage Account (Subscription: "a8dc551f-cbe8-47e9-87c1-d9570ac6d69d"  
│ Resource Group Name: "rg-terraform-state"  
│ Storage Account Name: "stjmavzhot"): executing request: unexpected status 403 (403 Key based authentication is not permitted on this storage account.) with…
```

---
{"dg-publish":true,"dg-path":"Slipbox Notes/Terraform.md","permalink":"/slipbox-notes/terraform/","tags":["notes"],"created":"2023-05-08","updated":"2025-11-28"}
---

Terraform is a Declarative, Domain Specific Language, [[90_slipbox/Infrastructure as code\|Infrastructure as code]] tool by [[90_slipbox/HashiCorp\|HashiCorp]] used to manage public cloud platforms like [[90_slipbox/Azure\|Azure]] [[Google Cloud Provider\|Google Cloud Provider]] [[Amazon Web Services\|Amazon Web Services]], as well as self hosted platforms like [[VmWare vSphere\|VmWare vSphere]].

Terraform uses a simple built upon individual blocks called Resources to build a Dependency Graph by linking items together.

The language supports tools for Lifecycle management, as well as [Refactoring](<[https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax)>).

## State File and Backend

If Terraform touches a secret, it is now in the state file.  
This includes using a `data` block to reference a Azure Key Vault secret. the contents of that `data` go into state in plain text.

## MOC

### Providers

[[90_slipbox/AzureAD Provider\|AzureAD Provider]]  
[[90_slipbox/AzApi Provider\|AzApi Provider]]  
[[90_slipbox/Time Provider\|Time Provider]]  

### Related Tools

[[90_slipbox/Inframap\|Inframap]]  
[[90_slipbox/Terragrunt\|Terragrunt]]  
[[90_slipbox/Terraform Cloud Development Kit\|Terraform Cloud Development Kit]]

### Snippets

#### Locals for Empty Values

### Locals for Empty Values

``` go
# The following block of locals are used to avoid using
# empty object types in the code
locals {
  empty_list   = []
  empty_map    = tomap({})
  empty_string = ""
}
```

```go
locals {
  base_module_tags = {
    deployedBy = "terraform/azure/caf-enterprise-scale"
  }
  connectivity_resources_tags = merge(
    local.disable_base_module_tags ? local.empty_map : local.base_module_tags,
    local.default_tags,
    local.configure_connectivity_resources.tags,
  )
  management_resources_tags = merge(
    local.disable_base_module_tags ? local.empty_map : local.base_module_tags,
    local.default_tags,
    local.configure_management_resources.tags,
  )
}

```

### Referencing Key Vault Secrets in Azure Web Apps

````
@Microsoft.KeyVault(SecretUri=${azurerm_key_vault.app_vault.vault_uri}secrets/app-insights-connection-string/)```
````

```
"@Microsoft.KeyVault(VaultName=${azurerm_key_vault.app_vault.name};SecretName=${azurerm_key_vault_secret.stytch_secret_key.name};SecretVersion=${azurerm_key_vault_secret.stytch_secret_key.version})"
```

```
“@Microsoft.KeyVault(VaultName=myvault;SecretName=mysecret)”
```

### Other

[[90_slipbox/Terraform Tips and Tricks\|Terraform Tips and Tricks]]  
[[terraform-cheat-sheet.pdf]]  
[[90_slipbox/How CAF TF module works\|How CAF TF module works]]  
[[90_slipbox/Types in Terraform\|Types in Terraform]]

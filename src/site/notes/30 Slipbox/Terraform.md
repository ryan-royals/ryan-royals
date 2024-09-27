---
{"dg-publish":true,"dg-path":"Terraform.md","permalink":"/terraform/","tags":["#software"]}
---


Terraform is a Declarative, [[Domain Specific Language\|Domain Specific Language]], [[30 Slipbox/Infrastructure as code\|Infrastructure as code]] tool by [[30 Slipbox/HashiCorp\|HashiCorp]] used to manage public cloud platforms like [[30 Slipbox/Azure\|Azure]] [[Google Cloud Provider\|Google Cloud Provider]] [[Amazon Web Services\|Amazon Web Services]], as well as self hosted platforms like [[VmWare vSphere\|VmWare vSphere]].

Terraform uses a simple built upon individual blocks called Resources to build a Dependency Graph by linking items together.

The language supports tools for Lifecycle management, as well as [Refactoring](<[https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax)>).

## State File and Backend

If Terraform touches a secret, it is now in the state file.  
This includes using a `data` block to reference a Azure Key Vault secret. the contents of that `data` go into state in plain text.

## MOC

### Providers

[[30 Slipbox/Null Provider\|Null Provider]]  
[[30 Slipbox/AzureRM Provider\|AzureRM Provider]]  
[[30 Slipbox/AzureAD Provider\|AzureAD Provider]]  
[[30 Slipbox/AzApi Provider\|AzApi Provider]]  
[[30 Slipbox/ALZ Provider\|ALZ Provider]]  
[[30 Slipbox/Ansible Provider\|Ansible Provider]]  
[[30 Slipbox/Time Provider\|Time Provider]]  
[[30 Slipbox/ALZ Provider\|ALZ Provider]]

### Backends

[[30 Slipbox/Azurerm Backend\|Azurerm Backend]]

### Modules

[[30 Slipbox/Lz-vending Module\|Lz-vending Module]]  
[[30 Slipbox/caf-enterprise-scale Module\|caf-enterprise-scale Module]]

### Training and Certificates

[[40 References/readwise/HashiCorp Certified Terraform Associate\|HashiCorp Certified Terraform Associate]]  

### Related Tools

[[30 Slipbox/Inframap\|Inframap]]  
[[30 Slipbox/Terragrunt\|Terragrunt]]  
[[30 Slipbox/Terraform Cloud Development Kit\|Terraform Cloud Development Kit]]

### Snippets

[[30 Slipbox/Locals for Empty Values\|Locals for Empty Values]]  
[[30 Slipbox/Renaming Maps in a List of Maps\|Renaming Maps in a List of Maps]]  
[[30 Slipbox/Referencing Key Vault Secrets in Azure Web Apps\|Referencing Key Vault Secrets in Azure Web Apps]]

### Other

[[30 Slipbox/Terraform Tips and Tricks\|Terraform Tips and Tricks]]  
[[terraform-cheat-sheet.pdf]]  
[[30 Slipbox/How CAF TF module works\|How CAF TF module works]]  
[[30 Slipbox/Conditional where Key is not known\|Conditional where Key is not known]]

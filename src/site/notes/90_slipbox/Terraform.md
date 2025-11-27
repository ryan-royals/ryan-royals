---
{"dg-publish":true,"dg-path":"Slipbox Notes/Terraform.md","permalink":"/slipbox-notes/terraform/","tags":["notes"],"created":"2023-05-08","updated":"2025-11-27"}
---

Terraform is a Declarative, Domain Specific Language, [[90_slipbox/Infrastructure as code\|Infrastructure as code]] tool by [[90_slipbox/HashiCorp\|HashiCorp]] used to manage public cloud platforms like [[90_slipbox/Azure\|Azure]] [[Google Cloud Provider\|Google Cloud Provider]] [[Amazon Web Services\|Amazon Web Services]], as well as self hosted platforms like [[VmWare vSphere\|VmWare vSphere]].

Terraform uses a simple built upon individual blocks called Resources to build a Dependency Graph by linking items together.

The language supports tools for Lifecycle management, as well as [Refactoring](<[https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring#moved-block-syntax)>).

## State File and Backend

If Terraform touches a secret, it is now in the state file.  
This includes using a `data` block to reference a Azure Key Vault secret. the contents of that `data` go into state in plain text.

## MOC

### Providers

[[Null Provider\|Null Provider]]  
[[90_slipbox/AzureRM Provider\|AzureRM Provider]]  
[[90_slipbox/AzureAD Provider\|AzureAD Provider]]  
[[90_slipbox/AzApi Provider\|AzApi Provider]]  
[[90_slipbox/ALZ Provider\|ALZ Provider]]  
[[90_slipbox/Ansible Provider\|Ansible Provider]]  
[[90_slipbox/Time Provider\|Time Provider]]  
[[90_slipbox/ALZ Provider\|ALZ Provider]]

### Backends

[[90_slipbox/Azurerm Backend\|Azurerm Backend]]

### Modules

[[90_slipbox/Lz-vending Module\|Lz-vending Module]]  
[[90_slipbox/caf-enterprise-scale Module\|caf-enterprise-scale Module]]

### Training and Certificates

[HashiCorp Certified Terraform Associate](https://www.hashicorp.com/certification/terraform-associate)

### Related Tools

[[90_slipbox/Inframap\|Inframap]]  
[[90_slipbox/Terragrunt\|Terragrunt]]  
[[90_slipbox/Terraform Cloud Development Kit\|Terraform Cloud Development Kit]]

### Snippets

[[90_slipbox/Locals for Empty Values\|Locals for Empty Values]]  
[[90_slipbox/Renaming Maps in a List of Maps\|Renaming Maps in a List of Maps]]  
[[90_slipbox/Referencing Key Vault Secrets in Azure Web Apps\|Referencing Key Vault Secrets in Azure Web Apps]]

### Other

[[90_slipbox/Terraform Tips and Tricks\|Terraform Tips and Tricks]]  
[[terraform-cheat-sheet.pdf]]  
[[90_slipbox/How CAF TF module works\|How CAF TF module works]]  
[[90_slipbox/Conditional where Key is not known\|Conditional where Key is not known]]  
[[90_slipbox/Types in Terraform\|Types in Terraform]]

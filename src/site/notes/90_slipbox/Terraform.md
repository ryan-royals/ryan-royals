---
{"dg-publish":true,"permalink":"/90-slipbox/terraform/","tags":["notes"],"created":"2026-03-27T09:57:51.532+10:30","updated":"2026-03-27T09:57:51.532+10:30","dg-note-properties":{"created":"2023-05-08","modified":"2026-03-03","references":null,"tags":"notes","related":["[[90_slipbox/Infrastructure as code\|Infrastructure as code]]","[[Programming]]"],"orgs":["[[90_slipbox/HashiCorp\|HashiCorp]]"]}}
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

### Other

[[90_slipbox/Terraform Tips and Tricks\|Terraform Tips and Tricks]]  
[terraform-cheat-sheet.pdf](/img/user/10_attachments/terraform-cheat-sheet.pdf)  
[[90_slipbox/How CAF TF module works\|How CAF TF module works]]  
[[90_slipbox/Types in Terraform\|Types in Terraform]]

## Tips

### `_override.tf` File

Using a file name that ends with `_override.tf` makes a special file that merges with other blocks, in a way that overrides config. This includes working for module sources.

```go
# main.tf
module "some_module"{
    source = "./node_modules/@arkahna-elements/some_module
    var_1 = true
    var_2 = {}
}

######
# _override.tf

module "some_module" {
    source = "../a_different_path"
}
```

Any over lapping declarations on the blocks are merged, with the `_override.tf` taking priority.

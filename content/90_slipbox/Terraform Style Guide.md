---
{"dg-publish":true,"dg-path":"Slipbox Notes/Terraform Style Guide.md","permalink":"/slipbox-notes/terraform-style-guide/","tags":["notes"],"created":"2023-11-12","updated":"2025-11-28"}
---


## Definitions

| Term           | Definition                                                                                                                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Block          | The base syntax of each asset tracked in Terraform. Types include: `resource`, `data`, `module`, `variable`, `locals`, `output`, `terraform`, `provider`              |
| Project        | The top level scope of the Terraform instance, used to define the overall intention of the Resources being deployed.                                                  |
| Root Module    | The top level of the Project, where the `Plan` and `Apply` actions are scoped. Terraform treats the top directory as a Module, and has its own Variables and Outputs. |
| Feature Toggle | The ability to enable or disable a Resource from being deployed based on an input.                                                                                    |

## 1. Project Scoping and Meta

### 1. Environments

1. Each Project should be reusable for different environments .
	1. Environments are defined within the `./variables` folder under `*env*.tfvars`.
	2. *Justification*: This creates a strong pattern for how to scope a Terraform Project
2. Environments should have their own state files.
	1. State file inputs should be defined within the `./variabless` folder under `*env*.tfbackend`.
	2. *Justification*: This creates a strong pattern for how to scope a Terraform Project

### 2. Resource Scope

1. Each Project should be scoped at a single application lifecycle. Context: If the Project was to be destroyed, all associated resources should be cleaned up. This action should ideally not affect another Application.
	1. *Justification:* If the Project was to be destroyed, all associated resources should be cleaned up. This action should ideally not affect another Application.

### 3. Version Locks

1. The Root Module and all sub modules should have `required_version` for Terraform.
2. The Root Module and all sub modules should have `required_providers` with a `version` property.
3. The Root Module should have a `.terraform.lock.hcl` checked into Version Control.

### 4. Directory Structure

1. The Root Module should consist of the following files:

```dir
.
├── variabless/
│   ├── *env*.tfbackend
│   └── *env*.tfvars
├── modules/
├── main.tf
├── variables.tf
├── providers.tf
├── locals.tf
├── outputs.tf
├── .gitignore
└── .terraform.lock.hcl
```

 1. `main.tf` for shared `resource`, `data` and `module` blocks.
 2. `variables.tf` for all `variable` blocks.
 3. `providers.tf` for `terraform` and `provider` blocks.
 4. `locals.tf` for shared `locals` blocks.
 5. `outputs.tf` for all `output` blocks.
 6. `modules/` folder should be used for any local Modules.
 7. `variables/` folder defining all environments for the Project.

### 5. Project Inputs and Outputs

1. All Inputs should be defined in the Project environments variables.
2. `Outputs` from the Root Module should be avoided.
	1. *Justification:* This is due minimise surface area for potential security issues regarding the state file.
3. `Terraform Remote State` blocks should be avoided.
	1. If required, use `Data` blocks with Variables to lookup the required information.
	2. *Context:* If required, use `Data` blocks with Variables to lookup the required information.
	3. *Justification:* This is due minimise surface area for potential security issues regarding the state file.
4. `Variable` blocks should be scoped and group to intention, not individually declared.

```terraform
variable "networking" {
  type = object({
    address_space = string
    subnets = list(object({
      name           = string
      address_prefix = number
    }))
  })
  description = <<EOT
    Networking configuration for the virtual network
    
    - address_space: CIDR Block for the virtual network. Example: "192.168.1.1/24"
    - subnets: List of subnets to create in the virtual network. 
        - name: Name of the subnet. Example: "vm"
        - address_prefix: CIDR Notation for the subnet. Example: "27"
    EOT
}
```

1. `Variables` should use `<<EOT` to describe each parameter over multiple lines.
	1. *Justification:* This allows print outs to TfDocs and the Command Prompt to be legible.
2. `Variables` descriptions should offer Examples and Defaults as relevant.
3. `Optionals` are to be used within `Objects` to avoid the use of a `default` parameter.
	1. *Justification:* Defaults are overwritten by inputs and create confusion when this happens.
4. `Default` parameters should only be used on simple inputs like String or Number, and not on Lists or Objects, or complex inputs that collate multiple parameters.
	1. *Justification:* Defaults are overwritten by inputs and create confusion when this happens.
5. Collections (`Lists` and `Tuples`) should use plurals in naming convention.
6. `Output` blocks should include the type in the name. Example: `output "virtual_network_obj"`.
7. `map` inputs types should be avoided due the difficulty to work with. Use `list(object({}))` if possible.
	1. *Justification:* Maps can be a varying length, and since both the key and value can change types, make it difficult to work with later in the project.
8. `object` type should be fully defined with sub types, and never left as `any`.
	1. *Justification:* `any` values are difficult to work with and lead to misconfiguration.
9. All inputs should be constrained by a valid type, and never `any`.
	1. *Justification:* `any` values are difficult to work with and lead to misconfiguration.

### 6. Locals

1. `Locals` blocks should be used to avoid Loops and Functions inside of Resource blocks.
2. `Locals` that are used across the Project should be stored within the `locals.tf` file.
3. `Locals` that are specific to a Resource should be logically placed before or after relevant block.
4. `Locals` should be used to logically group similar scoped items.
	1. *Example:* `locals { naming = {...} }`.
5. `Locals` keys should be static, and not include variables.
	1. *Justification*: Terraform struggles when Keys are unable to be calculated pre plan.

## 2. Loops

### 1. Resource & Locals Loops

1. `Counts` should only be used for Feature Toggling, or in instances where Resources are otherwise disposable (VM Scale sets).
	1. *Example:* `count = var.os_type == "linux" ? 1 : 0`.
	2. *Justification:* `Counts` lead to errors as Terraform will move and delete resources to fit the count and can lead to unintended side effects
2. `for_each` loops should be used to avoid creating the same Resource block twice.
	1. *Example:* `azurerm_storage_account.st` instead of `azurerm_storage_account.st_1` `azurerm_storage_account.st_2`.
3. `for_each` loops should use reusable Keys easily identifiable for later use in the Project.
	1. *Example:* `for_each = { for o in var.virtual_machines : o.vm_name_suffix => o}`.
4. `for_each` loops should use 'O' when referring to an object.
	1. *Example:* `for_each = { for o in var.virtual_machines : o.vm_name_suffix => o}`.
5. `for_each` loops should use 'k, v' when referring to a Key and Value individually.
	1. *Example:* `for_each = { for k,v in azurerm_windows_virtual_machine : k => v}`.
6. Collections (`Lists` and `Tuples`) should use plurals in naming convention.

## 3. Resources, Module, Data Blocks

### 1. Formatting

1. Blocks should utilise Loops wherever possible.
2. Block Keys should be generic where ever possible.
	1. *Example:* `azurerm_virtual_machine.vm` instead of `azurerm_virtual_machine.apiServer`.
3. Block object Keys should use underscores for naming.
4. Block object Keys should be lowercase.
5. Blocks parameters should be tightly, consistently and logically grouped based on values.

```terraform
module "vm" {
  for_each = {
    for o in var.virtual_machines : o.vm_name_suffix => o
  }
  
  # This has a space due to make it clear the origin of the module
  source = "./modules/virtual_machine"

  # This has a space as they are common values for all Azurerm resources
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  # This has a space as these values configure the virtual machines themselves.
  vm_name     = join("-", concat(local.naming.prefix, ["vm"], local.naming.suffix, [each.value.vm_name_suffix]))
  vm_hostname = each.value.vm_hostname
  vm_username = each.value.vm_username
  vm_password = each.value.vm_password
  vm_sku      = each.value.vm_sku
  os_type     = each.value.os_type
  subnet_id   = local.deployed_subnets[each.value.subnet_name].id
}
```

1. String Interpolation should be used sparingly for naming in simple join actions.
2. Values should be hard coded with intention, otherwise default action should be to define the value in the relevant Variable default.

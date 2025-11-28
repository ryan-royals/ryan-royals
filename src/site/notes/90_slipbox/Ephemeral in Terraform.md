---
{"dg-publish":true,"permalink":"/90-slipbox/ephemeral-in-terraform/","tags":["notes"]}
---


You get 3 places where the word `ephemeral` is now added to Terraform: `variables`, the `ephemeral` block (which is basically a `data` block), and `outputs`.

## Limitations

A limitation consistent between all the places you can use `ephemeral` is that it is sticky. If you reference a `ephemeral` var/block/output, the rest of the chain becomes `ephemeral`. The only valid places Ephemeral values can be referenced are: `locals`, `variables`, `outputs`, `providers` , `provisioners` and `connections`. Note that `resources` are not in this list, as they give the error `"Ephemeral values are not valid in resource arguments, because resource instances must persist between Terraform phases."`

**Sample code:**

```terraform
variable "password" {
  type      = string
  ephemeral = true
}
resource "azurerm_key_vault_secret" "password" {
  name         = "password"
  value        = var.password
  key_vault_id = azurerm_key_vault.kv.id
}
```

**Output:**

```bash
│ Error: Invalid use of ephemeral value
│
│   with azurerm_key_vault_secret.password,
│   on ephemeral.tf line 9, in resource "azurerm_key_vault_secret" "password":
│    9:   value        = var.password
│
│ Ephemeral values are not valid in resource arguments, because resource instances must persist between Terraform phases.
```

`Ephemeral` blocks have the ability to use a `depends_on` attribute, but this does not stop it validating at Plan time, so in this example it fails as the Secret named `password` does not exist.

**Sample code:**

```terraform
ephemeral "azurerm_key_vault_secret" "password" {
  name         = "password"
  key_vault_id = azurerm_key_vault.kv.id
  depends_on   = [time_sleep.minute]
}
```

**Output:**

```bash
│ Error: secret password does not exist in Key Vault (Subscription: "3bb8d2ac-64fc-4d58-af80-f6097055fd34"
│ Resource Group Name: "rg-loer"
│ Key Vault Name: "kv-loer")
│
│   with ephemeral.azurerm_key_vault_secret.password,
│   on ephemeral.tf line 12, in ephemeral "azurerm_key_vault_secret" "password":
│   12: ephemeral "azurerm_key_vault_secret" "password" {
│
│ keyvault.BaseClient#GetSecret: Failure responding to request: StatusCode=404 -- Original Error: autorest/azure: Service returned an error. Status=404 Code="SecretNotFound"      
│ Message="A secret with (name/id) password was not found in this key vault. If you recently deleted this secret you may be able to recover it using the correct recovery command. 
│ For help resolving this issue, please see https://go.microsoft.com/fwlink/?linkid=2125182"
```

## When Its All Working

When working, you can see Terraform opening and closing the connection to read the value. And if you later inspect the state file, there is no entry for the `ephemeral` block at all.

```bash
ephemeral.azurerm_key_vault_secret.password: Opening...
ephemeral.azurerm_key_vault_secret.password: Opening complete after 2s
ephemeral.azurerm_key_vault_secret.password: Closing...
ephemeral.azurerm_key_vault_secret.password: Closing complete after 0s
```

## So what Do I Use This for

Authentication keys on `Providers` are the primary use case for `ephemeral`,  
Unfortunately the use cases are pretty limited in the `AzureRM` provider as there is no reason to do this, but this does open up cool use cases when connecting to other things, like when using the `postgresql` provider as in this example from the Terraform documentation

```terraform
ephemeral "aws_secretsmanager_secret_version" "db_master" {
  secret_id = data.aws_db_instance.example.master_user_secret[0].secret_arn
}

locals {
  credentials = jsondecode(ephemeral.aws_secretsmanager_secret_version.db_master.secret_string)
}

provider "postgresql" {
  host     = data.aws_db_instance.example.address
  port     = data.aws_db_instance.example.port
  username = local.credentials["username"]
  password = local.credentials["password"]
}

```

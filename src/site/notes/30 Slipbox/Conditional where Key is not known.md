---
{"dg-publish":true,"dg-path":"Conditional where Key is not known.md","permalink":"/Conditional where Key is not known/","tags":["notes"]}
---


Terraform can be a pain when working with Conditional For_each loops. When Terraform can not calculate all the Keys at plan time, it will fail a deploy.

```bash
│ The "for_each" value depends on resource attributes that cannot be
│ determined until apply, so Terraform cannot predict how many instances will
│ be created. To work around this, use the -target argument to first apply
│ only the resources that the for_each depends on
```

Using a combination of `try` and `count` we can work around this.

```terraform
# Generic catchall for diagnostic settings.check "name" {
# Adding resources to this locals block will automatically enable all log and metric categories for the resource.
locals {
  resource_ids_to_monitor = [
    for o in [azurerm_public_ip.apim,
      azapi_resource.apim,
    azurerm_virtual_network.vnet] : o.id
  ]

  conditional_resource_ids_to_monitor = [azurerm_key_vault.key_vault[0].id, azurerm_public_ip.appgw[0].id]
}

# Using Counts as Terraform needs to know the Keys for For_each Loops, 
# and since we are using conditionals to build out that with the var.load_balancing_configuration.deploy_load_balancing conditional
# it is easier to use counts.
data "azurerm_monitor_diagnostic_categories" "dc" {
  count = length(local.resource_ids_to_monitor)

  resource_id = local.resource_ids_to_monitor[count.index]
}
resource "azurerm_monitor_diagnostic_setting" "ds" {
  count = length(data.azurerm_monitor_diagnostic_categories.dc)

  name                       = "generic-diagnostic-settings"
  target_resource_id         = data.azurerm_monitor_diagnostic_categories.dc[count.index].resource_id
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log_analytics_workspace.id

  dynamic "enabled_log" {
    for_each = data.azurerm_monitor_diagnostic_categories.dc[count.index].log_category_types
    content {
      category = enabled_log.value
    }
  }

  dynamic "metric" {
    for_each = data.azurerm_monitor_diagnostic_categories.dc[count.index].metrics
    content {
      category = metric.value
    }
  }
}

#-------------------------------
data "azurerm_monitor_diagnostic_categories" "lb" {
  count       = var.load_balancing_configuration.deploy_load_balancing ? length(local.conditional_resource_ids_to_monitor) : 0
  resource_id = local.conditional_resource_ids_to_monitor[count.index]
}
resource "azurerm_monitor_diagnostic_setting" "lb" {
  count = var.load_balancing_configuration.deploy_load_balancing ? length(local.conditional_resource_ids_to_monitor) : 0

  name                       = "lb-diagnostic-settings"
  target_resource_id         = local.conditional_resource_ids_to_monitor[count.index]
  log_analytics_workspace_id = azurerm_log_analytics_workspace.log_analytics_workspace.id

  dynamic "enabled_log" {
    for_each = data.azurerm_monitor_diagnostic_categories.lb[count.index].log_category_types
    content {
      category = enabled_log.value
    }
  }

  dynamic "metric" {
    for_each = data.azurerm_monitor_diagnostic_categories.lb[count.index].metrics
    content {
      category = metric.value
    }
  }
}
```

[[30 Slipbox/Terraform Tips and Tricks\|Counts still suck to work with]], but this can get you across the line to let your deploy finish if you don't care about the individual resources being deployed.

If it does not work still... maybe wait for [[30 Slipbox/Terraform Stacks preview\|Terraform Stacks preview]]

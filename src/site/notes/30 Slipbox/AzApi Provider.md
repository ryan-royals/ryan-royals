---
{"dg-publish":true,"dg-path":"AzApi Provider.md","permalink":"/az-api-provider/","tags":["notes"]}
---


## AzAPI Provider

AzAPI is a [[30 Slipbox/Terraform\|Terraform]] Provider used to interact with Azure using API calls instead of using layer of obscurity supplied by the [[30 Slipbox/AzureRM Provider\|AzureRM Provider]].

```go
resource "azapi_resource" "action_group" {
  type      = "Microsoft.Insights/actionGroups@2021-09-01"
  name      = var.action_group_name
  location  = var.location
  parent_id = "/subscriptions/${var.subscription_id}/resourceGroups/${var.resource_group_name}"
  tags      = var.tags


  body = jsonencode({
    properties = {
      enabled        = true
      groupShortName = "var.action_group_short_name"
      emailReceivers = [var.email_receivers]
    }
  })
}
```

In order to get the right Type and body, there is [Documentation Supplied](https://learn.microsoft.com/en-us/azure/templates/) to effectively import and use, as well as the [Terraform AzApi Provider - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=azapi-vscode.azapi).

**azapi_resource** is the primary *Resource* that deploys new Azure resources. It is aware enough of Azure to Create Read Update Delete as required.

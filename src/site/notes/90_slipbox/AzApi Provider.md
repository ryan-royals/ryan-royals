---
{"dg-publish":true,"permalink":"/90-slipbox/az-api-provider/","tags":["notes"],"created":"2023-08-29","updated":"2025-11-27"}
---


AzAPI is a [[90_slipbox/Terraform\|Terraform]] Provider used to interact with Azure using API calls instead of using layer of obscurity supplied by the [[90_slipbox/AzureRM Provider\|AzureRM Provider]].

```hcl
resource "azapi_resource" "action_group" {
  type      = "Microsoft.Insights/actionGroups@2021-09-01"
  name      = var.action_group_name
  location  = var.location
  parent_id = "/subscriptions/${var.subscription_id}/resourceGroups/${var.resource_group_name}"
  tags      = var.tags

  body = {
    properties = {
      enabled        = true
      groupShortName = "var.action_group_short_name"
      emailReceivers = [var.email_receivers]
    }
  }
}
```

In order to get the right Type and body, there is [Documentation Supplied](https://learn.microsoft.com/en-us/azure/templates/) to effectively import and use, as well as the [Terraform AzApi Provider - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=azapi-vscode.azapi).  
I also have my fancy dancy[fztfaz tool](https://github.com/ryan-royals/kachow/blob/main/stow/zsh/.zsh/tools/fztfaz.zsh) that I (Claude) made.

My recommendation is to always use the Azapi Provider instead of [[90_slipbox/AzureRM Provider\|AzureRM Provider]] due to the obscurity AzureRm adds. There is a trade off that Azapi is harder to read and write, but it compensates for that by the JSON body matching the `view json` button all resources in Azure have, so it takes less translating.

## Features

### Sensitive Body

Found that [[90_slipbox/AzApi Provider\|AzApi Provider]] has way better support for [[90_slipbox/Terraform\|Terraform]] Ephemeral blocks that [[90_slipbox/AzureRM Provider\|AzureRM Provider]].  
You can just use a `sensitve_body` to mark whatever argument you want as sensitive, and it just works.  
This is way better than the AzureRM equivalent where it needs to be hand crafted, and there are resources that currently do not support it.

## Troubleshooting

### Operation Hangs Forever

Enabling `TF_lOG = DEBUG` allows for you to see the full ARM template being used, and the full http response. This may reveal that a operation is retrying infinite times, or other information about why the run never ends.

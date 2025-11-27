---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Logic Apps.md","permalink":"/slipbox-notes/azure-logic-apps/","tags":["notes"],"created":"2023-12-11","updated":"2025-11-28"}
---


## Deploying via Pipeline

Logic Apps Standard under the hood is just [[90_slipbox/Azure Functions Apps\|Azure Functions Apps]].  
Files are stored under `/wwwroot` :

```
.
└── wwwroot/
    ├── example_workflow/
    │   └── workflow.json
    ├── connections.json
    └── host.json
```

These can be explored in the Kudu web management console.  
Uploading a Zip file using [Azure/functions-action Github Action](https://github.com/Azure/functions-action/tree/master) like you would a Function App works, but it makes the Portal GUI read only as it toggles the app setting `WEBSITE_RUN_FROM_PACKAGE` which makes the Logic Apps instance effectively Read Only.

## Troubleshooting

### Host Runtime Error in Logic Apps

When deploying with default settings in Terraform, certain settings are missing that are required for the Logic Apps instance to work, and presents as a error when you click on the Workflows tab.  
The required settings are:

```go
resource "azurerm_logic_app_standard" "la" {
  name                = local.sp_naming.la_name
  location            = var.location
  resource_group_name = data.azurerm_resource_group.resource_group.name

  app_service_plan_id        = azurerm_service_plan.sp[0].id
  storage_account_name       = azurerm_storage_account.la[0].name
  storage_account_access_key = azurerm_storage_account.la[0].primary_access_key
  version                    = "~v4"
  app_settings = {
    FUNCTIONS_WORKER_RUNTIME     = "node"
    WEBSITE_NODE_DEFAULT_VERSION = "~18"
  }
}
```

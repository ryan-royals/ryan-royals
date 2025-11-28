---
{"dg-publish":true,"permalink":"/90-slipbox/azure-app-service/","tags":["notes"]}
---


Azure App Service Plan is used to host apps like [[90_slipbox/Azure Functions Apps\|Azure Functions Apps]], [[90_slipbox/Azure Logic Apps\|Azure Logic Apps]] and [[90_slipbox/Azure Web App\|Azure Web App]]

## Network Integration

Subnet Delegation is required to give the App Service Plan access to connect its apps to a subnet.

```go
delegations = [{
    name    = "serverfarmsdelegation"
    sd_name = "Microsoft.Web/serverFarms"
    actions = ["Microsoft.Network/virtualNetworks/subnets/action"]
}]
```

## Troubleshooting

### DNS Lookup not on VNET Integration Azure Apps

Need to have settings in `Configuration > Application Settings` to get it to talk to the [[90_slipbox/Azure Magic IP\|Azure Magic IP]], as well as `Networking > Outbound Traffic > VNet integration > Route All: Enabled`

```JSON
{
"name": "WEBSITE_DNS_ALT_SERVER",
"value": "168.63.129.16",
"slotSetting": false
},
{
"name": "WEBSITE_DNS_SERVER",
"value": "168.63.129.16",
"slotSetting": false
},
```

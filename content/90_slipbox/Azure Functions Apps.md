---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Functions Apps.md","permalink":"/slipbox-notes/azure-functions-apps/","tags":["notes"],"created":"2023-03-08","updated":"2025-11-27"}
---


Azure Functions is hosted on [[90_slipbox/Azure App Service\|Azure App Service]] to provide headless compute based on API calls.

## Troubleshooting

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

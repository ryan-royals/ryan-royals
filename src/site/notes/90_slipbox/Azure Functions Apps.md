---
{"dg-publish":true,"permalink":"/90-slipbox/azure-functions-apps/","tags":["notes"],"created":"2026-03-27T09:57:51.499+10:30","updated":"2026-06-11T09:30:38.365+09:30","dg-note-properties":{"created":"2023-03-08","modified":"2026-06-11","references":null,"related":["[[Azure]]"],"tags":"notes"}}
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

There is also a GUI side change that can be made to point DNS to replicate this setting.

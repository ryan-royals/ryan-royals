---
{"dg-publish":true,"dg-path":"Azure Functions Apps.md","permalink":"/azure-functions-apps/","tags":["notes"]}
---


## Azure Functions

### Overview

Azure Functions is hosted on [[30 Slipbox/Azure App Service\|Azure App Service]] to provide headless compute based on API calls.

### Troubleshooting

Need to have settings in `Configuration > Application Settings` to get it to talk to the [[30 Slipbox/Azure Magic IP\|Azure Magic IP]], as well as `Networking > Outbound Traffic > VNet integration > Route All: Enabled`

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

---

Links: [[30 Slipbox/Azure\|Azure]]  
Tags:  
Reference: [[40 References/readwise/Azure Functions Overview\|Azure Functions Overview]]

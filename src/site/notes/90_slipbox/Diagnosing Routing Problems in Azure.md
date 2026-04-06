---
{"dg-publish":true,"permalink":"/90-slipbox/diagnosing-routing-problems-in-azure/","tags":["notes"],"created":"2026-03-27T09:57:51.501+10:30","updated":"2026-03-27T09:57:51.502+10:30","dg-note-properties":{"tags":"notes","related":["[[Azure]]"],"created":"2023-09-04","modified":"2026-03-03"}}
---


When troubleshooting, starting by viewing the Effective Routes by placing or using a Azure Network Interface Card present on the [[90_slipbox/Azure Subnet\|Subnet]] that you are trying to diagnose.

1. Open the Network Interface in the Portal.
2. `Support + Troubleshooting/Effective Routes`![Diagnosing Routing Problems in Azure-1693823524054.png](/img/user/10_attachments/Diagnosing%20Routing%20Problems%20in%20Azure-1693823524054.png)

```Powershell
Get-AzEffectiveRouteTable `
-NetworkInterfaceName myVMNic1 `
-ResourceGroupName myResourceGroup `
```

> [!info]  
> Remember that Azure User Defined Route overrules [[90_slipbox/Border Gateway Protocol\|Border Gateway Protocol]] which overrules [[90_slipbox/Routing in Azure\|Routing in Azure]]

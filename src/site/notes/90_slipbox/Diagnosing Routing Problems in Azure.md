---
{"dg-publish":true,"dg-path":"Slipbox Notes/Diagnosing Routing Problems in Azure.md","permalink":"/slipbox-notes/diagnosing-routing-problems-in-azure/","tags":["notes"],"created":"2023-09-04","updated":"2025-11-28"}
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

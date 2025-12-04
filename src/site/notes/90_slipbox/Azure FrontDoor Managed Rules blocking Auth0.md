---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure FrontDoor Managed Rules blocking Auth0.md","permalink":"/slipbox-notes/azure-front-door-managed-rules-blocking-auth0/","tags":["notes"],"created":"2024-02-18","updated":"2025-11-28"}
---


Auth0 has some cookies that look like SQL Injections when passed to WAF, and this causes the `AnomalyScoring` to increase, and ultimately get the traffic blocked. This happens on the Azure FrontDoor when the Managed Rules are enabled.

This can be checked in Diagnostic Logs using a query:

```KQL
AzureDiagnostics
| where ResourceType == "FRONTDOORS" and Category == "FrontdoorAccessLog"

// [Azure Front Door Standard/Premium] Firewall blocked request count per hour 
// Count number of firewall blocked requests per hour. Summarize number of firewall blocked requests per hour by policy. 
AzureDiagnostics
| where ResourceProvider == "MICROSOFT.CDN" and Category == "FrontDoorWebApplicationFirewallLog"
| where policy_s == "prdappwaf"
| where clientIP_s == "8.8.8.8"
// | where action_s == "Block"
// | where requestUri_s == "https://app.company.com.au:443/callback"
| summarize RequestCount = count() by bin(TimeGenerated, 1h), ruleName_s, action_s
// | order by RequestCount desc
```

You will get hits that look like this:  

| ruleName_s                                              | action_s       | RequestCount |
| ------------------------------------------------------- | -------------- | ------------ |
| Microsoft_DefaultRuleSet-2.1-SQLI-942370                | AnomalyScoring | 3            |
| Microsoft_DefaultRuleSet-2.1-SQLI-942200                | AnomalyScoring | 90           |
| Microsoft_DefaultRuleSet-2.1-SQLI-942340                | AnomalyScoring | 90           |
| Microsoft_DefaultRuleSet-2.1-SQLI-942370                | AnomalyScoring | 62           |
| Microsoft_DefaultRuleSet-2.1-BLOCKING-EVALUATION-949110 | Block          | 90           |

> [!note]  
> The `SQLI` rules with `AnomalyScoring` are the rules that are being hit and are giving information to the WAF, while the `BLOCKING-EVALUATION-949110` is the WAF deciding to block the traffic.  
`949110` is a red herring as it the operator that is blocking, but does not specifically tell you why. This is show in the Microsoft documentation [Here](https://learn.microsoft.com/en-us/azure/web-application-firewall/afds/waf-front-door-drs?tabs=drs21#drs99001-21)

## How to Resolve

A `Exclusion` can be applied to the Managed Rule in the WAF under:  
`Frontdoor resource | Security policies >> waf policy | Managed Rules >> Manage exclusions`  
The Exclusion added should have the following values:

- Rule set: Microsoft_DefaultRuleSet_2.1
- Rule Group: SQLI
- Rule: All rules in rule group  

| Match variable | Operator | Selector |  
| --- | --- | --- |  
| RequestCookieNames | Contains | \_com.auth0.auth |  
| RequestCookieNames | Contains | com.auth0.auth |  
| RequestCookieNames | Contains | {app}\_portal_session |

> [!note]  
> Unsure the exact naming for the the last {app}\_portal_session cookie, but in my experience there was 3 cookies we added to the exclusion.

---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure App Configuration.md","permalink":"/slipbox-notes/azure-app-configuration/","tags":["notes"],"created":"2024-09-26","updated":"2025-11-27"}
---


## Overview

App Configuration helps developers manage application settings (key/value pairs) and control feature availability (feature toggling). It aims to simplify many of the tasks of working with complex configuration data.

App Configuration supports:

- Hierarchical namespaces (Not Hierarchical RBAC)
- Labelling
- Extensive queries
- Batch retrieval
- Specialized management operations
- A feature-management user interface  
[^1]  
Access to App Configuration is either by Access key or RBAC with the *App Configuration Data Owner* and *App Configuration Data Reader* roles.

### Tiers

3 Tiers are available. Key differences are:  

|                                                                                  | Free                                                                                                                             | Standard                                                                                                                                                                                                              | Premium                                                                                                |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Resources per subscription (A resource consists of a single configuration store) | 1 per region                                                                                                                     | Unlimited                                                                                                                                                                                                             | Unlimited                                                                                              |
| Storage per resource                                                             | 10 MB                                                                                                                            | 1 GB                                                                                                                                                                                                                  | 4 GB                                                                                                   |
| Revision history                                                                 | 7 days                                                                                                                           | 30 days                                                                                                                                                                                                               | 30 days                                                                                                |
| Request quota per resource                                                       | **1,000 per day** (Once the quota is exhausted, HTTP status code 429 will be returned for all requests until the end of the day) | 30,000 per hour (Once the quota is exhausted, requests may return HTTP status code 429 indicating Too Many Requests - until the end of the hour). For Geo Replication enabled resources, 30,000 per hour per replica. | No hourly request quota limits                                                                         |
| SLA                                                                              | None                                                                                                                             | 99.95%                                                                                                                                                                                                                | 99.99%                                                                                                 |
| Features                                                                         | Encryption with Microsoft-managed keys,HMAC or AAD authentication,RBAC support ,Managed identity,Service tags                    | All Free tier functionality plus:  Encryption with customer-managed keys, **Private Link support**, Soft Delete, Geo Replication                                                                                      | All Standard tier functionality plus: 1 replica included (optional to configure during Store creation) |
| Snapshot storage per resource*                                                   | 10 MB                                                                                                                            | 1 GB                                                                                                                                                                                                                  | 4 GB                                                                                                   |

[^2]

[^1]: [Azure App Configuration FAQ](https://learn.microsoft.com/en-us/azure/azure-app-configuration/faq)
[^2]: [App Configuration Pricing](https://azure.microsoft.com/en-us/pricing/details/app-configuration/)

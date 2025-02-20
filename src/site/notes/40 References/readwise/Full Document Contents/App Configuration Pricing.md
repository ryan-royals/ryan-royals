---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/app-configuration-pricing/","tags":["rw/articles"]}
---

![rw-book-cover](https://azure.microsoft.com/svghandler/app-configuration/?width=600&height=315)

#### Fast, scalable parameter storage for app configuration

Get hosted, universal storage for all of your Azure apps. Manage configurations effectively and reliably, in real time, without affecting customers by avoiding time-consuming redeployments. Azure App Configuration is built for speed, scalability, and security.

#### Explore pricing options

Apply filters to customize pricing options to your needs.

Prices are estimates only and are not intended as actual price quotes. Actual pricing may vary depending on the type of agreement entered with Microsoft, date of purchase, and the currency exchange rate. Prices are calculated based on US dollars and converted using London closing spot rates that are captured in the two business days prior to the last business day of the previous month end. If the two business days prior to the end of the month fall on a bank holiday in major markets, the rate setting day is generally the day immediately preceding the two business days. This rate applies to all transactions during the upcoming month. Sign in to the [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) to see pricing based on your current program/offer with Microsoft. Contact an [Azure sales specialist](https://azure.microsoft.com/en-us/contact/pricing/) for more information on pricing or to request a price quote. See [frequently asked questions](https://azure.microsoft.com/en-us/pricing/) about Azure pricing.

Region: 

Currency: United States – Dollar ($) USD 

1 USD = 1.4725 AUD

#### Features and Quotas

|  | Free | Standard | Premium |
| --- | --- | --- | --- |
| Resources per subscription (A resource consists of a single configuration store) | 1 per region | Unlimited | Unlimited |
| Storage per resource | 10 MB | 1 GB | 4 GB |
| Revision history | 7 days | 30 days | 30 days |
| Request quota per resource | 1,000 per day (Once the quota is exhausted, HTTP status code 429 will be returned for all requests until the end of the day) | 30,000 per hour (Once the quota is exhausted, requests may return HTTP status code 429 indicating Too Many Requests - until the end of the hour). For Geo Replication enabled resources, 30,000 per hour per replica. | No hourly request quota limits |
| SLA | None | 99.95%\*\* | 99.99%\*\* |
| Features |  Encryption with Microsoft-managed keys HMAC or AAD authentication RBAC support Managed identity Service tags  |  All Free tier functionality plus: Encryption with customer-managed keys Private Link support Soft Delete Geo Replication  | All Standard tier functionality plus: 1 replica included (optional to configure during Store creation) |
| Snapshot storage per resource\* | 10 MB | 1 GB | 4 GB |

\*Snapshot storage quota is additional and not counted towards Storage per resource.

\*\*This SLA is only applicable when the store has at least one replica. If no replica is configured, the SLA will be 99.9%.

#### Pricing Information

|  | Free | Standard | Premium |
| --- | --- | --- | --- |
| Cost per store1 | Free |  $1.768 per store per day, plus an overage charge at $0.089 per 10,000 requests. The first 200,000 requests are included in the daily charge. Additional requests will be billed as overage.  |  $14.137 per store per day which includes 1 replica, plus an overage charge at $0.089 per 10,000 requests. The first 1.6M (800,000 + additional 800,000 with the included replica) are included in the daily charge. Additional requests will be billed as overage.  |
| Cost per replica | Not applicable |  $1.768 per replica per day plus an overage charge at $0.089 per 10,000 requests per replica. The first 200,000 requests for each replica are included in the daily charge. Additional requests will be billed as overage.  |  1 replica included with the store, and $7.069 per additional replica per day, plus an overage charge at $0.089 per 10,000 requests per replica. The first 800,000 requests are included in the daily charge. Additional requests will be billed as overage.  |
1Cost per store doesn’t include the price of replicas. For replicas pricing, check "Cost per replica".   
   
 Have questions about App Configuration? Check out our [FAQ](https://docs.microsoft.com/en-us/azure/azure-app-configuration/faq#which-app-configuration-tier-should-i-use)

#### Azure pricing and purchasing options

##### Connect with us directly

Get a walkthrough of Azure pricing. Understand pricing for your cloud solution, learn about cost optimization and request a custom proposal.

[Talk to a sales specialist](https://azure.microsoft.com/en-us/contact/pricing/)

##### See ways to purchase

Purchase Azure services through the Azure website, a Microsoft representative, or an Azure partner.

[Explore your options](https://azure.microsoft.com/en-us/pricing/purchase-options/)

#### Additional resources

Learn more about App Configuration features and capabilities.

Estimate your expected monthly costs for using any combination of Azure products.

Review the Service Level Agreement for App Configuration.

Review technical tutorials, videos, and more App Configuration resources.

Talk to a sales specialist for a walk-through of Azure pricing. Understand pricing for your cloud solution.

---
{"dg-publish":true,"permalink":"/40-references/readwise/use-azure-front-door-in-a-multitenant-solution/","tags":["rw/articles"]}
---


![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

  

URL: <https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/front-door>  
Author: Raj Nemani

## Summary

Learn about the features of Azure Front Door that are useful when you work in multitenant solutions.

## Highlights Added July 17, 2024 at 11:02 AM

> Wildcard domains simplify the configuration of DNS records and Azure Front Door traffic routing configuration when you use a shared stem domain and tenant-specific subdomains. For example, suppose your tenants access their applications by using subdomains like `tenant1.app.contoso.com` and `tenant2.app.contoso.com`. You can configure a wildcard domain, `*.app.contoso.com`, instead of configuring each tenant-specific domain individually. ([View Highlight] (<https://read.readwise.io/read/01h4fw00jbevcbn9b8mvwnm09n>))

> Wildcard domains work well if you send all your traffic to a single origin group. But if you have separate stamps of your solution, a single-level wildcard domain isn't sufficient. You either need to use multi-level stem domains or supply extra configuration by, for example, overriding the routes to use for each tenant's subdomain. For more information, see [Considerations when using domain names in a multitenant solution](https://learn.microsoft.com/en-us/azure/architecture/guide/multitenant/service/front-door/../considerations/domain-names). ([View Highlight] (<https://read.readwise.io/read/01h4fw0hzqbkxzkg0ddwmvwve0>))

> Azure Front Door doesn't issue managed TLS certificates for wildcard domains, so you need to purchase and supply your own certificate. ([View Highlight] (<https://read.readwise.io/read/01h4fw0m0ycf65bnsxbcx08r5h>))

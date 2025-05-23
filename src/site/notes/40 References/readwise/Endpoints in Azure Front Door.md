---
{"dg-publish":true,"permalink":"/40-references/readwise/endpoints-in-azure-front-door/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

## Full Document
[[40 References/readwise/Full Document Contents/Endpoints in Azure Front Door\|Readwise/Full Document Contents/Endpoints in Azure Front Door.md]]

## Highlights
In Azure Front Door Standard/Premium, an *endpoint* is a logical grouping of one or more routes that are associated with domain names. Each endpoint is [assigned a domain name](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#endpoint-domain-names) by Front Door, and you can associate your own custom domains by using routes. ([View Highlight] (https://read.readwise.io/read/01h4fw1ntnh99pfvpg5rhn0xhr))


How many endpoints should I create?
A Front Door profile can contain multiple endpoints. However, in many situations you might only need a single endpoint.
When you're planning the endpoints to create, consider the following factors:
• If all of your domains use the same or similar route paths, it's probably best to combine them into a single endpoint.
• If you use different routes and route paths for each domain, consider using separate endpoints, such as by having an endpoint for each custom domain.
• If you need to enable or disable all of your domains together, consider using a single endpoint. An entire endpoint can be enabled or disabled together. ([View Highlight] (https://read.readwise.io/read/01h4fw21ceagnsjq0e9e05vrat))



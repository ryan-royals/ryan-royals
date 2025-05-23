---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/endpoints-in-azure-front-door/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [How many endpoints should I create?](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#how-many-endpoints-should-i-create)
2. [Endpoint domain names](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#endpoint-domain-names)
3. [Next steps](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#next-steps)

In Azure Front Door Standard/Premium, an *endpoint* is a logical grouping of one or more routes that are associated with domain names. Each endpoint is [assigned a domain name](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#endpoint-domain-names) by Front Door, and you can associate your own custom domains by using routes.

#### How many endpoints should I create?

A Front Door profile can contain multiple endpoints. However, in many situations you might only need a single endpoint.

When you're planning the endpoints to create, consider the following factors:

* If all of your domains use the same or similar route paths, it's probably best to combine them into a single endpoint.
* If you use different routes and route paths for each domain, consider using separate endpoints, such as by having an endpoint for each custom domain.
* If you need to enable or disable all of your domains together, consider using a single endpoint. An entire endpoint can be enabled or disabled together.

#### Endpoint domain names

Endpoint domain names are automatically generated when you create a new endpoint. Front Door generates a unique domain name based on several components, including:

* The endpoint's name.
* A pseudorandom hash value, which is determined by Front Door. By using hash values as part of the domain name, Front Door helps to protect against [subdomain takeover](https://learn.microsoft.com/en-us/azure/security/fundamentals/subdomain-takeover) attacks.
* The base domain name for your Front Door environment. This is generally `z01.azurefd.net`.

For example, suppose you have created an endpoint named `myendpoint`. The endpoint domain name might be `myendpoint-mdjf2jfgjf82mnzx.z01.azurefd.net`.

The endpoint domain is accessible when you associate it with a route.

##### Reuse of an endpoint domain name

When you delete and redeploy an endpoint, you might expect to get the same pseudorandom hash value, and therefore the same endpoint domain name. Front Door enables you to control how the pseudorandom hash values are reused on an endpoint-by-endpoint basis.

An endpoint's domain can be reused within the same tenant, subscription, or resource group scope level. You can also choose to not allow the reuse of an endpoint domain. By default, Front Door allows reuse of the endpoint domain within the same Azure Active Directory tenant.

You can use Bicep, an Azure Resource Manager template (ARM template), the Azure CLI, or Azure PowerShell to configure the scope level of the endpoint's domain reuse behavior. You can also configure it for all Front Door endpoints in your whole organization by using Azure Policy. The Azure portal uses the scope level you define through the command line once it has been changed.

The following table lists the allowable values for the endpoint's domain reuse behavior:

| Value | Description |
| --- | --- |
| `TenantReuse` | This is the default value. Endpoints with the same name in the same Azure Active Directory tenant receive the same domain label. |
| `SubscriptionReuse` | Endpoints with the same name in the same Azure subscription receive the same domain label. |
| `ResourceGroupReuse` | Endpoints with the same name in the same resource group will receive the same domain label. |
| `NoReuse` | Endpoints will always receive a new domain label. |

Note

You can't modify the reuse behavior of an existing Front Door endpoint. The reuse behavior only applies to newly created endpoints.

The following example shows how to create a new Front Door endpoint with a reuse scope of `SubscriptionReuse`:

* [Azure CLI](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#tabpanel_1_azurecli)
* [Azure PowerShell](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#tabpanel_1_azurepowershell)
* [Bicep](https://learn.microsoft.com/en-us/azure/frontdoor/endpoint?tabs=azurecli#tabpanel_1_bicep)

Azure CLI 

```
az afd endpoint create \
  --resource-group MyResourceGroup \
  --profile-name MyProfile \
  --endpoint-name myendpoint \
  --name-reuse-scope SubscriptionReuse

```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
Azure PowerShell 

```
New-AzFrontDoorCdnEndpoint `
   -ResourceGroupName MyResourceGroup `
   -ProfileName MyProfile `
   -EndpointName myendpoint `
   -Location global `
   -AutoGeneratedDomainNameLabelScope SubscriptionReuse

```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
Bicep 

```
resource endpoint 'Microsoft.Cdn/profiles/afdEndpoints@2021-06-01' = {
  name: endpointName
  parent: profile
  location: 'global'
  properties: {
    autoGeneratedDomainNameLabelScope: 'SubscriptionReuse'
  }
}

```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)
#### Next steps

* [Configure an origin](https://learn.microsoft.com/en-us/azure/frontdoor/origin) for Azure Front Door.

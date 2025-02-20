---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-app-configuration-faq/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

This article answers frequently asked questions about Azure App Configuration.

App Configuration helps developers manage application settings and control feature availability. It aims to simplify many of the tasks of working with complex configuration data.

App Configuration supports:

* Hierarchical namespaces
* Labeling
* Extensive queries
* Batch retrieval
* Specialized management operations
* A feature-management user interface

App Configuration complements Key Vault, and the two should be used side by side in most application deployments.

Although App Configuration provides hardened security, Key Vault is still the best place for storing application secrets. Key Vault provides hardware-level encryption, granular access policies, and management operations such as certificate rotation.

You can create App Configuration key-values that reference secrets stored in Key Vault. For more information, see [Use Key Vault references in an ASP.NET Core app](https://learn.microsoft.com/en-us/azure/azure-app-configuration/use-key-vault-references-dotnet-core).

Yes. App Configuration always encrypts all data in transit and at rest. All network communication is over TLS 1.2 or TLS 1.3. App Configuration supports encryption at rest with either [Microsoft-managed keys or customer-managed keys](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-customer-managed-keys).

Azure App Service allows you to define app settings for each App Service instance. These settings are passed as environment variables to the application code. You can associate a setting with a specific deployment slot, if you want. For more information, see [Configure app settings](https://learn.microsoft.com/en-us/azure/app-service/configure-common#configure-app-settings).

In contrast, Azure App Configuration allows you to define settings that can be shared among multiple apps. This includes apps running in App Service, as well as other platforms. Your application code accesses these settings through the configuration providers for .NET and Java, through the Azure SDK, or directly via REST APIs.

You can add [references to your App Configuration data](https://learn.microsoft.com/en-us/azure/app-service/app-service-configuration-references) in the Application settings of your App Service. You can also [import and export settings](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-import-export-data) between App Service and App Configuration. This capability allows you to quickly set up a new App Configuration store based on existing App Service settings. You can also share configuration with an existing app that relies on App Service settings.

There's a limit of 10 KB for a single key-value, including attributes such as label, content-type, tags, and other metadata.

This limit should be sufficient for a single setting in most applications. If you find that your setting is larger than this limit, you may consider storing your data elsewhere, and [add a reference of that data](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-best-practices#references-to-external-data) in App Configuration.

For more information, see [Azure subscription and service limits](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/azure-subscription-service-limits#azure-app-configuration).

You control who can access App Configuration at a per-store level. Use a separate store for each environment that requires different permissions. This approach provides the best security isolation.

If you don't need security isolation between environments, you can use labels to differentiate between configuration values. [Use labels to enable different configurations for different environments](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-labels-aspnet-core) provides a complete example.

See [best practices](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-best-practices).

There are three pricing tiers: Free, Standard, and Premium. For detailed pricing information, refer to the [App Configuration pricing](https://azure.microsoft.com/en-us/pricing/details/app-configuration/) page.

All App Configuration tiers offer core functionality, including config settings, feature flags, Key Vault references, configuration snapshots, basic management operations, metrics, and logs.

The following are considerations for choosing a tier.

* **Purpose**: The Free tier is perfect for evaluating the service in non-production environments, allowing you to explore its features without any cost. The Standard tier is tailored for medium-volume production use cases, providing a balance of performance and cost-efficiency. For high-volume or enterprise-level production needs, the Premium tier offers the highest level of performance and scalability, ensuring your applications run smoothly even under heavy load.
* **Resources per subscription**: A resource consists of a single configuration store. Each subscription is limited to one configuration store per region in the Free tier. Subscriptions can have an unlimited number of configuration stores in the Standard and Premium tiers.
* **Storage per resource**: In the Free tier, each configuration store is limited to 10 MB of regular storage and 10 MB of snapshot storage. In the Standard tier, each configuration store can use up to 1 GB of regular storage and an additional 1 GB of snapshot storage. In the Premium tier, each configuration store can use up to 4 GB of regular storage and an additional 4 GB of snapshot storage.
* **Revision history**: App Configuration stores a history of all changes made to keys. In the Free tier, this history is stored for seven days. In the Standard and Premium tiers, this history is stored for 30 days.
* **Requests quota**: Free tier stores are limited to 1,000 requests per day. When a store reaches 1,000 requests, it returns HTTP status code 429 for all requests until midnight UTC.

 Standard tier stores are limited to 30,000 requests per hour. Once the hourly quota is exhausted, additional requests may return an HTTP status code 429, indicating too many requests, until the end of the hour. As more requests are sent which are above quota, a higher percentage of them may return status code 429.

 Premium tier stores have no quota limit on requests, ensuring that access to the store is never blocked.
* **Throughput**: App Configuration stores in all tiers have a throughput allowance. Requests exceeding this allowance will receive an HTTP status code 429 response. Stores in the Free tier have no guaranteed throughput.

 Stores in the Standard tier allow up to 300 requests per second (RPS) for read requests and up to 60 RPS for write requests.

 Stores in the Premium tier allow up to 450 RPS for read requests and up to 100 RPS for write requests.
* **Service level agreement**: The Free tier doesn't have an SLA. The Standard tier has an SLA of 99.9% availability and 99.95% availability with geo-replication enabled. The Premium tier has an SLA of 99.9% availability and 99.99% availability with geo-replication enabled.
* **Features**: All tiers include functionalities, including encryption with Microsoft-managed keys, authentication via access key or Microsoft Entra ID, Azure role-based access control (RBAC), managed identity, service tags, and availability zone redundancy. The Standard and Premium tiers offer more functionalities, including Private Link support, encryption with customer-managed keys, soft delete protection, and geo-replication capability.
* **Cost**: There's no cost to use a Free tier store.

 Standard tier stores have a daily usage charge, which includes the first 200,000 requests each day. Requests beyond this daily allocation incur an overage charge.

 Premium tier stores also have a daily usage charge and include a replica. The first 800,000 requests for the origin and the first 800,000 requests for the replica each day are included in the daily charge. Requests exceeding this daily allocation incur an overage charge.

You can upgrade an App Configuration store at any time, for example, from the Free tier to the Standard or Premium tier, or from the Standard tier to the Premium tier.

You can't downgrade an App Configuration store, for example, from the Premium tier to the Standard tier, or from the Standard tier to the Free tier. However, you can create a new store in the desired tier and then [import configuration data into that store](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-import-export-data).

Customer data stored in App Configuration reside in the region where the customer's App Configuration store was created. Customer data will be replicated to another region only if the customer enables [geo-replication](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-geo-replication) for that region. This applies to all available regions. Customers may move, copy, or access their data from any location globally.

Azure App Configuration supports [geo-replication](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-geo-replication) for enhanced resiliency to regional outages.

Azure App Configuration supports Azure availability zones to protect your application and data from single datacenter failures. All availability zone enabled regions consist of a minimum of 3 availability zones, where each is a physically independent datacenter. For resiliency, this support in App Configuration is enabled for all customers at no extra cost. Following are regions that App Configuration has enabled availability zone support. For more information, see [Regions and Availability Zones in Azure.](https://learn.microsoft.com/en-us/azure/reliability/availability-zones-service-support)

Following are regions where App Configuration has enabled availability zone support.

| Americas | Europe | Middle East | Africa | Asia Pacific |
| --- | --- | --- | --- | --- |
| Brazil South | France Central | Qatar Central |  | Australia East |
| Canada Central | Italy North | UAE North |  | Central India |
| Central US | Germany West Central | Israel Central |  | Japan East |
| East US | North Europe |  |  | Korea Central |
| East US 2 | Norway East |  |  | Southeast Asia |
| South Central US | UK South |  |  | East Asia |
| US Gov Virginia | West Europe |  |  | China North 3 |
| West US 2 | Sweden Central |  |  |  |
| West US 3 | Switzerland North |  |  |  |
| Mexico Central | Poland Central |  |  |  |
|  | Spain Central |  |  |  |

App Configuration stores have different request quotas based on their tier. Free tier stores are limited to 1,000 requests per day, Standard tier stores to 30,000 requests per hour, and Premium tier stores have no request limits, ensuring uninterrupted access.

App Configuration stores have throughput allowances based on their tier. Free tier stores do not have guaranteed throughput. Standard tier stores support up to 300 requests per second (RPS) for read operations and up to 60 RPS for write operations. Premium tier stores support up to 450 RPS for read operations and up to 100 RPS for write operations.

Let's take an example and assume you have an application with 1,000 configuration settings. Your application loads all those settings from App Configuration upon startup. After that, it checks for a sentinel key for configuration changes every 30 seconds. Whether you are running on Kubernetes, App Service, or VMs, let's assume you have 50 instances of your application running simultaneously.

Firstly, let's estimate the requests for configuration monitoring. Each instance of your application will send one request for the sentinel key to App Configuration every 30 seconds, so it will send 120 (=3600/30) requests in an hour. Given you have 50 instances of your application, your application sends 6,000 (=120x50) total requests every hour for configuration monitoring. Note that because the sentinel key requests are frequent and mostly unchanged, the majority of them won't count against the store hourly quota limits†.

Secondly, let's estimate the requests for configuration loading/reloading. Your application loads all settings at the startup or whenever a sentinel key change is detected. Each request to App Configuration can retrieve up to 100 key-values, so it will take 10 (=1000/100) requests to load all settings. Given you have 50 application instances, you send 500 (=10x50) total requests when your application restarts or reloads its configuration.

Finally, let's put it together. Assuming you updated the sentinel key twice within an hour, your App Configuration store will thus receive 7,000 (=6,000+500x2) total requests for that hour. Note that out of these requests, only about 1,000 (=500x2) requests will use the available hourly quota. Update the numbers in this example to match your specific setup and design accordingly so you have a sufficient buffer against the hourly throttling limit.

†Free tier stores do not have frequent, repeated requests excluded from their daily limit.

Your application may receive an HTTP status code 429 response under the following circumstances:

* Exceeding the daily request quota for a store in the Free tier.
* Exceeding the hourly request quota for a store in the Standard tier.
* Exceeding the throughput allowance for a store in any tier.
* Exceeding the bandwidth allowance for a store in any tier.
* Attempting to create or modify a key-value when the storage quota is exceeded.

Check the body of the 429 response for the specific reason why the request failed. You can also collect logs for your [App Configuration store in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-app-configuration/monitor-app-configuration) and set up alerts for the *Request Quota Usage* metric.

Receiving momentary HTTP status code 429 responses usually causes no harm, as App Configuration clients handle them gracefully. However, if your application regularly experiences HTTP status code 429 responses, consider the following options:

* **Upgrade your store to the Premium tier**: This tier has no quota limit on requests and has significantly increased storage quota.
* **Use App Configuration Providers**: The providers have built-in retry and caching capabilities along with many other resiliency features.
* **Use App Configuration SDKs** if your application needs to send write requests. Although the SDKs may not be as feature-rich as providers, they automatically retry on HTTP status code 429 responses.
* **Include retry logic in custom clients** if you can't use App Configuration Providers or SDKs. The `retry-after-ms` header in the response provides a suggested wait time (in milliseconds) before retrying the request.
* **Distribute requests across multiple client instances**: This helps achieve the maximum throughput from your App Configuration store.
* **Reduce requests made to App Configuration**: Follow the guidance to [minimize the number of requests](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-best-practices#reduce-requests-made-to-app-configuration).
* **Improve your application resiliency**: Consider integrating geo-replication to allow failover and load balancing. Check the best practices for [building highly resilient applications](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-best-practices#building-applications-with-high-resiliency).

All App Configuration stores in the Standard and Premium tiers have automatically enabled the [soft-delete](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-soft-delete) feature. When a Standard or Premium tier App Configuration store is deleted, its name is reserved for the retention period. To recreate a store with the same name before the retention period expires, you need to [purge the soft-deleted store](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-recover-deleted-stores-in-azure-app-configuration#list-recover-or-purge-a-soft-deleted-app-configuration-store) first, provided the store doesn't have purge protection enabled. If the purge protection is enabled, you must wait for the retention period to elapse. Use the purge function or set a shorter retention period if you often need to recreate a store with the same name. Workflows that require recreating a store with the same name should allow for one hour between purging a configuration store and performing the subsequent create. This recommendation is in place because once a purge is requested the actual cleanup of configuration store resources is performed asynchronously, requiring a bit of extra time to finalize. To avoid any need to wait, workflows that create ephemeral configuration stores are recommended to use unique names.

All App Configuration stores in the Standard and Premium tiers support the [soft-delete](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-soft-delete) feature, which can't be disabled. You can recover a deleted store within its retention period. Follow these [instructions](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-recover-deleted-stores-in-azure-app-configuration) to recover a mistakenly deleted App Configuration store.

Yes. While you can manage feature flags and Key Vault references in App Configuration through the Azure portal or CLI, you can also create and update them programmatically using App Configuration SDKs. Therefore, you can write your customized management portal or manage them in your CI/CD programmatically. The feature flag and Key Vault reference APIs are available in SDKs of all supported languages. Check out the [sample links](https://github.com/Azure/AppConfiguration#sdks) for examples in each supported language.

Evaluating and consuming feature flags in your application requires the App Configuration provider and feature management libraries, which are available in .NET and Java Spring. Check out the *Feature management* section under *Quickstarts* and *Tutorials* for more information.

Spring profiles provide a way to separate parts of your application, including configuration, and make it only available in certain environments or when specific libraries are used.

You're recommended to set the label of your key-values to match your Spring profiles. By default, the App Configuration Spring provider library will load the key-values with the label(s) matching the current active Spring profile(s) (`${spring.profiles.active}`) if the label filter isn't set explicitly. If there's no active Spring profile set, key-values with "no label" will be loaded.

For example, with profiles `dev` and `prod`, you create key-values accordingly with the following labels.

| Key | Label | Value |
| --- | --- | --- |
| /application/config.message | dev | Hello from dev |
| /application/config.message | prod | Hello from prod |

When the Spring profile is set to `dev`, the value of `config.message` will be `Hello from dev`. When the Spring profile is set to `prod`, the value of `config.message` will be `Hello from prod`.

This default behavior can be overridden by setting the label filter in your bootstrap file. The Spring provider library will load key-values with the specified label(s) regardless of the active Spring profile.

YAML 

```
spring.cloud.azure.appconfiguration.stores[0].selects[0].label-filter: my-label

```

To select other labels and your Spring profile(s), you can use a label filter like `',${spring.profiles.active}'`, which will select all keys without a label and the ones matching your Spring profiles. The rightmost label(s) take priority when duplicate keys are found.

Starting with version 3.1.0, the `Microsoft.FeatureManagement` library allows running feature management services, including feature filters, as scoped services in dependency injection-based .NET applications. To take advantage of this feature, you can simply replace the `AddFeatureManagement` call in your code with `AddScopedFeatureManagement`, as shown in the following code snippet:

C# 

```
services.AddScopedFeatureManagement();

```

Feature filters can evaluate a feature flag based on the properties of an HTTP Request. This is usually performed by inspecting the `HttpContext` through the singleton `IHttpContextAccessor` [pattern](https://learn.microsoft.com/en-us/azure/azure-app-configuration/howto-targetingfilter-aspnet-core#update-the-web-application-code-to-use-targetingfilter). However, this pattern does not work for [Blazor server applications](https://learn.microsoft.com/en-us/aspnet/core/blazor/security/server/interactive-server-side-rendering?view=aspnetcore-7.0#ihttpcontextaccessorhttpcontext-in-razor-components) where scoped services should be used instead. In this case, `AddScopedFeatureManagement` method should be used.

Subscribe to our [GitHub announcements repo](https://github.com/Azure/AppConfiguration-Announcements).

You can reach us directly on [GitHub](https://github.com/Azure/AppConfiguration/issues).

* [About Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/overview)

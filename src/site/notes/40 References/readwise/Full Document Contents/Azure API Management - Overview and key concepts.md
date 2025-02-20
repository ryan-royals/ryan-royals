---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azure-api-management-overview-and-key-concepts/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_rUrD9xy.png)

#### In this article

1. [Scenarios](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#scenarios)
2. [API Management components](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#api-management-components)
3. [API gateway](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#api-gateway)
4. [Management plane](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#management-plane)
5. [Developer portal](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#developer-portal)
6. [Integration with Azure services](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#integration-with-azure-services)
7. [Key concepts](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#key-concepts)
8. [Next steps](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#next-steps)

This article provides an overview of common scenarios and key components of Azure API Management. Azure API Management is a hybrid, multicloud management platform for APIs across all environments. As a platform-as-a-service, API Management supports the complete API lifecycle.

Tip

If you're already familiar with API Management and ready to start, see these resources:

* [Features and service tiers](https://learn.microsoft.com/en-us/azure/api-management/api-management-features)
* [Create an API Management instance](https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance)
* [Import and publish an API](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)
* [API Management policies](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies)

#### Scenarios

APIs enable digital experiences, simplify application integration, underpin new digital products, and make data and services reusable and universally accessible. ​With the proliferation and increasing dependency on APIs, organizations need to manage them as first-class assets throughout their lifecycle.​

![Diagram showing role of APIs in connected experiences.](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-key-concepts-experiment/apis-connected-experiences.png)
Azure API Management helps customers meet these challenges:

* Abstract backend architecture diversity and complexity from API consumers
* Securely expose services hosted on and outside of Azure as APIs
* Protect, accelerate, and observe APIs
* Enable API discovery and consumption by internal and external users

Common scenarios include:

* **Unlocking legacy assets** - APIs are used to abstract and modernize legacy backends and make them accessible from new cloud services and modern applications. APIs allow innovation without the risk, cost, and delays of migration.
* **API-centric app integration** - APIs are easily consumable, standards-based, and self-describing mechanisms for exposing and accessing data, applications, and processes. They simplify and reduce the cost of app integration.
* **Multi-channel user experiences** - APIs are frequently used to enable user experiences such as web, mobile, wearable, or Internet of Things applications. Reuse APIs to accelerate development and ROI.
* **B2B integration** - APIs exposed to partners and customers lower the barrier to integrate business processes and exchange data between business entities. APIs eliminate the overhead inherent in point-to-point integration. Especially with self-service discovery and onboarding enabled, APIs are the primary tools for scaling B2B integration.

#### API Management components

Azure API Management is made up of an API *gateway*, a *management plane*, and a *developer portal*. These components are Azure-hosted and fully managed by default. API Management is available in various [tiers](https://learn.microsoft.com/en-us/azure/api-management/api-management-features) differing in capacity and features.

![Diagram showing key components of Azure API Management.](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-key-concepts-experiment/api-management-components.png)
#### API gateway

All requests from client applications first reach the API gateway, which then forwards them to respective backend services. The API gateway acts as a facade to the backend services, allowing API providers to abstract API implementations and evolve backend architecture without impacting API consumers. The gateway enables consistent configuration of routing, security, throttling, caching, and observability.

Specifically, the gateway:

* Acts as a facade to backend services by accepting API calls and routing them to appropriate backends
* Verifies [API keys](https://learn.microsoft.com/en-us/azure/api-management/api-management-subscriptions) and other credentials such as [JWT tokens and certificates](https://learn.microsoft.com/en-us/azure/api-management/api-management-access-restriction-policies) presented with requests
* Enforces [usage quotas and rate limits](https://learn.microsoft.com/en-us/azure/api-management/api-management-access-restriction-policies)
* Optionally transforms requests and responses as specified in [policy statements](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies)
* If configured, [caches responses](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-cache) to improve response latency and minimize the load on backend services
* Emits logs, metrics, and traces for [monitoring, reporting, and troubleshooting](https://learn.microsoft.com/en-us/azure/api-management/observability)

##### Self-hosted gateway

With the [self-hosted gateway](https://learn.microsoft.com/en-us/azure/api-management/self-hosted-gateway-overview), customers can deploy the API gateway to the same environments where they host their APIs, to optimize API traffic and ensure compliance with local regulations and guidelines. The self-hosted gateway enables customers with hybrid IT infrastructure to manage APIs hosted on-premises and across clouds from a single API Management service in Azure.

The self-hosted gateway is packaged as a Linux-based Docker container and is commonly deployed to Kubernetes, including to Azure Kubernetes Service and [Azure Arc-enabled Kubernetes](https://learn.microsoft.com/en-us/azure/api-management/how-to-deploy-self-hosted-gateway-azure-arc).

More information:

* [API gateway in Azure API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-gateways-overview)

#### Management plane

API providers interact with the service through the management plane, which provides full access to the API Management service capabilities.

Customers interact with the management plane through Azure tools including the Azure portal, Azure PowerShell, Azure CLI, a [Visual Studio Code extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-apimanagement&ssr=false#overview), or client SDKs in several popular programming languages.

Use the management plane to:

* Provision and configure API Management service settings
* Define or import API schemas from a wide range of sources, including OpenAPI specifications, Azure compute services, or WebSocket or GraphQL backends
* Package APIs into products
* Set up [policies](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#policies) like quotas or transformations on the APIs
* Get insights from analytics
* Manage users

#### Developer portal

The open-source [developer portal](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#developer-portal) is an automatically generated, fully customizable website with the documentation of your APIs.

![Screenshot of API Management developer portal - administrator mode.](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-key-concepts-experiment/cover.png)
API providers can customize the look and feel of the developer portal by adding custom content, customizing styles, and adding their branding. Extend the developer portal further by [self-hosting](https://learn.microsoft.com/en-us/azure/api-management/developer-portal-self-host).

App developers use the open-source developer portal to discover the APIs, onboard to use them, and learn how to consume them in applications. (APIs can also be exported to the [Power Platform](https://learn.microsoft.com/en-us/azure/api-management/export-api-power-platform) for discovery and use by citizen developers.)

Using the developer portal, developers can:

* Read API documentation
* Call an API via the interactive console
* Create an account and subscribe to get API keys
* Access analytics on their own usage
* Download API definitions
* Manage API keys

#### Integration with Azure services

API Management integrates with many complementary Azure services to create enterprise solutions, including:

* [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview) for secure safekeeping and management of [client certificates](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-mutual-certificates) and [secrets​](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties)
* [Azure Monitor](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-use-azure-monitor) for logging, reporting, and alerting on management operations, systems events, and API requests​
* [Application Insights](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-app-insights) for live metrics, end-to-end tracing, and troubleshooting
* [Virtual networks](https://learn.microsoft.com/en-us/azure/api-management/virtual-network-concepts), [private endpoints](https://learn.microsoft.com/en-us/azure/api-management/private-endpoint), and [Application Gateway](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-integrate-internal-vnet-appgateway) for network-level protection​
* Azure Active Directory for [developer authentication](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-aad) and [request authorization](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-protect-backend-with-aad)​
* [Event Hubs](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-log-event-hubs) for streaming events​
* Several Azure compute offerings commonly used to build and host APIs on Azure, including [Functions](https://learn.microsoft.com/en-us/azure/api-management/import-function-app-as-api), [Logic Apps](https://learn.microsoft.com/en-us/azure/api-management/import-logic-app-as-api), [Web Apps](https://learn.microsoft.com/en-us/azure/api-management/import-app-service-as-api), [Service Fabric](https://learn.microsoft.com/en-us/azure/api-management/how-to-configure-service-fabric-backend), and others.​

**More information**:

* [Basic enterprise integration](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/enterprise-integration/basic-enterprise-integration?toc=%2Fazure%2Fapi-management%2Ftoc.json&bc=/azure/api-management/breadcrumb/toc.json)
* [Landing zone accelerator](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/app-platform/api-management/landing-zone-accelerator?toc=%2Fazure%2Fapi-management%2Ftoc.json&bc=/azure/api-management/breadcrumb/toc.json)

#### Key concepts

##### APIs

APIs are the foundation of an API Management service instance. Each API represents a set of *operations* available to app developers. Each API contains a reference to the backend service that implements the API, and its operations map to backend operations.

Operations in API Management are highly configurable, with control over URL mapping, query and path parameters, request and response content, and operation response caching.

**More information**:

* [Import and publish your first API](https://learn.microsoft.com/en-us/azure/api-management/import-and-publish)
* [Mock API responses](https://learn.microsoft.com/en-us/azure/api-management/mock-api-responses)

##### Products

Products are how APIs are surfaced to developers. Products in API Management have one or more APIs, and can be *open* or *protected*. Protected products require a subscription key, while open products can be consumed freely.

When a product is ready for use by developers, it can be published. Once published, it can be viewed or subscribed to by developers. Subscription approval is configured at the product level and can either require an administrator's approval or be automatic.

**More information**:

* [Create and publish a product](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-add-products)
* [Subscriptions in API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-subscriptions)

##### Groups

Groups are used to manage the visibility of products to developers. API Management has the following built-in groups:

* **Administrators** - Manage API Management service instances and create the APIs, operations, and products that are used by developers.

 Azure subscription administrators are members of this group.
* **Developers** - Authenticated developer portal users that build applications using your APIs. Developers are granted access to the developer portal and build applications that call the operations of an API.
* **Guests** - Unauthenticated developer portal users, such as prospective customers visiting the developer portal. They can be granted certain read-only access, such as the ability to view APIs but not call them.

Administrators can also create custom groups or use external groups in an [associated Azure Active Directory tenant](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-aad) to give developers visibility and access to API products. For example, create a custom group for developers in a partner organization to access a specific subset of APIs in a product. A user can belong to more than one group.

**More information**:

* [How to create and use groups](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-create-groups)

##### Developers

Developers represent the user accounts in an API Management service instance. Developers can be created or invited to join by administrators, or they can sign up from the [developer portal](https://learn.microsoft.com/en-us/azure/api-management/api-management-key-concepts#developer-portal). Each developer is a member of one or more groups, and can subscribe to the products that grant visibility to those groups.

When developers subscribe to a product, they're granted the primary and secondary key for the product for use when calling the product's APIs.

**More information**:

* [How to manage user accounts](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-create-or-invite-developers)

##### Policies

With [policies](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies), an API publisher can change the behavior of an API through configuration. Policies are a collection of statements that are executed sequentially on the request or response of an API. Popular statements include format conversion from XML to JSON and call-rate limiting to restrict the number of incoming calls from a developer. For a complete list, see [API Management policies](https://learn.microsoft.com/en-us/azure/api-management/api-management-policies).

Policy expressions can be used as attribute values or text values in any of the API Management policies, unless the policy specifies otherwise. Some policies such as the [Control flow](https://learn.microsoft.com/en-us/azure/api-management/choose-policy) and [Set variable](https://learn.microsoft.com/en-us/azure/api-management/set-variable-policy) policies are based on policy expressions.

Policies can be applied at different scopes, depending on your needs: global (all APIs), a product, a specific API, or an API operation.

**More information**:

* [Transform and protect your API](https://learn.microsoft.com/en-us/azure/api-management/transform-api).
* [Policy expressions](https://learn.microsoft.com/en-us/azure/api-management/api-management-policy-expressions)

#### Next steps

Complete the following quickstart and start using Azure API Management:

[Create an Azure API Management instance by using the Azure portal](https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance)

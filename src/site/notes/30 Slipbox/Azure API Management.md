---
{"dg-publish":true,"dg-path":"Azure API Management.md","permalink":"/azure-api-management/","tags":["notes"]}
---


Azure APIM is a hybrid, multicloud management platform for APIs across al environments. As a platform-as-a-service, API Management supports the complete API Lifecycle.  
It helps resolve challenges by:

- Abstracting backend architecture diversity and complexity from API consumers
- Securely expose services hosted on and outside of Azure as APIs
- Protect, accelerate, and observe APIs
- Enable API discovery and consumption by internal and external users

APIM works with [[30 Slipbox/OpenAPI Specification\|OpenAPI Specification]]

Key tooling includes:

- Policy driven controls for
	- Throttling
	- Transform requests (REST to SOAP)
	- Only allow X calls in X minutes
- Access Key driven access profiles, can be revoked.
- Usage Metrics that can be sent to billing engine.

## Quick Notes

- Internal VNET mode is only available on Dev and Premium SKU's
- API's can have a whitelist / blacklist of calling IP's on the inbound processing for each API
- The latest version of API Management lets you have workspaces, which allows you to split the service into different workspaces, which are their own RBAC domain that have their own products and such underneath
- Named Values are Secrets that can be called used throughout the configuration, and can be a link to KeyVault secrets

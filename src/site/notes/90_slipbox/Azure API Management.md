---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure API Management.md","permalink":"/slipbox-notes/azure-api-management/","tags":["notes"],"created":"2023-05-26","updated":"2025-11-27"}
---


Azure APIM is a hybrid, multicloud management platform for APIs across al environments. As a platform-as-a-service, API Management supports the complete API Lifecycle.  
It helps resolve challenges by:

- Abstracting backend architecture diversity and complexity from API consumers
- Securely expose services hosted on and outside of Azure as APIs
- Protect, accelerate, and observe APIs
- Enable API discovery and consumption by internal and external users

APIM works with [[90_slipbox/OpenAPI Specification\|OpenAPI Specification]]

Key tooling includes:

- Policy driven controls for
	- Throttling
	- Transform requests (REST to SOAP)
	- Only allow X calls in X minutes
- Access Key driven access profiles, can be revoked.
- Usage Metrics that can be sent to billing engine.

## V2

### Quick Notes

- Public Access can only be disabled when a Private endpoint is connected, and authorized.

## V1

### Quick Notes

- Internal VNET mode is only available on Dev and Premium SKU's
- API's can have a whitelist / blacklist of calling IP's on the inbound processing for each API
- The latest version of API Management lets you have workspaces, which allows you to split the service into different workspaces, which are their own RBAC domain that have their own products and such underneath
- Named Values are Secrets that can be called used throughout the configuration, and can be a link to KeyVault secrets

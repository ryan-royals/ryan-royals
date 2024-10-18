---
{"dg-publish":true,"permalink":"/40-references/readwise/security-considerations-azure-data-factory/","tags":["rw/articles"]}
---

![40 References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg](/img/user/40%20References/attachments/aed272417ab44a26e6bdcceab03aeb5f_MD5.jpg)
  
URL: https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#firewall-requirements-for-on-premisesprivate-network
Author: ssabat

## Summary

Describes basic security infrastructure that data movement services in Azure Data Factory use to help secure your data.

## Highlights added August 30, 2024 at 2:23 PM
>Domain names Outbound ports Description `*.servicebus.windows.net` 443 Required by the self-hosted integration runtime for interactive authoring. `{datafactory}.{region}.datafactory.azure.net` 
>or `*.frontend.clouddatahub.net` 443 Required by the self-hosted integration runtime to connect to the Data Factory service. 
>For new created Data Factory, please find the FQDN from your Self-hosted Integration Runtime key which is in format {datafactory}.{region}.datafactory.azure.net. For old Data factory, if you don't see the FQDN in your Self-hosted Integration key, please use *.frontend.clouddatahub.net instead. `download.microsoft.com` 443 Required by the self-hosted integration runtime for downloading the updates. If you have disabled auto-update, you can skip configuring this domain. `*.core.windows.net` 443 Used by the self-hosted integration runtime to connect to the Azure storage account when you use the [staged copy](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations/copy-activity-performance#staged-copy) feature. `*.database.windows.net` 1433 Required only when you copy from or to Azure SQL Database or Azure Synapse Analytics and optional otherwise. Use the staged-copy feature to copy data to SQL Database or Azure Synapse Analytics without opening port 1433. ([View Highlight] (https://read.readwise.io/read/01gzct54jcbms13wvgt8pwg8yb))



---
{"dg-publish":true,"permalink":"/40-references/readwise/security-considerations-azure-data-factory/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_E61EJOG.png)

## Full Document
[[40 References/readwise/Full Document Contents/Security considerations - Azure Data Factory\|Readwise/Full Document Contents/Security considerations - Azure Data Factory.md]]

## Highlights
Domain names Outbound ports Description `*.servicebus.windows.net` 443 Required by the self-hosted integration runtime for interactive authoring. `{datafactory}.{region}.datafactory.azure.net` 
or `*.frontend.clouddatahub.net` 443 Required by the self-hosted integration runtime to connect to the Data Factory service. 
For new created Data Factory, please find the FQDN from your Self-hosted Integration Runtime key which is in format {datafactory}.{region}.datafactory.azure.net. For old Data factory, if you don't see the FQDN in your Self-hosted Integration key, please use *.frontend.clouddatahub.net instead. `download.microsoft.com` 443 Required by the self-hosted integration runtime for downloading the updates. If you have disabled auto-update, you can skip configuring this domain. `*.core.windows.net` 443 Used by the self-hosted integration runtime to connect to the Azure storage account when you use the [staged copy](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations/copy-activity-performance#staged-copy) feature. `*.database.windows.net` 1433 Required only when you copy from or to Azure SQL Database or Azure Synapse Analytics and optional otherwise. Use the staged-copy feature to copy data to SQL Database or Azure Synapse Analytics without opening port 1433. ([View Highlight] (https://read.readwise.io/read/01gzct54jcbms13wvgt8pwg8yb))



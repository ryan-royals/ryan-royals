---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/differences-from-azure-data-factory-azure-synapse-analytics/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Available features in ADF & Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/data-integration/concepts-data-factory-differences#available-features-in-adf--azure-synapse-analytics)
2. [Next steps](https://learn.microsoft.com/en-us/azure/synapse-analytics/data-integration/concepts-data-factory-differences#next-steps)

In Azure Synapse Analytics, the data integration capabilities such as Synapse pipelines and data flows are based upon those of Azure Data Factory. For more information, see [what is Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/introduction).

#### Available features in ADF & Azure Synapse Analytics

Check below table for features availability:

| Category | Feature | Azure Data Factory | Azure Synapse Analytics |
| --- | --- | --- | --- |
| **Integration Runtime** | Support for Cross-region Integration Runtime (Data Flows) | ✓ | ✗ |
|  | Integration Runtime Sharing | ✓*Can be shared across different data factories* | ✗ |
| **Pipelines Activities** | Support for Power Query Activity | ✓ | ✗ |
|  | Support for global parameters | ✓ | ✗ |
| **Template Gallery and Knowledge center** | Solution Templates | ✓*Azure Data Factory Template Gallery* | ✓*Synapse Workspace Knowledge center* |
| **GIT Repository Integration** | GIT Integration | ✓ | ✓ |
| **Monitoring** | Monitoring of Spark Jobs for Data Flow | ✗ | ✓*Leverage the Synapse Spark pools* |

#### Next steps

Get started with data integration in your Synapse workspace by learning how to [ingest data into an Azure Data Lake Storage gen2 account](https://learn.microsoft.com/en-us/azure/synapse-analytics/data-integration/data-integration-data-lake).

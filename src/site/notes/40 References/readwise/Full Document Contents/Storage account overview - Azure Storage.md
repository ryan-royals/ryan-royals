---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/storage-account-overview-azure-storage/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

#### In this article

1. [Types of storage accounts](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#types-of-storage-accounts)
2. [Storage account name](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#storage-account-name)
3. [Storage account endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#storage-account-endpoints)
4. [Migrate a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#migrate-a-storage-account)
5. [Transfer data into a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#transfer-data-into-a-storage-account)
6. [Storage account encryption](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#storage-account-encryption)
7. [Storage account billing](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#storage-account-billing)
8. [Legacy storage account types](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#legacy-storage-account-types)
9. [Scalability targets for standard storage accounts](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#scalability-targets-for-standard-storage-accounts)
10. [Next steps](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#next-steps)

An Azure storage account contains all of your Azure Storage data objects, including blobs, file shares, queues, tables, and disks. The storage account provides a unique namespace for your Azure Storage data that's accessible from anywhere in the world over HTTP or HTTPS. Data in your storage account is durable and highly available, secure, and massively scalable.

To learn how to create an Azure Storage account, see [Create a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create).

#### Types of storage accounts

Azure Storage offers several types of storage accounts. Each type supports different features and has its own pricing model.

The following table describes the types of storage accounts recommended by Microsoft for most scenarios. All of these use the [Azure Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview) deployment model.

| Type of storage account | Supported storage services | Redundancy options | Usage |
| --- | --- | --- | --- |
| Standard general-purpose v2 | Blob Storage (including Data Lake Storage1), Queue Storage, Table Storage, and Azure Files | Locally redundant storage (LRS) / geo-redundant storage (GRS) / read-access geo-redundant storage (RA-GRS)Zone-redundant storage (ZRS) / geo-zone-redundant storage (GZRS) / read-access geo-zone-redundant storage (RA-GZRS)2 | Standard storage account type for blobs, file shares, queues, and tables. Recommended for most scenarios using Azure Storage. If you want support for network file system (NFS) in Azure Files, use the premium file shares account type. |
| Premium block blobs3 | Blob Storage (including Data Lake Storage1) | LRSZRS2 | Premium storage account type for block blobs and append blobs. Recommended for scenarios with high transaction rates or that use smaller objects or require consistently low storage latency. [Learn more about example workloads.](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-block-blob-premium) |
| Premium file shares3 | Azure Files | LRSZRS2 | Premium storage account type for file shares only. Recommended for enterprise or high-performance scale applications. Use this account type if you want a storage account that supports both Server Message Block (SMB) and NFS file shares. |
| Premium page blobs3 | Page blobs only | LRS | Premium storage account type for page blobs only. [Learn more about page blobs and sample use cases.](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blob-pageblob-overview) |

1 Data Lake Storage is a set of capabilities dedicated to big data analytics, built on Azure Blob Storage. For more information, see [Introduction to Data Lake Storage Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction) and [Create a storage account to use with Data Lake Storage Gen2](https://learn.microsoft.com/en-us/azure/storage/blobs/create-data-lake-storage-account).

2 ZRS, GZRS, and RA-GZRS are available only for standard general-purpose v2, premium block blobs, and premium file shares accounts in certain regions. For more information, see [Azure Storage redundancy](https://learn.microsoft.com/en-us/azure/storage/common/storage-redundancy).

3 Premium performance storage accounts use solid-state drives (SSDs) for low latency and high throughput.

Legacy storage accounts are also supported. For more information, see [Legacy storage account types](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#legacy-storage-account-types).

The service-level agreement (SLA) for Azure Storage accounts is available at [SLA for Storage Accounts](https://azure.microsoft.com/support/legal/sla/storage/v1_5/).

Note

You can't change a storage account to a different type after it's created. To move your data to a storage account of a different type, you must create a new account and copy the data to the new account.

#### Storage account name

When naming your storage account, keep these rules in mind:

* Storage account names must be between 3 and 24 characters in length and may contain numbers and lowercase letters only.
* Your storage account name must be unique within Azure. No two storage accounts can have the same name.

#### Storage account endpoints

A storage account provides a unique namespace in Azure for your data. Every object that you store in Azure Storage has a URL address that includes your unique account name. The combination of the account name and the service endpoint forms the endpoints for your storage account.

There are two types of service endpoints available for a storage account:

* [Standard endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#standard-endpoints) (recommended). You can create up to 250 storage accounts per region with standard endpoints in a given subscription.
* [Azure DNS zone endpoints](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-overview#azure-dns-zone-endpoints-preview) (preview). You can create up to 5000 storage accounts per region with Azure DNS zone endpoints in a given subscription.

Within a single subscription, you can create accounts with either standard or Azure DNS Zone endpoints, for a maximum of 5250 accounts per subscription.

Important

Azure DNS zone endpoints are currently in PREVIEW. See the [Supplemental Terms of Use for Microsoft Azure Previews](https://azure.microsoft.com/support/legal/preview-supplemental-terms/) for legal terms that apply to Azure features that are in beta, preview, or otherwise not yet released into general availability.

You can configure your storage account to use a custom domain for the Blob Storage endpoint. For more information, see [Configure a custom domain name for your Azure Storage account](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-custom-domain-name).

##### Standard endpoints

A standard service endpoint in Azure Storage includes the protocol (HTTPS is recommended), the storage account name as the subdomain, and a fixed domain that includes the name of the service.

The following table lists the format for the standard endpoints for each of the Azure Storage services.

| Storage service | Endpoint |
| --- | --- |
| Blob Storage | `https://<storage-account>.blob.core.windows.net` |
| Static website (Blob Storage) | `https://<storage-account>.web.core.windows.net` |
| Data Lake Storage Gen2 | `https://<storage-account>.dfs.core.windows.net` |
| Azure Files | `https://<storage-account>.file.core.windows.net` |
| Queue Storage | `https://<storage-account>.queue.core.windows.net` |
| Table Storage | `https://<storage-account>.table.core.windows.net` |

When your account is created with standard endpoints, you can easily construct the URL for an object in Azure Storage by appending the object's location in the storage account to the endpoint. For example, the URL for a blob will be similar to:

`https://*mystorageaccount*.blob.core.windows.net/*mycontainer*/*myblob*`

##### Azure DNS zone endpoints (preview)

When you create an Azure Storage account with Azure DNS zone endpoints (preview), Azure Storage dynamically selects an Azure DNS zone and assigns it to the storage account when it is created. The new storage account's endpoints are created in the dynamically selected Azure DNS zone. For more information about Azure DNS zones, see [DNS zones](https://learn.microsoft.com/en-us/azure/dns/dns-zones-records#dns-zones).

An Azure DNS zone service endpoint in Azure Storage includes the protocol (HTTPS is recommended), the storage account name as the subdomain, and a domain that includes the name of the service and the identifier for the DNS zone. The identifier for the DNS zone always begins with `z` and can range from `z00` to `z99`.

The following table lists the format for Azure DNS Zone endpoints for each of the Azure Storage services, where the zone is `z5`.

| Storage service | Endpoint |
| --- | --- |
| Blob Storage | `https://<storage-account>.z[00-99].blob.storage.azure.net` |
| Static website (Blob Storage) | `https://<storage-account>.z[00-99].web.storage.azure.net` |
| Data Lake Storage Gen2 | `https://<storage-account>.z[00-99].dfs.storage.azure.net` |
| Azure Files | `https://<storage-account>.z[00-99].file.storage.azure.net` |
| Queue Storage | `https://<storage-account>.z[00-99].queue.storage.azure.net` |
| Table Storage | `https://<storage-account>.z[00-99].table.storage.azure.net` |

Important

You can create up to 5000 accounts with Azure DNS Zone endpoints per subscription. However, you may need to update your application code to query for the account endpoint at runtime. You can call the [Get Properties](https://learn.microsoft.com/en-us/rest/api/storagerp/storage-accounts/get-properties) operation to query for the storage account endpoints.

Azure DNS zone endpoints are supported for accounts created with the Azure Resource Manager deployment model only. For more information, see [Azure Resource Manager overview](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/overview).

To learn how to create a storage account with Azure DNS Zone endpoints, see [Create a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create).

###### About the preview

The Azure DNS zone endpoints preview is available in all public regions. The preview is not available in any government cloud regions.

To register for the preview, follow the instructions provided in [Set up preview features in Azure subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/preview-features#register-preview-feature). Specify `PartitionedDnsPublicPreview` as the feature name and `Microsoft.Storage` as the provider namespace.

#### Migrate a storage account

The following table summarizes and points to guidance on how to move, upgrade, or migrate a storage account:

| Migration scenario | Details |
| --- | --- |
| Move a storage account to a different subscription | Azure Resource Manager provides options for moving a resource to a different subscription. For more information, see [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription). |
| Move a storage account to a different resource group | Azure Resource Manager provides options for moving a resource to a different resource group. For more information, see [Move resources to a new resource group or subscription](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/move-resource-group-and-subscription). |
| Move a storage account to a different region | To move a storage account, create a copy of your storage account in another region. Then, move your data to that account by using AzCopy, or another tool of your choice. For more information, see [Move an Azure Storage account to another region](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-move). |
| Upgrade to a general-purpose v2 storage account | You can upgrade a general-purpose v1 storage account or Blob Storage account to a general-purpose v2 account. Note that this action can’t be undone. For more information, see [Upgrade to a general-purpose v2 storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-upgrade). |
| Migrate a classic storage account to Azure Resource Manager | The Azure Resource Manager deployment model is superior to the classic deployment model in terms of functionality, scalability, and security. For more information about migrating a classic storage account to Azure Resource Manager, see the "Migration of storage accounts" section of [Platform-supported migration of IaaS resources from classic to Azure Resource Manager](https://learn.microsoft.com/en-us/azure/virtual-machines/migration-classic-resource-manager-overview#migration-of-storage-accounts). |

#### Transfer data into a storage account

Microsoft provides services and utilities for importing your data from on-premises storage devices or third-party cloud storage providers. Which solution you use depends on the quantity of data you're transferring. For more information, see [Azure Storage migration overview](https://learn.microsoft.com/en-us/azure/storage/common/storage-migration-overview).

#### Storage account encryption

All data in your storage account is automatically encrypted on the service side. For more information about encryption and key management, see [Azure Storage encryption for data at rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption).

#### Storage account billing

Azure Storage bills based on your storage account usage. All objects in a storage account are billed together as a group. Storage costs are calculated according to the following factors:

* **Region** refers to the geographical region in which your account is based.
* **Account type** refers to the type of storage account you're using.
* **Access tier** refers to the data usage pattern you’ve specified for your general-purpose v2 or Blob Storage account.
* **Capacity** refers to how much of your storage account allotment you're using to store data.
* **Redundancy** determines how many copies of your data are maintained at one time, and in what locations.
* **Transactions** refer to all read and write operations to Azure Storage.
* **Data egress** refers to any data transferred out of an Azure region. When the data in your storage account is accessed by an application that isn’t running in the same region, you're charged for data egress. For information about using resource groups to group your data and services in the same region to limit egress charges, see [What is an Azure resource group?](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/govern/resource-consistency/resource-access-management#what-is-an-azure-resource-group).

The [Azure Storage pricing page](https://azure.microsoft.com/pricing/details/storage) provides detailed pricing information based on account type, storage capacity, replication, and transactions. The [Data Transfers pricing details](https://azure.microsoft.com/pricing/details/data-transfers) provides detailed pricing information for data egress. You can use the [Azure Storage pricing calculator](https://azure.microsoft.com/pricing/calculator/?scenario=data-management) to help estimate your costs.

Azure services cost money. Azure Cost Management helps you set budgets and configure alerts to keep spending under control. Analyze, manage, and optimize your Azure costs with Cost Management. To learn more, see the [quickstart on analyzing your costs](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis?WT.mc_id=costmanagementcontent_docsacmhorizontal_-inproduct-learn).

#### Legacy storage account types

The following table describes the legacy storage account types. These account types aren’t recommended by Microsoft, but may be used in certain scenarios:

| Type of legacy storage account | Supported storage services | Redundancy options | Deployment model | Usage |
| --- | --- | --- | --- | --- |
| Standard general-purpose v1 | Blob Storage, Queue Storage, Table Storage, and Azure Files | LRS/GRS/RA-GRS | Resource Manager, classic1 | General-purpose v1 accounts may not have the latest features or the lowest per-gigabyte pricing. Consider using it for these scenarios:* Your applications require the Azure [classic deployment model](https://learn.microsoft.com/en-us/azure/azure-portal/supportability/classic-deployment-model-quota-increase-requests)1.
* Your applications are transaction-intensive or use significant geo-replication bandwidth, but don’t require large capacity. In this case, a general-purpose v1 account may be the most economical choice.
* You use a version of the Azure Storage REST API that is earlier than February 14, 2014, or a client library with a version lower than 4.x, and you can’t upgrade your application.
* You're selecting a storage account to use as a cache for Azure Site Recovery. Because Site Recovery is transaction-intensive, a general-purpose v1 account may be more cost-effective. For more information, see [Support matrix for Azure VM disaster recovery between Azure regions](https://learn.microsoft.com/en-us/azure/site-recovery/azure-to-azure-support-matrix#cache-storage).
 |
| Standard Blob Storage | Blob Storage (block blobs and append blobs only) | LRS/GRS/RA-GRS | Resource Manager | Microsoft recommends using standard general-purpose v2 accounts instead when possible. |

1 Beginning August 1, 2022, you'll no longer be able to create new storage accounts with the classic deployment model. Resources created prior to that date will continue to be supported through August 31, 2024. For more information, see [Azure classic storage accounts will be retired on 31 August 2024](https://azure.microsoft.com/updates/classic-azure-storage-accounts-will-be-retired-on-31-august-2024).

#### Scalability targets for standard storage accounts

The following table describes default limits for Azure general-purpose v2 (GPv2), general-purpose v1 (GPv1), and Blob storage accounts. The *ingress* limit refers to all data that is sent to a storage account. The *egress* limit refers to all data that is received from a storage account.

Microsoft recommends that you use a GPv2 storage account for most scenarios. You can easily upgrade a GPv1 or a Blob storage account to a GPv2 account with no downtime and without the need to copy data. For more information, see [Upgrade to a GPv2 storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-upgrade).

Note

You can request higher capacity and ingress limits. To request an increase, contact [Azure Support](https://azure.microsoft.com/support/faq/).

| Resource | Limit |
| --- | --- |
| Maximum number of storage accounts with standard endpoints per region per subscription, including standard and premium storage accounts. | 250 |
| Maximum number of storage accounts with Azure DNS zone endpoints (preview) per region per subscription, including standard and premium storage accounts. | 5000 (preview) |
| Default maximum storage account capacity | 5 PiB 1 |
| Maximum number of blob containers, blobs, file shares, tables, queues, entities, or messages per storage account. | No limit |
| Default maximum request rate per storage account | 20,000 requests per second1 |
| Default maximum ingress per general-purpose v2 and Blob storage account in the following regions (LRS/GRS):* Australia East
* Central US
* East Asia
* East US 2
* Japan East
* Korea Central
* North Europe
* South Central US
* Southeast Asia
* UK South
* West Europe
* West US
 | 60 Gbps1 |
| Default maximum ingress per general-purpose v2 and Blob storage account in the following regions (ZRS):* Australia East
* Central US
* East US
* East US 2
* Japan East
* North Europe
* South Central US
* Southeast Asia
* UK South
* West Europe
* West US 2
 | 60 Gbps1 |
| Default maximum ingress per general-purpose v2 and Blob storage account in regions that aren't listed in the previous row. | 25 Gbps1 |
| Default maximum ingress for general-purpose v1 storage accounts (all regions) | 10 Gbps1 |
| Default maximum egress for general-purpose v2 and Blob storage accounts in the following regions (LRS/GRS):* Australia East
* Central US
* East Asia
* East US 2
* Japan East
* Korea Central
* North Europe
* South Central US
* Southeast Asia
* UK South
* West Europe
* West US
 | 120 Gbps1 |
| Default maximum egress for general-purpose v2 and Blob storage accounts in the following regions (ZRS): * Australia East
* Central US
* East US
* East US 2
* Japan East
* North Europe
* South Central US
* Southeast Asia
* UK South
* West Europe
* West US 2
 | 120 Gbps1 |
| Default maximum egress for general-purpose v2 and Blob storage accounts in regions that aren't listed in the previous row. | 50 Gbps1 |
| Maximum number of IP address rules per storage account | 200 |
| Maximum number of virtual network rules per storage account | 200 |
| Maximum number of resource instance rules per storage account | 200 |
| Maximum number of private endpoints per storage account | 200 |

1 Azure Storage standard accounts support higher capacity limits and higher limits for ingress and egress by request. To request an increase in account limits, contact [Azure Support](https://azure.microsoft.com/support/faq/).

#### Next steps

* [Create a storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create)
* [Upgrade to a general-purpose v2 storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-upgrade)
* [Recover a deleted storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-recover)

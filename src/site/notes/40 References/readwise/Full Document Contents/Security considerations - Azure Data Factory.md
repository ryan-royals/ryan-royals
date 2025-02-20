---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/security-considerations-azure-data-factory/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_E61EJOG.png)

#### In this article

1. [Cloud scenarios](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#cloud-scenarios)
2. [Hybrid scenarios](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#hybrid-scenarios)
3. [Frequently asked questions](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#frequently-asked-questions)
4. [Next steps](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#next-steps)

 Select the version of Data Factory service you are using:

* [Version 1](https://learn.microsoft.com/en-us/azure/data-factory/v1/data-factory-data-movement-security-considerations)
* [Current version](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations)

**APPLIES TO:**

![](https://learn.microsoft.com/en-us/azure/data-factory/media/applies-to/yes.png)
Azure Data Factory

![](https://learn.microsoft.com/en-us/azure/data-factory/media/applies-to/yes.png)
Azure Synapse Analytics

This article describes basic security infrastructure that data movement services in Azure Data Factory use to help secure your data. Data Factory management resources are built on Azure security infrastructure and use all possible security measures offered by Azure.

In a Data Factory solution, you create one or more data [pipelines](https://learn.microsoft.com/en-us/azure/data-factory/concepts-pipelines-activities). A pipeline is a logical grouping of activities that together perform a task. These pipelines reside in the region where the data factory was created.

Even though Data Factory is only available in few regions, the data movement service is [available globally](https://learn.microsoft.com/en-us/azure/data-factory/concepts-integration-runtime#integration-runtime-location) to ensure data compliance, efficiency, and reduced network egress costs.

Azure Data Factory including Azure Integration Runtime and Self-hosted Integration Runtime does not store any temporary data, cache data or logs except for linked service credentials for cloud data stores, which are encrypted by using certificates. With Data Factory, you create data-driven workflows to orchestrate movement of data between [supported data stores](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-overview#supported-data-stores-and-formats), and processing of data by using [compute services](https://learn.microsoft.com/en-us/azure/data-factory/compute-linked-services) in other regions or in an on-premises environment. You can also monitor and manage workflows by using SDKs and Azure Monitor.

Data Factory has been certified for:

| **[CSA STAR Certification](https://www.microsoft.com/trustcenter/compliance/csa-star-certification)** |
| --- |
| **[ISO 20000-1:2011](https://www.microsoft.com/trustcenter/Compliance/ISO-20000-1)** |
| **[ISO 22301:2012](https://learn.microsoft.com/en-us/compliance/regulatory/offering-iso-22301)** |
| **[ISO 27001:2013](https://www.microsoft.com/trustcenter/compliance/iso-iec-27001)** |
| **[ISO 27017:2015](https://www.microsoft.com/trustcenter/compliance/iso-iec-27017)** |
| **[ISO 27018:2014](https://www.microsoft.com/trustcenter/compliance/iso-iec-27018)** |
| **[ISO 9001:2015](https://www.microsoft.com/trustcenter/compliance/iso-9001)** |
| **[SOC 1, 2, 3](https://www.microsoft.com/trustcenter/compliance/soc)** |
| **[HIPAA BAA](https://learn.microsoft.com/en-us/compliance/regulatory/offering-hipaa-hitech)** |
| **[HITRUST](https://learn.microsoft.com/en-us/compliance/regulatory/offering-hitrust)** |

If you're interested in Azure compliance and how Azure secures its own infrastructure, visit the [Microsoft Trust Center](https://microsoft.com/trustcenter/default.aspx). For the latest list of all Azure Compliance offerings check - <https://aka.ms/AzureCompliance>.

In this article, we review security considerations in the following two data movement scenarios:

* **Cloud scenario**: In this scenario, both your source and your destination are publicly accessible through the internet. These include managed cloud storage services such as Azure Storage, Azure Synapse Analytics, Azure SQL Database, Azure Data Lake Store, Amazon S3, Amazon Redshift, SaaS services such as Salesforce, and web protocols such as FTP and OData. Find a complete list of supported data sources in [Supported data stores and formats](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-overview#supported-data-stores-and-formats).
* **Hybrid scenario**: In this scenario, either your source or your destination is behind a firewall or inside an on-premises corporate network. Or, the data store is in a private network or virtual network (most often the source) and is not publicly accessible. Database servers hosted on virtual machines also fall under this scenario.

Note

We recommend that you use the Azure Az PowerShell module to interact with Azure. See [Install Azure PowerShell](https://learn.microsoft.com/en-us/powershell/azure/install-az-ps) to get started. To learn how to migrate to the Az PowerShell module, see [Migrate Azure PowerShell from AzureRM to Az](https://learn.microsoft.com/en-us/powershell/azure/migrate-from-azurerm-to-az).

#### Cloud scenarios

##### Securing data store credentials

* **Store encrypted credentials in an Azure Data Factory managed store**. Data Factory helps protect your data store credentials by encrypting them with certificates managed by Microsoft. These certificates are rotated every two years (which includes certificate renewal and the migration of credentials). For more information about Azure Storage security, see [Azure Storage security overview](https://learn.microsoft.com/en-us/azure/storage/blobs/security-recommendations).
* **Store credentials in Azure Key Vault**. You can also store the data store's credential in [Azure Key Vault](https://azure.microsoft.com/services/key-vault/). Data Factory retrieves the credential during the execution of an activity. For more information, see [Store credential in Azure Key Vault](https://learn.microsoft.com/en-us/azure/data-factory/store-credentials-in-key-vault).

Centralizing storage of application secrets in Azure Key Vault allows you to control their distribution. Key Vault greatly reduces the chances that secrets may be accidentally leaked. Instead of storing the connection string in the app's code, you can store it securely in Key Vault. Your applications can securely access the information they need by using URIs. These URIs allow the applications to retrieve specific versions of a secret. There's no need to write custom code to protect any of the secret information stored in Key Vault.

##### Data encryption in transit

If the cloud data store supports HTTPS or TLS, all data transfers between data movement services in Data Factory and a cloud data store are via secure channel HTTPS or TLS.

Note

All connections to Azure SQL Database and Azure Synapse Analytics require encryption (SSL/TLS) while data is in transit to and from the database. When you're authoring a pipeline by using JSON, add the encryption property and set it to **true** in the connection string. For Azure Storage, you can use **HTTPS** in the connection string.

Note

To enable encryption in transit while moving data from Oracle follow one of the below options:

1. In Oracle server, go to Oracle Advanced Security (OAS) and configure the encryption settings, which supports Triple-DES Encryption (3DES) and Advanced Encryption Standard (AES), refer [here](https://docs.oracle.com/cd/E11882_01/network.112/e40393/asointro.htm#i1008759) for details. ADF automatically negotiates the encryption method to use the one you configure in OAS when establishing connection to Oracle.
2. In ADF, you can add EncryptionMethod=1 in the connection string (in the Linked Service). This will use SSL/TLS as the encryption method. To use this, you need to disable non-SSL encryption settings in OAS on the Oracle server side to avoid encryption conflict.

Note

TLS version used is 1.2.

##### Data encryption at rest

Some data stores support encryption of data at rest. We recommend that you enable the data encryption mechanism for those data stores.

###### Azure Synapse Analytics

Transparent Data Encryption (TDE) in Azure Synapse Analytics helps protect against the threat of malicious activity by performing real-time encryption and decryption of your data at rest. This behavior is transparent to the client. For more information, see [Secure a database in Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/sql-data-warehouse-overview-manage-security).

###### Azure SQL Database

Azure SQL Database also supports transparent data encryption (TDE), which helps protect against the threat of malicious activity by performing real-time encryption and decryption of the data, without requiring changes to the application. This behavior is transparent to the client. For more information, see [Transparent data encryption for SQL Database and Data Warehouse](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption-azure-sql).

###### Azure Data Lake Store

Azure Data Lake Store also provides encryption for data stored in the account. When enabled, Data Lake Store automatically encrypts data before persisting and decrypts before retrieval, making it transparent to the client that accesses the data. For more information, see [Security in Azure Data Lake Store](https://learn.microsoft.com/en-us/azure/data-lake-store/data-lake-store-security-overview).

###### Azure Blob storage and Azure Table storage

Azure Blob storage and Azure Table storage support Storage Service Encryption (SSE), which automatically encrypts your data before persisting to storage and decrypts before retrieval. For more information, see [Azure Storage Service Encryption for Data at Rest](https://learn.microsoft.com/en-us/azure/storage/common/storage-service-encryption).

###### Amazon S3

Amazon S3 supports both client and server encryption of data at rest. For more information, see [Protecting Data Using Encryption](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingEncryption.html).

###### Amazon Redshift

Amazon Redshift supports cluster encryption for data at rest. For more information, see [Amazon Redshift Database Encryption](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-db-encryption.html).

###### Salesforce

Salesforce supports Shield Platform Encryption that allows encryption of all files, attachments, and custom fields. For more information, see [Understanding the Web Server OAuth Authentication Flow](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_understanding_web_server_oauth_flow.htm).

#### Hybrid scenarios

Hybrid scenarios require self-hosted integration runtime to be installed in an on-premises network, inside a virtual network (Azure), or inside a virtual private cloud (Amazon). The self-hosted integration runtime must be able to access the local data stores. For more information about self-hosted integration runtime, see [How to create and configure self-hosted integration runtime](https://learn.microsoft.com/en-us/azure/data-factory/create-self-hosted-integration-runtime).

![self-hosted integration runtime channels](https://learn.microsoft.com/en-us/azure/data-factory/media/data-movement-security-considerations/data-management-gateway-channels.png)
The command channel allows communication between data movement services in Data Factory and self-hosted integration runtime. The communication contains information related to the activity. The data channel is used for transferring data between on-premises data stores and cloud data stores.

##### On-premises data store credentials

The credentials can be stored within data factory or be [referenced by data factory](https://learn.microsoft.com/en-us/azure/data-factory/store-credentials-in-key-vault) during the runtime from Azure Key Vault. If storing credentials within data factory, it is always stored encrypted on the self-hosted integration runtime.

* **Store credentials locally**. If you directly use the **Set-AzDataFactoryV2LinkedService** cmdlet with the connection strings and credentials inline in the JSON, the linked service is encrypted and stored on self-hosted integration runtime. In this case the credentials flow through Azure backend service, which is extremely secure, to the self-hosted integration machine where it is finally encrypted and stored. The self-hosted integration runtime uses Windows [DPAPI](https://learn.microsoft.com/en-us/previous-versions/ms995355(v=msdn.10)) to encrypt the sensitive data and credential information.
* **Store credentials in Azure Key Vault**. You can also store the data store's credential in [Azure Key Vault](https://azure.microsoft.com/services/key-vault/). Data Factory retrieves the credential during the execution of an activity. For more information, see [Store credential in Azure Key Vault](https://learn.microsoft.com/en-us/azure/data-factory/store-credentials-in-key-vault).
* **Store credentials locally without flowing the credentials through Azure backend to the self-hosted integration runtime**. If you want to encrypt and store credentials locally on the self-hosted integration runtime without having to flow the credentials through data factory backend, follow the steps in [Encrypt credentials for on-premises data stores in Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/encrypt-credentials-self-hosted-integration-runtime). All connectors support this option. The self-hosted integration runtime uses Windows [DPAPI](https://learn.microsoft.com/en-us/previous-versions/ms995355(v=msdn.10)) to encrypt the sensitive data and credential information.
* Use the **New-AzDataFactoryV2LinkedServiceEncryptedCredential** cmdlet to encrypt linked service credentials and sensitive details in the linked service. You can then use the JSON returned (with the **EncryptedCredential** element in the connection string) to create a linked service by using the **Set-AzDataFactoryV2LinkedService** cmdlet.

###### Ports used when encrypting linked service on self-hosted integration runtime

By default, when remote access from intranet is enabled, PowerShell uses port 8060 on the machine with self-hosted integration runtime for secure communication. If necessary, this port can be changed from the Integration Runtime Configuration Manager on the Settings tab:

![Integration Runtime Configuration Manager's Settings tab](https://learn.microsoft.com/en-us/azure/data-factory/media/data-movement-security-considerations/integration-runtime-configuration-manager-settings.png)
![HTTPS port for the gateway](https://learn.microsoft.com/en-us/azure/data-factory/media/data-movement-security-considerations/https-port-for-gateway.png)
##### Encryption in transit

All data transfers are via secure channel HTTPS and TLS over TCP to prevent man-in-the-middle attacks during communication with Azure services.

You can also use [IPSec VPN](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices) or [Azure ExpressRoute](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction) to further secure the communication channel between your on-premises network and Azure.

Azure Virtual Network is a logical representation of your network in the cloud. You can connect an on-premises network to your virtual network by setting up IPSec VPN (site-to-site) or ExpressRoute (private peering).

The following table summarizes the network and self-hosted integration runtime configuration recommendations based on different combinations of source and destination locations for hybrid data movement.

| Source | Destination | Network configuration | Integration runtime setup |
| --- | --- | --- | --- |
| On-premises | Virtual machines and cloud services deployed in virtual networks | IPSec VPN (point-to-site or site-to-site) | The self-hosted integration runtime should be installed on an Azure virtual machine in the virtual network. |
| On-premises | Virtual machines and cloud services deployed in virtual networks | ExpressRoute (private peering) | The self-hosted integration runtime should be installed on an Azure virtual machine in the virtual network. |
| On-premises | Azure-based services that have a public endpoint | ExpressRoute (Microsoft peering) | The self-hosted integration runtime can be installed on-premises or on an Azure virtual machine. |

The following images show the use of self-hosted integration runtime for moving data between an on-premises database and Azure services by using ExpressRoute and IPSec VPN (with Azure Virtual Network):

###### Express Route

![Use ExpressRoute with gateway](https://learn.microsoft.com/en-us/azure/data-factory/media/data-movement-security-considerations/express-route-for-gateway.png)
###### IPSec VPN

![IPSec VPN with gateway](https://learn.microsoft.com/en-us/azure/data-factory/media/data-movement-security-considerations/ipsec-vpn-for-gateway.png)
##### Firewall configurations and allow list setting up for IP addresses

Note

You might have to manage ports or set up allow list for domains at the corporate firewall level as required by the respective data sources. This table only uses Azure SQL Database, Azure Synapse Analytics, and Azure Data Lake Store as examples.

Note

For details about data access strategies through Azure Data Factory, see [this article](https://learn.microsoft.com/en-us/azure/data-factory/data-access-strategies#data-access-strategies-through-azure-data-factory).

###### Firewall requirements for on-premises/private network

In an enterprise, a corporate firewall runs on the central router of the organization. Windows Firewall runs as a daemon on the local machine in which the self-hosted integration runtime is installed.

The following table provides outbound port and domain requirements for corporate firewalls:

| Domain names | Outbound ports | Description |
| --- | --- | --- |
| `*.servicebus.windows.net` | 443 | Required by the self-hosted integration runtime for interactive authoring. |
| `{datafactory}.{region}.datafactory.azure.net` or `*.frontend.clouddatahub.net` | 443 | Required by the self-hosted integration runtime to connect to the Data Factory service. For new created Data Factory, please find the FQDN from your Self-hosted Integration Runtime key which is in format {datafactory}.{region}.datafactory.azure.net. For old Data factory, if you don't see the FQDN in your Self-hosted Integration key, please use \*.frontend.clouddatahub.net instead. |
| `download.microsoft.com` | 443 | Required by the self-hosted integration runtime for downloading the updates. If you have disabled auto-update, you can skip configuring this domain. |
| `*.core.windows.net` | 443 | Used by the self-hosted integration runtime to connect to the Azure storage account when you use the [staged copy](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-performance#staged-copy) feature. |
| `*.database.windows.net` | 1433 | Required only when you copy from or to Azure SQL Database or Azure Synapse Analytics and optional otherwise. Use the staged-copy feature to copy data to SQL Database or Azure Synapse Analytics without opening port 1433. |
| `*.azuredatalakestore.net``login.microsoftonline.com/<tenant>/oauth2/token` | 443 | Required only when you copy from or to Azure Data Lake Store and optional otherwise. |

Note

You might have to manage ports or set up allow list for domains at the corporate firewall level as required by the respective data sources. This table only uses Azure SQL Database, Azure Synapse Analytics, and Azure Data Lake Store as examples.

The following table provides inbound port requirements for Windows Firewall:

| Inbound ports | Description |
| --- | --- |
| 8060 (TCP) | Required by the PowerShell encryption cmdlet as described in [Encrypt credentials for on-premises data stores in Azure Data Factory](https://learn.microsoft.com/en-us/azure/data-factory/encrypt-credentials-self-hosted-integration-runtime), and by the credential manager application to securely set credentials for on-premises data stores on the self-hosted integration runtime. |

![Gateway port requirements](https://learn.microsoft.com/en-us/azure/data-factory/media/data-movement-security-considerations/gateway-port-requirements.png)
###### IP configurations and allow list setting up in data stores

Some data stores in the cloud also require that you allow the IP address of the machine accessing the store. Ensure that the IP address of the self-hosted integration runtime machine is allowed or configured in the firewall appropriately.

The following cloud data stores require that you allow the IP address of the self-hosted integration runtime machine. Some of these data stores, by default, might not require allow list.

* [Azure SQL Database](https://learn.microsoft.com/en-us/azure/azure-sql/database/firewall-configure)
* [Azure Synapse Analytics](https://learn.microsoft.com/en-us/azure/synapse-analytics/sql-data-warehouse/create-data-warehouse-portal)
* [Azure Data Lake Store](https://learn.microsoft.com/en-us/azure/data-lake-store/data-lake-store-secure-data#set-ip-address-range-for-data-access)
* [Azure Cosmos DB](https://learn.microsoft.com/en-us/azure/cosmos-db/how-to-configure-firewall)
* [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/rs-gsg-authorize-cluster-access.html)

#### Frequently asked questions

**Can the self-hosted integration runtime be shared across different data factories?**

Yes. More details [here](https://azure.microsoft.com/blog/sharing-a-self-hosted-integration-runtime-infrastructure-with-multiple-data-factories/).

**What are the port requirements for the self-hosted integration runtime to work?**

The self-hosted integration runtime makes HTTP-based connections to access the internet. The outbound ports 443 must be opened for the self-hosted integration runtime to make this connection. Open inbound port 8060 only at the machine level (not the corporate firewall level) for credential manager application. If Azure SQL Database or Azure Synapse Analytics is used as the source or the destination, you need to open port 1433 as well. For more information, see the [Firewall configurations and allow list setting up for IP addresses](https://learn.microsoft.com/en-us/azure/data-factory/data-movement-security-considerations#firewall-configurations-and-allow-list-setting-up-for-ip-addresses) section.

#### Next steps

For information about Azure Data Factory Copy Activity performance, see [Copy Activity performance and tuning guide](https://learn.microsoft.com/en-us/azure/data-factory/copy-activity-performance).

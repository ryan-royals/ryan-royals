---
{"dg-publish":true,"permalink":"/40-references/readwise/configure-azure-storage-firewalls-and-virtual-networks/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

## Summary

Configure layered network security for your storage account by using the Azure Storage firewall.

## Highlights

To restrict access to Azure services deployed in the same region as the storage account. Services deployed in the same region as the storage account use private Azure IP addresses for communication. So, you can't restrict access to specific Azure services based on their public outbound IP address range. ([View Highlight] (https://read.readwise.io/read/01hmaa9ez7ets2ntrnzt51v9kk))


[](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#trusted-access-for-resources-registered-in-your-microsoft-entra-tenant)Trusted access for resources registered in your Microsoft Entra tenant
Resources of some services can access your storage account for selected operations, such as writing logs or running backups. Those services must be registered in a subscription that is located in the same Microsoft Entra tenant as your storage account. The following table describes each service and the allowed operations.
Expand table
Service
Resource provider name
Allowed operations
Azure Backup
`Microsoft.RecoveryServices`
Run backups and restores of unmanaged disks in infrastructure as a service (IaaS) virtual machines (not required for managed disks). [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../backup/backup-overview).
Azure Data Box
`Microsoft.DataBox`
Import data to Azure. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../databox/data-box-overview).
Azure DevTest Labs
`Microsoft.DevTestLab`
Create custom images and install artifacts. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../devtest-labs/devtest-lab-overview).
Azure Event Grid
`Microsoft.EventGrid`
Enable [Azure Blob Storage event publishing](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../event-grid/concepts#event-sources) and allow [publishing to storage queues](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../event-grid/event-handlers).
Azure Event Hubs
`Microsoft.EventHub`
Archive data by using Event Hubs Capture. [Learn More](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../event-hubs/event-hubs-capture-overview).
Azure File Sync
`Microsoft.StorageSync`
Transform your on-premises file server to a cache for Azure file shares. This capability allows multiple-site sync, fast disaster recovery, and cloud-side backup. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../file-sync/file-sync-planning).
Azure HDInsight
`Microsoft.HDInsight`
Provision the initial contents of the default file system for a new HDInsight cluster. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../hdinsight/hdinsight-hadoop-use-blob-storage).
Azure Import/Export
`Microsoft.ImportExport`
Import data to Azure Storage or export data from Azure Storage. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../import-export/storage-import-export-service).
Azure Monitor
`Microsoft.Insights`
Write monitoring data to a secured storage account, including resource logs, Microsoft Entra sign-in and audit logs, and Microsoft Intune logs. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../azure-monitor/roles-permissions-security).
Azure networking services
`Microsoft.Network`
Store and analyze network traffic logs, including through the Azure Network Watcher and Azure Traffic Manager services. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../network-watcher/network-watcher-nsg-flow-logging-overview).
Azure Site Recovery
`Microsoft.SiteRecovery`
Enable replication for disaster recovery of Azure IaaS virtual machines when you're using firewall-enabled cache, source, or target storage accounts. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../site-recovery/azure-to-azure-tutorial-enable-replication).
[](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal#trusted-access-based-on-a-managed-identity)Trusted access based on a managed identity
The following table lists services that can access your storage account data if the resource instances of those services have the appropriate permission.
Expand table
Service
Resource provider name
Purpose
Azure FarmBeats
`Microsoft.AgFoodPlatform/farmBeats`
Enables access to storage accounts.
Azure API Management
`Microsoft.ApiManagement/service`
Enables access to storage accounts behind firewalls via policies. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../api-management/authentication-managed-identity-policy#use-managed-identity-in-send-request-policy).
Microsoft Autonomous Systems
`Microsoft.AutonomousSystems/workspaces`
Enables access to storage accounts.
Azure Cache for Redis
`Microsoft.Cache/Redis`
Enables access to storage accounts. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../azure-cache-for-redis/cache-managed-identity).
Azure AI Search
`Microsoft.Search/searchServices`
Enables access to storage accounts for indexing, processing, and querying.
Azure AI services
`Microsoft.CognitiveService/accounts`
Enables access to storage accounts. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../cognitive-services/cognitive-services-virtual-networks).
Azure Container Registry
`Microsoft.ContainerRegistry/registries`
Through the ACR Tasks suite of features, enables access to storage accounts when you're building container images.
Microsoft Cost Management
`Microsoft.CostManagementExports`
Enables export to storage accounts behind a firewall. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../cost-management-billing/costs/tutorial-export-acm-data).
Azure Databricks
`Microsoft.Databricks/accessConnectors`
Enables access to storage accounts.
Azure Data Factory
`Microsoft.DataFactory/factories`
Enables access to storage accounts through the Data Factory runtime.
Azure Backup Vault
`Microsoft.DataProtection/BackupVaults`
Enables access to storage accounts.
Azure Data Share
`Microsoft.DataShare/accounts`
Enables access to storage accounts.
Azure Database for PostgreSQL
`Microsoft.DBForPostgreSQL`
Enables access to storage accounts.
Azure IoT Hub
`Microsoft.Devices/IotHubs`
Allows data from an IoT hub to be written to Blob Storage. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../iot-hub/virtual-network-support#egress-connectivity-from-iot-hub-to-other-azure-resources).
Azure DevTest Labs
`Microsoft.DevTestLab/labs`
Enables access to storage accounts.
Azure Event Grid
`Microsoft.EventGrid/domains`
Enables access to storage accounts.
Azure Event Grid
`Microsoft.EventGrid/partnerTopics`
Enables access to storage accounts.
Azure Event Grid
`Microsoft.EventGrid/systemTopics`
Enables access to storage accounts.
Azure Event Grid
`Microsoft.EventGrid/topics`
Enables access to storage accounts.
Microsoft Fabric
`Microsoft.Fabric`
Enables access to storage accounts.
Azure Healthcare APIs
`Microsoft.HealthcareApis/services`
Enables access to storage accounts.
Azure Healthcare APIs
`Microsoft.HealthcareApis/workspaces`
Enables access to storage accounts.
Azure IoT Central
`Microsoft.IoTCentral/IoTApps`
Enables access to storage accounts.
Azure Key Vault Managed HSM
`Microsoft.keyvault/managedHSMs`
Enables access to storage accounts.
Azure Logic Apps
`Microsoft.Logic/integrationAccounts`
Enables logic apps to access storage accounts. [Learn more](https://learn.microsoft.com/en-us/azure/storage/common/storage-network-security?tabs=azure-portal/../../logic-apps/create-managed-service-identity#authenticate-access-with-managed-identity).
Azure Logic Apps
`Microsoft.Logic/workflows`
Enables logic apps to access storage ([View Highlight] (https://read.readwise.io/read/01j4r6rwhmcbbm49g804a87r3j))



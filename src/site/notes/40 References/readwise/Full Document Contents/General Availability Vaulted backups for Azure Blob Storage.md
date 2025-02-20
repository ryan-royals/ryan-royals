---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/general-availability-vaulted-backups-for-azure-blob-storage/","tags":["rw/articles"]}
---

![rw-book-cover](https://techcommunity.microsoft.com/favicon.ico)

We are excited to announce the general availability of vaulted backups for Azure Blob Storage. Vaulted backups can help you achieve complete protection for your blobs data against data loss. We encourage you to consider adding vaulted backup protection to your Azure Blob Storage data protection strategy.

Vaulted backup for Azure Blob Storage is a native, fully-managed backup solution from Azure Backup. It enables comprehensive protection of your blob storage data against data loss scenarios by storing a dedicated backup copy of the data in an Azure . These backups can be used to recover data in the event of any data loss on production systems. Vaulted backups, used in conjunction with other data protection capabilities (for example: soft delete, versioning and operational backups), provide multilayer protection against data loss. Vaulted backups can be configured together or separately from [operational backups](https://learn.microsoft.com/en-us/azure/backup/blob-backup-configure-manage?tabs=operational-backup).

![thumbnail image 1 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							General Availability: Vaulted backups for Azure Blob Storage
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/605488iD8881005D7E0047B/image-dimensions/578x339?v=v2)thumbnail image 1 of blog post titled General Availability: Vaulted backups for Azure Blob Storage 
Protecting your data against loss or corruption has become even more important with the increased frequency and sophistication of cyberattacks. Azure Blob Storage offers several data protection capabilities within the same storage account such as resource locks, soft delete, versioning, and point-in- time restore. However, these capabilities alone might not comprehensively protect from events such as accidental or malicious storage account deletion. Vaulted backups provide an additional, complementary protection layer against these events.

#### Example use cases

Here are a few of the common scenarios where vaulted backups can help you.

**Scenario 1: Better protection against ransomware attacks**

In a ransomware attack, backups enable organizations to recover their data without succumbing to ransom demands. Vaulted backups, independent of the primary storage account's status or availability, ensure that you can reliably recover your data. There are several ways that vaulted backups can help protect you in such scenarios. First, all vaulted backup data is isolated from the production storage accounts and stored in a separate tenant that is managed by Microsoft. The only way to manage this data is through the Backup with its own separate permissions, allowing for the separation of responsibilities. Second, for additional protection, vaulted backups allow you to leverage advanced security capabilities provided by Azure Backup, such as immutable vaults, multiuser authorization and soft delete, which can help you make sure that your data is protected and recoverable when it’s needed. Third, Azure Backup also allows you to better manage and govern the security of your backups with the business continuity and disaster recovery (BCDR) security posture. This helps ensure that backups have the right level of security (refer to the image below).

![thumbnail image 2 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							General Availability: Vaulted backups for Azure Blob Storage
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/605489i9164D58540F3BAE8/image-dimensions/600x393?v=v2)thumbnail image 2 of blog post titled General Availability: Vaulted backups for Azure Blob Storage 
**Scenario 2: Accidental or malicious storage account deletion**

Mistakes are made, insider threats exist, and credentials can be stolen. All of these can lead to storage accounts being deleted. Thankfully, with vaulted backups, your backups are stored securely in storage managed by Microsoft. So, an additional copy of your data exists outside of your storage account. This additional copy can help recover in cases where the entire storage account is deleted accidentally or maliciously. Vaulted backups allow you to recover all blobs or a subset of blobs in a storage account (refer to the image below). You can also leverage advanced security capabilities such as immutability, multiuser authorization, and soft delete. When used together, these capabilities add multi-layered protection against accidental and malicious data loss and ensure your backups are there when you need them.

![thumbnail image 3 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							General Availability: Vaulted backups for Azure Blob Storage
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/605490i1E600BB926D2904B/image-dimensions/475x449?v=v2)thumbnail image 3 of blog post titled General Availability: Vaulted backups for Azure Blob Storage 
**Scenario 3: Regulatory Compliance**

In some industries, regulations require offsite backups and/or long-term retention of data. The backup vault can help create an offsite backup that will be in the same Azure region as the primary storage account and can optionally be replicated to another region. With vaulted backups, data can be retained for up to 10 years which allows for audits, legal holds, and compliance retention. Azure Business Continuity Center makes it easy to manage and govern backups of your blob data across your estate (refer to the image below).

![thumbnail image 4 of blog post titled 
	
	
	 
	
	
	
				
		
			
				
						
							General Availability: Vaulted backups for Azure Blob Storage
							
						
					
			
		
	
			
	
	
	
	
	
](https://techcommunity.microsoft.com/t5/image/serverpage/image-id/605491i6AE9849312A716BF/image-dimensions/521x348?v=v2)thumbnail image 4 of blog post titled General Availability: Vaulted backups for Azure Blob Storage 
#### Pricing and availability

Vaulted backup for Azure Blob is available in [these](https://learn.microsoft.com/azure/backup/blob-backup-support-matrix?tabs=vaulted-backup#supported-regions) regions. To learn about pricing, refer to the [Azure Blob backup pricing page](https://azure.microsoft.com/pricing/details/backup/). Consistent with the billing experience we had in public preview, the Azure Backup protected instance fee and the vault backup storage fees are not currently charged. We will enable these charges starting in October 2024. Now is a great time to give vaulted backups a try!

#### Getting started

Here are three simple steps to help you get started with configuring vaulted backup for Azure blob storage:

1. **Create a backup vault:** A vault is a management entity that stores backups and allows you to access and manage them.

2. **Create a backup policy:** Backup policy enables you to configure the frequency and retention of backups based on your business requirements.

3. **Select the storage account and containers to backup:** You can choose to back up all containers or select specific containers depending on the criticality of the data they contain.

To learn more about vaulted backup for blobs, refer to [this article](https://learn.microsoft.com/azure/backup/blob-backup-overview?tabs=vaulted-backup).

#### Contact us

If you have questions or feedback, please reach out to us at [AskAzureBackupTeam@microsoft.com](mailto:AskAzureBackupTeam@microsoft.com).

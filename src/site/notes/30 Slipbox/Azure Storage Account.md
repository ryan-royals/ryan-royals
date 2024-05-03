---
{"dg-publish":true,"dg-path":"Azure Storage Account.md","permalink":"/azure-storage-account/","tags":["notes"]}
---


## Azure Storage Account

### Overview

Used in Azure to container Data objects, including blobs, file shares, queues, tables, and disks.  
Accessible via Http or Https.

Is the base layer for several services:

- [[Azure Files\|Azure Files]]
- [[Azure Storage Queues\|Azure Storage Queues]]
- [[Azure Storage Tables\|Azure Storage Tables]]
- [[Azure Static Website\|Azure Static Website]]
- [[30 Slipbox/Azure Data Lake Storage Gen2\|Azure Data Lake Storage Gen2]]

### Naming

- Must be between 3-24 characters, alphanumeric, and globally unique.

### Types of Storage Accounts

**Standard General Purpose V2**  
Used for Blob storage, Queues, Tables and Files

**Premium Block Blobs**  
Used for blob storage for block blobs and append blobs. Recommended for high transaction rates and / or low latency.

**Premium File Shares**  
Used for [[Server Message Blob\|SMB]] and [[Network File Share\|NFS]] file shares.

**Premium Page Blobs**  
Used specifically for page blobs

### SFTP

- Requires account type Premium Block Blob.
- Cost ~$0.50 an hour.
- Requires [[30 Slipbox/Hierarchical namespace\|Hierarchical namespace]] to be enabled. ([[30 Slipbox/Azure Data Lake Storage Gen2\|Azure Data Lake Storage Gen2]])

### Troubleshooting

[[30 Slipbox/NFS Deployment Failed\|NFS Deployment Failed]]

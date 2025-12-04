---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Storage Account.md","permalink":"/slipbox-notes/azure-storage-account/","tags":["notes"],"created":"2023-05-05","updated":"2025-11-27"}
---


Used in Azure to container Data objects, including blobs, file shares, queues, tables, and disks.  
Accessible via Http or Https.

Is the base layer for several services:

- Azure Files
- Azure Storage Queues
- Azure Storage Tables
- Azure Storage Blob
- Azure Static Website
- [[90_slipbox/Azure Data Lake Storage Gen2\|Azure Data Lake Storage Gen2]]

## Naming

- Must be between 3-24 characters, alphanumeric, and globally unique.

## Types of Storage Accounts

**Standard General Purpose V2**  
Used for Blob storage, Queues, Tables and Files

**Premium Block Blobs**  
Used for blob storage for block blobs and append blobs. Recommended for high transaction rates and / or low latency.

**Premium File Shares**  
Used for Server Message Blob (SMB) and Network File Share ( NFS) file shares.

**Premium Page Blobs**  
Used specifically for page blobs

## SFTP

- Requires account type Premium Block Blob.
- Cost ~$0.50 an hour.
- Requires Hierarchical namespace to be enabled. ([[90_slipbox/Azure Data Lake Storage Gen2\|Azure Data Lake Storage Gen2]])
    - A Hierarchical namespace is effectively what is expected from a standard file system, where files and folders can be nested over and over.

## Troubleshooting

### NFS Deployment Failed

When toggling the `nfsv3_enabled` parameter in Terraform, confirm that:

- **is_hns_enabled:** `true`
- **account_replication_type:** `LRS` or `RAGRS`  
  *and*
- **account_tier:** `Standard`
- **account_kind:** `StorageV2`  
  *or*
- **account_tier:** `Premium`
- **account_kind:** `BlockBlobStorage`

If those settings are not correct, Storage account will not deploy correct. This could surface as the Storage Account taking hours to appear in the Portal, and being in a half deployed state.

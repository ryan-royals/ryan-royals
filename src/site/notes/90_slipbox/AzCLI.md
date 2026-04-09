---
{"dg-publish":true,"permalink":"/90-slipbox/az-cli/","tags":["notes"],"created":"2025-06-11T10:28:47.646+09:30","updated":"2026-03-03T09:55:32.443+10:30","dg-note-properties":{"created":"2023-06-14","modified":"2026-03-03","tags":"notes","related":["[[Azure]]"],"references":null}}
---


## Common Commands

### Login without a sub

```shell
az login --allow-no-subscriptions
```

### Logout of All Contexts

```bash
az logout
az account clear
```

### Log into Specific Tenant

```bash
az login --tenant $tenant
```

### Show All Subscriptions

```bash
az account list
```

### Print All Policies at All Management Groups to File

```bash
az account management-group list --query "[].{id:id,name:name}" -o tsv | while read -r mgid name; do 
	az policy assignment list --scope "$mgid" >> $name
done
```

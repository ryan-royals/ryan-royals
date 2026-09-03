---
{"dg-publish":true,"permalink":"/90-slipbox/az-cli/","tags":["notes"],"created":"2025-06-11T10:28:47.646+09:30","updated":"2026-06-11T09:30:38.377+09:30","dg-note-properties":{"created":"2023-06-14","modified":"2026-06-11","references":null,"related":["[[Azure]]"],"tags":"notes"}}
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

---
{"dg-publish":true,"dg-path":"Slipbox Notes/AzCLI.md","permalink":"/slipbox-notes/az-cli/","tags":["notes"],"created":"2023-06-14","updated":"2025-11-28"}
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

---
{"dg-publish":true,"dg-path":"AzCLI.md","permalink":"/az-cli/","tags":["#notes","notes"]}
---

### Common Commands

#### Login without a sub

```shell
az login --allow-no-subscriptions
```

#### Logout of All Contexts

```bash
az logout
az account clear
```

#### Log into Specific Tenant

```bash
az login --tenant $tenant
```

#### Show All Subscriptions

```bash
az account list
```

#### Print all policies at all management groups to file
```bash
az account management-group list --query "[].{id:id,name:name}" -o tsv | while read -r mgid name; do 
	az policy assignment list --scope "$mgid" >> $name
done
```
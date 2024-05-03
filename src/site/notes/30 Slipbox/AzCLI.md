---
{"dg-publish":true,"dg-path":"AzCLI.md","permalink":"/az-cli/","tags":["#software","notes"]}
---


## AzCLI

### Overview

Multi Platform Tool used to Manage Azure

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

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/apim-landing-zone-acceleratorreference-implementations-app-gw-iapim-functerraform-at-main-azureapim-landing-zone-accelerator/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/40a93c69f3ac17551c53f88a6a7e3af39a01ee58e1c994559bb285dcad1c137b/Azure/apim-landing-zone-accelerator)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Azure/apim-landing-zone-accelerator/tree/main?resume=1) 

#### [README.md](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#readme)

### API Management - Terraform Implementation Guide

#### Table of Contents

* [Overview](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#overview)
	+ [Folder Structure](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#folder-structure)
		- [Deployment Files](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#deployment-files)
		- [Modules](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#modules)
	+ [Naming convention](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#naming-convention)
* [🚀 Getting started](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#-rocket--getting-started)
	+ [Setting up your environment](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#setting-up-your-environment)
		- [Configure Terraform](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#configure-terraform)
		- [Configure Remote Storage Account](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#configure-remote-storage-account)
	+ [Deploy the API Management Landing Zone](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#deploy-the-api-management-landing-zone)
		- [Configure Terraform Remote State](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#configure-terraform-remote-state)
		- [Provide Parameters Required for Deployment](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#provide-parameters-required-for-deployment)
		- [Deploy](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#deploy)

#### Pre-requisites

1. [Terraform](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#configure-terraform)
2. [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
3. Azure Subscription

#### Overview

##### Folder Structure

```
.
└──reference-implementations/AppGW-IAPIM-Func/terraform
    ├── modules
    │   ├── backend
    │   ├── shared
    │   ├── networking
    │   ├── apim
    │   └── gateway
    ├── provider.tf
    ├── main.tf
    ├── variables.tf
    └── outputs.tf

```

###### Deployment Files

* [`module.md`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/module.md) - Terraform implementation summary document generated via [pre-commit hooks](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/.pre-commit-config.yaml).
* [`main.tf`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/main.tf) - Main deployment file, specifies module references, dependency chains, and manages input arguments.
* [`provider.tf`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/provider.tf) - Configure remote backend state storage and required provider versions.
* [`variables.tf`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/variables.tf) - Input variable declarations with descriptions.

###### Modules

Each module has a `module.md` document that aims to give a quick overview of the module arguments, and terraform resources that are being leveraged when the module is being deployed. This document is automatically generated based upon the configuration found in the `*.tf` files in the module directory.

* [`apim`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/apim/module.md) - Deploys API Management and monitoring resources, as well as the resource group
* [`backend`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/backend/module.md) - Deploys the backend resources for the application (Function, Storage Account, App Service Plan)
* [`gateway`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/gateway/module.md) - Deploys the application gateway with its associated dependencies.
* [`networking`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/networking/module.md) - Deploys networking configuration for the APIM deployment.
* [`service-suffix`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/service-suffix/module.md) - Constructs suffix to support naming standards (see [Naming Convention](https://github.com/Azure/apim-landing-zone-accelerator/tree/main/reference-implementations/AppGW-IAPIM-Func/terraform#naming-convention))
* [`shared`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/shared/module.md) - Deploys Private DNS with a Windows VM

##### Naming convention

This project leverages the [`service-suffix`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/modules/service-suffix) module to standardize and construct the `resource_suffix` to enforce naming standards across deployments.

`resource_suffix` is constructed based on terraform input variables as follows:

```
resource_suffix = ${workloadName}-${environment}-${location}-${resource_suffix}
```

Examples:

```
ResourceGroupName = rg-${module}-${resource_suffix} [e.g. rg-shared-apidemo-dev-eastus-001]
APIMName = apim-${resource_suffix} [e.g. apim-apidemo-dev-eastus-001]
AppInsightsName = appi-${resource_suffix} [e.g. appi-apidemo-dev-eastus-001]
```

#### 🚀 Getting started

##### Setting up your environment

###### Configure Terraform

If you haven't already done so, configure Terraform using one of the following options:

* [Configure Terraform in Azure Cloud Shell with Bash](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-cloud-shell-bash)
* [Configure Terraform in Azure Cloud Shell with PowerShell](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-cloud-shell-powershell)
* [Configure Terraform in Windows with Bash](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-windows-bash)
* [Configure Terraform in Windows with PowerShell](https://learn.microsoft.com/en-us/azure/developer/terraform/get-started-windows-powershell)

###### Configure Remote Storage Account

Before you use Azure Storage as a backend, you must create a storage account. Run the following commands or configuration to create an Azure storage account and container:

Powershell

```
$RESOURCE_GROUP_NAME='tfstate'
$STORAGE_ACCOUNT_NAME="tfstate$(Get-Random)"
$CONTAINER_NAME='tfstate'

# Create resource group
New-AzResourceGroup -Name $RESOURCE_GROUP_NAME -Location eastus

# Create storage account
$storageAccount = New-AzStorageAccount -ResourceGroupName $RESOURCE_GROUP_NAME -Name $STORAGE_ACCOUNT_NAME -SkuName Standard_LRS -Location eastus -AllowBlobPublicAccess $true

# Create blob container
New-AzStorageContainer -Name $CONTAINER_NAME -Context $storageAccount.context -Permission blob
```

Alternatively, the [Terraform Dependencies](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/.github/workflows/terraform-dependencies.yml) actions workflow can provision the Terraform remote state storage account and container. Customize the deployment through setting the following GITHUB\_SECRETS for your own repository's action workflows:

* `AZURE_TF_STATE_RESOURCE_GROUP_NAME` - Name of the Resource Group to create to store the Terraform remote state backend resources within.
* `AZURE_TF_STATE_STORAGE_ACCOUNT_NAME` - Name of the Storage Account for the Terraform remote state.
* `AZURE_TF_STATE_STORAGE_CONTAINER_NAME` - Name of the Storage Account Container to store the Terraform state files.

For additional reading around remote state:

* [MS Doc: Store Terraform state in Azure Storage](https://learn.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage?tabs=azure-cli)
* [TF Doc: AzureRM Provider Configuration Documentation](https://www.terraform.io/language/settings/backends/azurerm)
* [GitHub Doc: GitHub Actions Secrets](https://learn.github.com/en/github-ae@latest/rest/actions/secrets)

##### Deploy the API Management Landing Zone

###### Configure Terraform Remote State

To configure your Terraform deployment to use the newly provisioned storage account and container, edit the [`./provider.tf`](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/provider.tf) file at lines 3-7 as below:

```
  backend "azurerm" {
    storage_account_name = "apimlztfbackend "
    container_name       = "terraform-state"
    key                  = "terraform.tfstate"
  }
```

* `storage_account_name`: Name of the Azure Storage Account to be used to hold remote state.
* `container_name`: Name of the Azure Storage Account Blob Container to store and retrieve remote state.
* `key`: Path and filename for the remote state file to be placed in the Storage Account Container. If the state file does not exist in this path, Terraform will automatically generate one for you.

###### Provide Parameters Required for Deployment

As you configured the backend remote state with your live Azure infrastructure resource values, you must also provide them for your deployment.

1. Review the available variables with their descriptions and default values in the [variables.tf](https://github.com/Azure/apim-landing-zone-accelerator/blob/main/reference-implementations/AppGW-IAPIM-Func/terraform/variables.tf) file.
2. Provide any custom values to the defined variables by creating a `terraform.tfvars` file in this directory (`reference-implementations/AppGW-IAPIM-Func/terraform/terraform.tfvars`)
	* [TF Docs: Variable Definitions (.tfvars) Files](https://www.terraform.io/language/values/variables#variable-definitions-tfvars-files)

###### Deploy

1. Navigate to the Terraform directory `reference-implementations/AppGW-IAPIM-Func/terraform`
2. Initialize Terraform to install `required_providers` specified within the `backend.tf` and to initialize the backend remote state

	* to run locally without the remote state, comment out the `backend "azurerm"` block in `backend.tf` (lines 8-13)
```
terraform init
```
3. See the planned Terraform deployment and verify resource values

 
```
terraform plan
```
4. Deploy

 
```
terraform apply
```

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/git-hub-dpantaz-az-naming-tool-tf/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/38fdc781a2cbd00c61db42b2986f30b7816c78228be65cf50148e20820a5a7e8/dpantaz/AzNamingTool-TF)

### dpantaz/AzNamingTool-TF

### AzNamingTool-TF

This repo can help you quickly deploy the Azure Naming Tool on an Azure Web App running on a linux Docker container using Terraform.

#### Instructions

Download the repo files, create a new `terraform.tfvars` file under the root directory of the repo and paste the following lines:

```
app_service_name      = ""
app_service_plan_name = ""
location              = ""
resource_group_name   = ""
storage_account_name  = ""
acr_name              = ""
managed_identity_name = ""

```

The above variables are used for the deployment of the Azure resources that will host the Azure Naming tool web application. Make sure that you provide your own values to these variables.

Login to your Azure subscription using Azure CLI.

`az login`

Deploy the Azure infrastructure using the typical Terraform flow.

```
terraform init
terraform plan
terraform apply
```

Keep a note of the hostname, you will use it later to access the application

[![image](https://user-images.githubusercontent.com/43405869/236496978-adfa28b9-505f-40b7-8b53-6bb2d2779710.png)](https://user-images.githubusercontent.com/43405869/236496978-adfa28b9-505f-40b7-8b53-6bb2d2779710.png)
Download/clone the [CloudAdoptionFramework](https://github.com/microsoft/CloudAdoptionFramework) repo on your machine.

CD to the following path under the repo folder:

`.\CloudAdoptionFramework-master\CloudAdoptionFramework-master\ready\AzNamingTool`

Run the following command to build the docker image:

`docker build -t azurenamingtool .`

Login to the Azure Container Registry (provide the name of the Azure Container Registry as specified in the terraform.tfvars file (acr\_name variable) ):

`az acr login -n <the_name_of_your_acr>`

Publish the docker image to the Azure Container Registry that was created by Terraform using the following command (provide the name of the Azure Container Registry as specified in the terraform.tfvars file):

```
docker tag azurenamingtool:latest <the_name_of_your_acr>.azurecr.io/tools/azurenamingtool
docker push <the_name_of_your_acr>.azurecr.io/tools/azurenamingtool
```

Your app should be available in a couple of minutes at the hostname that you recorded earlier.

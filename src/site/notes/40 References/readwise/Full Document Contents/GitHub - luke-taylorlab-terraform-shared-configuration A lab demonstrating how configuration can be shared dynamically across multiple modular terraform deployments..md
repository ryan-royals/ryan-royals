---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/git-hub-luke-taylorlab-terraform-shared-configuration-a-lab-demonstrating-how-configuration-can-be-shared-dynamically-across-multiple-modular-terraform-deployments/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/6fcd6b60e75ab310d661916a644b0aac0531cf12d3609f49feedb5187df5a37b/luke-taylor/lab-terraform-shared-configuration)

### luke-taylor/lab-terraform-shared-configuration

### Dynamically Sharing Configuration Across Multiple Terraform Deployments

In the realm of large enterprises, employing a monolithic Terraform setup becomes impractical. Dividing the infrastructure deployments into separate components not only reduces code complexity but also confines the blast radius of any change, as each component resides in its distinct Terraform state file. However, this segmentation introduces a new challenge: how can dependent configurations be dynamically shared among these deployments? Unlike in a monolithic deployment where resource attributes facilitate information exchange and dependency graph construction, this capability is lost when deployments are separated. This repository serves as a demonstration of effectively sharing configuration across different Terraform deployments.

#### Table of Contents

1. [Scenario](https://github.com/luke-taylor/terraform-shared-configuration#scenario)
	* [The Architecture](https://github.com/luke-taylor/terraform-shared-configuration#the-architecture)
	* [The Code](https://github.com/luke-taylor/terraform-shared-configuration#the-code)
	* [The Goal](https://github.com/luke-taylor/terraform-shared-configuration#the-goal)
2. [High Level Solution Design](https://github.com/luke-taylor/terraform-shared-configuration#high-level-solution-design)
3. [Design Decisions](https://github.com/luke-taylor/terraform-shared-configuration#design-decisions)
	* [Azure App Configuration Store](https://github.com/luke-taylor/terraform-shared-configuration#azure-app-configuration-store)
	* [Why Not Use The `terraform_remote_state` Data Source?](https://github.com/luke-taylor/terraform-shared-configuration#why-not-use-the-terraform_remote_state-data-source)
	* [Separate Terraform Deployments](https://github.com/luke-taylor/terraform-shared-configuration#separate-terraform-deployments)
4. [Deployment Instructions](https://github.com/luke-taylor/terraform-shared-configuration#deployment-instructions)
	* [Prerequisite Tooling](https://github.com/luke-taylor/terraform-shared-configuration#prerequisite-tooling)
	* [Automated Script](https://github.com/luke-taylor/terraform-shared-configuration#automated-script)
	* [Pre-deployment](https://github.com/luke-taylor/terraform-shared-configuration#pre-deployment)
	* [Hub Deployment](https://github.com/luke-taylor/terraform-shared-configuration#hub-deployment)
	* [Spoke Deployment - Identity](https://github.com/luke-taylor/terraform-shared-configuration#spoke-deployment-identity)
	* [Spoke Deployment - Landing Zone](https://github.com/luke-taylor/terraform-shared-configuration#spoke-deployment-landing-zone)
	* [Post-deployment](https://github.com/luke-taylor/terraform-shared-configuration#post-deployment)
5. [Clean Up](https://github.com/luke-taylor/terraform-shared-configuration#clean-up)

#### Scenario

##### The Architecture

The scenario we aim to address involves a standard hub-and-spoke architecture. In this setup, the *hub* represents a centralized virtual network housing shared services like firewalls, Azure Bastion jumpboxes, and gateways to on-premises infrastructure. Conversely, the *spokes* are isolated virtual networks peered back to the hub, typically hosting application workloads. This architecture, a common pattern in Azure, is extensively documented in the [Azure Architecture Center](https://docs.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/hub-spoke). While our specific case involves a hub and two spokes, the solution should seamlessly scale to accommodate any number of spokes.

>  **Note:**  
>  In the diagram below, the *Identity* virtual network functions as a spoke, peered to the hub. Though it typically wouldn't host workloads, it's utilized for other shared services such as Domain Controllers and DNS.
> 
>  

##### The Code

From an Infrastructure as Code (IaC) perspective, our objective is to deploy the hub and spoke architecture modularly. Each hub and spoke should be deployed separately using Terraform, resulting in three distinct state files.

##### The Goal

Our aim is to dynamically share the hub virtual network's resource ID with the spoke deployments, enabling them to peer with the hub without resorting to hardcoding the hub virtual network resource ID in the spoke deployments.

#### High Level Solution Design

[![Diagram](https://github.com/luke-taylor/lab-terraform-shared-configuration/raw/main/.images/diagram.png)](https://github.com/luke-taylor/lab-terraform-shared-configuration/blob/main/.images/diagram.png)
As depicted, our solution leverages an Azure first-party service called App Configuration Store to serve as our central lightweight configuration database. This store facilitates both reading and writing operations, seamlessly integrated with Terraform via the `azurerm` provider. The hub virtual network's resource ID will reside in this configuration store, which the spoke deployments will read to establish peering with the hub.

#### Design Decisions

##### Azure App Configuration Store

We opt for Azure App Configuration Store as our central configuration database due to its lightweight nature, minimal maintenance requirements, and support for key-value pairs accessible from anywhere. Additionally, it boasts features like availability zones, geo-replication, private endpoints, and, crucially its integration with Terraform via the `azurerm` provider.

>  **Note:**  
>  A similar setup could be achieved using Azure Storage Table or equivalent services.
> 
>  

##### Why Not Use The `terraform_remote_state` Data Source?

While the `terraform_remote_state` data source enables dynamic sharing of configuration between deployments by exposing root-level outputs, it necessitates full access to the state snapshot, posing potential security risks due to sensitive information exposure.

##### Separate Terraform Deployments

As previously mentioned, dividing the infrastructure deployments into separate components reduces code complexity and mitigates the impact of changes by confining components to separate Terraform state files.

#### Deployment Instructions

##### Prerequisite Tooling

1. Azure CLI
2. Terraform
3. Azure Subscription where you have Owner permissions.

##### 0. Automated Script

Though it is recommended to go through the manual steps to understand the process and the code, you can also run `. '.scripts\Deploy.ps1'` in the root directory to deploy the full multi-deployment infrastructure.

##### 1. Pre-deployment

In this we will deploy the pre-requisites for the deployment of our hub and spoke architecture. This will include deploying the Azure App Configuration Store and also giving the necessary permissions to the principal doing the deployment to access the App Configuration Store, that is, the RBAC Role "App Configuration Data Owner". This used to perform data plane operations on the App Configuration Store such as reading and writing configuration key-values.

###### Resources

| Name | Type |
| --- | --- |
| [azurerm\_app\_configuration.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/app_configuration) | resource |
| [azurerm\_resource\_group.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group) | resource |
| [azurerm\_role\_assignment.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_assignment) | resource |
| [random\_bytes.this](https://registry.terraform.io/providers/hashicorp/random/latest/docs/resources/bytes) | resource |
| [azurerm\_client\_config.current](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/client_config) | data source |

###### Steps

1. clone the repository:

```
git clone https://github.com/luke-taylor/terraform-shared-configuration
```

2. Change directory to the pre-deployment folder:

```
cd terraform-shared-configuration/pre-deployment
```

3. Authenticate to Azure using the Azure CLI:

```
az login
```

4. Initialize the Terraform configuration:

```
terraform init
```

5. Apply the Terraform configuration:

```
terraform apply -auto-approve
```

6. Set environment variable for `app_configuration_store_id` for the next deployments:

```
$env:APP_CONFIGURATION_STORE_ID = (terraform output app_configuration_store_id | convertFrom-Json)
```

7. Checkout root directory:

```
cd ..
```

##### 2. Hub Deployment

The hub deployment will create the hub virtual network and some other optional resources like Azure Bastion and Azure Firewall which will be defaulted to disabled unless specified otherwise. The virtual network resource ID will be written to the Azure App Configuration Store through the `terraform-azurerm-app-configuration-read-write` module, this dynamically handles the JSON decoding and encoding of the values for us so we don't have to worry about it.

###### Modules

| Name | Source | Version |
| --- | --- | --- |
| [write\_data](https://github.com/luke-taylor/terraform-shared-configuration#module_write_data) | ./../../modules/terraform-azurerm-app-configuration-read-write | n/a |

###### Resources

| Name | Type |
| --- | --- |
| [azurerm\_bastion\_host.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/bastion_host) | resource |
| [azurerm\_firewall.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/firewall) | resource |
| [azurerm\_public\_ip.bastion](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/public_ip) | resource |
| [azurerm\_public\_ip.firewall](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/public_ip) | resource |
| [azurerm\_resource\_group.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group) | resource |
| [azurerm\_virtual\_network.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network) | resource |

###### Inputs

| Name | Description | Type | Default | Required |
| --- | --- | --- | --- | --- |
| [app\_configuration\_store\_id](https://github.com/luke-taylor/terraform-shared-configuration#input_app_configuration_store_id) | The name of the configuration store. | `string` | n/a | yes |
| [bastion\_enabled](https://github.com/luke-taylor/terraform-shared-configuration#input_bastion_enabled) | Whether to create the bastion. | `bool` | `false` | no |
| [firewall\_enabled](https://github.com/luke-taylor/terraform-shared-configuration#input_firewall_enabled) | Whether to create the firewall. | `bool` | `false` | no |

###### Steps

1. Change directory to the hub deployment folder:

```
cd deployments/hub
```

2. Initialize the Terraform configuration:

```
terraform init
```

3. Apply the Terraform configuration:

```
terraform apply -auto-approve
```

>  **Note:**  
>  Ensure to set the `app_configuration_store_id` input variable to the value outputted from the pre-deployment step.
> 
>  

4. Change directory back to the root:

```
cd ..\..
```

##### 3. Spoke Deployment - Identity

This deployment will create the spoke virtual network for the Identity resources, and we will peer this virtual network with the hub virtual network using the `terraform-azurerm-app-configuration-read-write` module to read the hub virtual network resource ID by simply specifying the key (`hub_vnet_id`) in the module inputs. We will also create a private DNS zone and link this back to the hub virtual network.

###### Modules

| Name | Source | Version |
| --- | --- | --- |
| [hub\_virtual\_network\_id](https://github.com/luke-taylor/terraform-shared-configuration#module_hub_virtual_network_id) | ./../../modules/terraform-azurerm-app-configuration-read-write | n/a |

###### Resources

| Name | Type |
| --- | --- |
| [azurerm\_private\_dns\_zone.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/private_dns_zone) | resource |
| [azurerm\_private\_dns\_zone\_virtual\_network\_link.link\_to\_hub](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/private_dns_zone_virtual_network_link) | resource |
| [azurerm\_private\_dns\_zone\_virtual\_network\_link.link\_to\_identity](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/private_dns_zone_virtual_network_link) | resource |
| [azurerm\_resource\_group.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group) | resource |
| [azurerm\_virtual\_network.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network) | resource |
| [azurerm\_virtual\_network\_peering.hub\_to\_identity](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network_peering) | resource |
| [azurerm\_virtual\_network\_peering.identity\_to\_hub](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network_peering) | resource |

###### Inputs

| Name | Description | Type | Default | Required |
| --- | --- | --- | --- | --- |
| [app\_configuration\_store\_id](https://github.com/luke-taylor/terraform-shared-configuration#input_app_configuration_store_id) | The name of the configuration store. | `string` | n/a | yes |

###### Steps

1. Change directory to the identity deployment folder:

```
cd deployments/identity
```

2. Initialize the Terraform configuration:

```
terraform init
```

3. Apply the Terraform configuration:

```
terraform apply -auto-approve
```

>  **Note:**  
>  Ensure to set the `app_configuration_store_id` input variable to the value outputted from the pre-deployment step.
> 
>  

4. Change directory back to the root:

```
cd ..\..
```

##### 4. Spoke Deployment - Landing Zone

Finally, we will deploy the spoke virtual network for the Landing Zone resources, and we will peer this virtual network with the hub virtual network using the `terraform-azurerm-app-configuration-read-write` module to read the hub virtual network resource ID by simply specifying the key (`hub_vnet_id`) in the module inputs.

###### Modules

| Name | Source | Version |
| --- | --- | --- |
| [hub\_virtual\_network\_id](https://github.com/luke-taylor/terraform-shared-configuration#module_hub_virtual_network_id) | ./../../modules/terraform-azurerm-app-configuration-read-write | n/a |

###### Resources

| Name | Type |
| --- | --- |
| [azurerm\_resource\_group.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group) | resource |
| [azurerm\_virtual\_network.this](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network) | resource |
| [azurerm\_virtual\_network\_peering.hub\_to\_landing\_zone](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network_peering) | resource |
| [azurerm\_virtual\_network\_peering.landing\_zone\_to\_hub](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network_peering) | resource |

###### Inputs

| Name | Description | Type | Default | Required |
| --- | --- | --- | --- | --- |
| [app\_configuration\_store\_id](https://github.com/luke-taylor/terraform-shared-configuration#input_app_configuration_store_id) | The name of the configuration store. | `string` | n/a | yes |

###### Steps

1. Change directory to the identity deployment folder:

```
cd deployments/identity
```

2. Initialize the Terraform configuration:

```
terraform init
```

3. Apply the Terraform configuration:

```
terraform apply -auto-approve
```

>  **Note:**  
>  Ensure to set the `app_configuration_store_id` input variable to the value outputted from the pre-deployment step.
> 
>  

4. Change directory back to the root:

```
cd ..\..
```

##### 5. Post-deployment

Obsevere the deployed resources in the Azure Portal.

[![Portal](https://github.com/luke-taylor/lab-terraform-shared-configuration/raw/main/.images/peering.png)](https://github.com/luke-taylor/lab-terraform-shared-configuration/blob/main/.images/peering.png)
#### Clean Up

To remove all resources efficiently run the following destroy script in the root directory:

```
 . '.scripts\Destroy.ps1'
```

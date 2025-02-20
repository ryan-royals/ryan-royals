---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azureterraform-azure-hubnetworking-terraform-verified-module-for-deploying-multi-hub-and-spoke-architectures/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/a3856337b634368e8e7157be3c3283410f6efa2f2b6ef4a8b1bd531e47245494/Azure/terraform-azure-hubnetworking)

#### Create list

Beta Lists are currently in beta. [Share feedback and report bugs.](https://github.com//github/feedback/discussions/categories/lists)

 [Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/)

### Azure/terraform-azure-hubnetworking

####  [README.md](https://github.com/Azure/terraform-azure-hubnetworking#readme)

### Terraform Verified Module for multi-hub network architectures

[![Average time to resolve an issue](https://camo.githubusercontent.com/9d630f0a6ea03cdbb69fee44310b11699a5f7482c874227665a1c1dfeecb34ec/687474703a2f2f697369746d61696e7461696e65642e636f6d2f62616467652f7265736f6c7574696f6e2f417a7572652f7465727261666f726d2d617a7572652d6875626e6574776f726b696e672e737667)](http://isitmaintained.com/project/Azure/terraform-azure-hubnetworking)
[![Percentage of issues still open](https://camo.githubusercontent.com/b140405cc097f3610e61395d33f6e9fbd309bfffc63d2643f44208c0a06605bf/687474703a2f2f697369746d61696e7461696e65642e636f6d2f62616467652f6f70656e2f417a7572652f7465727261666f726d2d617a7572652d6875626e6574776f726b696e672e737667)](http://isitmaintained.com/project/Azure/terraform-azure-hubnetworking)
This module is designed to simplify the creation of multi-region hub networks in Azure. It will create a number of virtual networks and subnets, and optionally peer them together in a mesh topology with routing.

#### Features

* This module will deploy `n` number of virtual networks and subnets. Optionally, these virtual networks can be peered in a mesh topology.
* A routing address space can be specified for each hub network, this module will then create route tables for the other hub networks and associate them with the subnets.
* Azure Firewall can be deployed iun each hub network. This module will configure routing for the AzureFirewallSubnet.

#### Example

```
module "hubnetworks" {
  source  = "Azure/hubnetworking/azure"
  version = "<version>" # change this to your desired version, https://www.terraform.io/language/expressions/version-constraints

  hub_virtual_networks = {
    weu-hub = {
      name                  = "vnet-prod-weu-0001"
      address_space         = ["192.168.0.0/23"]
      routing_address_space = ["192.168.0.0/20"]
      firewall = {
        subnet_address_prefix = "192.168.1.0/24"
        sku_tier              = "Premium"
        sku_name              = "AZFW_Hub"
      }
    }
  }
}
```

#### Documentation

#### Requirements

The following requirements are needed by this module:

* [terraform](https://github.com/Azure/terraform-azure-hubnetworking#requirement_terraform) (>= 1.3.0)
* [azurerm](https://github.com/Azure/terraform-azure-hubnetworking#requirement_azurerm) (>= 3.7.0, < 4.0)

#### Modules

The following Modules are called:

#####  [hub\_virtual\_networks](https://github.com/Azure/terraform-azure-hubnetworking#module_hub_virtual_networks)

Source: Azure/subnets/azurerm

Version: 1.0.0

#### Required Inputs

No required inputs.

#### Optional Inputs

The following input variables are optional (have default values):

#####  [hub\_virtual\_networks](https://github.com/Azure/terraform-azure-hubnetworking#input_hub_virtual_networks)

Description: A map of the hub virtual networks to create. The map key is an arbitrary value to avoid Terraform's restriction that map keys must be known at plan time.

##### Mandatory fields

* `name` - The name of the Virtual Network.
* `address_space` - A list of IPv4 address spaces that are used by this virtual network in CIDR format, e.g. `["192.168.0.0/24"]`.
* `location` - The Azure location where the virtual network should be created.
* `resource_group_name` - The name of the resource group in which the virtual network should be created.

##### Optional fields

* `bgp_community` - The BGP community associated with the virtual network.
* `ddos_protection_plan_id` - The ID of the DDoS protection plan associated with the virtual network.
* `dns_servers` - A list of DNS servers IP addresses for the virtual network.
* `flow_timeout_in_minutes` - The flow timeout in minutes for the virtual network. Default `4`.
* `mesh_peering_enabled` - Should the virtual network be peered to other hub networks with this flag enabled? Default `true`.
* `resource_group_creation_enabled` - Should the resource group for this virtual network be created by this module? Default `true`.
* `resource_group_lock_enabled` - Should the resource group for this virtual network be locked? Default `true`.
* `resource_group_lock_name` - The name of the resource group lock.
* `resource_group_tags` - A map of tags to apply to the resource group.
* `routing_address_space` - A list of IPv4 address spaces in CIDR format that are used for routing to this hub, e.g. `["192.168.0.0","172.16.0.0/12"]`.
* `hub_router_ip_address` - If not using Azure Firewall, this is the IP address of the hub router. This is used to create route table entries for other hub networks.
* `tags` - A map of tags to apply to the virtual network.

###### Route table entries

* `route_table_entries` - (Optional) A map of additional route table entries to add to the route table for this hub network. Default empty `{}`. The value is an object with the following fields:
	+ `name` - The name of the route table entry.
	+ `address_prefix` - The address prefix to match for this route table entry.
	+ `next_hop_type` - The type of the next hop. Possible values include `Internet`, `VirtualAppliance`, `VirtualNetworkGateway`, `VnetLocal`, `None`.
	+ `has_bgp_override` - Should the BGP override be enabled for this route table entry? Default `false`.
	+ `next_hop_ip_address` - The IP address of the next hop. Required if `next_hop_type` is `VirtualAppliance`.

###### Subnets

* `subnets` - (Optional) A map of subnets to create in the virtual network. The value is an object with the following fields:
	+ `address_prefixes` - The IPv4 address prefixes to use for the subnet in CIDR format.
	+ `nat_gateway` - (Optional) An object with the following fields:
		- `id` - The ID of the NAT Gateway which should be associated with the Subnet. Changing this forces a new resource to be created.
	+ `network_security_group` - (Optional) An object with the following fields:
		- `id` - The ID of the Network Security Group which should be associated with the Subnet. Changing this forces a new association to be created.
	+ `private_endpoint_network_policies_enabled` - (Optional) Enable or Disable network policies for the private endpoint on the subnet. Setting this to true will Enable the policy and setting this to false will Disable the policy. Defaults to true.
	+ `private_link_service_network_policies_enabled` - (Optional) Enable or Disable network policies for the private link service on the subnet. Setting this to true will Enable the policy and setting this to false will Disable the policy. Defaults to true.
	+ `assign_generated_route_table` - (Optional) Should the Route Table generated by this module be associated with this Subnet? Default `true`. Cannot be used with `external_route_table_id`.
	+ `external_route_table_id` - (Optional) The ID of the Route Table which should be associated with the Subnet. Changing this forces a new association to be created. Cannot be used with `assign_generated_route_table`.
	+ `service_endpoints` - (Optional) The list of Service endpoints to associate with the subnet.
	+ `service_endpoint_policy_ids` - (Optional) The list of Service Endpoint Policy IDs to associate with the subnet.
	+ `service_endpoint_policy_assignment_enabled` - (Optional) Should the Service Endpoint Policy be assigned to the subnet? Default `true`.
	+ `delegation` - (Optional) An object with the following fields:
		- `name` - The name of the delegation.
		- `service_delegation` - An object with the following fields:
			* `name` - The name of the service delegation.
			* `actions` - A list of actions that should be delegated, the list is specific to the service being delegated.

###### Azure Firewall

* `firewall` - (Optional) An object with the following fields:
	+ `sku_name` - The name of the SKU to use for the Azure Firewall. Possible values include `AZFW_Hub`, `AZFW_VNet`.
	+ `sku_tier` - The tier of the SKU to use for the Azure Firewall. Possible values include `Basic`, `Standard`, `Premium`.
	+ `subnet_address_prefix` - The IPv4 address prefix to use for the Azure Firewall subnet in CIDR format. Needs to be a part of the virtual network's address space.
	+ `subnet_route_table_id` = (Optional) The resource id of the Route Table which should be associated with the Azure Firewall subnet. If not specified the module will assign the generated route table.
	+ `name` - (Optional) The name of the firewall resource. If not specified will use `afw-{vnetname}`.
	+ `dns_servers` - (Optional) A list of DNS server IP addresses for the Azure Firewall.
	+ `firewall_policy_id` - (Optional) The resource id of the Azure Firewall Policy to associate with the Azure Firewall.
	+ `private_ip_ranges` - (Optional) A list of private IP ranges to use for the Azure Firewall, to which the firewall will not NAT traffic. If not specified will use RFC1918.
	+ `threat_intel_mode` - (Optional) The threat intelligence mode for the Azure Firewall. Possible values include `Alert`, `Deny`, `Off`.
	+ `zones` - (Optional) A list of availability zones to use for the Azure Firewall. If not specified will be `null`.
	+ `tags` - (Optional) A map of tags to apply to the Azure Firewall. If not specified
	+ `default_ip_configuration` - (Optional) An object with the following fields. If not specified the defaults below will be used:
		- `name` - (Optional) The name of the default IP configuration. If not specified will use `default`.
		- `public_ip_config` - (Optional) An object with the following fields:
			* `name` - (Optional) The name of the public IP configuration. If not specified will use `pip-afw-{vnetname}`.
			* `zones` - (Optional) A list of availability zones to use for the public IP configuration. If not specified will be `null`.
			* `ip_version` - (Optional) The IP version to use for the public IP configuration. Possible values include `IPv4`, `IPv6`. If not specified will be `IPv4`.
			* `sku_tier` - (Optional) The SKU tier to use for the public IP configuration. Possible values include `Regional`, `Global`. If not specified will be `Regional`.

Type:

```
map(object({
    name                = string
    address_space       = list(string)
    location            = string
    resource_group_name = string

    bgp_community                   = optional(string)
    ddos_protection_plan_id         = optional(string)
    dns_servers                     = optional(list(string))
    flow_timeout_in_minutes         = optional(number, 4)
    mesh_peering_enabled            = optional(bool, true)
    resource_group_creation_enabled = optional(bool, true)
    resource_group_lock_enabled     = optional(bool, true)
    resource_group_lock_name        = optional(string)
    resource_group_tags             = optional(map(string))
    routing_address_space           = optional(list(string), [])
    hub_router_ip_address           = optional(string)
    tags                            = optional(map(string), {})

    route_table_entries = optional(map(object({
      name           = string
      address_prefix = string
      next_hop_type  = string

      has_bgp_override    = optional(bool, false)
      next_hop_ip_address = optional(string)
    })), {})

    subnets = optional(map(object(
      {
        address_prefixes = list(string)
        nat_gateway = optional(object({
          id = string
        }))
        network_security_group = optional(object({
          id = string
        }))
        private_endpoint_network_policies_enabled     = optional(bool, true)
        private_link_service_network_policies_enabled = optional(bool, true)
        assign_generated_route_table                  = optional(bool, true)
        external_route_table_id                       = optional(string)
        service_endpoints                             = optional(set(string))
        service_endpoint_policy_ids                   = optional(set(string))
        delegations = optional(list(
          object(
            {
              name = string
              service_delegation = object({
                name    = string
                actions = optional(list(string))
              })
            }
          )
        ))
      }
    )), {})

    firewall = optional(object({
      sku_name              = string
      sku_tier              = string
      subnet_address_prefix = string
      subnet_route_table_id = optional(string)
      name                  = optional(string)
      dns_servers           = optional(list(string))
      firewall_policy_id    = optional(string)
      private_ip_ranges     = optional(list(string))
      threat_intel_mode     = optional(string, "Alert")
      zones                 = optional(list(string))
      tags                  = optional(map(string))
      default_ip_configuration = optional(object({
        name = optional(string)
        public_ip_config = optional(object({
          name       = optional(set(string))
          zones      = optional(set(string))
          ip_version = optional(string)
          sku_tier   = optional(string, "Regional")
        }))
      }))
    }))

    # TODO: ERGW variables

    # TODO: VPNGW variables
  }))
```

Default: `{}`

#### Resources

The following resources are used by this module:

* [azurerm\_firewall.fw](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/firewall) (resource)
* [azurerm\_management\_lock.rg\_lock](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/management_lock) (resource)
* [azurerm\_public\_ip.fw\_default\_ip\_configuration\_pip](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/public_ip) (resource)
* [azurerm\_resource\_group.rg](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/resource_group) (resource)
* [azurerm\_route\_table.hub\_routing](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/route_table) (resource)
* [azurerm\_subnet.fw\_subnet](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet) (resource)
* [azurerm\_subnet\_route\_table\_association.fw\_subnet\_routing\_creat](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet_route_table_association) (resource)
* [azurerm\_subnet\_route\_table\_association.fw\_subnet\_routing\_external](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet_route_table_association) (resource)
* [azurerm\_subnet\_route\_table\_association.hub\_routing\_creat](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet_route_table_association) (resource)
* [azurerm\_subnet\_route\_table\_association.hub\_routing\_external](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/subnet_route_table_association) (resource)
* [azurerm\_virtual\_network\_peering.hub\_peering](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/virtual_network_peering) (resource)

#### Outputs

The following outputs are exported:

#####  [firewalls](https://github.com/Azure/terraform-azure-hubnetworking#output_firewalls)

Description: n/a

#####  [hub\_route\_tables](https://github.com/Azure/terraform-azure-hubnetworking#output_hub_route_tables)

Description: n/a

#####  [resource\_groups](https://github.com/Azure/terraform-azure-hubnetworking#output_resource_groups)

Description: n/a

#####  [virtual\_networks](https://github.com/Azure/terraform-azure-hubnetworking#output_virtual_networks)

Description: n/a

#### Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit <https://cla.opensource.microsoft.com>.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

#### Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow Microsoft's Trademark & Brand Guidelines. Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.

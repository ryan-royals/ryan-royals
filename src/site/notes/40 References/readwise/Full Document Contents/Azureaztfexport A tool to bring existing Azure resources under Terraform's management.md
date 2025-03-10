---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azureaztfexport-a-tool-to-bring-existing-azure-resources-under-terraform-s-management/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/24e399a1761e19aa92edcba30a8f779ec05e98d2750a02336425da5698742e79/Azure/aztfexport)

#### Create list

Beta Lists are currently in beta. [Share feedback and report bugs.](https://github.com//github/feedback/discussions/categories/lists)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Azure/aztfexport?resume=1)

### Azure/aztfexport

####  [README.md](https://github.com/Azure/aztfexport#readme)

#### Microsoft Azure Export for Terraform

A tool to bring your existing Azure resources under the management of Terraform.

#### Goal

`aztfexport` imports the resources that are supported by the [Terraform AzureRM provider](https://github.com/hashicorp/terraform-provider-azurerm) into the Terraform state, and generates the corresponding Terraform configuration. Both the Terraform state and configuration are expected to be consistent with the resources' remote state, i.e., `terraform plan` shows no diff. The user then is able to use Terraform to manage these resources.

#### Non Goal

The Terraform configurations generated by `aztfexport` are not meant to be comprehensive and do not ensure that the infrastructure can be fully reproduced from the generated configurations. For details, please refer to the [limitation](https://github.com/Azure/aztfexport#limitation).

#### Install

##### From Release

Precompiled binaries and Window MSI are available at [Releases](https://github.com/Azure/aztfexport/releases).

##### From Go toolchain

```
go install github.com/Azure/aztfexport@latest
```

##### From Package Manager

###### Windows

```
winget install aztfexport
```

###### Homebrew (Linux/macOS)

```
brew install aztfexport
```

###### dnf (Linux)

Supported versions:

* RHEL 8 (amd64, arm64)
* RHEL 9 (amd64, arm64)

1. Import the Microsoft repository key:

 
```
rpm --import https://packages.microsoft.com/keys/microsoft.asc

```
2. Add `packages-microsoft-com-prod` repository:

 
```
ver=8 # or 9
dnf install -y https://packages.microsoft.com/config/rhel/${ver}/packages-microsoft-prod.rpm

```
3. Install:

 
```
dnf install aztfexport

```

###### apt (Linux)

Supported versions:

* Ubuntu 20.04 (amd64, arm64)
* Ubuntu 22.04 (amd64, arm64)

1. Import the Microsoft repository key:

 
```
curl -sSL https://packages.microsoft.com/keys/microsoft.asc > /etc/apt/trusted.gpg.d/microsoft.asc

```
2. Add `packages-microsoft-com-prod` repository:

 
```
ver=20.04 # or 22.04
apt-add-repository https://packages.microsoft.com/ubuntu/${ver}/prod

```
3. Install:

 
```
apt-get install aztfexport

```

#### Precondition

`aztfexport` requires a `terraform` executable installed in the `$PATH`, whose version `>= v0.12`.

#### Usage

Follow the [authentication guide](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs#authenticating-to-azure) from the Terraform AzureRM provider to authenticate to Azure.

Then you can go ahead and run `aztfexport resource <resource id>`, `aztfexport resource-group <resource group name>` or `aztfexport query <arg where predicate>` to import a single resource, a resource group including child resources, or a customized set of resources by an Azure Resource Graph query.

##### Export a Single Resource

`aztfexport resource [option] <resource id>` exports a single resource by its Azure control plane ID.

E.g.

```
aztfexport resource /subscriptions/0000/resourceGroups/rg1/providers/Microsoft.Compute/virtualMachines/vm1
```

The command will automatically identify the Terraform resource type (e.g. correctly identifies above resource as `azurerm_linux_virtual_machine`), and import it into state file and generate the Terraform configuration.

>  ❗ For data plane only or property-like resources, the Azure resource ID is using a pesudo format, as is defined [here](https://github.com/magodo/aztft#pesudo-resource-id).
> 
>  

##### Export a Resource Group

`aztfexport resource-group [option] <resource group name>` exports a resource group and its including resources by its name.

##### Export a Customized Set of Resources

`aztfexport query [option] <arg where predicate>` exports a set of resources (and its including resources with `--recursive`) by an Azure Resource Graph [`where` predicate](https://learn.microsoft.com/en-us/azure/data-explorer/kusto/query/whereoperator). Note that you can combine multiple conditions in one `where` predicate, e.g. `resourceGroup =~ "my-rg" and type =~ "microsoft.network/virtualnetworks"`.

>  💡 Resource group mode is the same as running `aztfexport query --recursive "resourceGroup =~ 'my-rg'"`, except it also add on the resource group itself.
> 
>  

`aztfexport` depends on `azlist`, which uses ARG behind the scenes. `azlist` will first make an ARG call with the given where predicate, then if `--recursive` is specified, it will recursively call the "LIST" on the known child resource types. Since ARG only returns ARM tracked resources at this moment, but not for the RP proxy resources (e.g. subnet, network security rules, storage containers, etc). If you uses predicate like `type =~ "microsoft.network/virtualnetworks/subnets"`, it returns you nothing since subnet is not an ARM tracked resource.

To workaround above, you can query with a bigger scope (e.g. `type =~ "microsoft.network/virtualnetworks"`) in interactive mode, then manually remove the resources other than subnets.

##### Export a Predefined Set of Resources

`aztfexport mapping-file [option] <resource mapping file>` exports a set of resources that is defined in the resource mapping file.

The format of the mapping file is defined below:

```
{
    "<Azure resource id1>": {
        "resource_type" : "<terraform resource type>",
        "resource_name" : "<terraform resource name>",
        "resource_id"   : "<terraform resource id>"
    },
    "<Azure resource id2>": {
        "resource_type" : "<terraform resource type>",
        "resource_name" : "<terraform resource name>",
        "resource_id"   : "<terraform resource id>"
    },
    ...
}
```

Example:

```
{
	"/subscriptions/0000/resourceGroups/aztfexport-vmdisk": {
		"resource_id": "/subscriptions/0000/resourceGroups/aztfexport-vmdisk",
		"resource_type": "azurerm_resource_group",
		"resource_name": "res-1"
	},
	"/subscriptions/0000/resourceGroups/aztfexport-vmdisk/providers/Microsoft.Compute/disks/aztfexport-test-test": {
		"resource_id": "/subscriptions/0000/resourceGroups/aztfexport-vmdisk/providers/Microsoft.Compute/disks/aztfexport-test-test",
		"resource_type": "azurerm_managed_disk",
		"resource_name": "res-2"
	},
	"/subscriptions/0000/resourceGroups/aztfexport-vmdisk/providers/Microsoft.Compute/virtualMachines/aztfexport-test-test": {
		"resource_id": "/subscriptions/0000/resourceGroups/aztfexport-vmdisk/providers/Microsoft.Compute/virtualMachines/aztfexport-test-test",
		"resource_type": "azurerm_linux_virtual_machine",
		"resource_name": "res-3"
	},
    ...
}
```

You can generate the mapping file in all other modes (i.e. `resource`, `resource-group`, `query`) by specifying the `--generate-mapping-file` option when running non-interactively, or press s when running interactively in the resource list stage. Also, each run of `aztfexport` will generate the resource mapping file for you, to record what resources have been imported.

Of course, you are welcome to manually construct or edit the mapping file. Note that only the object value in the mapping file matters, while the key just plays as an identifier in this mode.

##### Interactive vs Non-Interactive

By default `aztfexport` runs in interactive mode, whilst you can also run in non-interactive mode by adding the `--non-interactive`/`-n` option.

###### Interactive mode

In interactive mode, `aztfexport` list all the resources resides in the specified resource group or customized set. For each resource, `aztfexport` will try to recognize the corresponding Terraform resource type. If it finds one, the line will be prefixed by a 💡 as an indicator. Otherwise, user is expected to input the Terraform resource address in form of `<resource type>.<resource name>` (e.g. `azurerm_linux_virtual_machine.test`). Users can press `r` to see the possible resource type(s) for the selected resource.

In some cases, there are Azure resources that have no corresponding Terraform resources (e.g. due to lacks of Terraform support), or some resources might be created as a side effect of provisioning another resource (e.g. the OS Disk resource is created automatically when provisioning a VM). In these cases, you can skip these resources without typing anything.

After going through all the resources to be imported, users press `w` to instruct `aztfexport` to proceed importing resources into Terraform state and generating the Terraform configuration.

###### Non-Interactive mode

In non-interactive mode, `aztfexport` only imports the recognized resources, and skip the others. Users can further specify the `--continue`/`-k` option to make the tool continue even on hitting any import error.

##### Backend: local vs remote

By default, `aztfexport` checks the output directory whether it is empty. If it is not empty, the user can specify either `--overwrite` to clean up the directory, or `--append` to additively generate the config to the directory.

>  💡 In append mode, the file generated by `aztfexport` be named differently than normal, where each file will has `.aztfexport` suffix before the extension (e.g. `main.aztfexport.tf`), to avoid potential file name conflicts. If you run `aztfexport [subcommand] --append` multiple times, the generated config in `main.aztfexport.tf` will be appended in each run.
> 
>  

On top of this, `aztfexport` supports importing these resources to state either in local backend or [remote backend](https://www.terraform.io/language/settings/backends):

* In case the output directory is empty, or the user has specified `--overwrite`, the backend type is determined by `--backend-type`, which defaults to `local` when absent.
* Otherwise, the user append (via `--append`) to a non-empty output directory. Then `aztfexport` will honor any existing backend setting (i.e. in the [`terraform` setting](https://developer.hashicorp.com/terraform/language/settings)), and ensure it is consistent with the specified backend type (via `--backend-type`) and backend config (via `--backend-config`), if any.

This means there are two ways to export into remote state:

* Using the `--backend-type` and `--backend-config`, e.g.:

 
```
aztfexport [subcommand] --backend-type=azurerm --backend-config=resource_group_name=<resource group name> --backend-config=storage_account_name=<account name> --backend-config=container_name=<container name> --backend-config=key=terraform.tfstate 
```
* Prepare the [`terraform` setting](https://developer.hashicorp.com/terraform/language/settings) in the output directory, and run `aztfexport [subcommand] --append`

##### Config

`aztfexport` will create a configuration file at `$HOME/.aztfexport/config.json`. This file is aim to be managed by command `aztfexport config [subcommand]`, which includes following subcommands:

* `get`: Get a config item
* `set`: Set a config item
* `show`: Show the full configuration

Currently, following config items are supported:

* `installation_id`: A UUID created on first run. If there is Azure CLI or Azure Powershell installed on the current machine, the UUID will be the same value among these tools. Otherwise, a new one will be created. This is used as an identifier in the telemetry trace.
* `telemetry_enabled`: Whether to enable telemetry? We use telemetry to identify issues and areas for improvement, in order to optimize this tool for better performance, reliability, and user experience.

##### Cloud Environment

By default, `aztfexport` targets to the `public` Azure cloud. If you are interacting with other clouds like `usgovernment` or `china`, you can specify that by `--env` option, or the environment variable `AZTFEXPORT_ENV`.

#### How it Works

`aztfexport` leverage [`aztft`](https://github.com/magodo/aztft) to identify the Terraform resource type on its Azure resource ID. Then it runs `terraform import` under the hood to import each resource. Afterwards, it runs [`tfadd`](https://github.com/magodo/tfadd) to generate the Terraform template for each imported resource.

#### Demo

[![asciicast](https://camo.githubusercontent.com/23ce8de4b8d28a0359fa7a9599af06b1e8dcd471ce2108803ddded6875ad33a3/68747470733a2f2f61736369696e656d612e6f72672f612f734b59717a536945356270424a434234424d32486a7646346a2e737667)](https://asciinema.org/a/sKYqzSiE5bpBJCB4BM2HjvF4j)
#### Limitation

There are several limitations causing `aztfexport` can hardly generate reproducible Terraform configurations.

##### AzureRM Provider Validation

When generating the Terraform configuration, not all properties of the resource are exported for different reasons.

One reason is because there are flexible cross-property constraints defined in the AzureRM Terraform provider. E.g. `property_a` conflits with `property_b`. This might due to the nature of the API, or might be due to some deprecation process of the provider (e.g. `property_a` is deprecated in favor of `property_b`, but kept for backwards compatibility). These constraints require some properties must be absent in the Terraform configuration, otherwise, the configuration is not a valid and will fail during `terraform validate`.

Another reason is that an Azure resource can be a property of its parent resource (e.g. `azurerm_subnet` can be its own resource, or be a property of `azurerm_virtual_network`). Per Terraform's best practice, users should only use one of the forms, not both. `aztfexport` chooses to always generate all the resources, but omit the property in the parent resource that represents the child resource.

#### Additional Resources

* [The aztfexport Github Page](https://azure.github.io/aztfexport): Everything about aztfexport, including comparisons with other existing import solutions.
* [aztft](https://github.com/magodo/aztft): A Go program and library for identifying the correct Terraform AzureRM provider resource type on the Azure resource id.
* [tfadd](https://github.com/magodo/tfadd): A Go program and library for generating Terraform configuration from Terraform state.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/hashi-talks-2024-mastering-terraform-testing-a-layered-approach-to-testing-complex-infrastructure/","tags":["rw/articles"]}
---

![rw-book-cover](https://mattias.engineer/img/favicon/blue.png)

![HashiTalks 2024: Mastering Terraform Testing, a layered approach to testing complex infrastructure](https://mattias.engineer/posts/hashitalks-2024/cover.png)Cover Image
Today I am kicking of **HashiTalks 2024** with my talk **Mastering Terraform Testing: A layered approach to testing complex infrastructure**. HashiTalks is a 24-hour follow-the-sun online HashiCorp community event with speakers from around the globe.

Technically, this is my first time speaking publicly (although online, alone, at home, in front of my screen) outside of my day-to-day work and the HashiCorp User Group I’ve recently started.

My talk is pretty packed with information and demos. It assumes familiarity with the basics of the Terraform test framework. It also helps if you have some familiarity with GitHub Actions.

This blog post is the accompanying written content that goes deeper into the details of my talk.

#### Setting the scene

Imagine that you and I are part of a platform team in our organization. I will not spend time discussing the philosophical aspects of platform engineering and the “to be or not to be” of platform teams. In this particular scenario we work for an organization that has a platform team, and we are part of it!

The platform we are building for our developers rests upon three major components:

* We use **Terraform Cloud** for a few things. For us in the platform team the main component is our private Terraform module registry where we publish modules for our organization. We also govern the infrastructure our development teams are creating through the use of Sentinel policies connected to our Terraform Cloud organization. Our development teams use Terraform Cloud for handling state and running Terraform plan/apply for their infrastructure.
* All of our workloads are deployed to **Microsoft Azure**.
* We keep our source code in **GitHub**, this is also where we run a lot of CI/CD workflows both for Terraform but also for other things. GitHub is well integrated with Terraform Cloud and Azure, so it makes sense for us to put our source code here.

Note that in reality we would most likely have additional components be part of our platform, and we might have an abstraction layer on top of everything. But we’re only just beginning our platform engineering journey in our organization.

In order to discuss the Terraform test framework we need a few Terraform modules to focus on. In this post I will concentrate on the following five modules that are published to the private Terraform Cloud registry:

![terraform modules](https://assets.mattias.engineer/posts/hashitalks-2024/01.png)A brief explanation of these modules follow below:
* **Resource group module**: this module sets up an Azure resource group. A resource group in Azure is a container for other resources. If you want to create any resource you would need to have a resource group already, or create a new one. Sometimes this is only implicitly true, for instance if you want to create a subnet for a virtual network, then the requirement is rather that you have a virtual network already - however, the virtual network itself must reside in a resource group.
* **Network module**: this module creates a virtual network with any number of subnets that we require.
* **AKS module**: AKS is the Azure Kubernetes Service. This module sets up an AKS cluster according to our specifications.
* **Kubernetes platform module**: This module takes a bare Kubernetes cluster and configures any number of platform specific applications that we might need. To keep this module light it currently only installs Argo CD on a cluster. Argo CD will later be used to deploy applications using a GitOps approach.
* **Traffic manager module**: This module creates a traffic manager profile resource in Azure. Traffic manager is a service for DNS load balancing. It is usually used for applications spanning the globe, where users should be directed to regions closest to them, but it supports any kind of load balancing use case.

Our development teams are using our modules as part of their infrastructure. You can imagine that we have a lot more modules available, but for the purpose of this post we will concentrate on these five.

Later in this post I will introduce the concept of test-specific modules. These are modules specifically used for testing, primarily some kind of integration testing or end-to-end testing scenarios. I did not include these modules in the list of modules above, this is because they have a fundamentally different purpose.

#### Layer 1: Before we test, we validate.

A good Terraform module helps the module consumer to use it correctly. The first step to make this happen is to design a module with few required input variables, using sensible defaults for most variables, and include a lot of declarative validation logic. The last point is all about making sure that the module consumers will not accidentally provide invalid values that will later cause errors during `terraform apply`.

In ths first layer of my approach to testing we will not really be doing any testing at all. However, the validation of inputs, outputs, and resources make up the foundation of many of the tests we later write.

To remind you of what Terraform is capable of when it comes to testing I want to take a brief moment to go through both imperative validation using CLI commands and declarative validation using custom conditions.

##### Imperative validation using the CLI

This type of validation belongs to the category of imperative validation. We can run CLI commands and have Terraform tell us if something is wrong.

The first command I want to highlight is that one command that everyone using Terraform has to start with in order to do anything else: `terraform init`. You might not think of `terraform init` as a validation command, but it will capture trivial mistakes like when you try to download an invalid version of a given provider.

Once we can successfully run `terraform init` we have another command at our disposal that can go further with validation: `terraform validate`. See, *validate* is even the name of the command! This command compares your Terraform configuration to the provider resource schemas to see that you are providing all the required arguments and that you are using the correct argument types, and more. This should definitely be part of your CI/CD pipeline.

Now you are in a position that Terraform can download your required providers and it believes your configuration follows all the provider resource schemas. You are ready to create infrastructure, and the first step towards that is `terraform plan`. Of all the available Terraform commands I believe `terraform plan` is the most useful one available[1](https://mattias.engineer/posts/hashitalks-2024/?utm_source=tldrdevops#fn:1). Running `terraform plan` will tell you what changes Terraform will do if you were to run `terraform apply` with the current configuration and the current state of the world. This is a superpower for you as a Terraform user.

I thought about writing something about `terraform fmt` (and now I am doing it), but in the end it does not really do much more than format your code. Of course it will tell you if there is an error in your syntax, but this should already be evident to you in your editor - if not, then you should install support for Terraform in your editor!

##### Declarative validation using HCL

Terraform has the concept of custom validations that we can utilize in variables, outputs, resources, data sources, and check blocks. Custom conditions allow you to safeguard your module from mistakes coming from your module consumers or your providers.

For variables we have the concept of a `validation` block. Actually, we can include any number of `validation` blocks for a given variable. For our resource group module we have a variable named `location` with the following definition:

```
variable "location" {
  type = string

  validation {
    condition     = contains([
      "swedencentral",
      "westeurope",
      "northeurope"
    ], var.location)
    error_message = "Use an approved location!"
  }
}

```

The variable specifies in what Azure location the resource group should be created. The `validation` block checks the provided value and validates that it is one of three allowed values. If it is not, Terraform will produce an error and stop the plan or apply. I will come back to this specific example later when I talk about policy-as-code.

Moving on to our output values. For output values we have `precondition` blocks which allow us to set up guarantees for our values. If the validation in a `precondition` block fails, then Terraform will produce an error message and stop. This makes sure that we don’t provide output values that might be missing attributes or having invalid values of some kind, which would later result in an error further along in the Terraform apply operation. An example of what this could look like:

```
output "resource_group" {
  value = data.azurerm_storage_account.this

  precondition {
    condition     = data.azurerm_storage_account.this.enable_https_traffic_only
    error_message = "Storage account is not securely configured"
  }
}

```

Here we have a data source reading an existing Azure storage account resource and we have an output with the value of this data source. However, the validation checks that the storage account is only allowing HTTPS traffic, if not we do not want to use that storage account for whatever else we were planning to do.

For our resources and data sources we can use `precondition` and `postcondition` blocks inside of the `lifecycle` block. This allows us to perform validations before or after creating a resource or reading a data source.

The last type of custom condition I want to highlight is the `check` block. This allows us to perform validations outside of resource lifecycles and not necessarily tied to anything else in our configuration. An example of what this can look like:

```
check "website_responds" {
  data "http" "this" {
    url = module.website.endpoint
  }

  assert {
    condition     = http.this.status_code == 200
    error_message = "Website is not healthy"
  }
}

```

In this `check` block we send a HTTP GET request to an endpoint we get as output from a website module. Then we use an `assert` block to check that the response was a 200 OK. A failing `check` block will not cause Terraform apply to fail, but it will produce a warning. You can use `check` blocks together with Terraform Cloud to set up continuous checks that runs through each `check` block periodically and notifies you of any failures.

#### Layer 2: Taking the test framework for a spin.

With validation in place we are ready to start using the Terraform test framework. When you write tests for your Terraform modules you want to make sure to test the full module interface. What is part of the module interface? Generally:

* Variables.
* Outputs.
* Any resource that is externally visible and of importance to your module consumers.
* Any behavior or functionality that is exposed by the resources or data sources that are part of your module.

A good place to start writing tests is to test the validation logic you added in the previous layer. This is where the beta feature of test generation in Terraform Cloud could be a good starting point. It is good at generating tests to validate basic things for your module.

For our resource group module it makes sense to start testing the validation for our input variables. We have a variable named `location`:

```
variable "location" {
  type = string

  validation {
    condition     = contains([
      "swedencentral",
      "westeurope",
      "northeurope"
    ], var.location)
    error_message = "Use an approved location!"
  }
}

```

We only wanted certain values to be allowed. A good test for this validation logic is to provide a value not in the list of allowed locations:

```
run "should_not_allow_invalid_location" {
  command = plan

  variables {
    location = "westus"
  }

  expect_failures = [
    var.location
  ]
}

```

Most of your tests should use `command = plan` since these tests will be fast. When it comes to testing your validation logic many (all?) of the tests will be using the `expect_failure` array instead of `assert` blocks.

If you have a variable that contain many different validation blocks you should write tests for all of the validations individually. Another of the variables for the resource group module is the `name_suffix`:

```
variable "name_suffix" {
  type        = string
  description = "Resource group name suffix (i.e. rg-<NAME_SUFFIX>)"

  validation {
    condition     = !can(regex("\\s+", var.name_suffix))
    error_message = "Name suffix should not contain whitespace characters"
  }

  validation {
    condition     = !startswith(var.name_suffix, "rg-")
    error_message = "Do not add 'rg-' in the name, this is added automatically"
  }

  validation {
    condition     = length("rg-${var.name_suffix}") <= 90
    error_message = "Name suffix is too long (should be at most 87 characters)"
  }
}

```

This variable has three different `validation` blocks. We demand that the name does not contain any whitespace characters, that it does not start with `rg-`, and that the provided value is at most 87 characters long. We can write tests for this:

```
run "should_not_allow_whitespace_in_name_suffix" {
  command = plan

  variables {
    name_suffix = "my name suffix"
  }

  expect_failures = [
    var.name_suffix
  ]
}

run "should_not_allow_rg_prefix_in_name_suffix" {
  command = plan

  variables {
    name_suffix = "rg-test"
  }

  expect_failures = [
    var.name_suffix
  ]
}

run "should_not_allow_too_long_name_suffix" {
  command = plan

  variables {
    name_suffix = replace("**********", "*", "abcdefghij")
  }

  expect_failures = [
    var.name_suffix
  ]
}

```

In the third example test we see a new feature available since Terraform 1.7: we can use any Terraform built-in functions in our variables. Here I am using the `replace` function to create a long string without having to type it out in full. If you have the need to create a lot of synthetic data for tests you could set up a setup/helper module specifically for this. As a first `run` block in your test file you can call the setup module and then use the output from this module in the following `run` blocks.

Another kind of test you might want to do for this type of module is to make sure it actually works for all the values you allow as input. In this case we would like to make sure that the module works for each value of the `location` variable. You could add three separate tests for this:

```
run "should_work_for_swedencentral" {
  variables {
    location = "swedencentral"
  }

  assert {
    // assert something
  }
}

// repeat for westeurope and northeurope ...

```

However, imagine you also want to make sure that a few of your latest versions of your module works for each intended value of the `location` variable and you want to make sure there is no regression. One way to do this is to set up a test using GitHub Actions and varying the inputs you want. I have written about this [before](https://mattias.engineer/posts/test-permutations-terraform-github-actions/), so I will only briefly lay out the details here. Instead of having a specific test file I create a template file containing placeholders for values I want to vary:

```
variables {
  location    = "{{LOCATION}}"
  name_suffix = "hashitalks-${uuid()}"
  tags        = {
    team        = "HashiTalks Team"
    project     = "HashiTalks Project"
    cost_center = "1234"
    version     = "{{VERSION}}"
    location    = "{{LOCATION}}"
  }
}

provider "azurerm" {
  features {}
}

run "create" {
  module {
    source  = "app.terraform.io/mattias-fjellstrom/resource-group-module/hashitalks"
    version = "{{VERSION}}"
  }
}

```

I have added `{{VERSION}}` and `{{LOCATION}}` as placeholders. Note that I have included the use of a `uuid()` function in my `name_suffix` variable, this is to allow multiple tests to run simultaneously without any name collision. Next I have a GitHub Actions workflow:

```
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        location: ["swedencentral", "westeurope", "northeurope"]
        version: ["2.0.0", "3.0.0", "3.1.0"]
    runs-on: ubuntu-latest
    steps:
      - name: Azure login
        uses: azure/login@v1
      - uses: actions/checkout@v4
      - run: |
          sed 's/{{VERSION}}/${{ matrix.version }}/g; s/{{LOCATION}}/${{ matrix.location }}/g' \
            templates/main.tftest.hcl.template > tests/main.tftest.hcl          
      - uses: hashicorp/setup-terraform@v2
        with:
          terraform_wrapper: false
      - run: terraform init
        env:
          TF_TOKEN_app_terraform_io: ${{ secrets.TF_TOKEN }}
      - run: terraform test

```

Note that I have removed some lines in this file for brevity, the full content is available [here](https://github.com/mattias-fjellstrom-demo/terraform-hashitalks-github-actions-single/blob/main/.github/workflows/workflow.yaml). The important pieces are in the `strategy` and in the third step. In the `strategy` I specify which values I want to use for my location and my version, and in the third step of the workflow I use `sed` to replace the placeholders with my values. When this workflow runs there will be nine parallel tests running, one for each permutation of location and version:

![github actions](https://assets.mattias.engineer/posts/hashitalks-2024/02.png)github actions
#### Layer 3: Our modules do not exist in isolation. Integration testing!

Validation for our modules is in place, and we have now written tests for our module interface. Our module works, in isolation! It is likely that our modules have dependencies with other modules. This could be our own modules or third-party modules. This leads us to the need of adding integration testing.

To illustrate integration testing we will focus on the resource group module and the network module. As I mentioned earlier, a resource in Azure requires the existence of a resource group. So naturally our network module has a dependency on a resource group.

We have a few options for how to handle dependencies:

1. If you have written and published both modules and you intend for them to be compatible with each other, then it makes sense to use the published module to fill the dependency. This means we would use the published resource group module to set up a resource group that is then used when testing the network module.
2. If you want to create standalone tests for the network module you can create any dependencies you have using a helper module (or we could also call it a setup module). This means we would include a small local module inside of the code for the network module with the sole purpose of creating a resource group specifically for filling the dependency while testing.
3. If our tests do not actually need a resource group, we could just provide static values for any attribute of the resource group that we are referencing. In this specific case the network module requires that the resource group has a name and a location attribute.
4. Starting in Terraform 1.7 we could use mocks and replace the resource group by a mock. This is probably the easiest way of doing it using the least amount of code.

The last two options (static values or mocks) have a drawback for us in this particular situation. If we want to run tests with `command = apply`, then we are required to have a real resource group to place our network inside of. Note that this does not necessarily mean that mocks are useless when it comes to testing Azure infrastructure, we can still use them in situations where we do not want to create all the infrastructure in our modules but only some of it. You just have to be aware of what resources you do need to create when running an `apply` operation, and for Azure this will certainly always include your resource groups.

An example of what it looks like to use the real published version of a module to fill a dependency looks like the following:

```
run "setup_resource_group" {
  variables {
    location = "swedencentral"
    tags = {
      team        = "HashiTalks Team"
      project     = "HashiTalks Project"
      cost_center = "1234"
    }
  }

  module {
    source  = "app.terraform.io/mattias-fjellstrom/resource-group-module/hashitalks"
    version = "3.1.0"
  }
}

```

This is a `run` block with the sole purpose of setting up required dependencies. In the `module` block I reference my published version of the resource group module in my private Terraform registry. Note that if you do it like this and you run your tests (locally, in a CI/CD pipeline, or in Terraform Cloud) you must configure credentials so that the tests can access the private module.

Once this `run` block is done you can reference the output from the resource group module in your following tests:

```
run "should_not_allow_vnet_name_prefix" {
  command = plan

  variables {
    name_suffix    = "vnet-test"
    resource_group = run.setup_resource_group.resource_group
  }

  expect_failures = [
    var.name_suffix,
  ]
}

```

If we instead opt for option 2 above, to use a helper module, the code only changes slightly. In the setup `run` block we reference a local module:

```
run "setup_resource_group" {
  variables {
    resource_group_name     = "rg-hashitalks"
    resource_group_location = "swedencentral"
  }

  module {
    source = "./testing/resource-group"
  }
}

```

The module located in `./testing/resource-group` might look similar to the published version, but it could be simplified a lot to just produce exactly what is needed for the test. Referencing output from this `run` block works exactly like in the previous example.

An example of what we need to do to use static values for the dependency is shown below:

```
variables {
  resource_group = {
    name     = "rg-hashitalks"
    location = "swedencentral"
    tags = {
      team        = "HashiTalks Team"
      project     = "HashiTalks Project"
      cost_center = "1234"
    }
  }
}

```

In this case we have a global `variables` block defining a `resource_group` variable. This variable will automatically be used by the tests unless we override it locally inside of a `run` block.

Remember in the last section (or layer) how we tested different permutations of locations and versions using GitHub Actions? When it comes to integration testing with modules we might be interested in testing dependencies between different versions of two modules. To do this we can setup a similar test like we did in the previous section. I will use the same template approach, with the following template:

```
variables {
  name_suffix = "hashitalks-${uuid()}"
  // other variables left out for brevity
}

run "set_up_resource_group" {
  module {
    source  = "app.terraform.io/mattias-fjellstrom/resource-group-module/hashitalks"
    version = "{{RESOURCE_GROUP_VERSION}}"
  }
}

run "set_up_virtual_network" {
  variables {
    // left out for brevity
  }

  module {
    source  = "app.terraform.io/mattias-fjellstrom/network-module/hashitalks"
    version = "{{NETWORK_VERSION}}"
  }
}

```

Note once again that I am using the `uuid()` function to create a `name_suffix` variable that will be unique, because otherwise I would get tests trying to create resources with the same name.

For my modules I have replaced the static version number with placeholders: `{{RESOURCE_GROUP_VERSION}}` and `{{NETWORK_VERSION}}`.

In my GitHub Actions workflow I use the following settings:

```
jobs:
  test:
    strategy:
      fail-fast: false
      matrix:
        rg_version: ["3.0.0", "3.1.0"]
        vnet_version: ["2.1.0", "3.0.0"]
    runs-on: ubuntu-latest
    name: R ${{ matrix.rg_version }} - N ${{ matrix.vnet_version }}
    
    // ... rest of workflow is the same as before

```

I am testing the compatibility of two versions of the resource group module and two versions of the network module. In total this will result in four different test runs. You can construct the matrix in a way that makes sense for you, for instance if you want to have the last three versions of each module be available for your consumers then you might want to include them in this matrix.

#### Layer 4: Testing all the modules! End-to-end scenario testing.

The next layer of tests involve complex infrastructure and complex operations.

You might have a large number of modules that you are supporting and developing for your organization. There might also be a few suggested use cases of your modules that you have in mind. In the ongoing example of this post there is a suggested way of how these modules should be combined.

In our imaginary organization we have an idea of how our modules fit together to create Kubernetes clusters frontend by an Azure Traffic Manager.

![test case](https://assets.mattias.engineer/posts/hashitalks-2024/03-new.png)test case
If this scenario is important for our organization we should have tests for it. To do this we will use another dedicated test module, i.e. a module with the sole purpose of testing. The test file is long and complex, and involves some complications. Below I will go through the file step by step, but you can see the full test file [on GitHub](https://github.com/mattias-fjellstrom-demo/terraform-hashitalks-integration-module/blob/main/tests/e2e.tftest.hcl).

The first step is to configure the AzureRM provider:

```
provider "azurerm" {
  features {}
}

```

This step is required for Azure because the minimum amount of configuration for this provider is an empty `features` block. You might also need to configure credentials at this point, but this can also be done via environment variables or some other means.

Next up we define global variables:

```
variables {
  name_suffix = "hashitalks2024"
}

```

The `name_suffix` variable is used in most of the modules we will use, thus it makes sense to keep it as a global variable.

Since we are creating Azure infrastructure the first dependency we need to set up is the resource group:

```
run "setup_resource_group" {
  variables {
    location = "swedencentral"
    tags = {
      team        = "HashiTalks Team"
      project     = "HashiTalks Project"
      cost_center = "1234"
    }
  }

  module {
    source  = "app.terraform.io/mattias-fjellstrom/resource-group-module/hashitalks"
    version = "3.1.0"
  }
}

```

We have seen this before, we use the published version of the resource group module and provide the required variables to it. Following the resource group we do the same thing with the virtual network:

```
run "setup_virtual_network" {
  variables {
    resource_group  = run.setup_resource_group.resource_group
    vnet_cidr_range = "10.0.0.0/16"
    subnets = [
      {
        name              = "aks01"
        subnet_cidr_range = "10.0.10.0/24"
      },
      {
        name              = "aks02"
        subnet_cidr_range = "10.0.20.0/24"
      }
    ]
  }

  module {
    source  = "app.terraform.io/mattias-fjellstrom/network-module/hashitalks"
    version = "3.0.0"
  }
}

```

We define two subnets for our virtual network, one subnet each for the Kubernetes clusters.

Now we are in a position where we would like to create the two Kubernetes clusters using our AKS module. In your first iteration you might add two run blocks, each calling the AKS module, and each configuring the cluster accordingly. However, this approach will not work. This is because the test framework keeps one state file for each module you reference in a `run` block. So the first reference of the AKS module would create a state file containing our first Kubernetes cluster. The following `run` block referencing the same AKS module would update the state file, which in practice would create a new Kubernetes cluster and delete the old one. We would be left with a single cluster! To get around this we create a helper module and reference that instead:

```
run "setup_clusters" {
  variables {
    resource_group = run.setup_resource_group.resource_group
    subnet01       = run.setup_virtual_network.subnets[0]
    subnet02       = run.setup_virtual_network.subnets[1]
  }

  module {
    source = "./helper/cluster"
  }
}

```

The helper module takes the resource group and the subnets as input. The main part of the helper module itself looks like this:

```
// ./helper/cluster/main.tf
module "cluster01" {
  source                   = "app.terraform.io/mattias-fjellstrom/aks-module/hashitalks"
  version                  = "2.0.0"
  environment              = "prod"
  name_suffix              = "aks01"
  resource_group           = var.resource_group
  subnet                   = var.subnet01
  node_resource_group_name = "rg-cluster01-node-resources"
}

module "cluster02" {
  source                   = "app.terraform.io/mattias-fjellstrom/aks-module/hashitalks"
  version                  = "2.0.0"
  environment              = "prod"
  name_suffix              = "aks02"
  resource_group           = var.resource_group
  subnet                   = var.subnet02
  node_resource_group_name = "rg-cluster02-node-resources"
}

output "cluster01_kubeconfig" {
  value     = module.cluster01.kube_config
  sensitive = true
}

output "cluster02_kubeconfig" {
  value     = module.cluster02.kube_config
  sensitive = true
}

```

We create the two clusters using our desired AKS module, and we output the kube config for each cluster.

Next up in our test we would like to configure the Kubernetes platform. We might try to do this in the same helper module as for the clusters, but it is easier to split it up into separate steps. So we use another helper module:

```
run "setup_kubernetes_platforms" {
  variables {
    kube_config01 = run.setup_clusters.cluster01_kubeconfig
    kube_config02 = run.setup_clusters.cluster02_kubeconfig
  }

  module {
    source = "./helper/platform"
  }
}

```

The platform helper module works exactly like the cluster helper module, it creates two instances of the platform module.

Now we are ready to start deploying sample applications to our clusters. To do this we will first configure two Kubernetes providers:

```
provider "kubernetes" {
  alias                  = "cluster01"
  host                   = run.setup_clusters.cluster01_kubeconfig.host
  client_certificate     = base64decode(run.setup_clusters.cluster01_kubeconfig.client_certificate)
  client_key             = base64decode(run.setup_clusters.cluster01_kubeconfig.client_key)
  cluster_ca_certificate = base64decode(run.setup_clusters.cluster01_kubeconfig.cluster_ca_certificate)
}

provider "kubernetes" {
  alias                  = "cluster02"
  host                   = run.setup_clusters.cluster02_kubeconfig.host
  client_certificate     = base64decode(run.setup_clusters.cluster02_kubeconfig.client_certificate)
  client_key             = base64decode(run.setup_clusters.cluster02_kubeconfig.client_key)
  cluster_ca_certificate = base64decode(run.setup_clusters.cluster02_kubeconfig.cluster_ca_certificate)
}

```

This is a new feature in Terraform 1.7, we can configure a provider using output from `run` blocks. This allows us to not having to define all providers upfront. Using the configured providers we can create two sample applications using an application module, and since we want to use the same module twice we have to do it using a helper module:

```
run "setup_applications" {
  providers = {
    kubernetes.cluster01 = kubernetes.cluster01
    kubernetes.cluster02 = kubernetes.cluster02
  }

  module {
    source = "./helper/apps"
  }
}

```

We do not know the IP addresses of the applications upfront, so we need to query the clusters for this information. This demonstrates another use of helper modules, to query for information. The `run` block looks like this:

```
run "query_service_ips" {
  providers = {
    kubernetes.cluster01 = kubernetes.cluster01
    kubernetes.cluster02 = kubernetes.cluster02
  }

  module {
    source = "./helper/service-ip"
  }
}

```

And the relevant parts of the helper module looks like this:

```
resource "time_sleep" "this" {
  create_duration = "60s"
}

data "kubernetes_service" "service01" {
  provider = kubernetes.cluster01
  metadata {
    name = "hello-hashitalks-svc"
  }
  depends_on = [time_sleep.this]
}

data "kubernetes_service" "service02" {
  provider = kubernetes.cluster02
  metadata {
    name = "hello-hashitalks-svc"
  }
  depends_on = [time_sleep.this]
}

output "service01_ip" {
  value = data.kubernetes_service.service01.status[0].load_balancer[0].ingress[0].ip
}

output "service02_ip" {
  value = data.kubernetes_service.service02.status[0].load_balancer[0].ingress[0].ip
}

```

We use the time provider to give the clusters some time to settle down and actually assign IP addresses to our services. Next we use a `kubernetes_service` data source to query for the IP addresses we want, and we set the IP addresses as output from the module.

We’re soon at the end of the test, but we still have things to set up: the traffic manager:

```
run "set_up_traffic_manager" {
  variables {
    resource_group = run.setup_resource_group.resource_group
    endpoints = [
      {
        name     = "cluster01"
        target   = run.query_service_ips.service01_ip
        priority = 100
        enabled  = true
      },
      {
        name     = "cluster02"
        target   = run.query_service_ips.service02_ip
        priority = 200
        enabled  = false
      }
    ]
  }

  module {
    source  = "app.terraform.io/mattias-fjellstrom/traffic-manager-module/hashitalks"
    version = "1.0.0"
  }
}

```

We create the traffic manager using two endpoints, one for each application in their respective cluster. We enable the first endpoint and disable the second endpoint.

This finally means we can run our first actual test, in the traditional sense. We want to verify that if we send a request to the traffic manager we reach the application running in the first cluster:

```
run "poll_traffic_manager_app01" {
  variables {
    fqdn    = run.set_up_traffic_manager.traffic_manager_profile.fqdn
    trigger = "test-app-01"
  }

  module {
    source = "./helper/http"
  }

  assert {
    condition     = data.http.tm.status_code == 200
    error_message = "Invalid response code from app01: ${data.http.tm.status_code}"
  }

  assert {
    condition     = strcontains(data.http.tm.response_body, "Hello HashiTalks 2024 v1!")
    error_message = "Invalid response body from app01"
  }
}

```

To send the request we use a helper module, this module uses the HTTP data source:

```
// ./helper/http/main.tf
data "http" "tm" {
  depends_on = [time_sleep.sleep]
  url        = "http://${var.fqdn}"
}

output "response" {
  value = data.http.tm.response_body
}

```

We make two assertions, we expect the status code to be 200 and that the response contains the string *Hello HashiTalks 2024 v1!*.

Next we want to change so that the traffic manager points at the application running in the second cluster. We do this by calling the traffic manager module again, this time accepting that the state is updated:

```
run "update_traffic_manager_endpoints" {
  variables {
    resource_group = run.setup_resource_group.resource_group
    endpoints = [
      {
        name     = "cluster01"
        target   = run.query_service_ips.service01_ip
        priority = 100
        enabled  = false
      },
      {
        name     = "cluster02"
        target   = run.query_service_ips.service02_ip
        priority = 200
        enabled  = true
      }
    ]
  }

  module {
    source  = "app.terraform.io/mattias-fjellstrom/traffic-manager-module/hashitalks"
    version = "1.0.0"
  }
}

```

Here we disable the first endpoint and enable the second endpoint. After this is done we can once again query the traffic manager endpoint, but this time expect a different response:

```
run "poll_traffic_manager_app02" {
  variables {
    fqdn    = run.set_up_traffic_manager.traffic_manager_profile.fqdn
    trigger = "test-app-02"
  }

  module {
    source = "./helper/http"
  }

  assert {
    condition     = data.http.tm.status_code == 200
    error_message = "Invalid response code from app02: ${data.http.tm.status_code}"
  }

  assert {
    condition     = strcontains(data.http.tm.response_body, "Hello HashiTalks 2024 v2!")
    error_message = "Invalid response body from app02"
  }
}

```

The difference here is that we expect the response body to contain *Hello HashiTalks 2024 v2!* instead.

This concludes the test! If everything succeeds it means we have verified that we can set up the desired infrastructure, we were able to deploy sample applications, we could retrieve relevant information from the resources, and perform a switch of endpoints in our traffic manager and verify that the response was OK before and after. Not bad!

This was one example of a fairly complex test involving many moving pieces. It demonstrated how helper modules are required to perform things as setting up dependencies and query for information. When it comes to setting up dependencies we see that we are required to use a helper module if we want to reference the same module twice or more times without having issues with the state.

How often should you run tests like this? Most likely you want to do this for each new revision of one or more of your modules that are part of the test. Define a strategy that makes sense for you and your organization.

#### Layer 5: Some things are not tests. Some things are policies.

In the fifth and last layer we take a wholistic view of all of our usage of Terraform. Remember how I added validation for the `location` variable in my resource group module? I made sure that the provided value was one of three allowed locations. This is the type of validation that might seep into many of your modules.

If I have hundreds of modules that each include the same `location` variable with the same validation logic, then it is easy to see how it will be an administrative nightmare whenever I need to change this validation logic.

Another issue with this validation logic is that it is only present in the modules that we are in charge of. Your development teams might be using their own modules, third-party modules, or just plain resources in the root module. Of course we would like to have the same validation no matter where the resources are coming from.

This is a case where a policy makes more sense than validation logic and tests. A policy allows us to verify that all Terraform configuration fulfils the rules we set.

In our imaginary scenario we are deploying our workloads on Azure. A good first idea could be to use the native Azure Policy service to set up the policies we are interested of. This might, or might not, play well with Terraform Cloud. In a best case scenario Azure would tell Terraform that a policy violation is about to happen during the plan phase. However, this might not be true always. Some plans might go through without any issues and Terraform would move on to the apply operation and eventually error out. Luckily we are using Terraform Cloud and it includes options for policy-as-code! We can pick from HashiCorp Sentinel policies or Open Policy Agent (OPA) OPA policies written in Rego.

Personally I prefer Sentinel policies because I think they are easier to write. The end result will be the same no matter what language we write the policies in.

We can add all our policies in a dedicated repository and then connect the repository to our Terraform Cloud organization. It might make sense to have a small number of policies that we will enforce on every workspace in the whole organization. Then we could have other repositories with more specific policies for certain workspaces, for instance production workloads.

Working with Sentinel policies in a repository connected to Terraform Cloud is a lot more convenient than setting up something similar for Azure Policy, although it is possible to do so.

If we were using additional providers apart from Azure we can also see how using Sentinel policies in Terraform Cloud is a better approach, because then we can centralize our policies in one place with one tool.

An example of what a policy to replace the location validation would look like is this:

```
// allowed-locations-for-azure-resources.sentinel
import "tfplan/v2" as tfplan

allowedLocations = ["swedencentral", "westeurope", "northeurope"]

allAzureResources = filter tfplan.resource_changes as _, resource_changes {
    resource_changes.provider_name is "registry.terraform.io/hashicorp/azurerm" and
    resource_changes.change.actions contains "create"
}

locationsAreAllowed = rule {
    all allAzureResources as _, azureResources {
        azureResources.change.after.location in allowedLocations
    }
}

main = rule {
	locationsAreAllowed
}

```

The currently allowed locations are stored in the `allowedLocations` variable. The policy looks at a Terraform plan file and finds all resources from the AzureRM provider that is about to be created and checks that the location is set to one of the allowed locations. To make this policy work when we connect the repository to Terraform Cloud we also must add a `sentinel.hcl` file:

```
// sentinel.hcl
policy "allowed-locations-for-azure-resources" {
  source            = "./allowed-locations-for-azure-resources.sentinel"
  enforcement_level = "hard-mandatory"
}

```

We can pick what `enforcement_level` we want from:

* **Advisory**: policies are allowed to fail but warnings will be displayed.
* **Soft Mandatory**: policies must pass unless an override has been configured. This allows for exceptions from policies, for instance if you must create a given resource in a different location than normally allowed. This might be the case for preview resources where it’s only available in certain locations during the preview period.
* **Hard Mandatory**: policies must pass and no overrides are possible.

When working with policies in your organization it is advisable to start small and expand the scope overtime. When introducing a new policy it makes sense to set the enforcement level to advisory to see how the policy behaves.

#### Summary and key takeaways

We have been through a journey through testing and validation with Terraform. If there is one major takeaway from this it would be **test your Terraform modules**. However, you should set the level of your testing depending on what needs you have. This might vary from module to module.

* Start by making sure your modules are user friendly. This involves limiting the number of required variables, providing sensible defaults for most variables, and most importantly adding validation to make sure only valid values are allowed. You should add custom conditions wherever it makes sense in your Terraform module in order to help your module consumers to use your module properly.
* Once that is in place, move on to the Terraform test framework. Start by adding tests to see if your validation logic works as intended. Add tests to verify that your providers are working as intended. As a first step with testing you can treat each module independently and avoid making the tests overly complex.
* Next up, start thinking about integration testing for your module estate. Turn your compatibility requirements into tests, for instance if your last three major versions of a module is expected to be supported together with a third-party module, make sure that this is the case by using integration tests. Use any technique that makes sense when it comes to integration testing: using the intended published module for dependencies, using helper modules, or mocking away the dependencies.
* Take the testing to the extreme by identifying use-cases or scenarios that your modules are intended to support. Build up end-to-end tests where you set up these scenarios. Tests in this category might involve multiple modules, multiple providers, and complex operations.
* Introduce policy-as-code in your organization. You might do this from day 1 or you might do it whenever your organization is ready for it. Start small with a set of common policies for the whole organization, then expand the scope and the number of policies successively. Use policy frameworks native to your platform, this could be Azure Policy or Sentinel policies in Terraform Cloud. It might make sense to keep policies in multiple locations as well.

1. Since I am using Microsoft Azure in this post it is proper to include a comparison with native tools for Azure when it comes to planning changes. Azure has its Azure Resource Manager, the underlying control plane API for resources in Azure. Creating infrastructure using a code approach in Azure long meant using ARM-templates. Along came Bicep, a DSL on top of ARM-templates. Bicep is a drastic improvement upon ARM-templates, and in many ways a better tool for infrastructure-as-code specifically for Azure. However, ARM-templates and Bicep have a surprisingly bad plan-type command called `what-if`. For simple templates you can mostly trust the output it gives you, but it quickly turns from somewhat useful to terrible. I know they are aware of this, and I believe there is work conducted to make `what-if` be a useful command. [↩︎](https://mattias.engineer/posts/hashitalks-2024/?utm_source=tldrdevops#fnref:1)

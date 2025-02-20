---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/cycloidioinframap-read-your-tfstate-or-hcl-to-generate-a-graph-specific-for-each-provider-showing-only-the-resources-that-are-most-importantrelevant/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/69ee1e8f6f3b75a0ef333dd0b77e3090dd5b270968c65b3f8ec7acb6e74eff9e/cycloidio/inframap)

#### Create list

Beta Lists are currently in beta. [Share feedback and report bugs.](https://github.com//github/feedback/discussions/categories/lists)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/cycloidio/inframap?resume=1)

### cycloidio/inframap

####  [README.md](https://github.com/cycloidio/inframap#readme)

[![](https://github.com/cycloidio/inframap/raw/master/docs/inframap-logo_color-RGB.png)](https://github.com/cycloidio/inframap/blob/master/docs/inframap-logo_color-RGB.png)
### InfraMap

[![PkgGoDev](https://camo.githubusercontent.com/14068000fc07ab656299d659400afec87ec6a8e7fd222982ebac69601ef866fa/68747470733a2f2f706b672e676f2e6465762f62616467652f6769746875622e636f6d2f6379636c6f6964696f2f696e6672616d6170)](https://pkg.go.dev/github.com/cycloidio/inframap)
[![AUR package](https://camo.githubusercontent.com/6d775a427e65b9bc8101ef997e61b757c74ba824eef8dbe9144ba9516aaf895d/68747470733a2f2f7265706f6c6f67792e6f72672f62616467652f76657273696f6e2d666f722d7265706f2f6175722f696e6672616d61702e737667)](https://repology.org/project/inframap/versions)
[![Homebrew](https://camo.githubusercontent.com/76113bcb03961ce30f46961dfd244b720737fa58f13ed350722ba926d5dc9b0b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f64796e616d69632f6a736f6e2e7376673f75726c3d68747470733a2f2f666f726d756c61652e627265772e73682f6170692f666f726d756c612f696e6672616d61702e6a736f6e2671756572793d242e76657273696f6e732e737461626c65266c6162656c3d686f6d6562726577)](https://formulae.brew.sh/formula/inframap)
[![Join the chat at https://gitter.im/cycloidio/inframap](https://camo.githubusercontent.com/77430f67aec7ea60f768c254fd9a22e58915c8f1be0288a729433aed15f2746b/68747470733a2f2f6261646765732e6769747465722e696d2f6379636c6f6964696f2f696e6672616d61702e737667)](https://gitter.im/cycloidio/inframap)
Read your tfstate or HCL to generate a graph specific for each provider, showing only the resources that are most important/relevant.

[![](https://github.com/cycloidio/inframap/raw/master/docs/inframap.png)](https://github.com/cycloidio/inframap/blob/master/docs/inframap.png)
#### Cloud Providers

We support **all** cloud providers, but we have some (listed below) that we have specific logic that allows us to better represent information that comes from these providers.

For the other providers the resulting representation will simply be all resources present without any simplification or refinement.

For TFState generations we are limited to versions 3 and 4.

| Provider | State | HCL | Grouping1 | External Nodes2 | IAM3 |
| --- | --- | --- | --- | --- | --- |
| [AWS](https://github.com/cycloidio/inframap/blob/master/docs/aws.png) | ✔️ | ✔️ | [WIP](https://github.com/cycloidio/inframap/issues/6) | ✔️ | ✖️ ([#11](https://github.com/cycloidio/inframap/issues/11)) |
| [Google](https://github.com/cycloidio/inframap/blob/master/docs/google-cloud.svg) | ✔️ | ✔️ | ✖️ | ✖️ | ✖️ |
| [Azure](https://github.com/cycloidio/inframap/blob/master/docs/azure.svg) | ✔️ | ✔️ | ✖️ | ✖️ | ✖️ |
| [OpenStack](https://github.com/cycloidio/inframap/blob/master/docs/Openstack-vertical-small.png) | ✔️ | ✔️ | ✖️ | ✖️ | ✖️ |
| [FlexibleEngine](https://github.com/cycloidio/inframap/blob/master/docs/flexibleengine.png) | ✔️ | ✔️ | ✖️ | ✖️ | ✖️ |

1. **Grouping**: Group elements that belong to the same group like VPCs or regions
2. **External Nodes**: Show the ingress of the Nodes if any
3. **IAM**: Connections based on IAM (Identity Access Management)

#### Installation

##### Stable

To install the latest release of Inframap, you can pick one of this methods:

* pull the latest release from the [Releases](https://github.com/cycloidio/inframap/releases/) page
* pull the latest docker [image](https://hub.docker.com/r/cycloid/inframap) from the Docker hub
* use your Linux package manager (only [AUR](https://aur.archlinux.org/packages/inframap) at the moment)

##### Development

You can build and install with the latest sources, you will enjoy the new features and bug fixes. It uses Go Modules (1.13+)

```
$ git clone https://github.com/cycloidio/inframap
$ cd inframap
$ go mod download
$ make build
```

##### Install via brew

If you're macOS user and using [Homebrew](https://brew.sh/), you can install via brew command:

```
$ brew install inframap
```

#### Usage

The `inframap --help` will show you the basics.

[![asciicast](https://camo.githubusercontent.com/9f5b2d6763b117744ee9bdd35d59a04f4fa8f111751e24b5760e3ea2f467933a/68747470733a2f2f61736369696e656d612e6f72672f612f3334373630302e737667)](https://asciinema.org/a/347600)
The most important subcommands are:

* `generate`: generates the graph from STDIN or file.
* `prune`: removes all unnecessary information from the state or HCL (not supported yet) so it can be shared without any security concerns

##### Example

Visualizing with [dot](https://graphviz.org/download/)

```
$ inframap generate state.tfstate | dot -Tpng > graph.png
```

or from the terminal itself with [graph-easy](https://github.com/ironcamel/Graph-Easy)

```
$ inframap generate state.tfstate | graph-easy
```

or from HCL

```
$ inframap generate config.tf | graph-easy
```

or HCL module

```
$ inframap generate ./my-module/ | graph-easy
```

using docker image (assuming that your Terraform files are in the working directory)

```
$ docker run --rm -v ${PWD}:/opt cycloid/inframap generate /opt/terraform.tfstate
```

**Note:** InfraMap will guess the type of the input (HCL or TFState) by validating if it's a JSON and if it fails then we fallback to HCL (except if you send a directory on args, the it'll use HCL directly), to force one specific type you can use `--hcl` or `--tfstate` flags.

#### How is it different to `terraform graph`

[Terraform Graph](https://www.terraform.io/docs/commands/graph.html) outputs a dependency graph of all the resources on the tfstate/HCL. We try to go one step further, by trying to make it human-readable.

If the provider is not supported, the output will be closer to the Terraform Graph version (without displaying provider / variable nodes)

Taking <https://github.com/cycloid-community-catalog/stack-magento/> as a reference this is the difference in output:

With `terraform graph`:

[![](https://github.com/cycloidio/inframap/raw/master/docs/terraformgraph.svg)](https://github.com/cycloidio/inframap/blob/master/docs/terraformgraph.svg)
With `inframap generate ./terraform/module-magento/ | dot -Tpng > inframap.png`:

[![](https://github.com/cycloidio/inframap/raw/master/docs/inframap.png)](https://github.com/cycloidio/inframap/blob/master/docs/inframap.png)
With `inframap generate --connections=false ./terraform/module-magento/ | dot -Tpng > inframapconnections.png`:

[![](https://github.com/cycloidio/inframap/raw/master/docs/inframapconnections.png)](https://github.com/cycloidio/inframap/blob/master/docs/inframapconnections.png)
With `inframap generate ./terraform/module-magento/ --raw | dot -Tpng > inframapraw.png`:

[![](https://github.com/cycloidio/inframap/raw/master/docs/inframapraw.png)](https://github.com/cycloidio/inframap/blob/master/docs/inframapraw.png)
#### How does it work?

For each provider, we support specific types of connections; we have a static list of resources that can be nodes or edges. Once we identify the edges, we try to create one unique edge from the resources they connect.

For a state file, we rely on the `dependencies` key (for the <0.13 we replace all `depends_on` for `dependencies` so we support them) and, for HCL we rely on interpolation to create the base graph one which we then apply specific provider logic if supported. If not supported, then basic graph is returned.

#### FAQ

##### Why is my Graph generated empty?

If a graph is returned empty, it means that we support one of the providers you are using on your HCL/TFState but we do not recognize any connection or relevant node.

To show the configuration without any InfraMap applied logic you can use the `--raw` flag logic and print everything that we read. If it works, it would be good to try to know why it was empty before so we can take a look at it as it could potentially be an issue on InfraMap (open an issue if you want us to take a look).

By default unconnected nodes are removed, you can use `--clean=false` to prevent that.

##### Does InfraMap support Terraform backends ?

Terraform allows users to use `backends` (S3, Google Cloud Storage, Swift, etc.) in order to store the `terraform.state`. We currently do not support graph generation from `tfstate` stored in such backends. As mentioned in this [issue](https://github.com/cycloidio/inframap/issues/44), it is possible to play around `stdin/out` to generate graph from Terraform backends.

| backend | command |
| --- | --- |
| S3 | `aws s3 cp s3://bucket/path/to/your/file.tfstate - | inframap generate` |
| GCS | `gsutil cat gs://bucket/path/to/your/file.tfstate | inframap generate` |

A general solution is also to just use `terraform state pull \| inframap generate` as it'll pull the state from whichever backend is actually stored

#### License

Please see the [MIT LICENSE](https://github.com/cycloidio/inframap/blob/master/LICENSE) file.

#### Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

#### Meet Cycloid

[Cycloid](https://www.cycloid.io/) is a hybrid cloud DevOps collaboration platform providing end-to-end frameworks to accelerate and industrialize software delivery.

As of now, we have three open-source tools:

* [TerraCognita](https://github.com/cycloidio/terracognita): Read from your existing cloud providers and generate IaC in Terraform
* [InfraMap](https://github.com/cycloidio/inframap): Reads .tfstate or HCL to generate a graph specific for each provider
* [TerraCost](https://github.com/cycloidio/terracost): Cloud cost estimation for Terraform in the CLI

...and the functionality of each is also embedded in our DevOps solution, which you can find out more about [here](https://www.cycloid.io/hybrid-cloud-devops-platform).

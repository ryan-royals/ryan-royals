---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azureipam-ip-address-management-on-azure/","tags":["rw/articles"]}
---

![rw-book-cover](https://repository-images.githubusercontent.com/417262301/5d1ff5a1-688c-4311-8b5e-abf23b6cc5db)

#### Create list

Beta Lists are currently in beta. [Share feedback and report bugs.](https://github.com//github/feedback/discussions/categories/lists)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Azure/ipam?resume=1)

### Azure/ipam

####  [README.md](https://github.com/Azure/ipam#readme)

### Azure IPAM

Azure IPAM is a lightweight solution developed on top of the Azure platform designed to help Azure customers manage their IP Address space easily and effectively.

#### Repo Contents

| File/folder | Description |
| --- | --- |
| `.github/` | Bug Report & Issue Templates |
| `.vscode/` | VSCode Configuration |
| `deploy/` | Deployment Bicep Templates & PowerShell Deployment Scripts |
| `docs/` | Documentation Folder |
| `engine/` | Engine Application Code |
| `lb/` | Load Balancer (NGINX) Configs |
| `ui/` | UI Application Code |
| `.dockerignore` | Untracked Docker Files to Ignore |
| `.gitignore` | Untracked Git Files to Ignore |
| `CODE_OF_CONDUCT.md` | Microsoft Code of Conduct |
| `default.conf` | NGINX Default Configuration File |
| `default.dev.conf` | NGINX Development Default Configuration File |
| `docker-compose.prod.yml` | Production Docker Compose File |
| `docker-compose.yml` | Development Docker Compose File |
| `Dockerfile` | Development Dockerfile |
| `init.sh` | Single Container Init Script |
| `LICENSE` | Microsoft MIT License |
| `README.md` | This README File |
| `SECURITY.md` | Microsoft Open Source Security Information & Details |
| `sshd_config` | Container SSH Config File |
| `SUPPORT.md` | Support Contact Information |

#### Documentation

IPAM uses both [Docsify](https://docsify.js.org/) and [GitHub Pages](https://docs.github.com/en/github/working-with-github-pages) to present the project documentation, which can be found [here](https://azure.github.io/ipam/)

#### Questions or Comments for the team?

The IPAM team welcomes questions and contributions from the community. We have set up a GitHub Discussions page [here](https://github.com/Azure/ipam/discussions) to make it easy to engage with the IPAM team without opening an issue.

#### FAQ

**Why should I use IPAM?** You realize that you do not have a clear picture as to what is deployed into your Azure environment and connected to your private IP address space. Or, you would like a way to easily manage, assign, and track your private IP addess space usage!

**What does the roadmap for IPAM look like?**

* We are assessing leveraging Azure Container Apps for hosting the two containers that make up the IPAM application
* We are assessing support for multiple Tenants, as today the tool is designed with a single Tenant in mind
* We are working on capturing IP address infromation for resources that support hybrid connectivity (ie Gateways)

**Who are the awesome people that built this solution??** Matt and Harvey are Architects at Microsoft! We are always on the look out for interesting ways to help our customers overcome their challenges!

#### Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us the rights to use your contribution. For details, visit <https://cla.opensource.microsoft.com>.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

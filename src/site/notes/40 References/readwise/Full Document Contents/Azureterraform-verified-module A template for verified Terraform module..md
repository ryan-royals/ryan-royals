---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azureterraform-verified-module-a-template-for-verified-terraform-module/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/57c7c2d39201b023bd4990f96cf61071a1645379a37176d9b20cfca162fdf475/Azure/terraform-verified-module)

#### Create list

Beta Lists are currently in beta. [Share feedback and report bugs.](https://github.com//github/feedback/discussions/categories/lists)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Azure/terraform-verified-module?resume=1)

### Azure/terraform-verified-module

####  [README.md](https://github.com/Azure/terraform-verified-module#readme)

### Microsoft Verified Terraform Module

The Verified Terraform module is a template repository to help developers create their own Terraform Module.

As we've used Microsoft 1ES Runners Pool as our acceptance test runner, **only Microsoft members could use this template for now**.

Enjoy it by following steps:

1. Use [this template](https://github.com/Azure/terraform-verified-module) to create your repository.
2. Read [Onboard 1ES hosted Github Runners Pool through Azure Portal](https://eng.ms/docs/cloud-ai-platform/devdiv/one-engineering-system-1es/1es-docs/1es-github-runners/createpoolportal), install [1ES Resource Management](https://github.com/apps/1es-resource-management) on your repo.
3. Add a Github [Environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment) named **acctests** in your repo, setup [**Required Reviewers**](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#required-reviewers).
4. Update [`acc-test.yaml`](https://github.com/Azure/terraform-verified-module/blob/main/.github/workflows/acc-test.yaml), modify `runs-on: [self-hosted, 1ES.Pool=<YOUR_REPO_NAME>]` with your 1es runners' pool name (basically it's your repo's name).
5. Write Terraform code in a new branch.
6. Run `docker run --rm -v ${pwd}:/src -w /src mcr.microsoft.com/azterraform:latest make pre-commit` to format the code.
7. Run `docker run --rm -v $(pwd):/src -w /src mcr.microsoft.com/azterraform:latest make pr-check` to run the check in local.
8. Create a pull request for the main branch.
	* CI pr-check will be executed automatically.
	* Once pr-check was passed, with manually approval, the e2e test and version upgrade test would be executed.
9. Merge pull request.
10. Enjoy it!

#### Requirements

| Name | Version |
| --- | --- |
| [terraform](https://github.com/Azure/terraform-verified-module#requirement_terraform) | >= 1.1 |
| [null](https://github.com/Azure/terraform-verified-module#requirement_null) | >= 3.1 |

#### Providers

| Name | Version |
| --- | --- |
| [null](https://github.com/Azure/terraform-verified-module#provider_null) | >= 3.1 |

#### Modules

No modules.

#### Resources

| Name | Type |
| --- | --- |
| [null\_resource.nop](https://registry.terraform.io/providers/hashicorp/null/latest/docs/resources/resource) | resource |

#### Inputs

| Name | Description | Type | Default | Required |
| --- | --- | --- | --- | --- |
| [echo\_text](https://github.com/Azure/terraform-verified-module#input_echo_text) | The text to echo | `string` | n/a | yes |

#### Outputs

| Name | Description |
| --- | --- |
| [echo\_text](https://github.com/Azure/terraform-verified-module#output_echo_text) | The text to echo |

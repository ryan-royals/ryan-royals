---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/version-2-of-the-packer-azure-plugin-is-now-available/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1675791969-products-og-img-packer.png)

We're excited to announce the version 2.0.0 release of the [Packer Azure plugin](https://github.com/hashicorp/packer-plugin-azure), which enables users to build Azure virtual hard disks, managed images, and Compute Gallery (shared image gallery) images. The plugin is one of the most popular ways to build Azure Virtual Machine images and is used by Microsoft Azure via the [Azure Image Builder](https://learn.microsoft.com/en-us/azure/virtual-machines/image-builder-overview?tabs=azure-powershell)

For the past year, we have been tracking the changes to the Azure SDKs and keeping our eyes on the upcoming deprecations, which were sure to disrupt how Packer interacts with Azure. When we found that the version of the Azure SDK the Packer plugin was using would soon be [deprecated](https://azure.github.io/azure-sdk/releases/deprecated/index.html) we began work to migrate to the Terraform tested [HashiCorp Go Azure SDK](https://github.com/hashicorp/go-azure-sdk). The HashiCorp Go Azure SDK is generated from and based on the Azure API definitions to provide parity with the official Azure SDK — making it a near drop-in replacement for the Azure SDK, with the ability to resolve issues around auto-rest, polling, and API versioning. Version 2.0.0 of the Packer Azure plugin addresses the known deprecations with minimal disruption to the user, introduces new highly requested features, and combines the stability of the Packer Azure plugin with the Terraform Azure provider

Many users want to bring their own authentication provider when connecting to Azure, and some organizations have policies requiring this. Version 2 of the Packer Azure plugin supports using an OIDC provider to authenticate to Azure using the `client_jwt` field in the builder configuration. You can follow [this guide](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure) to setting up GitHub as your OIDC Provider and adding its federated credentials to Azure. For example, configuring a GitHub action like this:

```

  	available: "${{ steps.check-secrets.outputs.available }}"

      	echo "ARM_OIDC_TOKEN=$(curl -H "Accept: application/json; api-version=2.0" -H "Authorization: Bearer ${ACTIONS_ID_TOKEN_REQUEST_TOKEN}" -H "Content-Type: application/json" -G --data-urlencode "audience=api://AzureADTokenExchange" "${ACTIONS_ID_TOKEN_REQUEST_URL}" | jq -r '.value')"  >>${GITHUB_ENV}

    	uses: actions/setup-go@4d34df0c2316fe8122ab82dc22947d607c0c91f9 # v4.0.0
      	go-version: '1.19.5'

```

And using this example Packer template with the client\_jwt set as our GitHub provided OIDC token:

```

  location                          = "westus"
  managed_image_name                = "oidc-example"
  winrm_timeout                     = "3m"
  winrm_use_ssl                     = "true"

  sources = ["source.azure-arm.oidc"]

```

Beginning with version 2, the Packer Azure plugin now supports only PKCS#12 bundle (.pfx file) for client certificate authentication. For more information on generating a pfx cert and adding it to Azure, check out the [Terraform Azure provider documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_certificate#generating-a-client-certificate). Certificates encoded in the .pem format, which previously worked in the Azure plugin, will no longer be recognized by the plugin.

Historically, the Packer Azure plugin notified users that Azure VHD (virtual hard disk) builds were deprecated and would be removed at a later date. This has led to confusion on whether users can rely on VHD functionality remaining in the plugin, and when or if they will be forced to migrate. We found that many users continue to build VHD images using the Packer Azure plugin, so we decided to remove the deprecation warning. VHD builds will continue to work on v2.0.0 of Azure, and we have no plans to deprecate it again in the immediate future.

We also made changes to let the plugin fail faster when users are creating an image build that won't succeed based on invalid shared image gallery version values. We also added support for setting a WinRM expiration time for Azure tenants/subscriptions that have that policy requirement. You can find a full list of changes in the [Packer Azure plugin release notes](https://github.com/hashicorp/packer-plugin-azure/releases/tag/v2.0.0).

Please report any issues with and share your feedback on Version 2.0.0 in the [Packer Azure plugin GitHub issue tracker](https://github.com/hashicorp/packer-plugin-azure/issues).

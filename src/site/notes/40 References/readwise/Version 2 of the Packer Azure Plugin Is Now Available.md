---
{"dg-publish":true,"permalink":"/40-references/readwise/version-2-of-the-packer-azure-plugin-is-now-available/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1675791969-products-og-img-packer.png)

## Full Document
[[40 References/readwise/Full Document Contents/Version 2 of the Packer Azure Plugin Is Now Available\|Readwise/Full Document Contents/Version 2 of the Packer Azure Plugin Is Now Available.md]]

## Highlights
Many users want to bring their own authentication provider when connecting to Azure, and some organizations have policies requiring this. Version 2 of the Packer Azure plugin supports using an OIDC provider to authenticate to Azure using the `client_jwt` field in the builder configuration. You can follow [this guide](https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-azure) to setting up GitHub as your OIDC Provider and adding its federated credentials to Azure. For example, configuring a GitHub action like this: ([View Highlight] (https://read.readwise.io/read/01hrdp6kf3gcn5z0ajp05s6yj5))


steps: - name: Set OIDC Token run: | echo "ARM_OIDC_TOKEN=$(curl -H "Accept: application/json; api-version=2.0" -H "Authorization: Bearer ${ACTIONS_ID_TOKEN_REQUEST_TOKEN}" -H "Content-Type: application/json" -G --data-urlencode "audience=api://AzureADTokenExchange" "${ACTIONS_ID_TOKEN_REQUEST_URL}" | jq -r '.value')" >>${GITHUB_ENV} ([View Highlight] (https://read.readwise.io/read/01hrdp79cfpsr984awdf54tvvj))


- name: Try to run an AzureARM build with our OIDC token run: packer build -force ./example/oidc-example.pkr.hcl env: ARM_CLIENT_ID: ${{ secrets.ARM_CLIENT_ID}} ARM_SUBSCRIPTION_ID: ${{ secrets.ARM_SUBSCRIPTION_ID}} ([View Highlight] (https://read.readwise.io/read/01hrdpbkaxxasafk77zmda6ttt))



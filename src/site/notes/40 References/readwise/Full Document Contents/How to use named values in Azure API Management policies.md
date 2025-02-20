---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/how-to-use-named-values-in-azure-api-management-policies/","tags":["rw/articles"]}
---

![rw-book-cover](https://learn.microsoft.com/en-us/media/open-graph-image.png)

#### In this article

1. [Value types](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#value-types)
2. [Key vault secrets](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#key-vault-secrets)
3. [Prerequisites](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#prerequisites)
4. [Add or edit a named value](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#add-or-edit-a-named-value)
5. [Use a named value](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#use-a-named-value)
6. [Delete a named value](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#delete-a-named-value)
7. [Next steps](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#next-steps)

[API Management policies](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies) are a powerful capability of the system that allow the publisher to change the behavior of the API through configuration. Policies are a collection of statements that are executed sequentially on the request or response of an API. Policy statements can be constructed using literal text values, policy expressions, and named values.

*Named values* are a global collection of name/value pairs in each API Management instance. There is no imposed limit on the number of items in the collection. Named values can be used to manage constant string values and secrets across all API configurations and policies.

![Named values in the Azure portal](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-howto-properties/named-values.png)
#### Value types

| Type | Description |
| --- | --- |
| Plain | Literal string or policy expression |
| Secret | Literal string or policy expression that is encrypted by API Management |
| [Key vault](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#key-vault-secrets) | Identifier of a secret stored in an Azure key vault. |

Plain values or secrets can contain [policy expressions](https://learn.microsoft.com/en-us/azure/api-management/api-management-policy-expressions). For example, the expression `@(DateTime.Now.ToString())` returns a string containing the current date and time.

For details about the named value attributes, see the API Management [REST API reference](https://learn.microsoft.com/en-us/rest/api/apimanagement/current-ga/named-value/create-or-update).

#### Key vault secrets

Secret values can be stored either as encrypted strings in API Management (custom secrets) or by referencing secrets in [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/general/overview).

Using key vault secrets is recommended because it helps improve API Management security:

* Secrets stored in key vaults can be reused across services
* Granular [access policies](https://learn.microsoft.com/en-us/azure/key-vault/general/security-features#privileged-access) can be applied to secrets
* Secrets updated in the key vault are automatically rotated in API Management. After update in the key vault, a named value in API Management is updated within 4 hours. You can also manually refresh the secret using the Azure portal or via the management REST API.

#### Prerequisites

* If you have not created an API Management service instance yet, see [Create an API Management service instance](https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance).

##### Prerequisites for key vault integration

* If you don't already have a key vault, create one. For steps to create a key vault, see [Quickstart: Create a key vault using the Azure portal](https://learn.microsoft.com/en-us/azure/key-vault/general/quick-create-portal).

 To create or import a secret to the key vault, see [Quickstart: Set and retrieve a secret from Azure Key Vault using the Azure portal](https://learn.microsoft.com/en-us/azure/key-vault/secrets/quick-create-portal).
* Enable a system-assigned or user-assigned [managed identity](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-use-managed-service-identity) in the API Management instance.

##### Configure access to key vault

1. In the portal, navigate to your key vault.
2. In the left menu, select **Access configuration**, and note the **Permission model** that is configured.
3. Depending on the permission model, configure either a [key vault access policy](https://learn.microsoft.com/en-us/azure/key-vault/general/assign-access-policy) or [Azure RBAC access](https://learn.microsoft.com/en-us/azure/key-vault/general/rbac-guide) for an API Management managed identity.

 **To add a key vault access policy:**

	1. In the left menu, select **Access policies**.
	2. On the **Access policies** page,select **+ Create**.
	3. On the **Permissions** tab, under **Secret permissions**, select **Get** and **List**, then select **Next**.
	4. On the **Principal** tab, **Select principal**, search for the resource name of your managed identity, and then select **Next**. If you're using a system-assigned identity, the principal is the name of your API Management instance.
	5. Select **Next** again. On the **Review + create** tab, select **Create**.**To configure Azure RBAC access:**

	1. In the left menu, select **Access control (IAM)**.
	2. On the **Access control (IAM)** page, select **Add role assignment**.
	3. On the **Role** tab, select **Key Vault Secrets User**.
	4. On the **Members** tab, select **Managed identity** > **+ Select members**.
	5. On the **Select managed identity** page, select the system-assigned managed identity or a user-assigned managed identity associated with your API Management instance, and then select **Select**.
	6. Select **Review + assign**.

###### Requirements for Key Vault firewall

If [Key Vault firewall](https://learn.microsoft.com/en-us/azure/key-vault/general/network-security) is enabled on your key vault, the following are additional requirements:

* You must use the API Management instance's **system-assigned** managed identity to access the key vault.
* In Key Vault firewall, enable the **Allow Trusted Microsoft Services to bypass this firewall** option.
* Ensure that your local client IP address is allowed to access the key vault temporarily while you select a certificate or secret to add to Azure API Management. For more information, see [Configure Azure Key Vault networking settings](https://learn.microsoft.com/en-us/azure/key-vault/general/how-to-azure-key-vault-network-security).

 After completing the configuration, you may block your client address in the key vault firewall.

###### Virtual network requirements

If the API Management instance is deployed in a virtual network, also configure the following network settings:

* Enable a [service endpoint](https://learn.microsoft.com/en-us/azure/key-vault/general/overview-vnet-service-endpoints) to Azure Key Vault on the API Management subnet.
* Configure a network security group (NSG) rule to allow outbound traffic to the AzureKeyVault and AzureActiveDirectory [service tags](https://learn.microsoft.com/en-us/azure/virtual-network/service-tags-overview).

For details, see [Network configuration when setting up Azure API Management in a VNet](https://learn.microsoft.com/en-us/azure/api-management/virtual-network-reference).

#### Add or edit a named value

##### Add a key vault secret to API Management

See [Prerequisites for key vault integration](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#prerequisites-for-key-vault-integration).

Important

When adding a key vault secret to your API Management instance, you must have permissions to list secrets from the key vault.

Caution

When using a key vault secret in API Management, be careful not to delete the secret, key vault, or managed identity used to access the key vault.

1. In the [Azure portal](https://portal.azure.com), navigate to your API Management instance.
2. Under **APIs**, select **Named values** > **+Add**.
3. Enter a **Name** identifier, and enter a **Display name** used to reference the property in policies.
4. In **Value type**, select **Key vault**.
5. Enter the identifier of a key vault secret (without version), or choose **Select** to select a secret from a key vault.

  Important

 If you enter a key vault secret identifier yourself, ensure that it doesn't have version information. Otherwise, the secret won't rotate automatically in API Management after an update in the key vault.
6. In **Client identity**, select a system-assigned or an existing user-assigned managed identity. Learn how to [add or modify managed identities in your API Management service](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-use-managed-service-identity).

  Note

 The identity needs permissions to get and list secrets from the key vault. If you haven't already configured access to the key vault, API Management prompts you so it can automatically configure the identity with the necessary permissions.
7. Add one or more optional tags to help organize your named values, then **Save**.
8. Select **Create**.

  ![Add key vault secret value](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-howto-properties/add-property.png)

##### Add a plain or secret value to API Management

* [Portal](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#tabpanel_1_azure-portal)
* [Azure CLI](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-properties?tabs=azure-portal#tabpanel_1_azure-cli)

1. In the [Azure portal](https://portal.azure.com), navigate to your API Management instance.
2. Under **APIs**, select **Named values** > **+Add**.
3. Enter a **Name** identifier, and enter a **Display name** used to reference the property in policies.
4. In **Value type**, select **Plain** or **Secret**.
5. In **Value**, enter a string or policy expression.
6. Add one or more optional tags to help organize your named values, then **Save**.
7. Select **Create**.

Once the named value is created, you can edit it by selecting the name. If you change the display name, any policies that reference that named value are automatically updated to use the new display name.

To begin using Azure CLI:

* Use the Bash environment in [Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/overview). For more information, see [Quickstart for Bash in Azure Cloud Shell](https://learn.microsoft.com/en-us/azure/cloud-shell/quickstart).

 [![](https://learn.microsoft.com/en-us/azure/reusable-content/azure-cli/media/hdi-launch-cloud-shell.png)](https://shell.azure.com)
* If you prefer to run CLI reference commands locally, [install](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) the Azure CLI. If you're running on Windows or macOS, consider running Azure CLI in a Docker container. For more information, see [How to run the Azure CLI in a Docker container](https://learn.microsoft.com/en-us/cli/azure/run-azure-cli-docker).

	+ If you're using a local installation, sign in to the Azure CLI by using the [az login](https://learn.microsoft.com/en-us/cli/azure/reference-index#az-login) command. To finish the authentication process, follow the steps displayed in your terminal. For other sign-in options, see [Sign in with the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/authenticate-azure-cli).
	+ When you're prompted, install the Azure CLI extension on first use. For more information about extensions, see [Use extensions with the Azure CLI](https://learn.microsoft.com/en-us/cli/azure/azure-cli-extensions-overview).
	+ Run [az version](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-version) to find the version and dependent libraries that are installed. To upgrade to the latest version, run [az upgrade](https://learn.microsoft.com/en-us/cli/azure/reference-index?#az-upgrade).

To add a named value, use the [az apim nv create](https://learn.microsoft.com/en-us/cli/azure/apim/nv#az-apim-nv-create) command:

Azure CLI 

```
az apim nv create --resource-group apim-hello-word-resource-group \
    --display-name "named_value_01" --named-value-id named_value_01 \
    --secret true --service-name apim-hello-world --value test

```

After you create a named value, you can update it by using the [az apim nv update](https://learn.microsoft.com/en-us/cli/azure/apim/nv#az-apim-nv-update) command. To see all your named values, run the [az apim nv list](https://learn.microsoft.com/en-us/cli/azure/apim/nv#az-apim-nv-list) command:

Azure CLI 

```
az apim nv list --resource-group apim-hello-word-resource-group \
    --service-name apim-hello-world --output table

```

To see the details of the named value you created for this example, run the [az apim nv show](https://learn.microsoft.com/en-us/cli/azure/apim/nv#az-apim-nv-show) command:

Azure CLI 

```
az apim nv show --resource-group apim-hello-word-resource-group \
    --service-name apim-hello-world --named-value-id named_value_01

```

This example is a secret value. The previous command does not return the value. To see the value, run the [az apim nv show-secret](https://learn.microsoft.com/en-us/cli/azure/apim/nv#az-apim-nv-show-secret) command:

Azure CLI 

```
az apim nv show-secret --resource-group apim-hello-word-resource-group \
    --service-name apim-hello-world --named-value-id named_value_01

```

To delete a named value, use the [az apim nv delete](https://learn.microsoft.com/en-us/cli/azure/apim/nv#az-apim-nv-delete) command:

Azure CLI 

```
az apim nv delete --resource-group apim-hello-word-resource-group \
    --service-name apim-hello-world --named-value-id named_value_01

```

#### Use a named value

The examples in this section use the named values shown in the following table.

| Name | Value | Secret |
| --- | --- | --- |
| ContosoHeader | `TrackingId` | False |
| ContosoHeaderValue | •••••••••••••••••••••• | True |
| ExpressionProperty | `@(DateTime.Now.ToString())` | False |
| ContosoHeaderValue2 | `This is a header value.` | False |

To use a named value in a policy, place its display name inside a double pair of braces like `{{ContosoHeader}}`, as shown in the following example:

XML 

```
<set-header name="{{ContosoHeader}}" exists-action="override">
  <value>{{ContosoHeaderValue}}</value>
</set-header>

```

In this example, `ContosoHeader` is used as the name of a header in a `set-header` policy, and `ContosoHeaderValue` is used as the value of that header. When this policy is evaluated during a request or response to the API Management gateway, `{{ContosoHeader}}` and `{{ContosoHeaderValue}}` are replaced with their respective values.

Named values can be used as complete attribute or element values as shown in the previous example, but they can also be inserted into or combined with part of a literal text expression as shown in the following example:

XML 

```
<set-header name = "CustomHeader{{ContosoHeader}}" ...>

```

Named values can also contain policy expressions. In the following example, the `ExpressionProperty` expression is used.

XML 

```
<set-header name="CustomHeader" exists-action="override">
    <value>{{ExpressionProperty}}</value>
</set-header>

```

When this policy is evaluated, `{{ExpressionProperty}}` is replaced with its value, `@(DateTime.Now.ToString())`. Since the value is a policy expression, the expression is evaluated and the policy proceeds with its execution.

You can test this in the Azure portal or the [developer portal](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-developer-portal) by calling an operation that has a policy with named values in scope. In the following example, an operation is called with the two previous example `set-header` policies with named values. Notice that the response contains two custom headers that were configured using policies with named values.

![Test API response](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-howto-properties/api-management-send-results.png)
If you look at the outbound [API trace](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-api-inspector) for a call that includes the two previous sample policies with named values, you can see the two `set-header` policies with the named values inserted as well as the policy expression evaluation for the named value that contained the policy expression.

![API Inspector trace](https://learn.microsoft.com/en-us/azure/api-management/media/api-management-howto-properties/api-management-api-inspector-trace.png)
String interpolation can also be used with named values.

XML 

```
<set-header name="CustomHeader" exists-action="override">
    <value>@($"The URL encoded value is {System.Net.WebUtility.UrlEncode("{{ContosoHeaderValue2}}")}")</value>
</set-header>

```

The value for `CustomHeader` will be `The URL encoded value is This+is+a+header+value.`.

Caution

If a policy references a secret in Azure Key Vault, the value from the key vault will be visible to users who have access to subscriptions enabled for [API request tracing](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-api-inspector).

While named values can contain policy expressions, they can't contain other named values. If text containing a named value reference is used for a value, such as `Text: {{MyProperty}}`, that reference won't be resolved and replaced.

#### Delete a named value

To delete a named value, select the name and then select **Delete** from the context menu (**...**).

Important

If the named value is referenced by any API Management policies, you can't delete it until you remove the named value from all policies that use it.

#### Next steps

* Learn more about working with policies
	+ [Policies in API Management](https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies)
	+ [Policy reference](https://learn.microsoft.com/en-us/azure/api-management/api-management-policies)
	+ [Policy expressions](https://learn.microsoft.com/en-us/azure/api-management/api-management-policy-expressions)

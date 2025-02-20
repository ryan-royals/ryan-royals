---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/alz-terraform-acceleratordocswiki-user-guide-quick-start-phase-1-md-at-main-azurealz-terraform-accelerator/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/13cafa45bc3cff709660c0e1cdee47d06cc0d0859156d36494e45e2cefb4a12f/Azure/alz-terraform-accelerator)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Azure/alz-terraform-accelerator/tree/main?resume=1) 

t

Phase 1 of the accelerator is to setup your pre-requisites. Follow the steps below to do that.

#### [1.1 Tools](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#11-tools)

You'll need to install the following tools before getting started.

* PowerShell Core: [Follow the instructions for your operating system](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell)
* Terraform CLI: [Follow the instructions for your operating system](https://developer.hashicorp.com/terraform/downloads)
* Azure CLI: [Follow the instructions for your operating system](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli)
* Git: [Follow the instructions for your operating system](https://git-scm.com/downloads)

[!NOTE] In all cases, ensure that the tools are available from a PowerShell core (pwsh) terminal. You may need to add them to your environment path if they are not.

#### [1.2 Azure Subscriptions](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#12-azure-subscriptions)

We recommend setting up 3 subscriptions for Azure landing zones. These are management, identity and networking. You can read more about this in the [Landing Zone docs](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/landing-zone/deploy-landing-zones-with-terraform).

To create the subscriptions you will need access to a billing agreement. The following links detail the permissions required for each type of agreement:

* [Enterprise Agreement (EA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-enterprise-subscription)
* [Microsoft Customer Agreement (MCA)](https://learn.microsoft.com/en-us/azure/cost-management-billing/manage/create-subscription)

Once you have the access required, create three subscriptions following your desired naming convention with the following purposes:

* management
* identity
* networking

Take note of the subscription id of each subscription as we'll need them later.

#### [1.3 Azure Credentials](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#13-azure-credentials)

You need an Azure User or Service Principal with the following permissions to run the bootstrap:

* `Management Group Contributor` on you root management groups (usually called `Tenant Root Group`)
* `Owner` on your Azure landing zone subscriptions

For simplicity we recommend using a User account since this is a one off proceess that you are unlikely to repeat.

##### [1.3.1 Azure Permissions](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#131-azure-permissions)

It is likely that if you were able to create the subscriptions you already have the level of access required for a user account, however you should follow these steps to validate them.

If your preference is to run the bootstrap in the context of a Service Principal, follow these steps to create one:

###### [1.3.1.1 Create Service Principal (Skip this if using a User account)](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#1311-create-service-principal-skip-this-if-using-a-user-account)

1. Navigate to the [Azure Portal](https://portal.azure.com) and sign in to your tenant.
2. Search for `Azure Active Directory` and open it.
3. Copy the `Tenant ID` field and save it somewhere safe, making a note it is the `ARM_TENANT_ID`.
4. Click `App registrations` in the left navigation.
5. Click `+ New registration`.
6. Choose a name (SPN) that you will remember and make a note of it, we recommend using `sp-alz-boostrap`.
7. Type the chosen name into the `Name` field.
8. Leave the other settings as default and click `Register`.
9. Wait for it to be created.
10. Copy the `Application (client) ID` field and save it somewhere safe, making a note it is the `ARM_CLIENT_ID`.
11. Click `Certificates & secrets` in the left navigation.
12. Ensure the `Client secrets` tab is selected and click `+ New client secret`.
13. Enter `ALZ Bootstrap` in the `Description` field.
14. Change the `Expires` field, choose `Custom`.
15. Set the `Start` field to todays date.
16. Set the `End` field to tomorrows date.
17. Click `Add`.
18. Copy the `Value` field save it somewhere safe, making a note that it is the `ARM_CLIENT_SECRET`.

###### [1.3.1.2 Create Permissions](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#1312-create-permissions)

1. The service principal name (SPN) is the username of the User account or the name of the app registration you c reated.
2. Search for `Subscriptions` and click to navigate to the subscription view.
3. For each of the subscriptions you created in the previous step:
	1. Navigate to the subscription.
	2. Click `Access control (IAM)` in the left navigation.
	3. Click `+ Add` and choose `Add role assignment`.
	4. Choose the `Priviledged administrator roles` tab.
	5. Click `Owner` to highlight the row and then click `Next`.
	6. Leave the `User, group or service principal` option checked.
	7. Click `+ Select Members` and search for your SPN in the search box on the right.
	8. Click on your User to highlight it and then click `Select`.
	9. Click `Review + assign`, then click `Review + assign` again when the warning appears.
	10. Wait for the role to be assinged and move onto the next subscription.
4. Search for `Management Groups` and click to navigate to the management groups view.
5. Click the `Tenant Root Group` management group (Note, it is possible someone changed the name of your root management group, select the one at the very top of the hierarchy if that is the case)
6. Click `Access control (IAM)` in the left navigation.
7. Click `+ Add` and choose `Add role assignment`.
8. Remain on the `Job function roles` tab.
9. Search for `Management Group Contributor` and click the row to highlight that role.
10. Click `Next`.
11. Leave the `User, group or service principal` option checked.
12. Click `+ Select Members` and search for your SPN in the search box on the right.
13. Click on your User to highlight it and then click `Select`.
14. Click `Review + assign`, then click `Review + assign` again when the warning appears.
15. Wait for the role to be assinged and you are done with this part.

#### [1.4 Login / Set Credentials](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#14-login--set-credentials)

Follow these steps to login as a User or user Service Princiapl credentials:

##### [1.4.1 User Login](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#141-user-login)

1. Open a new PowerShell Core (pwsh) terminal.
2. Run `az login`.
3. You'll be redirected to a browser to login, perform MFA, etc.
4. Find the subscription id of the management subscription you made a note of earlier.
5. Type `az account set --subscription "<subscription id of your management subscription>"` and hit enter.
6. Type `az account show` and verify that you are connected to the management subscription.

##### [1.4.2 Service Principal Credentials](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#142-service-principal-credentials)

1. Open a new PowerShell Core (pwsh) terminal.
2. Find the `ARM_TENANT_ID` you made a note of earlier.
3. Type `$env:ARM_TENANT_ID="<tenant id>"` and hit enter.
4. Find the `ARM_CLIENT_ID` you made a note of earlier.
5. Type `$env:ARM_CLIENT_ID="<client id>"` and hit enter.
6. Find the `ARM_CLIENT_SECRET` you made a note of earlier.
7. Type `$env:ARM_CLIENT_SECRET="<client id>"` and hit enter.
8. Find the subscription id of the manangement subscription you made a note of earlier.
9. Type `$env:ARM_SUBSCRIPTION_ID="<subscription id>"` and hit enter.

[!NOTE] If you close your PowerShell prompt prior to running the bootstrap, you need to re-enter these environment variables.

#### [1.5 Version Control System Personal Access Token (PAT)](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#15-version-control-system-personal-access-token-pat)

You'll need to decide whether you are using GitHub or Azure DevOps and follow the instructions below to generate a PAT:

##### [1.5.1 Azure DevOps](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#151-azure-devops)

1. Navigate to [dev.azure.com](https://dev.azure.com) and sign in to your organization.
2. Ensure you navigate to the organization you want to deploy to.
3. Click the `User settings` icon in the top right and select `Personal access tokens`.
4. Click `+ New Token`.
5. Enter `Azure Landing Zone Terraform Accelerator` in the `Name` field.
6. Alter the `Expiration` drop down and select `Custom defined`.
7. Choose tommorrows date in the date picker.
8. Click the `Show all scopes` link at the bottom.
9. Check the following scopes:
	1. `Agent Pools`: `Read & manage`
	2. `Build`: `Read & execute`
	3. `Code`: `Full`
	4. `Environment`: `Read & manage`
	5. `Graph`: `Read & manage`
	6. `Pipeline Resources`: `Use & manage`
	7. `Project and Team`: `Read, write & manage`
	8. `Service Connections`: `Read, write & manage`
	9. `Variable Groups`: `Read, create & manage`
10. Click `Create`.
11. Copy the token and save it somewhere safe.
12. Click `Close`.

##### [1.5.2 GitHub](https://github.com/Azure/alz-terraform-accelerator/blob/main/docs/wiki/%5BUser-Guide%5D-Quick-Start-Phase-1.md#152-github)

1. Navigate to [github.com](https://github.com).
2. Click on your user icon in the top right and select `Settings`.
3. Scroll down and click on `Developer Settings` in the left navigation.
4. Click `Personal access tokens` in the left navigation and select `Tokens (classic)`.
5. Click `Generate new token` at the top and select `Generate new token (classic)`.
6. Enter `Azure Landing Zone Terraform Accelerator` in the `Note` field.
7. Alter the `Expiration` drop down and select `Custom`.
8. Choose tommorrows date in the date picker.
9. Check the following scopes:
	1. `repo`
	2. `workflow`
	3. `admin:org`: `write:org`
	4. `user`: `read:user`
	5. `user`: `user:email`
	6. `delete_repo`
10. Click `Generate token`.
11. Copy the token and save it somewhere safe.
12. If your organization uses single sign on, then click the `Configure SSO` link next to your new PAT.
13. Select your organization and click `Authorize`, then follow the prompts to allow SSO.

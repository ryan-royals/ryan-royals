---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/boost-dev-team-agility-with-customized-project-specific-templates-in-azure-deployment-environments/","tags":["rw/articles"]}
---

![rw-book-cover](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/ADE-Developer-Portal.png)

Have you heard the latest news about Azure Deployment Environments? Last month, we released an extensibility model that’s set to transform how platform engineers tailor deployments to their organization’s unique needs. This new model empowers you to customize deployments using any infrastructure-as-Code (IaC) framework you prefer—whether that’s Bicep, Terraform, or any other popular IaC or scripting tool. And it’s incredibly user-friendly, requiring just a few simple steps to unlock its full potential.

The goal of the extensibility model was to give organizations more powerful, flexible ways to define and tailor environment templates for app dev projects, and you can learn more about it in [the blog we released last month](https://aka.ms/ade-extensibility-model-blog).

Today, we’re excited to announce new capabilities that are built on our extensibility model. These new features give dev teams the flexibility to leverage templates that are more customized to their projects and make it easier to get started with service.

Read on to learn how these new capabilities in Azure Deployment Environments unlock several benefits for development and platform teams alike.

##### **Expanding the extensibility model to Pulumi**

Today, we’re very excited to announce the expansion of our extensibility model to Pulumi. In addition to first class support for [Azure Resource Manager (ARM) and Bicep](https://learn.microsoft.com/en-us/azure/deployment-environments/how-to-configure-extensibility-bicep-container-image), and [guidance on performing Terraform deployments](https://learn.microsoft.com/en-us/azure/deployment-environments/how-to-configure-extensibility-terraform-container-image), customers can now easily perform Pulumi deployments using ADE’s extensibility model.

Pulumi is easy to adopt and use as it allows you to write infrastructure-as-code in the language you are most comfortable with—like TypeScript, JavaScript, Python, Go, or C#—or convert existing templates from ARM, Terraform, and other formats. Pulumi offers a simplified, accelerated way to deploy infrastructure in Azure through Deployment Environments.

[![ADE + Pulumi](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/ADEPulumi.jpg)](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/ADEPulumi.jpg)
We’ve partnered with Pulumi to make it easier for customers to leverage the extensibility model in Deployment Environments. You can now either directly use the standard [Pulumi image](https://aka.ms/ade/pulumi-docker-image) or build your own container image by leveraging [workflows published by Pulumi](https://aka.ms/ade/pulumi-repo). This feature is in preview, and we’re eager to see what customers will accomplish with it. Read [Pulumi’s blog](https://www.pulumi.com/blog/azure-deployment-environments/?utm_source=microsoft&utm_medium=events&utm_campaign=FY2024Q4_Event_MSBuild) to learn more and give [Pulumi a try today with Deployment Environments](https://aka.ms/ade/pulumi-docs). You can also get a direct download on how to perform Pulumi deployments in Deployment Environments by [registering for the workshop hosted by Pulumi](https://bit.ly/4dwyrIz).

##### **Adding private registry support**

In addition, we’re building out our extensibility model by announcing support for private registries today. While the extensibility model allows you to configure images in any IaC framework you want, you can now bring these container images into Deployment Environments through a private registry for more controlled access. [Sign up for private preview today](https://aka.ms/ade/private-registry-signup) to try out private registries in Deployment Environments.

##### **Increasing team agility with project-level catalogs**

With Azure Deployment Environments, our goal has always been to empower dev teams with a seamless, intuitive way to provision app infrastructure within enterprise guardrails. Today, we are excited to introduce project-level catalogs that further enhance dev team access to the app infra they need. You can attach repos as catalogs directly to projects and deliver templates that are tailored to the unique needs of different dev teams.

[![Image Project Level Catalogs](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/Project-Level-Catalogs-1.png)](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/Project-Level-Catalogs-1.png)
Better yet, you can give dev leads the ability to directly customize their team’s templates. In turn, this can significantly increase dev team agility by ensuring they have the precise app infra they need and enabling dev teams to be more autonomous—all without compromising on governance. This feature is in preview, and you can learn more by reading our docs about how to [configure project-level catalogs](https://aka.ms/deployment-environments/project-catalog).

##### **Delivering catalog enhancements**

On top of all that, we’re also introducing capabilities to further improve the experience of setting up and managing catalogs in Deployment Environments, such as:

* [Catalog attach via GitHub apps](https://aka.ms/deployment-environments/github-app-catalog): Enable better collaboration between platform engineers and dev teams with a secure, robust mechanism for attaching GitHub repos as catalogs
* [Auto-sync functionality](https://aka.ms/deployment-environments/catalog-auto-sync): Configure a catalog to automatically sync every 30 mins and provide dev teams with the latest versions of each template, minimizing the risk of using outdated configurations.
* [Enhanced visibility into synced catalog items](https://aka.ms/deployment-environments/sync-catalog-items): Gain a centralized view of catalogs items that have been successfully synced, making it easier to track and manage catalog items.
* Trusted service support for PAT: For customers using personal access tokens (PAT) to attach their repos as catalogs and want to keep Key Vault’s private from the internet, you can now set your Key Vault to allow trusted Microsoft services to bypass your firewall rule.

[![Image Trusted Service Support](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/Trusted-Service-Support-2.png)](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/Trusted-Service-Support-2.png)
These features are all publicly available. Head over to our [documentation to learn more](https://aka.ms/ade/catalog).

##### **Streamlined setup with the quick-start template**

Lastly, we are releasing a new quick-start template to make it extremely easy to configure and deploy Azure Deployment Environments. If you are new to the service, you can now get started with a single-click deployment from the service-hub view.

[![Image Quick start template](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/Quick-start-template-1.png)](https://devblogs.microsoft.com/develop-from-the-cloud/wp-content/uploads/sites/81/2024/05/Quick-start-template-1.png)
This quick-start template gives devs even faster access to app infrastructure within guardrails for security, compliance, and cost management. This feature is now generally available, and you can [start using it today](https://aka.ms/ade/learn/quickstart-template).

##### **Get started with Azure Deployment Environments today**

You can check out our docs to learn more about these new capabilities – [leveraging Pulumi templates](https://aka.ms/ade/pulumi-docs), [project-based catalogs](https://aka.ms/deployment-environments/project-catalog), and [single-click deployment to configure the service](https://aka.ms/ade/learn/quickstart-template).

We can’t wait to see the amazing things you’ll accomplish with these new features in Azure Deployment Environments. The best part? You can [get started with Azure Deployment Environments today for free](https://aka.ms/ADE-getstarted).

Find out more about the latest in Azure Deployment Environments and see the service in action by watching our [Azure Deployment Environments session at Build 2024](https://aka.ms/ade-build-2024).

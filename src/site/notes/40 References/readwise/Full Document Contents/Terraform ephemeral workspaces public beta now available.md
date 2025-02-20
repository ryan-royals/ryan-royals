---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/terraform-ephemeral-workspaces-public-beta-now-available/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1620083068-blog-library-product-terraform-black.jpg)

Everyone working in IT understands the challenge of finding and turning off infrastructure that gets spun up and forgotten about. It's an ongoing issue that unnecessarily inflates IT costs.

Back in June at [HashiDays 2023](https://www.hashicorp.com/blog/new-terraform-cloud-capabilities-to-import-view-and-manage-infrastructure), we previewed the upcoming ephemeral workspaces feature, which is aimed at helping organizations manage the cleanup of old and unwanted resources accumulated over time. Today, the wait is over.

The public beta of ephemeral workspaces for Terraform Cloud Plus is now available. It allows customers to schedule a time to automatically destroy non-production resources, eliminating the need for manual cleanup, reducing infrastructure costs, and streamlining workspace management.

#### Benefits of ephemeral workspaces

This new feature benefits infrastructure teams in three ways:

**Cost savings**: Ephemeral workspaces not only reduce infrastructure costs, they also give more time back to infrastructure teams since they don’t have to hunt down or manually delete unused resources as often.

**Increased efficiency**: Administrators can set time-to-live (TTL) settings on workspaces through the API or UI, which simplifies management and testing.

**Improved security**: Workspaces that are not being actively watched or have been forgotten pose a security risk. Automatically destroying unused workspaces helps organizations meet compliance requirements and reduces the potential attack surface of your infrastructure.

#### Using ephemeral workspaces

It is easy to use ephemeral workspaces. Just set a date and time for when you would like the workspace to be de-provisioned. Auto-destroy settings can be found in Workspace Settings under the section in the sidebar called Destruction and Deletion.

![Auto destroy settings](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1692301401-auto-destroy-full.png&w=3840&q=75)Auto-destroy settings can be found in Workspace Settings.
The status of the auto-destroy setting shows up in the sidebar on your workspace's overview page, alongside settings like Execution mode and Auto apply. The auto-destroy status displays as Off if not configured. If configured, the status shows when the next auto-destroy is planned for. If, for any reason, the scheduled destroy run fails, the sidebar status will link to the failed run, where the run output will provide further details.

![Auto destroy overview](https://www.hashicorp.com/_next/image?url=https%3A%2F%2Fwww.datocms-assets.com%2F2885%2F1692303073-auto-destroy-overview.png&w=3840&q=75)The workspace overview shows when the next auto-destroy is planned.
Once the configured auto-destroy time is reached, Terraform will automatically run a destroy plan and apply it to destroy your managed resources. Notifications can be configured to send an auto destroy reminder before a `destroy` run is triggered and auto destroy results to indicate the success or failure of the `destroy` run.

##### Getting started with Terraform Cloud

Terraform Cloud is designed to standardize workflows from Day 1 infrastructure provisioning to Day 2 operations and beyond. It helps organizations optimize infrastructure investments and improve operational efficiency. Ephemeral workspaces further builds on this optimization.

Try the new ephemeral workspaces today — and if you are new to Terraform, [sign up for Terraform Cloud](https://app.terraform.io/public/signup/account) and [contact sales for a trial](https://www.hashicorp.com/contact-sales?interest=terraform) of Terraform Cloud Plus.

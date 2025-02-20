---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/hashi-corp-2024-year-in-review/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1734471527-eoy_blog_image_2024.png?w=1200&h=630&fit=crop&auto=format)

2024 was a stand-out year in the evolution of HashiCorp, and before we head into another exciting year I wanted to step back and reflect on just a fraction of the many remarkable things we’ve done this year. All of this, of course, doesn’t happen without our community, customers, partners, and employees. Thank you!

#### Making headlines

**IBM + HashiCorp:** Earlier this year, HashiCorp [signed an agreement](https://www.hashicorp.com/blog/hashicorp-joins-ibm) to be acquired by IBM and operate as a division inside IBM Software. With IBM, I believe we can bring modern infrastructure and security practices to an even greater number of organizations around the world, and I’m super excited by the improved workflows we can unlock together for hybrid and multi-cloud environments.

**The Infrastructure Cloud:** We introduced an approach for enterprises to manage not only the Day 0 and Day 1 actions of creating infrastructure and launching security workflows, but also to focus on the crucial Day 2 visibility and management concerns for security and infrastructure. We call this [The Infrastructure Cloud](https://www.hashicorp.com/blog/introducing-the-infrastructure-cloud), and it can be implemented through the HashCorp Cloud Platform (HCP) suite of services. 

**The 2024 State of Cloud Strategy:** Our fourth annual [State of Cloud Strategy survey](https://www.hashicorp.com/state-of-the-cloud), done in partnership with Forrester, focused on questions around cloud maturity and placed respondents into tiers based on 21 key practices in cloud infrastructure and security. Some of the findings: Higher cloud maturity pays major dividends, and high-maturity organizations were twice as likely to have [platform teams](https://www.hashicorp.com/resources/what-is-a-platform-team-and-why-do-we-need-them).

#### The tech

There were too many new features and enhancements across our product portfolio to list here, but these are some of the main changes that users were most excited about.

##### Infrastructure Lifecycle Management

###### Terraform

There were big, transformative changes in Terraform and HCP Terraform (formerly Terraform Cloud) this year that continued to build out a full lifecycle approach to infrastructure. Some new features made large deployment and migration workflows easier, while others removed significant friction and risk in secret-handling workflows. The main highlights were:

* Terraform Stacks to enable multi-component and multi-environment deployments ([Learn more](https://www.hashicorp.com/blog/terraform-stacks-explained))
* Module lifecycle management to simplify Day 2 upgrades and deprecations ([Learn more](https://www.hashicorp.com/blog/terraform-packer-nomad-and-waypoint-updates-help-scale-ilm-at-hashiconf-2024))
* Terraform migrate to adopt HCP Terraform ([Learn more](https://www.hashicorp.com/blog/terraform-packer-nomad-and-waypoint-updates-help-scale-ilm-at-hashiconf-2024))
* Test-integrated module publishing ([Learn more](https://developer.hashicorp.com/terraform/cloud-docs/registry/test))
* Explorer for workspace visibility ([Learn more](https://www.hashicorp.com/blog/terraform-gains-upgrades-for-module-tests-explorer-and-more#explorer-for-workspace-visibility))
* Ephemeral values to keep secrets out of state ([Learn more](https://www.hashicorp.com/blog/terraform-1-10-improves-handling-secrets-in-state-with-ephemeral-values))
* Config-driven state updates for refactoring and importing resources ([Learn more](https://www.hashicorp.com/blog/terraform-1-7-adds-test-mocking-and-config-driven-remove#config-driven-remove))
* Provider-defined functions to make HCL more flexible ([Learn more](https://www.hashicorp.com/blog/terraform-1-8-improves-extensibility-with-provider-defined-functions))
* New pre-written Sentinel policy library co-developed with AWS ([Learn more](https://www.hashicorp.com/blog/simplify-policy-adoption-in-terraform-with-pre-written-sentinel-policies-for-aws))

###### Packer

While [Packer 1.11](https://www.hashicorp.com/blog/predictable-plugin-loading-in-packer-1-11) introduced a more predictable plugin loading process, HCP Packer got more visibility and more sophisticated access controls. The highlights from HCP Packer this year included:

* Packer-version and plugin-version tracking ([Learn more](https://www.hashicorp.com/blog/hcp-packer-improves-metadata-visibility-for-artifact-creation))
* Bucket-level RBAC ([Learn more](https://www.hashicorp.com/blog/hcp-packer-now-tracks-ci-cd-pipeline-metadata))
* CI/CD pipeline metadata ([Learn more](https://www.hashicorp.com/blog/hcp-packer-adds-bucket-level-rbac))

###### Waypoint

We continued building out HCP Waypoint’s internal developer platform (IDP) capabilities as the service [reached general availability](https://www.hashicorp.com/blog/hcp-waypoint-now-ga-with-enhancements-to-golden-workflow-capabilities) at HashiConf. Here were the key enhancements:

* Templates general availability ([Learn more](https://www.youtube.com/watch?v=88EA4M8Y3dg))
* Upgrade workflow for templates ([Learn more](https://www.hashicorp.com/blog/hcp-waypoint-now-ga-with-enhancements-to-golden-workflow-capabilities#upgrade-workflow-for-templates))
* Add-ons general availability ([Learn more](https://www.youtube.com/watch?v=88EA4M8Y3dg))
* Actions public beta ([Learn more](https://www.hashicorp.com/blog/hcp-waypoint-actions-is-now-in-public-beta))

###### Nomad

Nomad saw significant performance optimizations this year along with new device drivers, enhanced GPU support, major task driver upgrades, and new workflows. These were the highlights:

* Nomad Bench: A load testing and benchmarking utility for Nomad ([Learn more](https://www.hashicorp.com/blog/nomad-bench-load-testing-and-benchmarking-for-nomad))
* NVIDIA device driver added support for Multi-Instance GPUs ([Learn more](https://www.hashicorp.com/blog/nomad-1-9-adds-nvidia-mig-support-golden-job-versions-and-more))
* Golden job versions ([Learn more](https://www.hashicorp.com/blog/nomad-1-9-adds-nvidia-mig-support-golden-job-versions-and-more))
* Enhancements for GPU scheduling and resource quotas ([Learn more](https://www.hashicorp.com/blog/nomad-1-9-adds-nvidia-mig-support-golden-job-versions-and-more#quotas-for-device-resources-enterprise))
* exec2 task driver general availability ([Learn more](https://www.hashicorp.com/blog/nomad-1-9-adds-nvidia-mig-support-golden-job-versions-and-more))
* libvirt task driver beta for improved virtual machine support ([Learn more](https://www.hashicorp.com/blog/nomad-1-9-adds-nvidia-mig-support-golden-job-versions-and-more))
* A Long-Term Support (LTS) release program for Nomad Enterprise ([Learn more](https://www.hashicorp.com/long-term-support))

###### Vagrant

[Vagrant Cloud](https://developer.hashicorp.com/vagrant/vagrant-cloud) functionality was migrated to HCP under the new name of [HCP Vagrant Registry](https://portal.cloud.hashicorp.com/services/vagrant/registries). We've auto-migrated Vagrant Cloud organizations to the HCP Vagrant Registry where users are now able to reclaim their box registries.

##### Security Lifecycle Management

###### Vault

The collection of Vault products matured significantly this year, with [HCP Vault Radar](https://developer.hashicorp.com/hcp/docs/vault-radar) entering public beta and [HCP Vault Secrets](https://developer.hashicorp.com/hcp/docs/vault-secrets) adding enterprise capabilities. The key features this year included:

* Secrets sync between Vault and external systems is GA (now available for [HCP Vault Dedicated](https://www.hashicorp.com/blog/hcp-vault-dedicated-adds-secrets-sync-wif-cross-region-dr-est-pki-and-more) and [Vault Enterprise](https://www.hashicorp.com/blog/vault-1-16-brings-enhanced-resilience-visibility-and-more) in addition to HCP Vault Secrets) ([Learn more](https://www.youtube.com/watch?v=cel1GQ0wpQA))
* Auto-rotation and dynamic secrets for HashiCorp Vault Secrets ([Learn more](https://www.hashicorp.com/blog/hcp-vault-secrets-adds-enterprise-capabilities-for-auto-rotation-dynamic-secrets))
* Secrets sync with HCP Terraform workspaces and variable sets in HashiCorp Vault Secrets ([Learn more](https://developer.hashicorp.com/hcp/docs/vault-secrets/integrations/hcp-terraform))
* Workload Identity Federation (WIF) support for major cloud providers ([Learn more](https://www.hashicorp.com/blog/vault-1-17-brings-wif-est-support-for-pki-and-more))
* PKI support for EST and CMPv2 ([Learn](https://www.hashicorp.com/blog/vault-1-17-brings-wif-est-support-for-pki-and-more) [more](https://www.hashicorp.com/blog/vault-1-18-introduces-support-for-ipv6-and-cmpv2-while-improving-security-team-ux))
* Adaptive overload protection for Vault’s integrated storage backend ([Learn more](https://www.hashicorp.com/blog/new-slm-offerings-vault-boundary-consul-hashiconf-2024-make-security-easier#improve-high-availability-with-adaptive-overload-protection))
* Vault Secrets Operator (VSO) for Kubernetes enhancements ([Learn more](https://www.hashicorp.com/blog/new-vault-boundary-offerings-advance-security-lifecycle-management-hashidays-2024#vault-secrets-operator))
* Long-Term Support (LTS) release program for Vault Enterprise ([Learn more](https://www.hashicorp.com/long-term-support))

###### HCP Vault Radar

HCP Vault Radar is a new product released this year that scans your digital estate for unmanaged secrets and PII. Along with exposure detection and prevention features, it has deep analysis, visualization, and management features. It was first released in private beta this year, then public beta at HashiConf. Its major features include:

* Risk prioritization using version history, string randomness, activeness, and Vault correlation ([Learn more](https://www.hashicorp.com/blog/hcp-vault-radar-for-secret-discovery-enters-limited-availability))
* Remediation workflows via integration with ticketing and alerting solutions ([Full list](https://www.hashicorp.com/blog/hcp-vault-radar-for-secret-discovery-enters-limited-availability#remediate-unmanaged-secrets))
* Support for scanning common leak sources ([Full list](https://www.hashicorp.com/blog/hcp-vault-radar-for-secret-discovery-enters-limited-availability#scan-top-developer-tools-in-the-cloud-or-on-premises))
* On-premises and self-managed scanning ([Learn more](https://www.hashicorp.com/blog/new-slm-offerings-vault-boundary-consul-hashiconf-2024-make-security-easier#implement-hcp-vault-radar-agent-for-self-managed-and-regulated-environments))
* Git pre-receive hook scanning ([Learn more](https://www.youtube.com/watch?v=mIKd8nhEUVI))

###### Boundary

It’s been a major year for Boundary and HCP Boundary with workflow and UI enhancements that have simplified and sped up the secure session establishment process significantly. Boundary has proven its value at companies like [Verizon](https://www.hashicorp.com/resources/secure-collaboration-with-boundary-at-the-verizon-innovation-labs), [BT Group](https://www.hashicorp.com/resources/how-vault-and-boundary-helped-bt-improve-security-without-compromising-ux), and [DXone](https://www.hashicorp.com/resources/cost-reduction-risk-mitigation-speed-please-choose-3-w-vault-boundary) — the data processor for Volkswagen's retail partners. Here were some of the biggest upgrades:

* Transparent sessions to provide a VPN-like experience ([Learn more](https://www.youtube.com/watch?v=mFyEq0N6rxU))
* Session recording storage for on-prem and any S3-compatible storage ([Learn more](https://www.hashicorp.com/blog/boundary-0-17-improves-management-failure-handling-and-adds-more-storage-support#more-storage-options-for-session-recordings))
* Many new search and filtering capabilities ([Learn more](https://www.hashicorp.com/blog/boundary-0-15-adds-new-storage-policies-and-desktop-cli-features#search-and-filtering))
* Vault and Boundary audit log correlation ([Learn more](https://www.hashicorp.com/blog/boundary-0-16-adds-aliases-minio-storage-and-improved-search#more-new-features-boundary-0-16))
* Performance enhancements for large deployments

###### Consul

As Consul continues to be a workhorse in many organizations’ critical networking infrastructure, we focused on enhancing visibility, stability, and integration with Nomad and Kubernetes. The biggest releases in 2024 were:

* Consul DNS views for Kubernetes ([Learn more](https://developer.hashicorp.com/consul/docs/k8s/dns/views))
* Transparent proxy mode for ECS on Amazon EC2 tasks ([Learn more](https://www.hashicorp.com/blog/consul-1-18-ga-improves-enterprise-reliability-with-long-term-support))
* Terminating gateway and API gateway support in Consul on ECS ([Learn more](https://www.hashicorp.com/blog/consul-1-18-ga-improves-enterprise-reliability-with-long-term-support))
* Registration CRD for Consul on Kubernetes ([Learn more](https://www.hashicorp.com/blog/consul-1-19-improves-kubernetes-workflows-snapshot-support-and-nomad-integration))
* LTS release program for Consul Enterprise ([Learn more](https://www.hashicorp.com/long-term-support))

#### Customer stories

Every year we’re honored to hear about the transformative impact we’ve had on our customers and in our user community. It’s not just one industry that benefits, we see use cases across every sector of the economy, from web design tooling like Canva, to telecoms like BT Group, to government agencies like California’s Department of Health Care Services.

##### Canva

Even with secrets management tools, Canva still had a secret sprawl problem. They needed a strategy to go along with the tools. When they built their new strategy and made HashiCorp Vault their company-standard, things got better. 

* They closed a whole category of risk by removing direct engineering access to secrets
* Saw 87.5% reduction in processes around secret provisioning
* And gained a bunch of other benefits around auditing and team satisfaction

Read our summary and watch their full talk [here](https://www.hashicorp.com/resources/streamlining-secrets-management-at-canva-with-hashicorp-vault).

##### California’s Department of Health Care Services

The California’s Department of Health Care Services (DHCS) is the largest SLED (state, local, and education) organization in the United States and they’re the backbone of California’s healthcare safety net. With the help of HCP Terraform, they were able to modernize its legacy applications and create a sustainable platform.

* They reduced new environment provisioning time from weeks to hours
* Apps reached production 70% faster
* And they build a lasting foundation for infrastructure management

Read the full story in this [case study](https://www.hashicorp.com/case-studies/department-of-healthcare-services).

##### BT Group

Security tooling and processes can often be seen as a hindrance to application development. At BT Group, they wanted to get past the defensiveness and arrive at a place where security is seen as an enabler. To do that, they’re moving toward a passwordless experience with Vault and Boundary, and they’ve already seen it significantly reduce the risk of credential theft.

* They eliminated around 50,000 unnecessary credentials
* Build strong user engagement with security processes in Vault and Boundary
* And reduced friction associated with accessing systems

Read our summary and watch their full talk [here](https://www.hashicorp.com/resources/how-vault-and-boundary-helped-bt-improve-security-without-compromising-ux).

See more user story presentations on the [HashiConf](https://www.youtube.com/playlist?list=PL81sUbsFNc5bdUUiBVCSjnPRivtDcofgd) and [HashiDays](https://www.youtube.com/playlist?list=PL81sUbsFNc5ZK1pLff1AutRsp78rfEBCj) YouTube playlists.

#### 2024 by the numbers

Here are some of the metrics that speak to the banner year we’ve had:

* 4,800+ customers
* Included in Fortune’s 2024 [Future 50](https://www.bcg.com/news/02december2024-the-future-50-companies-built-to-adapt-and-thrive-in-turbulent-times)
* Terraform Registry (as of December ‘24):
	+ 4,700+ providers
	+ 18,000+ modules
* [HUGs](https://www.meetup.com/pro/hugs/):
	+ 60+ countries
	+ 180+ groups
	+ 54,000+ members
* Total certification exams passed (all time): 73,000+

#### Looking forward

As we move towards a new stage at an even larger scale, we know we’ll be focused on a few things. 

One is our continued whole-lifecycle approach to infrastructure and security management. We know our products can bring immediate benefits to the security and infrastructure management processes in an organization, but we also want to ensure that the products will help maintain those benefits for years to come — Day 2 features are key. 

Our other focus is cross-product integration and making all HCP services function as a single platform that supports your own internal platform. 

We believe that 2024 has put us in position to help transform even more organizations as they learn how to build applications in a constantly evolving technology landscape. We look forward to doing great things with our users, customers, and partners again in 2025 as we continue to build the future of infrastructure and security together.

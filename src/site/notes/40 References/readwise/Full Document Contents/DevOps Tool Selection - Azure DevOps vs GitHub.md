---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/dev-ops-tool-selection-azure-dev-ops-vs-git-hub/","tags":["rw/articles"]}
---

![rw-book-cover](https://arkahna.atlassian.net/wiki/s/1309670192/6452/c99892e43709e6dc4870053247748ea8ec8c750a/8/_/favicon-update.ico)

* ![](https://arkahna.atlassian.net/wiki/aa-avatar/608f4cf60b80a60069c18371)

**GitHub Roadmap**

Customers often request guidance on selecting a DevOps tooling stack. As a Microsoft and GitHub partner we are in a position to provide guidance on both platforms. Internally we hold a strong preference for GitHub internally because we combine it with Jira to offset some of the weaknesses of GitHub in the work item management capabilities. Use the following decision space guidance to help guide customers on their decision.

|  |  |  |
| --- | --- | --- |
| **Description** | GitHub is a web-based code hosting platform that allows teams to collaborate on code and manage software projects. It is built around the Git version control system and provides a range of features such as pull requests, code reviews, and issue tracking. | Azure DevOps is a suite of tools that allows teams to plan, develop, test, and deploy software. It includes a range of services, such as Azure Boards, Azure Repos, Azure Test Plans, and Azure Artifacts, which are designed to help teams work more efficiently and collaboratively. |
| **Features** |  |  |
| * Identity & Access
 | * SSO & SCIM from Azure AD (Requires enterprise)
* Supports external collaborators
* Built-in RBAC model for access control
 | * SSO from Azure AD
* Team & External
* Supports external collaborators through Azure AD Guest or Email invite.
* Customisable RBAC model.
 |
| * Work Management, Issue Management, Planning & Iteration Management
 | * Supports Projects that span across multiple repositories/projects
* Everything is an “Issue” with unlimited nesting.
 | * Kanban & Scrum Boards - Azure Boards
* Customisable processes, issue fields and workflows supported.
 |
| * Source Control
 | * Git-based
* Unlimited Public & Private Repositories
* Template Repositories
* Branch Protection Policies
* Pull Requests & Status Checks
* Code Owners
* Required Viewers
 | * Git-based
* Unlimited Public & Private Repositories
* Template Repositories
* Branch Protection Policies
* Pull Requests & Status Checks
* Code Owners
* Required Viewers
 |
| * Build & Release
 | * GitHub Actions (YAML)
* Build & Release stored in repositories
* GitHub Hosted Runners
* Self Hosted Runners
* Environment protection rules and approvals (Requires enterprise)
* 3,000/50,000 included build minutes
* Free minutes for public repos
* GitHub OIDC for password less authentication to Azure.
 | * Azure DevOps Pipelines (YAML+Visual)
* Build & Release stored in repositories (YAML)
* DevOps Hosted Agents
* Self Hosted Agents
* Environment protection roles and approvals
* Unlimited build minutes per paid agent
* Service Connections for Azure Environments
 |
| * Dashboards & Monitoring
 | * Insights (limited repository/project reporting)
* Simplified charting (Burn-up/down etc) in projects
 | * + Dashboards
	+ Widgets
	+ Charts & Reports
 |
| * Integration & Tooling
 | * GitHub Desktop
* Visual Studio, Visual Studio Code
* [GitHub integrations](https://github.com/integrations)
* Web-based tools
* Command-line tools
* REST APIs
 | * Visual Studio, Visual Studio Code
* Office integration tools (e.g. Excel, useful for those with batch jobs)
* Web-based tools
* Command-line tools
* REST APIs
 |
| * Development Acceleration
 | * Code Spaces support for hosted development environments
* Copilot, CopilotX
 |  |
| **Licencing & Pricing** | **Team**$6 AUD Per User (Teams)$31 AUD Per User (Enterprise) | $9 AUD Per User (5 Free)$3 AUD Per Artifact Storage |
| **Pros & Cons** |  Projects for managing issues and tasks can span across multiple repositories. Support and general discoverability and hosting of public and open-source repositories. Sharing artifacts between repositories and organisations requires PAT tokens to grant access. |  |
| **Estimated cost*** Depends on configuration, licence count requirements and existing licences.
 |  | Medium |

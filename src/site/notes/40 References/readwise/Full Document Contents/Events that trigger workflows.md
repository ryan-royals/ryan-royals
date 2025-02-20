---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/events-that-trigger-workflows/","tags":["rw/articles"]}
---

![rw-book-cover](https://github.githubassets.com/images/modules/open_graph/github-logo.png)

You can configure your workflows to run when specific activity on GitHub happens, at a scheduled time, or when an event outside of GitHub occurs.

Workflow triggers are events that cause a workflow to run. For more information about how to use workflow triggers, see "[Triggering a workflow](https://docs.github.com/en/actions/using-workflows/triggering-a-workflow)."

Some events have multiple activity types. For these events, you can specify which activity types will trigger a workflow run. For more information about what each activity type means, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads)."

**Note:** Not all webhook events trigger workflows.

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`branch_protection_rule`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#branch_protection_rule) | - `created`- `edited`- `deleted` | Last commit on default branch | Default branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#branch_protection_rule)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when branch protection rules in the workflow repository are changed. For more information about branch protection rules, see "[About protected branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)." For information about the branch protection rule APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#branchprotectionrule)" in the GraphQL API documentation or "[Branches](https://docs.github.com/en/rest/branches)" in the REST API documentation.

For example, you can run a workflow when a branch protection rule has been `created` or `deleted`:

```
on:
  branch_protection_rule:
    types: [created, deleted]

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`check_run`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#check_run) | - `created`- `rerequested`- `completed`- `requested_action` | Last commit on default branch | Default branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#check_run)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when activity related to a check run occurs. A check run is an individual test that is part of a check suite. For information, see "[Using the REST API to interact with checks](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-checks)." For information about the check run APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#checkrun)" in the GraphQL API documentation or "[Checks](https://docs.github.com/en/rest/checks#runs)" in the REST API documentation.

For example, you can run a workflow when a check run has been `rerequested` or `completed`.

```
on:
  check_run:
    types: [rerequested, completed]

```

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#check_suite)." Although only the `started` activity type is supported, specifying the activity type will keep your workflow specific if more activity types are added in the future. By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note:** To prevent recursive workflows, this event does not trigger workflows if the check suite was created by GitHub Actions.

Runs your workflow when check suite activity occurs. A check suite is a collection of the check runs created for a specific commit. Check suites summarize the status and conclusion of the check runs that are in the suite. For information, see "[Using the REST API to interact with checks](https://docs.github.com/en/rest/guides/using-the-rest-api-to-interact-with-checks)." For information about the check suite APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#checksuite)" in the GraphQL API documentation or "[Checks](https://docs.github.com/en/rest/checks#suites)" in the REST API documentation.

For example, you can run a workflow when a check suite has been `completed`.

```
on:
  check_suite:
    types: [completed]

```

**Note**: An event will not be created when you create more than three tags at once.

Runs your workflow when someone creates a Git reference (Git branch or tag) in the workflow's repository. For information about the APIs to create a Git reference, see "[Mutations](https://docs.github.com/en/graphql/reference/mutations#createref)" in the GraphQL API documentation or "[Git database](https://docs.github.com/en/rest/git#create-a-reference)" in the REST API documentation.

For example, you can run a workflow when the `create` event occurs.

```
on:
  create

```

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note**: An event will not be created when you delete more than three tags at once.

Runs your workflow when someone deletes a Git reference (Git branch or tag) in the workflow's repository. For information about the APIs to delete a Git reference, see "[Mutations](https://docs.github.com/en/graphql/reference/mutations#deleteref)" in the GraphQL API documentation or "[Git database](https://docs.github.com/en/rest/git#delete-a-reference)" in the REST API documentation.

For example, you can run a workflow when the `delete` event occurs.

Runs your workflow when someone creates a deployment in the workflow's repository. Deployments created with a commit SHA may not have a Git ref. For information about the APIs to create a deployment, see "[Mutations](https://docs.github.com/en/graphql/reference/mutations#createdeployment)" in the GraphQL API documentation or "[Repositories](https://docs.github.com/en/rest/repos#deployments)" in the REST API documentation.

For example, you can run a workflow when the `deployment` event occurs.

```
on:
  deployment

```

**Note:** When a deployment status's state is set to `inactive`, a workflow run will not be triggered.

Runs your workflow when a third party provides a deployment status. Deployments created with a commit SHA may not have a Git ref. For information about the APIs to create a deployment status, see "[Mutations](https://docs.github.com/en/graphql/reference/mutations#createdeploymentstatus)" in the GraphQL API documentation or "[Deployments](https://docs.github.com/en/rest/deployments#create-a-deployment-status)" in the REST API documentation.

For example, you can run a workflow when the `deployment_status` event occurs.

```
on:
  deployment_status

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`discussion`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#discussion) | - `created`- `edited`- `deleted`- `transferred`- `pinned`- `unpinned`- `labeled`- `unlabeled`- `locked`- `unlocked`- `category_changed` - `answered` - `unanswered` | Last commit on default branch | Default branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#discussion)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note:** Webhook events for GitHub Discussions are currently in beta and subject to change.

Runs your workflow when a discussion in the workflow's repository is created or modified. For activity related to comments on a discussion, use the [`discussion_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#discussion_comment) event. For more information about discussions, see "[About discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)." For information about the GraphQL API, see "[Objects](https://docs.github.com/en/graphql/reference/objects#discussion)."

For example, you can run a workflow when a discussion has been `created`, `edited`, or `answered`.

```
on:
  discussion:
    types: [created, edited, answered]

```

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#discussion_comment)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note:** Webhook events for GitHub Discussions are currently in beta and subject to change.

Runs your workflow when a comment on a discussion in the workflow's repository is created or modified. For activity related to a discussion as opposed to comments on the discussion, use the [`discussion`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#discussion) event. For more information about discussions, see "[About discussions](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/about-discussions)." For information about the GraphQL API, see "[Objects](https://docs.github.com/en/graphql/reference/objects#discussion)."

For example, you can run a workflow when a discussion comment has been `created` or `deleted`.

```
on:
  discussion_comment:
    types: [created, deleted]

```

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when someone forks a repository. For information about the REST API, see "[Repositories](https://docs.github.com/en/rest/repos#create-a-fork)."

For example, you can run a workflow when the `fork` event occurs.

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when someone creates or updates a Wiki page. For more information, see "[About wikis](https://docs.github.com/en/communities/documenting-your-project-with-wikis/about-wikis)."

For example, you can run a workflow when the `gollum` event occurs.

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#issue_comment)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when an issue or pull request comment is created, edited, or deleted. For information about the issue comment APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#issuecomment)" in the GraphQL API documentation or "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#issue_comment)" in the REST API documentation.

For example, you can run a workflow when an issue or pull request comment has been `created` or `deleted`.

```
on:
  issue_comment:
    types: [created, deleted]

```

The `issue_comment` event occurs for comments on both issues and pull requests. You can use the `github.event.issue.pull_request` property in a conditional to take different action depending on whether the triggering object was an issue or pull request.

For example, this workflow will run the `pr_commented` job only if the `issue_comment` event originated from a pull request. It will run the `issue_commented` job only if the `issue_comment` event originated from an issue.

```
on: issue_comment

jobs:
  pr_commented:
    # This job only runs for pull request comments
    name: PR comment
    if: ${{ github.event.issue.pull_request }}
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo A comment on PR $NUMBER
        env:
          NUMBER: ${{ github.event.issue.number }}

  issue_commented:
    # This job only runs for issue comments
    name: Issue comment
    if: ${{ !github.event.issue.pull_request }}
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo A comment on issue $NUMBER
        env:
          NUMBER: ${{ github.event.issue.number }}

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`issues`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#issues) | - `opened`- `edited`- `deleted`- `transferred`- `pinned`- `unpinned`- `closed`- `reopened`- `assigned`- `unassigned`- `labeled`- `unlabeled`- `locked`- `unlocked`- `milestoned` - `demilestoned` | Last commit on default branch | Default branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#issues)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when an issue in the workflow's repository is created or modified. For activity related to comments in an issue, use the [`issue_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issue_comment) event. For more information about issues, see "[About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues)." For information about the issue APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#issue)" in the GraphQL API documentation or "[Issues](https://docs.github.com/en/rest/issues)" in the REST API documentation.

For example, you can run a workflow when an issue has been `opened`, `edited`, or `milestoned`.

```
on:
  issues:
    types: [opened, edited, milestoned]

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`label`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#label) | - `created`- `edited`- `deleted` | Last commit on default branch | Default branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#label)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when a label in your workflow's repository is created or modified. For more information about labels, see "[Managing labels](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/managing-labels)." For information about the label APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#label)" in the GraphQL API documentation or "[Issues](https://docs.github.com/en/rest/issues#labels)" in the REST API documentation.

If you want to run your workflow when a label is added to or removed from an issue, pull request, or discussion, use the `labeled` or `unlabeled` activity types for the [`issues`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issues), [`pull_request`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request), [`pull_request_target`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target), or [`discussion`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#discussion) events instead.

For example, you can run a workflow when a label has been `created` or `deleted`.

```
on:
  label:
    types: [created, deleted]

```

**Note**: More than one activity type triggers this event. Although only the `checks_requested` activity type is supported, specifying the activity type will keep your workflow specific if more activity types are added in the future. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#merge_group)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

Runs your workflow when a pull request is added to a merge queue, which adds the pull request to a merge group. For more information see "[Merging a pull request with a merge queue](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/merging-a-pull-request-with-a-merge-queue)".

For example, you can run a workflow when the `checks_requested` activity has occurred.

```
on:
  merge_group:
    types: [checks_requested]

```

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#milestone)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when a milestone in the workflow's repository is created or modified. For more information about milestones, see "[About milestones](https://docs.github.com/en/issues/using-labels-and-milestones-to-track-work/about-milestones)." For information about the milestone APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#milestone)" in the GraphQL API documentation or "[Issues](https://docs.github.com/en/rest/issues#milestones)" in the REST API documentation.

If you want to run your workflow when an issue is added to or removed from a milestone, use the `milestoned` or `demilestoned` activity types for the [`issues`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issues) event instead.

For example, you can run a workflow when a milestone has been `opened` or `deleted`.

```
on:
  milestone:
    types: [opened, deleted]

```

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when someone pushes to a branch that is the publishing source for GitHub Pages, if GitHub Pages is enabled for the repository. For more information about GitHub Pages publishing sources, see "[Configuring a publishing source for your GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)." For information about the REST API, see "[Repositories](https://docs.github.com/en/rest/repos#pages)."

For example, you can run a workflow when the `page_build` event occurs.

```
on:
  page_build

```

**Note**: More than one activity type triggers this event. The `edited` activity type refers to when a project board, not a column or card on the project board, is edited. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#project)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note**: This event only occurs for projects owned by the workflow's repository, not for organization-owned or user-owned projects or for projects owned by another repository.

**Note**: This event only occurs for projects (classic).

Runs your workflow when a project board is created or modified. For activity related to cards or columns in a project board, use the [`project_card`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#project_card) or [`project_column`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#project_column) events instead. For more information about project boards, see "[About projects (classic)](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards)." For information about the project board APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#project)" in the GraphQL API documentation or "[Projects (classic)](https://docs.github.com/en/rest/projects)" in the REST API documentation.

For example, you can run a workflow when a project has been `created` or `deleted`.

```
on:
  project:
    types: [created, deleted]

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`project_card`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#project_card) | - `created`- `moved`- `converted` to an issue- `edited`- `deleted` | Last commit on default branch | Default branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#project_card)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note**: This event only occurs for projects owned by the workflow's repository, not for organization-owned or user-owned projects or for projects owned by another repository.

**Note**: This event only occurs for projects (classic).

Runs your workflow when a card on a project board is created or modified. For activity related to project boards or columns in a project board, use the [`project`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#project) or [`project_column`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#project_column) event instead. For more information about project boards, see "[About projects (classic)](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards)." For information about the project card APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#projectcard)" in the GraphQL API documentation or "[Projects (classic)](https://docs.github.com/en/rest/projects#cards)" in the REST API documentation.

For example, you can run a workflow when a project card has been `created` or `deleted`.

```
on:
  project_card:
    types: [created, deleted]

```

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#project_column)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note**: This event only occurs for projects owned by the workflow's repository, not for organization-owned or user-owned projects or for projects owned by another repository.

**Note**: This event only occurs for projects (classic).

Runs your workflow when a column on a project board is created or modified. For activity related to project boards or cards in a project board, use the [`project`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#project) or [`project_card`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#project_card) event instead. For more information about project boards, see "[About projects (classic)](https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards)." For information about the project column APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#projectcolumn)" in the GraphQL API documentation or "[Projects (classic)](https://docs.github.com/en/rest/projects#columns)" in the REST API documentation.

For example, you can run a workflow when a project column has been `created` or `deleted`.

```
on:
  project_column:
    types: [created, deleted]

```

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when your workflow's repository changes from private to public. For information about the REST API, see "[Repositories](https://docs.github.com/en/rest/repos#edit)."

For example, you can run a workflow when the `public` event occurs.

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`pull_request`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request) | - `assigned`- `unassigned`- `labeled`- `unlabeled`- `opened`- `edited`- `closed`- `reopened`- `synchronize`- `converted_to_draft`- `ready_for_review`- `locked`- `unlocked` - `review_requested` - `review_request_removed` - `auto_merge_enabled` - `auto_merge_disabled` | Last merge commit on the `GITHUB_REF` branch | PR merge branch `refs/pull/:prNumber/merge` |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request)." By default, a workflow only runs when a `pull_request` event's activity type is `opened`, `synchronize`, or `reopened`. To trigger workflows by different activity types, use the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** Workflows will not run on `pull_request` activity if the pull request has a merge conflict. The merge conflict must be resolved first.

Conversely, workflows with the `pull_request_target` event will run even if the pull request has a merge conflict. Before using the `pull_request_target` trigger, you should be aware of the security risks. For more information, see [`pull_request_target`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_target).

Runs your workflow when activity on a pull request in the workflow's repository occurs. For example, if no activity types are specified, the workflow runs when a pull request is opened or reopened or when the head branch of the pull request is updated. For activity related to pull request reviews, pull request review comments, or pull request comments, use the [`pull_request_review`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review), [`pull_request_review_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review_comment), or [`issue_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issue_comment) events instead. For information about the pull request APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#pullrequest)" in the GraphQL API documentation or "[Pulls](https://docs.github.com/en/rest/pulls)" in the REST API documentation.

Note that `GITHUB_SHA` for this event is the last merge commit of the pull request merge branch. If you want to get the commit ID for the last commit to the head branch of the pull request, use `github.event.pull_request.head.sha` instead.

For example, you can run a workflow when a pull request has been opened or reopened.

```
on:
  pull_request:
    types: [opened, reopened]

```

You can use the event context to further control when jobs in your workflow will run. For example, this workflow will run when a review is requested on a pull request, but the `specific_review_requested` job will only run when a review by `octo-team` is requested.

```
on:
  pull_request:
    types: [review_requested]
jobs:
  specific_review_requested:
    runs-on: ubuntu-latest
    if: ${{ github.event.requested_team.name == 'octo-team'}}
    steps:
      - run: echo 'A review from octo-team was requested'

```

You can use the `branches` or `branches-ignore` filter to configure your workflow to only run on pull requests that target specific branches. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpull_requestpull_request_targetbranchesbranches-ignore)."

For example, this workflow will run when someone opens a pull request that targets a branch whose name starts with `releases/`:

```
on:
  pull_request:
    types:
      - opened
    branches:
      - 'releases/**'

```

**Note:** If you use both the `branches` filter and the `paths` filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a pull request that includes a change to a JavaScript (`.js`) file is opened on a branch whose name starts with `releases/`:

```
on:
  pull_request:
    types:
      - opened
    branches:
      - 'releases/**'
    paths:
      - '**.js'

```

To run a job based on the pull request's head branch name (as opposed to the pull request's base branch name), use the `github.head_ref` context in a conditional. For example, this workflow will run whenever a pull request is opened, but the `run_if` job will only execute if the head of the pull request is a branch whose name starts with `releases/`:

```
on:
  pull_request:
    types:
      - opened
jobs:
  run_if:
    if:  startsWith(github.head_ref, 'releases/')
    runs-on: ubuntu-latest
    steps:
      - run: echo "The head of this PR starts with 'releases/'"

```

You can also configure your workflow to run when a pull request changes specific files. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)."

For example, this workflow will run when a pull request includes a change to a JavaScript file (`.js`):

```
on:
  pull_request:
    paths:
      - '**.js'

```

**Note:** If you use both the `branches` filter and the `paths` filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a pull request that includes a change to a JavaScript (`.js`) file is opened on a branch whose name starts with `releases/`:

```
on:
  pull_request:
    types:
      - opened
    branches:
      - 'releases/**'
    paths:
      - '**.js'

```

When a pull request merges, the pull request is automatically closed. To run a workflow when a pull request merges, use the `pull_request` `closed` event type along with a conditional that checks the `merged` value of the event. For example, the following workflow will run whenever a pull request closes. The `if_merged` job will only run if the pull request was also merged.

```
on:
  pull_request:
    types:
      - closed

jobs:
  if_merged:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
    - run: |
        echo The PR was merged

```

Workflows don't run in forked repositories by default. You must enable GitHub Actions in the **Actions** tab of the forked repository.

With the exception of `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository. The `GITHUB_TOKEN` has read-only permissions in pull requests from forked repositories. For more information, see "[Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)."

For pull requests from a forked repository to the base repository, GitHub sends the `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review`, and `pull_request_target` events to the base repository. No pull request events occur on the forked repository.

When a first-time contributor submits a pull request to a public repository, a maintainer with write access may need to approve running workflows on the pull request. For more information, see "[Approving workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks)."

For pull requests from a forked repository to a private repository, workflows only run when they are enabled, see "[Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-forks-of-private-repositories)."

**Note:** Workflows triggered by Dependabot pull requests are treated as though they are from a forked repository, and are also subject to these restrictions.

To run your workflow when a comment on a pull request (not on a pull request's diff) is created, edited, or deleted, use the [`issue_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issue_comment) event. For activity related to pull request reviews or pull request review comments, use the [`pull_request_review`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review) or [`pull_request_review_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review_comment) events.

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request_review)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

Runs your workflow when a pull request review is submitted, edited, or dismissed. A pull request review is a group of pull request review comments in addition to a body comment and a state. For activity related to pull request review comments or pull request comments, use the [`pull_request_review_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review_comment) or [`issue_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issue_comment) events instead. For information about the pull request review APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#pullrequest)" in the GraphQL API documentation or "[Pulls](https://docs.github.com/en/rest/pulls#reviews)" in the REST API documentation.

For example, you can run a workflow when a pull request review has been `edited` or `dismissed`.

```
on:
  pull_request_review:
    types: [edited, dismissed]

```

To run your workflow when a pull request has been approved, you can trigger your workflow with the `submitted` type of `pull_request_review` event, then check the review state with the `github.event.review.state` property. For example, this workflow will run whenever a pull request review is submitted, but the `approved` job will only run if the submitted review is an approving review:

```
on:
  pull_request_review:
    types: [submitted]

jobs:
  approved:
    if: github.event.review.state == 'approved'
    runs-on: ubuntu-latest
    steps:
      - run: echo "This PR was approved"

```

Workflows don't run in forked repositories by default. You must enable GitHub Actions in the **Actions** tab of the forked repository.

With the exception of `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository. The `GITHUB_TOKEN` has read-only permissions in pull requests from forked repositories. For more information, see "[Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)."

For pull requests from a forked repository to the base repository, GitHub sends the `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review`, and `pull_request_target` events to the base repository. No pull request events occur on the forked repository.

When a first-time contributor submits a pull request to a public repository, a maintainer with write access may need to approve running workflows on the pull request. For more information, see "[Approving workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks)."

For pull requests from a forked repository to a private repository, workflows only run when they are enabled, see "[Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-forks-of-private-repositories)."

**Note:** Workflows triggered by Dependabot pull requests are treated as though they are from a forked repository, and are also subject to these restrictions.

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request_review_comment)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

Runs your workflow when a pull request review comment is modified. A pull request review comment is a comment on a pull request's diff. For activity related to pull request reviews or pull request comments, use the [`pull_request_review`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#pull_request_review) or [`issue_comment`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#issue_comment) events instead. For information about the pull request review comment APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#pullrequestreviewcomment)" in the GraphQL API documentation or "[Pulls](https://docs.github.com/en/rest/pulls#comments)" in the REST API documentation.

For example, you can run a workflow when a pull request review comment has been `created` or `deleted`.

```
on:
  pull_request_review_comment:
    types: [created, deleted]

```

Workflows don't run in forked repositories by default. You must enable GitHub Actions in the **Actions** tab of the forked repository.

With the exception of `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository. The `GITHUB_TOKEN` has read-only permissions in pull requests from forked repositories. For more information, see "[Automatic token authentication](https://docs.github.com/en/actions/security-guides/automatic-token-authentication)."

For pull requests from a forked repository to the base repository, GitHub sends the `pull_request`, `issue_comment`, `pull_request_review_comment`, `pull_request_review`, and `pull_request_target` events to the base repository. No pull request events occur on the forked repository.

When a first-time contributor submits a pull request to a public repository, a maintainer with write access may need to approve running workflows on the pull request. For more information, see "[Approving workflow runs from public forks](https://docs.github.com/en/actions/managing-workflow-runs/approving-workflow-runs-from-public-forks)."

For pull requests from a forked repository to a private repository, workflows only run when they are enabled, see "[Managing GitHub Actions settings for a repository](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/managing-github-actions-settings-for-a-repository#enabling-workflows-for-forks-of-private-repositories)."

**Note:** Workflows triggered by Dependabot pull requests are treated as though they are from a forked repository, and are also subject to these restrictions.

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`pull_request`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request) | - `assigned`- `unassigned`- `labeled`- `unlabeled`- `opened`- `edited`- `closed`- `reopened`- `synchronize`- `converted_to_draft`- `ready_for_review`- `locked`- `unlocked` - `review_requested` - `review_request_removed` - `auto_merge_enabled` - `auto_merge_disabled` | Last commit on the PR base branch | PR base branch |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#pull_request_target)." By default, a workflow only runs when a `pull_request_target` event's activity type is `opened`, `synchronize`, or `reopened`. To trigger workflows by different activity types, use the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

Runs your workflow when activity on a pull request in the workflow's repository occurs. For example, if no activity types are specified, the workflow runs when a pull request is opened or reopened or when the head branch of the pull request is updated.

This event runs in the context of the base of the pull request, rather than in the context of the merge commit, as the `pull_request` event does. This prevents execution of unsafe code from the head of the pull request that could alter your repository or steal any secrets you use in your workflow. This event allows your workflow to do things like label or comment on pull requests from forks. Avoid using this event if you need to build or run code from the pull request.

To ensure repository security, branches with names that match certain patterns (such as those which look similar to SHAs) may not trigger workflows with the `pull_request_target` event.

**Warning:** For workflows that are triggered by the `pull_request_target` event, the `GITHUB_TOKEN` is granted read/write repository permission unless the `permissions` key is specified and the workflow can access secrets, even when it is triggered from a fork. Although the workflow runs in the context of the base of the pull request, you should make sure that you do not check out, build, or run untrusted code from the pull request with this event. Additionally, any caches share the same scope as the base branch. To help prevent cache poisoning, you should not save the cache if there is a possibility that the cache contents were altered. For more information, see "[Keeping your GitHub Actions and workflows secure: Preventing pwn requests](https://securitylab.github.com/research/github-actions-preventing-pwn-requests)" on the GitHub Security Lab website.

For example, you can run a workflow when a pull request has been `assigned`, `opened`, `synchronize`, or `reopened`.

```
on:
  pull_request_target:
    types: [assigned, opened, synchronize, reopened]

```

You can use the `branches` or `branches-ignore` filter to configure your workflow to only run on pull requests that target specific branches. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpull_requestpull_request_targetbranchesbranches-ignore)."

For example, this workflow will run when someone opens a pull request that targets a branch whose name starts with `releases/`:

```
on:
  pull_request_target:
    types:
      - opened
    branches:
      - 'releases/**'

```

**Note:** If you use both the `branches` filter and the `paths` filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a pull request that includes a change to a JavaScript (`.js`) file is opened on a branch whose name starts with `releases/`:

```
on:
  pull_request_target:
    types:
      - opened
    branches:
      - 'releases/**'
    paths:
      - '**.js'

```

To run a job based on the pull request's head branch name (as opposed to the pull request's base branch name), use the `github.head_ref` context in a conditional. For example, this workflow will run whenever a pull request is opened, but the `run_if` job will only execute if the head of the pull request is a branch whose name starts with `releases/`:

```
on:
  pull_request_target:
    types:
      - opened
jobs:
  run_if:
    if:  startsWith(github.head_ref, 'releases/')
    runs-on: ubuntu-latest
    steps:
      - run: echo "The head of this PR starts with 'releases/'"

```

You can use the `paths` or `paths-ignore` filter to configure your workflow to run when a pull request changes specific files. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)."

For example, this workflow will run when a pull request includes a change to a JavaScript file (`.js`):

```
on:
  pull_request_target:
    paths:
      - '**.js'

```

**Note:** If you use both the `branches` filter and the `paths` filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a pull request that includes a change to a JavaScript (`.js`) file is opened on a branch whose name starts with `releases/`:

```
on:
  pull_request_target:
    types:
      - opened
    branches:
      - 'releases/**'
    paths:
      - '**.js'

```

When a pull request merges, the pull request is automatically closed. To run a workflow when a pull request merges, use the `pull_request_target` `closed` event type along with a conditional that checks the `merged` value of the event. For example, the following workflow will run whenever a pull request closes. The `if_merged` job will only run if the pull request was also merged.

```
on:
  pull_request_target:
    types:
      - closed

jobs:
  if_merged:
    if: github.event.pull_request.merged == true
    runs-on: ubuntu-latest
    steps:
    - run: |
        echo The PR was merged

```

**Note:** The webhook payload available to GitHub Actions does not include the `added`, `removed`, and `modified` attributes in the `commit` object. You can retrieve the full commit object using the API. For information, see "[Objects](https://docs.github.com/en/graphql/reference/objects#commit)" in the GraphQL API documentation or "[Commits](https://docs.github.com/en/rest/commits#get-a-commit)" in the REST API documentation.

**Note**: An event will not be created when you push more than three tags at once.

Runs your workflow when you push a commit or tag.

For example, you can run a workflow when the `push` event occurs.

**Note**: When a `push` webhook event triggers a workflow run, the Actions UI's "pushed by" field shows the account of the pusher and not the author or committer. However, if the changes are pushed to a repository using SSH authentication with a deploy key, then the "pushed by" field will be the repository admin who verified the deploy key when it was added it to a repository.

You can use the `branches` or `branches-ignore` filter to configure your workflow to only run when specific branches are pushed. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushbranchestagsbranches-ignoretags-ignore)."

For example, this workflow will run when someone pushes to `main` or to a branch that starts with `releases/`.

```
on:
  push:
    branches:
      - 'main'
      - 'releases/**'

```

**Note:** If you use both the `branches` filter and the `paths` filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a push that includes a change to a JavaScript (`.js`) file is made to a branch whose name starts with `releases/`:

```
on:
  push:
    branches:
      - 'releases/**'
    paths:
      - '**.js'

```

You can use the `tags` or `tags-ignore` filter to configure your workflow to only run when specific tags are pushed. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushbranchestagsbranches-ignoretags-ignore)."

For example, this workflow will run when someone pushes a tag that starts with `v1.`.

```
on:
  push:
    tags:
      - v1.**

```

You can use the `paths` or `paths-ignore` filter to configure your workflow to run when a push to specific files occurs. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onpushpull_requestpull_request_targetpathspaths-ignore)."

For example, this workflow will run when someone pushes a change to a JavaScript file (`.js`):

```
on:
  push:
    paths:
      - '**.js'

```

**Note:** If you use both the `branches` filter and the `paths` filter, the workflow will only run when both filters are satisfied. For example, the following workflow will only run when a push that includes a change to a JavaScript (`.js`) file is made to a branch whose name starts with `releases/`:

```
on:
  push:
    branches:
      - 'releases/**'
    paths:
      - '**.js'

```

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#registry_package)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note**: When pushing multi-architecture container images, this event occurs once per manifest, so you might observe your workflow triggering multiple times. To mitigate this, and only run your workflow job for the event that contains the actual image tag information, use a conditional:

```
jobs:
    job_name:
        if: ${{ github.event.registry_package.package_version.container_metadata.tag.name != '' }}

```

Runs your workflow when activity related to GitHub Packages occurs in your repository. For more information, see "[GitHub Packages Documentation](https://docs.github.com/en/packages)."

For example, you can run a workflow when a new package version has been `published`.

```
on:
  registry_package:
    types: [published]

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| [`release`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#release) | - `published` - `unpublished` - `created` - `edited` - `deleted` - `prereleased` - `released` | Last commit in the tagged release | Tag ref of release `refs/tags/<tag_name>` |

**Note**: More than one activity type triggers this event. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#release)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** Workflows are not triggered for the `created`, `edited`, or `deleted` activity types for draft releases. When you create your release through the GitHub browser UI, your release may automatically be saved as a draft.

**Note:** The `prereleased` type will not trigger for pre-releases published from draft releases, but the `published` type will trigger. If you want a workflow to run when stable *and* pre-releases publish, subscribe to `published` instead of `released` and `prereleased`.

Runs your workflow when release activity in your repository occurs. For information about the release APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#release)" in the GraphQL API documentation or "[Releases](https://docs.github.com/en/rest/releases)" in the REST API documentation.

For example, you can run a workflow when a release has been `published`.

```
on:
  release:
    types: [published]

```

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

You can use the GitHub API to trigger a webhook event called [`repository_dispatch`](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#repository_dispatch) when you want to trigger a workflow for activity that happens outside of GitHub. For more information, see "[Repositories](https://docs.github.com/en/rest/repos#create-a-repository-dispatch-event)."

When you make a request to create a `repository_dispatch` event, you must specify an `event_type` to describe the activity type. By default, all `repository_dispatch` activity types trigger a workflow to run. You can use the `types` keyword to limit your workflow to run when a specific `event_type` value is sent in the `repository_dispatch` webhook payload.

```
on:
  repository_dispatch:
    types: [test_result]

```

**Note:** The `event_type` value is limited to 100 characters.

Any data that you send through the `client_payload` parameter will be available in the `github.event` context in your workflow. For example, if you send this request body when you create a repository dispatch event:

```
{
  "event_type": "test_result",
  "client_payload": {
    "passed": false,
    "message": "Error: timeout"
  }
}

```

then you can access the payload in a workflow like this:

```
on:
  repository_dispatch:
    types: [test_result]

jobs:
  run_if_failure:
    if: ${{ !github.event.client_payload.passed }}
    runs-on: ubuntu-latest
    steps:
      - env:
          MESSAGE: ${{ github.event.client_payload.message }}
        run: echo $MESSAGE

```

**Notes**:

* The maximum number of top-level properties in `client_payload` is 10.
* The payload can contain a maximum of 65,535 characters.

Note: The `schedule` event can be delayed during periods of high loads of GitHub Actions workflow runs. High load times include the start of every hour. If the load is sufficiently high enough, some queued jobs may be dropped. To decrease the chance of delay, schedule your workflow to run at a different time of the hour.

The `schedule` event allows you to trigger a workflow at a scheduled time.

You can schedule a workflow to run at specific UTC times using [POSIX cron syntax](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/crontab.html#tag_20_25_07). Scheduled workflows run on the latest commit on the default or base branch. The shortest interval you can run scheduled workflows is once every 5 minutes.

This example triggers the workflow every day at 5:30 and 17:30 UTC:

```
on:
  schedule:
    # * is a special character in YAML so you have to quote this string
    - cron:  '30 5,17 * * *'

```

```
on:
  schedule:
    - cron: '30 5 * * 1,3'
    - cron: '30 5 * * 2,4'

jobs:
  test_schedule:
    runs-on: ubuntu-latest
    steps:
      - name: Not on Monday or Wednesday
        if: github.event.schedule != '30 5 * * 1,3'
        run: echo "This step will be skipped on Monday and Wednesday"
      - name: Every time
        run: echo "This step will always run"

```

Cron syntax has five fields separated by a space, and each field represents a unit of time.

```
┌───────────── minute (0 - 59)
│ ┌───────────── hour (0 - 23)
│ │ ┌───────────── day of the month (1 - 31)
│ │ │ ┌───────────── month (1 - 12 or JAN-DEC)
│ │ │ │ ┌───────────── day of the week (0 - 6 or SUN-SAT)
│ │ │ │ │
│ │ │ │ │
│ │ │ │ │
* * * * *

```

You can use these operators in any of the five fields:

| Operator | Description | Example |
| --- | --- | --- |
| \* | Any value | `15 * * * *` runs at every minute 15 of every hour of every day. |
| , | Value list separator | `2,10 4,5 * * *` runs at minute 2 and 10 of the 4th and 5th hour of every day. |
| - | Range of values | `30 4-6 * * *` runs at minute 30 of the 4th, 5th, and 6th hour. |
| / | Step values | `20/15 * * * *` runs every 15 minutes starting from minute 20 through 59 (minutes 20, 35, and 50). |

**Note:** GitHub Actions does not support the non-standard syntax `@yearly`, `@monthly`, `@weekly`, `@daily`, `@hourly`, and `@reboot`.

You can use [crontab guru](https://crontab.guru/) to help generate your cron syntax and confirm what time it will run. To help you get started, there is also a list of [crontab guru examples](https://crontab.guru/examples.html).

Notifications for scheduled workflows are sent to the user who last modified the cron syntax in the workflow file. For more information, see "[Notifications for workflow runs](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/notifications-for-workflow-runs)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when the status of a Git commit changes. For example, commits can be marked as `error`, `failure`, `pending`, or `success`. If you want to provide more details about the status change, you may want to use the [`check_run`](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#check_run) event. For information about the commit status APIs, see "[Objects](https://docs.github.com/en/graphql/reference/objects#status)" in the GraphQL API documentation or "[Commits](https://docs.github.com/en/rest/commits#commit-statuses)" in the REST API documentation.

For example, you can run a workflow when the `status` event occurs.

If you want to run a job in your workflow based on the new commit state, you can use the `github.event.state` context. For example, the following workflow triggers when a commit status changes, but the `if_error_or_failure` job only runs if the new commit state is `error` or `failure`.

```
on:
  status
jobs:
  if_error_or_failure:
    runs-on: ubuntu-latest
    if: >-
      github.event.state == 'error' ||
      github.event.state == 'failure'
    steps:
      - env:
          DESCRIPTION: ${{ github.event.description }}
        run: |
          echo The status is error or failed: $DESCRIPTION

```

**Note**: More than one activity type triggers this event. Although only the `started` activity type is supported, specifying the activity type will keep your workflow specific if more activity types are added in the future. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#watch)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

Runs your workflow when the workflow's repository is starred. For information about the pull request APIs, see "[Mutations](https://docs.github.com/en/graphql/reference/mutations#addstar)" in the GraphQL API documentation or "[Activity](https://docs.github.com/en/rest/activity#starring)" in the REST API documentation.

For example, you can run a workflow when someone stars a repository, which is the `started` activity type for a watch event.

```
on:
  watch:
    types: [started]

```

| Webhook event payload | Activity types | `GITHUB_SHA` | `GITHUB_REF` |
| --- | --- | --- | --- |
| Same as the caller workflow | Not applicable | Same as the caller workflow | Same as the caller workflow |

`workflow_call` is used to indicate that a workflow can be called by another workflow. When a workflow is triggered with the `workflow_call` event, the event payload in the called workflow is the same event payload from the calling workflow. For more information see, "[Reusing workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)."

The example below only runs the workflow when it's called from another workflow:

```
on: workflow_call

```

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

To enable a workflow to be triggered manually, you need to configure the `workflow_dispatch` event. You can manually trigger a workflow run using the GitHub API, GitHub CLI, or GitHub browser interface. For more information, see "[Manually running a workflow](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)."

```
on: workflow_dispatch

```

You can configure custom-defined input properties, default input values, and required inputs for the event directly in your workflow. When you trigger the event, you can provide the `ref` and any `inputs`. When the workflow runs, you can access the input values in the `inputs` context. For more information, see "[Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts)."

**Notes**:

* The workflow will also receive the inputs in the `github.event.inputs` context. The information in the `inputs` context and `github.event.inputs` context is identical except that the `inputs` context preserves Boolean values as Booleans instead of converting them to strings. The `choice` type resolves to a string and is a single selectable option.
* The maximum number of top-level properties for `inputs` is 10.
* The maximum payload for `inputs` is 65,535 characters.

This example defines inputs called `logLevel`, `tags`, and `environment`. You pass values for these inputs to the workflow when you run it. This workflow then prints the values to the log, using the `inputs.logLevel`, `inputs.tags`, and `inputs.environment` context properties.

```
on:
  workflow_dispatch:
    inputs:
      logLevel:
        description: 'Log level'
        required: true
        default: 'warning'
        type: choice
        options:
        - info
        - warning
        - debug
      tags:
        description: 'Test scenario tags'
        required: false
        type: boolean
      environment:
        description: 'Environment to run tests against'
        type: environment
        required: true

jobs:
  log-the-inputs:
    runs-on: ubuntu-latest
    steps:
      - run: |
          echo "Log level: $LEVEL"
          echo "Tags: $TAGS"
          echo "Environment: $ENVIRONMENT"
        env:
          LEVEL: ${{ inputs.logLevel }}
          TAGS: ${{ inputs.tags }}
          ENVIRONMENT: ${{ inputs.environment }}

```

If you run this workflow from a browser you must enter values for the required inputs manually before the workflow will run.

You can also pass inputs when you run a workflow from a script, or by using GitHub CLI. For example:

```
gh workflow run run-tests.yml -f logLevel=warning -f tags=false -f environment=staging

```

For more information, see the GitHub CLI information in "[Manually running a workflow](https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow)."

**Note**: More than one activity type triggers this event. The `requested` activity type does not occur when a workflow is re-run. For information about each activity type, see "[Webhook events and payloads](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#workflow_run)." By default, all activity types trigger workflows that run on this event. You can limit your workflow runs to specific activity types using the `types` keyword. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onevent_nametypes)."

**Note:** This event will only trigger a workflow run if the workflow file is on the default branch.

**Note:** You can't use `workflow_run` to chain together more than three levels of workflows. For example, if you attempt to trigger five workflows (named `B` to `F`) to run sequentially after an initial workflow `A` has run (that is: `A` → `B` → `C` → `D` → `E` → `F`), workflows `E` and `F` will not be run.

This event occurs when a workflow run is requested or completed. It allows you to execute a workflow based on execution or completion of another workflow. The workflow started by the `workflow_run` event is able to access secrets and write tokens, even if the previous workflow was not. This is useful in cases where the previous workflow is intentionally not privileged, but you need to take a privileged action in a later workflow.

In this example, a workflow is configured to run after the separate "Run Tests" workflow completes.

```
on:
  workflow_run:
    workflows: [Run Tests]
    types:
      - completed

```

If you specify multiple `workflows` for the `workflow_run` event, only one of the workflows needs to run. For example, a workflow with the following trigger will run whenever the "Staging" workflow or the "Lab" workflow completes.

```
on:
  workflow_run:
    workflows: [Staging, Lab]
    types:
      - completed

```

A workflow run is triggered regardless of the conclusion of the previous workflow. If you want to run a job or step based on the result of the triggering workflow, you can use a conditional with the `github.event.workflow_run.conclusion` property. For example, this workflow will run whenever a workflow named "Build" completes, but the `on-success` job will only run if the "Build" workflow succeeded, and the `on-failure` job will only run if the "Build" workflow failed:

```
on:
  workflow_run:
    workflows: [Build]
    types: [completed]

jobs:
  on-success:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'success' }}
    steps:
      - run: echo 'The triggering workflow passed'
  on-failure:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    steps:
      - run: echo 'The triggering workflow failed'

```

You can use the `branches` or `branches-ignore` filter to specify what branches the triggering workflow must run on in order to trigger your workflow. For more information, see "[Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#onworkflow_runbranchesbranches-ignore)." For example, a workflow with the following trigger will only run when the workflow named `Build` runs on a branch named `canary`.

```
on:
  workflow_run:
    workflows: [Build]
    types: [requested]
    branches: [canary]

```

You can access the [`workflow_run` event payload](https://docs.github.com/en/webhooks-and-events/webhooks/webhook-events-and-payloads#workflow_run) that corresponds to the workflow that triggered your workflow. For example, if your triggering workflow generates artifacts, a workflow triggered with the `workflow_run` event can access these artifacts.

The following workflow uploads data as an artifact. (In this simplified example, the data is the pull request number.)

```
name: Upload data

on:
  pull_request:

jobs:
  upload:
    runs-on: ubuntu-latest

    steps:
      - name: Save PR number
        env:
          PR_NUMBER: ${{ github.event.number }}
        run: |
          mkdir -p ./pr
          echo $PR_NUMBER > ./pr/pr_number
      - uses: actions/upload-artifact@v3
        with:
          name: pr_number
          path: pr/

```

When a run of the above workflow completes, it triggers a run of the following workflow. The following workflow uses the `github.event.workflow_run` context and the GitHub REST API to download the artifact that was uploaded by the above workflow, unzips the downloaded artifact, and comments on the pull request whose number was uploaded as an artifact.

```
name: Use the data

on:
  workflow_run:
    workflows: [Upload data]
    types:
      - completed

jobs:
  download:
    runs-on: ubuntu-latest
    steps:
      - name: 'Download artifact'
        uses: actions/github-script@v6
        with:
          script: |
            let allArtifacts = await github.rest.actions.listWorkflowRunArtifacts({
               owner: context.repo.owner,
               repo: context.repo.repo,
               run_id: context.payload.workflow_run.id,
            });
            let matchArtifact = allArtifacts.data.artifacts.filter((artifact) => {
              return artifact.name == "pr_number"
            })[0];
            let download = await github.rest.actions.downloadArtifact({
               owner: context.repo.owner,
               repo: context.repo.repo,
               artifact_id: matchArtifact.id,
               archive_format: 'zip',
            });
            let fs = require('fs');
            fs.writeFileSync(`${process.env.GITHUB_WORKSPACE}/pr_number.zip`, Buffer.from(download.data));

      - name: 'Unzip artifact'
        run: unzip pr_number.zip

      - name: 'Comment on PR'
        uses: actions/github-script@v6
        with:
          github-token: ${{ secrets.GITHUB_TOKEN }}
          script: |
            let fs = require('fs');
            let issue_number = Number(fs.readFileSync('./pr_number'));
            await github.rest.issues.createComment({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: issue_number,
              body: 'Thank you for the PR!'
            });

```

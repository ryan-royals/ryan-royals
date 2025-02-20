---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/a-pretty-good-terraform-module-template/","tags":["rw/articles"]}
---

![rw-book-cover](https://devopstar.com/static/1713331539805.0596469762156/a-pretty-good-terraform-module-template-seo.jpg)

4 min read

#### Introduction

When creating a Terraform module, it's essential to ensure that it's easy to use, maintain, and contribute to. I spent some time creating a pretty good Terraform module template that includes some of the nice-to-have features that I've found useful in my projects.

Publishing a module using this template will let you simply use and reference a versioned copy of your module like so - where the `ref` is the version you want to use:

```
module "your_module" {
  source = "github.com/t04glovern/terraform-repo-template?ref=v1.0.0"
  your_variable = "abcdefg"
}
```

To use the template, use this link to create a new repository with the template: [Create Terraform Module](https://github.com/new?template_name=terraform-repo-template&template_owner=t04glovern)

#### Features

##### Devcontainer for VSCode

The template includes a `.devcontainer` folder that allows you to open the project in a container with all the required tools and extensions pre-installed.

By default, the container includes the following tools:

* Terraform
	+ tfsec
	+ terraform-docs
	+ tflint (with format on save)
* pre-commit

##### Semantic Versioning with Releases

The template includes GitHub Action workflows that automatically create releases based on the commit messages.

Provided that the commit message follows the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format, the release will be automatically created with the correct version number and update the CHANGELOG.md file with the release notes.

* **fix**: a commit of the type fix patches a bug in your codebase (this correlates with `PATCH` in Semantic Versioning).
* **feat**: feat: a commit of the type feat introduces a new feature to the codebase (this correlates with `MINOR` in Semantic Versioning).
* **any!**: a commit that has a footer BREAKING CHANGE:, or appends a ! after the type/scope, introduces a breaking API change (correlating with `MAJOR` in Semantic Versioning).
	+ A BREAKING CHANGE can be part of commits of any type.
* **docs**: updates to documentation such as a the README or other markdown files
* **ci**: continuous integration related
* **chore**: changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)

An example of the workflow you should follow when making a change for example (assume the current version is 1.0.0):

```
# Create a new branch
git checkout -b my-new-feature

# Make some changes

# if the change made is a new feature, that is not a breaking change
git commit -m "feat: Add new feature" # produces version 1.1.0

# if the change made is a bug fix - results in 
git commit -m "fix: Fix bug" # produces version 1.0.1

# if a fix includes a breaking change
git commit -m "fix!: Add new fix" # produces version 2.0.0
```

##### Automatic README Generation

The template includes a `.terraform-docs.yml` file that generates a README.md file based on the Terraform module's variables and outputs.

When you run `terraform-docs . --config=.terraform-docs.yml`, the README.md file will be updated with the latest variables and outputs.

[![README Example](https://devopstar.com/static/1713331539809.0596469762159/36eca/terraform-docs-output-example.png)](https://devopstar.com/static/1713331539809.0596469762159/36eca/terraform-docs-output-example.png)README Example
##### Pre-commit Hooks

>  **Note**: these pre-commits are taken from the [https://github.com/terraform-aws-modules](https://github.com/terraform-aws-modules/terraform-aws-lambda/blob/master/.github/workflows/pre-commit.yml) repository.
> 
>  

The template includes a `.pre-commit-config.yaml` file that includes a set of pre-commit hooks that run before each commit.

They are automatically installed for you if you use the `.devcontainer` or you can install them manually by running `pre-commit install`.

For example, when you run `git commit -m "Add new feature"`, the pre-commit hooks will run and check the Terraform code for any issues.

```
Terraform fmt............................................................Passed
Terraform validate.......................................................Passed
Terraform docs...........................................................Failed
- hook id: terraform_docs
- files were modified by this hook
Terraform validate with tflint...........................................Passed
```

In the example above, the `terraform-docs` hook updated the README.md file with the latest variables, so you would need to commit the changes (run `git add .` and `git commit -m "docs: Update README.md"`).

This new commit should pass all the pre-commit hooks.

```
Terraform fmt............................................................Passed
Terraform validate.......................................................Passed
Terraform docs...........................................................Passed
Terraform validate with tflint...........................................Passed
```

##### Example module for testing

The template includes an [examples](https://github.com/t04glovern/terraform-repo-template/tree/main/examples) folder that includes a basic terraform project that calls the modules in the root of the repository.

[![Example of GitHub actions on pull requests](https://devopstar.com/static/1713331539809.0596469762158/8740f/terraform-ci-testing-github-actions.png)](https://devopstar.com/static/1713331539809.0596469762158/8740f/terraform-ci-testing-github-actions.png)Example of GitHub actions on pull requests
The tests are run using GitHub Actions and include the following steps:

* pre-commit hooks are run and must pass (terraform fmt, terraform validate, terraform docs).
* The example module is validated using `terraform validate` and `tflint`.
	+ validation is run against all versions of Terraform between the minimum terraform version specified in the `versions.tf` file and the latest version of Terraform.
* Pull request titles must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format. A GitHub action checks the title and will fail the PR if it doesn't match the format.

#### Conclusion

I hope this template helps you ignore some of the boilerplate and focus on creating the best Terraform modules you can.

If you have any questions or feedback, please feel free to reach out to me on [Twitter](https://twitter.com/nathangloverAUS) or [LinkedIn](https://www.linkedin.com/in/glovernathan/).

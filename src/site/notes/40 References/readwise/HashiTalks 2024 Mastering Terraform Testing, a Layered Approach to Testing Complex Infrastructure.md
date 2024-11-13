---
{"dg-publish":true,"permalink":"/40-references/readwise/hashi-talks-2024-mastering-terraform-testing-a-layered-approach-to-testing-complex-infrastructure/","tags":["rw/articles"]}
---

![rw-book-cover](https://mattias.engineer/img/favicon/blue.png)

## Summary

The document discusses the layered approach to testing complex infrastructure using Terraform, focusing on validating, testing, and integrating Terraform modules. It emphasizes the importance of thorough testing, including imperative and declarative validation techniques, and introduces the concept of test-specific modules. The text delves into creating tests for input variables, utilizing custom validations, and setting up continuous checks with Terraform Cloud. It also touches on integration testing, dependency management, and the use of mocks in testing scenarios, providing detailed examples and workflows for implementing testing strategies effectively.

## Highlights

jobs: test: strategy: fail-fast: false matrix: location: ["swedencentral", "westeurope", "northeurope"] version: ["2.0.0", "3.0.0", "3.1.0"] runs-on: ubuntu-latest steps: - name: Azure login uses: azure/login@v1 - uses: actions/checkout@v4 - run: | sed 's/{{VERSION}}/${{ matrix.version }}/g; s/{{LOCATION}}/${{ matrix.location }}/g' \ templates/main.tftest.hcl.template > tests/main.tftest.hcl - uses: hashicorp/setup-terraform@v2 with: terraform_wrapper: false - run: terraform init env: TF_TOKEN_app_terraform_io: ${{ secrets.TF_TOKEN }} - run: terraform test ([View Highlight] (https://read.readwise.io/read/01hrx6p52djmmyt1733tx4emag))



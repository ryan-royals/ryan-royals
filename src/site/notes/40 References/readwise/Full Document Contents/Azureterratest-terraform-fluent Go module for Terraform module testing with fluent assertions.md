---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/azureterratest-terraform-fluent-go-module-for-terraform-module-testing-with-fluent-assertions/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/1ed434553ec644f4876c5bfea6e0dbe532b4472bf9d2a760cb5249d5fbb92bd7/Azure/terratest-terraform-fluent)

#### Create list

Beta Lists are currently in beta. [Share feedback and report bugs.](https://github.com//github/feedback/discussions/categories/lists)

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Azure/terratest-terraform-fluent?resume=1)

### Azure/terratest-terraform-fluent

####  [README.md](https://github.com/Azure/terratest-terraform-fluent#readme)

### terratest-terraform-fluent

[![codecov](https://camo.githubusercontent.com/3dc13c8ca1569e2221efe2bcba4f15d9e176f11008476431c1508645e5e96b3e/68747470733a2f2f636f6465636f762e696f2f67682f417a7572652f7465727261746573742d7465727261666f726d2d666c75656e742f6272616e63682f6d61696e2f67726170682f62616467652e7376673f746f6b656e3d6f424731714663385336)](https://codecov.io/gh/Azure/terratest-terraform-fluent)
Terratest extension package for testing Terraform code with fluent assertions.

#### Usage

```
package test

import (
  "testing"

  "github.com/Azure/terratest-terraform-fluent/check"
  "github.com/Azure/terratest-terraform-fluent/setuptest"
  "github.com/stretchr/testify/assert"
  "github.com/stretchr/testify/require"
)

const (
  moduleDir = "../"
)

func TestSomeTerraform(t *testing.T) {
  // Set up the Terraform test and run terraform init, plan and show,
  // saving the plan output to a struct.
  // The returned struct in tftest contains the temp dir, the plan struct,
  // the terraform options, and the clean up func.
  //
  // The Dirs inputs are the test root directory and the relative path to the test code.
  // (this must be a subdirectory of the test root directory).
  // To test the module in the current directory, use "" for the second input.
  //
  // The WithVars inputs are the Terraform variables to pass to the test.
  // The InitPlanShow input is the testing.T pointer.
  tftest, err := setuptest.Dirs(moduleDir, "").WithVars(nil).InitPlanShow(t)
  require.NoError(t, err)

  // Defer the cleanup, which will delete the temporary directory and provide coherent logging.
  // THIS IS VERY IMPORTANT :)
  defer tftest.Cleanup()

  // Check that the plan contains the expected number of resources.
  check.InPlan(tftest.Plan).NumberOfResourcesEquals(1).ErrorIsNil(t)

  // Check that the plan contains the expected resource, with an attribute called `my_attribute` and
  // a corresponding value of `my_value`.
  check.InPlan(tftest.Plan).That("my_terraform_resource.name").Key("my_attribute").HasValue("my_value").ErrorIsNil(t)

  // Check that the plan contains the expected resource, with an attribute called `my_complex_attribute` and
  // a gjson query in a list called `mylist`, taking the first element, which is an object with a property
  // called `property`, with a value of `my_value`. See: https://github.com/tidwall/gjson/blob/master/SYNTAX.md
  check.InPlan(tftest.Plan).That("my_terraform_resource.name").Key("my_complex_attribute").Query("mylist.0.property").HasValue("my_value").ErrorIsNil(t)

  // Ensure that the terraform apply is idempotent.
  defer tftest.Destroy()
  tftest.ApplyIdempotent().ErrorIsNil(t)

  // Retrieve the value from the plan and check it using an external func.
  val, err := check.InPlan(tftest.Plan).That("my_terraform_resource.name").Key("my_other_attribute").GetValue()
  assert.NoError(t, err)
  assert.NoError(t, myValidationFunc(val))

  // Check that the output contains the expected value.
  tftest.Output("my_output").HasValue("my_output_value").ErrorIsNil(t)
}
```

![](https://storage.googleapis.com/pieces-web-extensions-cdn/pieces.png)
![](https://storage.googleapis.com/pieces-web-extensions-cdn/link.png)

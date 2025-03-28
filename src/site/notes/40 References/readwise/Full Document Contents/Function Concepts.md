---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/function-concepts/","tags":["rw/articles"]}
---

!rw-book-cover](https://developer.hashicorp.com/og-image/terraform.jpg)

This page describes Terraform concepts relating to provider-defined functions within framework-based provider code. Provider-defined functions are supported in Terraform 1.8 and later. The What is Terraform](/terraform/intro), Terraform language](/terraform/language), and Plugin Development](/terraform/plugin) documentation covers more general concepts behind Terraform's workflow, its configuration, and how it interacts with providers.

The purpose of provider-defined functions is to encapsulate offline, computational logic beyond Terraform's built-in functions to simplify practitioner configurations. Terraform expects that provider-defined functions are implemented without side-effects and as pure functions where given the same input data that they always return the same output. Refer to HashiCorp Provider Design Principles](/terraform/plugin/best-practices/hashicorp-provider-design-principles) for additional best practice details.

Example use cases include:

* Transforming existing data, such as merging complex data structures using a specific algorithm or converting between encodings.
* Parsing combined data into individual, referenceable components, such as taking an Amazon Resource Name (ARN) and returning an object of region, account identifier, etc. attributes.
* Building combined data from individual components, such as returning an Amazon Resource Name (ARN) based on given region, account identifier, etc. data.
* Static data lookups when there is no remote system query available, such as returning a data value typically necessary for a practitioner configuration.

Differences from other provider-defined concepts include:

* Data Sources](/terraform/plugin/framework/data-sources): Intended to perform online or provider configuration dependent data lookup, which participate in Terraform's operational graph.
* Resources](/terraform/plugin/framework/resources): Intended to manage the full lifecycle (create, update, destroy) of a remote system component, which participate in Terraform's operational graph.

There are two main components of provider-defined functions:

* **Definition**: Defines the expected input and output data along with documentation descriptions.
* **Call**: When a practioner configuration causes a function's logic to be run.

Within a function definition the components are:

* **Parameters**: An ordered list of definitions for input data.
	+ **Variadic Parameter**: An optional, final parameter which accepts zero, one, or multiple parts of input data.
* **Return**: The definition for output data.

Similar to many programming languages, when the function is called, the terminology for the data is slightly different than the terminology for the definition.

* **Arguments**: Positionally ordered data based on the definitions of the parameters.
* **Result**: Data based on the definition of the return.

For each provider listed as a required provider](/terraform/language/providers/requirements), Terraform will query the provider for its function definitions. If a configuration attempts to call a provider-defined function without listing the provider as required, Terraform will return an error.

Terraform will typically call functions before other provider concepts are evaluated. This includes before provider configuration being evaluated, which the framework enforces by not exposing provider configuration data to function implementations.

Terraform requires that function names must be valid identifiers](/terraform/language/syntax/configuration#identifiers).

Terraform will statically validate that the number and types of arguments in a configuration match the definitions of parameters, otherwise returning an error.

If a null value is given as an argument, without individual parameter definition opt-in, Terraform will return an error. If an unknown value is given as an argument, without individual parameter definition opt-in, Terraform will skip calling the provider logic entirely and set the function result to an unknown value matching the return type.

Terraform will statically validate that the return type is appropriately used in consuming configuration, otherwise returning an error.

Function logic must always set the result to the return type, otherwise Terraform will return an error.

Function logic can only set the result to an unknown value if there is a parameter that opted into unknown value handling and an unknown value argument was received for one of those parameters.

---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/cdktf-0-20-improves-implementation-of-iterators-and-enables-hcl-output/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.datocms-assets.com/2885/1704908313-share-cdktf-0-20-improves-implementation-of-iterators-and-enables-hcl-output.png?w=1200&h=630&fit=crop&auto=format)

The mission of CDK for Terraform (CDKTF) is to simplify Terraform adoption. We introduced the [generally available version of CDKTF](https://www.hashicorp.com/blog/cdk-for-terraform-now-generally-available) in August of 2022, enabling developers not familiar with HashiCorp Configuration Language (HCL) to write Terraform configurations in their choice of language, including TypeScript, Python, C#, Java, and Go. In CDKTF 0.12, we introduced a new API called `TerraformIterator` that supports dynamic list iterations on the block and resource level to enable workflows that users are familiar with in HCL.

Today, we’re releasing CDKTF version 0.20, which improves the existing implementation of iterators. This new support allows developers to handle more complex cases, in which resources are created based on data that’s known only at run time. CDKTF version 0.20 also enables HCL output and improves error messages.

The iterator improvements include:

* Chaining iterators
* Complex list iterators
* Support mapping to primitive values

#### Chaining iterators

CDKTF 0.20 supports accessing resources created by iterators. This was previously possible only with an [escape hatch](https://developer.hashicorp.com/terraform/cdktf/concepts/resources#escape-hatch). To [chain iterators](https://terraform-9uruiy3wt-hashicorp.vercel.app/terraform/cdktf/concepts/iterators#chaining-iterators) you can use the `TerraformIterator.fromResources()` or `TerraformIterator.fromDataSources()` methods with the resource or data source you want to chain as an argument:

```
const s3BucketConfigurationIterator = TerraformIterator.fromMap({
  website: {
	name: "website-static-files",
	tags: { app: "website" },
  },
  images: {
	name: "images",
	tags: { app: "image-converter" },
  },
});

const s3Buckets = new S3Bucket(this, "complex-iterator-buckets", {
  forEach: s3BucketConfigurationIterator,
  bucket: s3BucketConfigurationIterator.getString("name"),
  tags: s3BucketConfigurationIterator.getStringMap("tags"),
});

// This would be TerraformIterator.fromDataSources for data_sources
const s3BucketsIterator = TerraformIterator.fromResources(s3Buckets);
const helpFile = new TerraformAsset(this, "help", {
  path: "./help",
});

new S3BucketObject(this, "object", {
  forEach: s3BucketsIterator,
  bucket: s3BucketsIterator.getString("id"),
  key: "help",
  source: helpFile.path,
});
```
#### Complex list iterators

We now support iterating on resource attributes containing values that are known only after `apply`. The most common example for this use case is validating an AWS Certificate Manager (ACM) certificate through DNS. In this case, the `domain_validation_options` attribute contains values that are known only after the AWS ACM certificate resource has been created:

```
// Creates a new AWS managed SSL Certificate
const cert = new AcmCertificate(this, "cert", {
  domainName: "example.com",
  validationMethod: "DNS",
});

// The existing domain that we control and want to create an SSL certificate for
const dataAwsRoute53ZoneExample = new DataAwsRoute53Zone(this, "dns_zone", {
  name: "example.com",
  privateZone: false,
});

// NEW: fromComplexList() allows iterating over the domain validation options
//      while mapping it into a map with "domain_name" as the key
const exampleForEachIterator = TerraformIterator.fromComplexList(
  cert.domainValidationOptions,
  "domain_name"
);

// This will create the DNS records to validate the ACM certificate based
// on the domain validation options from the ACM Certificate Resource
const records = new Route53Record(this, "record", {
  forEach: exampleForEachIterator,
  allowOverwrite: true,
  name: exampleForEachIterator.getString("name"),
  records: [exampleForEachIterator.getString("record")],
  ttl: 60,
  type: exampleForEachIterator.getString("type"),
  zoneId: dataAwsRoute53ZoneExample.zoneId,
});

const recordsIterator = TerraformIterator.fromResources(records);

// This causes Terraform to wait until the validation through DNS was successful
new AcmCertificateValidation(this, "validation", {
  certificateArn: cert.arn,
  validationRecordFqdns: Token.asList(recordsIterator.pluckProperty("fqdn")),
});
```
#### Support mapping to primitive values

Iterators now support [expressing more variations of `for` expressions](https://developer.hashicorp.com/terraform/cdktf/concepts/iterators#using-for-expressions) in HCL. For example, it is now possible to map a list of objects into a list of strings by “plucking” one of their properties

```
new TerraformLocal(this, "list-of-names", mapIterator.pluckProperty("name"));
```
The new functions are exposed on complex (i.e. non-primitive) computed (i.e. not configurable) lists. They include `values()`, `keys()`, `pluckProperty()`, `forExpressionForList()` and `forExpressionForMap()`. The latter two are very close to HCL, allowing you to leverage the full power of HCL for expressions without using an [override escape hatch](https://developer.hashicorp.com/terraform/cdktf/concepts/resources#escape-hatch).

#### Output HCL instead of Terraform JSON

CDKTF synth now supports HCL as an output, in addition to the Terraform JSON which was previously supported. This makes it easier to debug the configuration that CDKTF creates, as HCL output is easier for people to read.

Moreover, this means you can use CDKTF as a templating engine to generate a Terraform config that will then be used and edited by other teams. Finally, it means you can now use CDKTF with tooling that supports only Terraform HCL. Although Terraform Cloud’s native features, like policy evaluation and health assessments, work with JSON, other common tools, like code scanners and linters, support only HCL.

#### Improved error messages

Error messages in the `cdktf` package now give more context and propose solutions to the problem at hand. For example:

**Old**:

```
No app could be identified for the construct at path 'path/to/construct'

```

**New**:

```
No app could be identified for the construct at path 'path/to/construct', likely a TerraformStack.
The scope of CDKTF's TerraformStack class is a single App instance created by 'const app = new App()'. The App is the root of your project that holds project configuration and validations.
You can learn more about the App here: https://developer.hashicorp.com/terraform/cdktf/concepts/cdktf-architecture#app-class:~:text=and%20Resource.-,App%20Class,-Each%20CDKTF%20project

```

#### Try CDK for Terraform

If you’re new to the project, these [tutorials for CDKTF](https://developer.hashicorp.com/terraform/tutorials/cdktf) are the best way to get started. You can dive deeper into our documentation with this [overview of CDKTF](https://developer.hashicorp.com/terraform/cdktf).

Whether you’re still experimenting or actively using CDK for Terraform, we’d love to hear from you. Please [file any bugs you encounter](https://cdk.tf/bug), let us know about your [feature requests](https://cdk.tf/feature), and share your questions, thoughts, and experiences in the [CDK for Terraform discussion forum](https://discuss.hashicorp.com/c/terraform-core/cdk-for-terraform/47).

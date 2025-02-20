---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/pulumi-for-terraform-users/","tags":["rw/articles"]}
---

![rw-book-cover](https://www.pulumi.com/logos/brand/og-default.png)

#### Increase scale and productivity with programming languages

Pulumi and Terraform describe and provision infrastructure differently. Terraform uses a proprietary domain-specific language (DSL) called HashiCorp Configuration Language (HCL). Pulumi uses general purpose languages that better help you tame cloud complexity and accelerate development velocity.

See our [Pulumi vs. Terraform guide](https://www.pulumi.com/docs/concepts/vs/terraform) for detailed differences between the two platforms.

Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/PqAP4BunQZU?rel=0) 

##### Take advantage of real coding features with Pulumi

Pulumi provides a more expressive and efficient way to define cloud resources:

* Use variable loops, not copy/paste
* Use any Node libaries (or Python/Go)
* On-the-fly error checking
* Freeform code instead of complex interpolations

[Find many other examples here](https://github.com/pulumi/examples).

```
import * as aws from "@pulumi/aws";
import { readdirSync } from "fs";
import { join as pathjoin } from "path";
const bucket = new aws.s3.Bucket("mybucket");
const folder = "./files";
let files = readdirSync(folder);
for (let file of files) {
    const object = new aws.s3.BucketObject(file, {
        bucket: bucket,
        source: new pulumi.FileAsset(pathjoin(folder, file))
    });
}
export const bucketname = bucket.id;

```

```
resource "aws_s3_bucket" "mybucket" {
    bucket_prefix = "mybucket"
}
resource "aws_s3_bucket_object" "data_txt" {
    key        = "data.txt"
    bucket     = "${aws_s3_bucket.mybucket.id}"
    source     = "./files/data.txt"
}
resource "aws_s3_bucket_object" "index_html" {
    key        = "index.html"
    bucket     = "${aws_s3_bucket.mybucket.id}"
    source     = "./files/index.html"
}
resource "aws_s3_bucket_object" "index_js" {
    key        = "index.js"
    bucket     = "${aws_s3_bucket.mybucket.id}"
    source     = "./files/index.js"
}
resource "aws_s3_bucket_object" "main.css" {
    key        = "main.css"
    bucket     = "${aws_s3_bucket.mybucket.id}"
    source     = "./files/main.css"
}
resource "aws_s3_bucket_object" "favicon.ico" {
    key        = "favicon.ico"
    bucket     = "${aws_s3_bucket.mybucket.id}"
    source     = "./files/favicon.ico"
}

```

##### Productive cloud native programming

Pulumi is designed with cloud native computing in mind - from containers to serverless, providing a productive model for quickly building and deploying apps:

* Rich, built in support for event handlers
* Easy-to-use in-line Lambdas for simple functions
* Use JavaScript for both infrastructure and Lambda callbacks
* Avoid the need for significant boiler plate code

[Find many other examples here](https://github.com/pulumi/examples).

```
import * as aws from "@pulumi/aws";
// Create an S3 Bucket.
const bucket = new aws.s3.Bucket("mybucket");
// Register a Lambda to handle the Bucket notification.
bucket.onObjectCreated("newObj", async (ev, ctx) => {
    // Write code inline, or use a Zip
    console.log(JSON.stringify(ev));
});
// Export the bucket name for easy scripting.
export const bucketName = bucket.id;

```

```
resource "aws_s3_bucket" "mybucket" {
    bucket_prefix = "mybucket"
}
data "archive_file" "lambda_zip" {
    type        = "zip"
    output_path = "lambda.zip"
    source {
        filename = "index.js"
        content = < {
            console.log(JSON.stringify(ev))
        }
        EOF
    }
}
data "aws_iam_policy_document" "lambda-assume-role-policy" {
    statement {
        actions = ["sts:AssumeRole"]
        principals {
            type        = "Service"
            identifiers = ["lambda.amazonaws.com"]
        }
    }
}
resource "aws_iam_role" "lambda" {
    assume_role_policy = "${data.aws_iam_policy_document.lambda-assume-role-policy.json}"
}
resource "aws_lambda_function" "my_lambda" {
    filename = "${data.archive_file.lambda_zip.output_path}"
    source_code_hash = "${data.archive_file.lambda_zip.output_base64sha256}"
    function_name = "my_lambda"
    role = "${aws_iam_role.lambda.arn}"
    handler = "index.handler"
    runtime = "nodejs8.10"
}
resource "aws_lambda_permission" "allow_bucket" {
    statement_id  = "AllowExecutionFromS3Bucket"
    action        = "lambda:InvokeFunction"
    function_name = "${aws_lambda_function.my_lambda.arn}"
    principal     = "s3.amazonaws.com"
    source_arn    = "${aws_s3_bucket.mybucket.arn}"
}
resource "aws_s3_bucket_notification" "bucket_notification" {
    bucket = "${aws_s3_bucket.mybucket.id}"
    lambda_function {
        lambda_function_arn = "${aws_lambda_function.my_lambda.arn}"
        events              = ["s3:ObjectCreated:*"]
    }
}
output "bucket_name" {
    value = "${aws_s3_bucket.mybucket.id}"
}

```

#### Next steps

As a Terraform user, there are many ways that you can adopt Pulumi. You can convert existing HCL to Pulumi programs, adopt existing Terraform resource state, and coexist by referencing Terraform stacks from within Pulumi programs.

* ###### Convert HCL to Pulumi code

[Learn more](https://www.pulumi.com/blog/converting-full-terraform-programs-to-pulumi)
* ###### Adopt existing resource state

[Learn more](https://www.pulumi.com/blog/adopting-existing-cloud-resources-into-pulumi)
* ###### Coexist with Terraform state

[Learn more](https://www.pulumi.com/blog/using-terraform-remote-state-with-pulumi/)

#### Need help migrating your Terraform?

We can help you migrate all of your Terraform workspaces as part of your Pulumi Enterprise and Business Critical onboarding. We will convert all your Terraform HCL to your favorite language and migrate the Terraform state. Contact us to get started.

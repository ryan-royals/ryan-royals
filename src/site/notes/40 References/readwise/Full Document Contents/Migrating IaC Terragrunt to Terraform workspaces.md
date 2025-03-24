---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/migrating-ia-c-terragrunt-to-terraform-workspaces/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*LQg0krnQta6xz4JuLenC3w.png)

In one of my projects I was tasked to migrating the IaC from Terragrunt to Terraform workspaces in order to align with the Organisation standard procedure to manage different AWS environments.

The challenge was to perform this migration with **minimum impact** on the Deployed Infrastructure of all environments. So **No re-creation of Resources, Updates in-place should not cause outage or distrub the development work**

This procedure can be very straight since Terragrunt is merely a terraform wrapper. But it can be challenging if we want a different target IaC Deployment structure.

![](https://miro.medium.com/v2/resize:fit:700/1*LQg0krnQta6xz4JuLenC3w.png)
The challenge was that the different applications/services werebroken into different components that were independently deployed. Example:

Terragrunt IaC structure

```
├── live  
│   ├── _env  
│   │   ├── lambda-resources.hcl  
│   │   ├── serverless-params.hcl  
│   │   ├── vpc-endpoints.hcl  
│   │   └── vpc.hcl  
│   ├── dev  
│   │   ├── account-service  
│   │   │   ├── lambda-resources  
│   │   │   │   └── terragrunt.hcl  
│   │   │   ├── serverless-params  
│   │   │   │   └── terragrunt.hcl  
│   │   │   ├── vpc  
│   │   │   │   └── terragrunt.hcl  
│   │   │   └── vpc-endpoints  
│   │   │       └── terragrunt.hcl  
│   │   ├── admin-service  
│   │   │   ├── lambda-resources  
│   │   │   │   └── terragrunt.hcl  
│   │   │   ├── serverless-params  
│   │   │   │   └── terragrunt.hcl  
│   │   │   ├── vpc  
│   │   │   │   └── terragrunt.hcl  
│   │   │   └── vpc-endpoints  
│   │   │       └── terragrunt.hcl  
│   │   └── database-service  
│   │       ├── rds-aurora  
│   │       │   └── terragrunt.hcl  
│   │       ├── serverless-params  
│   │       │   └── terragrunt.hcl  
│   │       ├── vpc  
│   │       │   └── terragrunt.hcl  
│   │       └── vpc-endpoints  
│   │           └── terragrunt.hcl  
│   ├── prod  
│   ├── qa
```

So this structure will produce a State file per component inside of each application/service.

The target deployment structure is 1 application/service at once. Example:

```
├── account-service  
│   ├── backend.tf  
│   ├── data.tf  
│   ├── env  
│   │   ├── dev.tfvars  
│   │   └── prod.tfvars  
│   ├── main.tf  
│   ├── outputs.tf  
│   ├── variables.tf  
│   └── versions.tf  
├── admin-service  
│   ├── backend.tf  
│   ├── data.tf  
│   ├── env  
│   │   ├── dev.tfvars  
│   │   └── prod.tfvars  
│   ├── main.tf  
│   ├── outputs.tf  
│   ├── variables.tf  
│   └── versions.tf  
└── database-service  
    ├── backend.tf  
    ├── data.tf  
    ├── env  
    │   ├── dev.tfvars  
    │   └── prod.tfvars  
    ├── main.tf  
    ├── outputs.tf  
    ├── variables.tf  
    └── versions.tf
```

### Migration Steps

1. Create a directory for the application/service (This can be in a mono-repo or live within the application source code under /infrastructure or any directory alike)
2. Add the backend.tf

```
terraform {  
  backend "s3" {  
    dynamodb_table = "terraform-lock-table"  
    bucket = "terraform-tfstate"  
    key = "account-service/terraform.tfstate"  
    region = "eu-west-1"  
  }  
}  
  
locals {  
  env                   = terraform.workspace  
  prefix                = "${local.env}-${var.service}"  
  region                = "eu-west-1"  
  azs                   = ["eu-west-1a", "eu-west-1b", "eu-west-1c"]  
  account_mapping = {  
    dev : 000000000000  
    qa : 000000000000  
    uat : 000000000000  
    prod : 000000000000  
  }  
}  
  
provider "aws" {  
  region = "eu-west-1"  
  
  default_tags {  
    tags = {  
      Environment = local.env  
      Service = var.service # set this depending on your needs like "account-service"  
      IaC_Component = "${local.env}/${var.service}"  
      ManagedBy = "terraform"  
    }  
  }  
  assume_role {  
    role_arn = "arn:aws:iam::${lookup(local.account_mapping, local.env, 000000000000)}:role/org-multiaccount-role"  
  }  
}
```

3. Add main.tf with all modules from the different components of Terragrunt

```
module "vpc" {  
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-vpc.git//"  
  name = "${var.service}-vpc"  
...  
  
module "s3_bucket" {  
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-s3-bucket.git//"  
...  
  
module "vpc_endpoints" {  
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-vpc.git//modules/vpc-endpoints/"  
...  

```

4. Replace dependencies with terraform data modules

Terragrunt

```
terraform {  
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-vpc.git//modules/vpc-endpoints/"  
}  
  
inputs = {  
  vpc_id = dependency.vpc.outputs.vpc_id  
...
```

Terraform

```
module "vpc_endpoints" {  
  source = "git::https://github.com/terraform-aws-modules/terraform-aws-vpc.git//modules/vpc-endpoints/"  
  vpc_id = module.vpc.vpc_id  
...
```

5. Create de necesary variables and outputs on variables.tf, outputs.tf and varsions.tf

### The problem with “terraform-aws-modules” and terraform state

The terraform state generated with modules form **terraform-aws-modules as shown on step 3** will look like this**:**

```
{  
      "mode": "managed",  
      "type": "aws_subnet",  
      "name": "public",  
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",  
      "instances": [  
       ...  
    },  
    {  
      "mode": "managed",  
      "type": "aws_vpc",  
      "name": "this",  
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",  
      "instances": [  
       ...  
    }
```

Needs to be updated to include the name of the module where we have now placed it, so for the vpc we created “module.vpc”. Example:

```
{  
      "module": "module.vpc",  
      "mode": "managed",  
      "type": "aws_subnet",  
      "name": "private",  
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",  
      "instances": [  
       ...  
{  
      "module": "module.vpc",  
      "mode": "managed",  
      "type": "aws_vpc",  
      "name": "this",  
      "provider": "provider[\"registry.terraform.io/hashicorp/aws\"]",  
      "instances": [
```

I have included a python script to do this automatically on this blogpost. This will fix the Issue.

### Merge the Terraform States of all components of the same application/service

Adding more components to the main.tf (lambda-resources, serverless-params and vpc-endpoints) requites the state files to be merged

1. Download current deployed terraform state files

```
aws s3 cp s3://bucket-tfstate/live/dev/account-service/vpc/terraform.tfstate ./dev-vpc.tfstate  
aws s3 cp s3://bucket-tfstate/live/dev/account-service/vpc-endpoints/terraform.tfstate ./dev-vpc-endpoints.tfstate  
aws s3 cp s3://bucket-tfstate/live/dev/account-service/serverless-params/terraform.tfstate ./dev-serverless-params.tfstate  
aws s3 cp s3://bucket-tfstate/live/dev/account-service/lambda-resources/terraform.tfstate ./dev-lambda-resources.tfstate
```

2. Use the following script to update the state to use a module (only required if the module was introduced to call another module)

```
python tfstatemodule.py dev-vpc.tfstate module.vpc  
python tfstatemodule.py dev-vpc-endpoints.tfstate module.vpc_endpoints  
python tfstatemodule.py dev-serverless-params.tfstate module.ssm_params  
python tfstatemodule.py dev-lambda-resources.tfstate module.lambda_resources
```

```
import json  
import sys  
  
def update_tf_state(json_file, module_string):  
    # Load data from the provided JSON file  
    with open(json_file, 'r') as state_file:  
        state_data = json.load(state_file)  
  
    # Update each item in the "resources" list  
    for resource in state_data['resources']:  
        resource['module'] = module_string  
  
    # Increment the 'serial' value by 1  
    state_data['serial'] += 1  
  
    # Write the updated data back to the JSON file  
    with open(json_file, 'w') as state_file:  
        json.dump(state_data, state_file, indent=2)  
  
if __name__ == "__main__":  
    if len(sys.argv) != 3:  
        print("Usage: python tfstatemodule.py input.json module_string")  
        sys.exit(1)  
  
    json_file = sys.argv[1]  
    module_string = sys.argv[2]  
  
    update_tf_state(json_file, module_string)  
    print(f"Update complete. Added 'module' field with value '{module_string}' to each resource."
```

#### Merge all terraform state files

Use the following script to append the resources of one state file to another

```
cp dev-vpc.tfstate dev.tfstate   
python tfstatemerge.py vpc-endpoints.tfstate dev.tfstate   
python tfstatemerge.py dev-serverless-params.tfstate dev.tfstate  
python tfstatemerge.py dev-lambda-resources.tfstate dev.tfstate
```

```
import json  
import sys  
  
  
def merge_tf_states(from_state_file, to_state_file):  
    # Load data from from-state.json  
    with open(from_state_file, 'r') as from_state:  
        from_data = json.load(from_state)  
  
    # Load data from to-state.json  
    with open(to_state_file, 'r') as to_state:  
        to_data = json.load(to_state)  
  
    # Append resources from from-state.json to to-state.json  
    to_data['resources'].extend(from_data['resources'])  
  
    # Increase the 'serial' value by 1 in to-state.json  
    to_data['serial'] += 1  
  
    # Write the updated data back to to-state.json  
    with open(to_state_file, 'w') as to_state:  
        json.dump(to_data, to_state, indent=2)  
  
  
if __name__ == "__main__":  
    if len(sys.argv) != 3:  
        print("Usage: python tfstatemerge.py from-state.json to-state.json")  
        sys.exit(1)  
  
    from_state_file = sys.argv[1]  
    to_state_file = sys.argv[2]  
  
    merge_tf_states(from_state_file, to_state_file)  
    print("Merge complete.")
```

#### The Single merged state file is ready… now we can use terraform workspaces to push the new state

```
terraform init  
terraform workspace new sandbox  
terraform state push dev.tfstate  
```

Now we can use terraform as usual

```
terraform plan  
terraform apply
```

Repeat this procedure for each environment to migrate

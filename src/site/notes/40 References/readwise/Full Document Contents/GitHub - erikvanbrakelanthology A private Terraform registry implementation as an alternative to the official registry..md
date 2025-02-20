---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/git-hub-erikvanbrakelanthology-a-private-terraform-registry-implementation-as-an-alternative-to-the-official-registry/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/642117082e3620574fee4dbf4b0d410dabef91eb8b56b45969fefca2457284db/erikvanbrakel/anthology)

### erikvanbrakel/anthology

[![Gitter chat](https://camo.githubusercontent.com/b6b57aa5448902d56e433de6c6f83b3fb4df3c97b474b36595f88e0904599ab4/68747470733a2f2f6261646765732e6769747465722e696d2f616e74686f6c6f67792d72656769737472792f636f6d6d756e6974792e706e67)](https://gitter.im/anthology-registry/community)
### Anthology, a private Terraform Registry

#### Description

Anthology is a reimplementation of the Terraform Registry API, intended to be used when your modules can't, shouldn't or don't need to be public. For all means and purposes it works in the same way as the [public registry](https://registry.terraform.io/).

#### How to use

##### Using Docker

Every release is automatically published to the [Docker Hub](https://hub.docker.com/r/erikvanbrakel/anthology/). You can set commandline parameters by overriding the command.

**running on port `80`, using `my-module-bucket` for storage:**

`docker run -p 80:80 erikvanbrakel/anthology --port=80 --backend=s3 --s3.bucket=my-module-bucket`

**using docker-compose**

```
version: '2.1'

services:

  registry:
    command: --port=80 --backend=s3 --s3.bucket=my-module-bucket
    build: erikvanbrakel/anthology:latest
    ports:
      - 80:80
```

##### AWS + terraform

The easiest way to deploy is to use the [anthology module](https://registry.terraform.io/modules/erikvanbrakel/anthology/aws/) in the [public registry](https://registry.terraform.io/).

```
module "anthology" {
  source  = "erikvanbrakel/anthology/aws"
  version = "0.0.2"

  storage_bucket = "this-bucket-stores-my-modules"
  tld            = "example.com"                   # the registry will be hosted at registry.example.com
}

```

**WARNING WARNING WARNING**

This module provisions several resources, among which compute and storage components. This is not free, so make sure you are aware of the cost before provisioning!

#### Command line parameters

##### Common parameters

| Parameter | Description | Allowed | Default |
| --- | --- | --- | --- |
| --port | Port to listen on | 1-65535 | 1234 |
| --backend | Backend to use. | [memory, filesystem, s3] |  |
| --ssl.certificate | Path to the server certificate | Any valid path |  |
| --ssl.key | Path to the server certificate | Any valid path |  |

##### Filesystem backend

| Parameter | Description | Allowed | Default |
| --- | --- | --- | --- |
| --filesystem.basepath | Base path for module storage | Any valid path |  |

##### S3 backend

| Parameter | Description | Allowed | Default |
| --- | --- | --- | --- |
| --s3.bucket | Name of the S3 bucket for storage | Any valid s3 bucket name |  |
| --s3.endpoint | Alternative S3 endpoint | http[s]://[hostname]:[port] |  |

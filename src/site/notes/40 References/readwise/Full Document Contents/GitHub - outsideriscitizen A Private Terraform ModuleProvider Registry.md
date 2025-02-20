---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/git-hub-outsideriscitizen-a-private-terraform-module-provider-registry/","tags":["rw/articles"]}
---

![rw-book-cover](https://opengraph.githubassets.com/5ed33fb82dea8144044e63272d66444665c3c397dd8d692d36a5f5df271b3213/outsideris/citizen)

### outsideris/citizen

### Citizen

[![Unit Test Status](https://github.com/outsideris/citizen/workflows/Unit%20tests/badge.svg)](https://github.com/outsideris/citizen/actions?query=workflow%3A%22Unit+tests%22+branch%3Amain)
[![Integration Test Status](https://github.com/outsideris/citizen/workflows/Integration%20Tests/badge.svg)](https://github.com/outsideris/citizen/actions?query=workflow%3A%22Integration+Tests%22+branch%3Amain)
[![FOSSA Status](https://camo.githubusercontent.com/731fcd06ef193fc0ab058b90ffb22319b2f29f0a74d82b9436aecdf1aefc4a12/68747470733a2f2f6170702e666f7373612e696f2f6170692f70726f6a656374732f6769742532426769746875622e636f6d2532466f757473696465726973253246636974697a656e2e7376673f747970653d736869656c64)](https://app.fossa.io/projects/git%2Bgithub.com%2Foutsideris%2Fcitizen?ref=badge_shield)
A Private [Terraform Module](https://registry.terraform.io/) and [Terraform Provider](https://www.terraform.io/docs/internals/provider-registry-protocol.html) registry.

#### Requirements

* HTTPS - Terraform module registry only support HTTPS.

#### Download

[Download the latest release!](https://github.com/outsideris/citizen/releases/latest)

Also, you can use to launch the registry server. The docker image is in [GitHub Container Registry](https://github.com/users/outsideris/packages/container/package/citizen) .

```
$ docker run -d -p "3000:3000" ghcr.io/outsideris/citizen:latest
```

#### Server Usage

##### `citizen server`

To launch the registry server

```
$ ./citizen server
```

It will be launched at <http://localhost:3000>. You can check it at <http://localhost:3000/health>.

Because [Terraform CLI](https://www.terraform.io/) works with only HTTPS server, you should set up HTTPS in front of the registry server.

If you want to test it at local, you need a tool which provides HTTPS like [ngrok](https://ngrok.com/).

Environment variables:

* `CITIZEN_DATABASE_TYPE`: Backend provider for registry metadata. Set to `mysql`, `mongodb` or `sqlite`.
* `CITIZEN_DATABASE_URL`: The URL of the database. `protocol//username:password@hosts:port/database?options`
* `CITIZEN_STORAGE`: Storage type to store module files. You can use `file`, `s3` or `gcs` type.

	+ `s3` is for [AWS S3](https://aws.amazon.com/ko/s3/).
	+ `gcs` is for [Google Cloud Storage](https://cloud.google.com/storage).
* `CITIZEN_STORAGE_PATH`: A directory to save module files only if `CITIZEN_STORAGE` is `file` (absolute/relative path can be used).
* `CITIZEN_STORAGE_BUCKET`: A S3 bucket to save module files only if `CITIZEN_STORAGE` is `s3` or `gcs`.(And AWS credentials required.)

If you want to use GCS as a storage, you need to [authenticate to Google Cloud services](https://cloud.google.com/docs/authentication/client-libraries).

##### Database migration

To migrate the database, you can use `citizen generate-migration` command. The command will generate migration files which are `schema.prisma` and `migrations/` directory. Because we use [prisma](https://www.prisma.io/) to handle databases, you need to [install prisma CLI](https://www.prisma.io/docs/concepts/components/prisma-cli/installation).

Then, Set `CITIZEN_DATABASE_TYPE` and `CITIZEN_DATABASE_URL` envorinment variables and Run [`prisma migrate deploy`](https://www.prisma.io/docs/reference/api-reference/command-reference#migrate-deploy) for Sqlite. For MongoDB, migration is not required.

#### Client Usage

##### `citizen module <namespace> <name> <provider> <version>`

Since [official Terraform Module Registry](https://registry.terraform.io/) is integrated with GitHub, users can publish terraform modules if they just push it on GitHub.

Citizen provides a special command to publish a module onto citizen registry server instead integrating GitHub.

In a module directory, you can publish your terraform module via a command below:

```
$ ./citizen module <namespace> <name> <provider> <version>
```

You should set `CITIZEN_ADDR` as citizen registry server address which you will publish your modules to. e.g. `<https://registry.example.com>`.

##### Examples

If you have ALB module in `./alb` directory, and your registry server is launched at `<https://registry.example.com>`, you run below command in `./alb` directory to publish ALB module.

```
$ CITIZEN_ADDR=https://registry.example.com \
  citizen module dev-team alb aws 0.1.0
```

Then, you can define it in your terraform file like this:

```
module "alb" {
  source = "registry.example.com/dev-team/alb/aws"
  version = "0.1.0"
}
```

##### `citizen provider <namespace> <type> <version> [protocols]`

Citizen provides a special command to publish providers onto citizen.

* `-g, --gpg-key <gpgkey>`: GPG key to sign your SHA256SUMS.

	+ You need to publish your provider with your GPG public key to terraform registry. Otherwise, terraform will refuse to install providers. Terraform official resistry manage partners' public keys, but, each provider version has own public key and signature in citizen registry.

You must first [build and package](https://www.terraform.io/docs/registry/providers/publishing.html), citizen expects following files in the provider location:

* `<namespace>-<type>_<version>_<os>_<arch>.zip` (one per os/arch combination)

Where `<namespace>` and `<type>` is a name of the provider and `<version>` is a provider version in the `MAJOR.MINOR.PATCH` version format.

Citizen will generate a SHA256SUMS file and a GPG signature file automatically for you: Following files will be generated in your directory during publising provider. So, You don’t need prepare theses files.

* `<namespace>-<type>_<version>_SHA256SUMS`
* `<namespace>-<type>_<version>_SHA256SUMS.sig`

Therefore, `shasum` and `gpg` commands should be available in your machine.

In a provider directory, you can publish your terraform provider via a command below:

```
$ ./citizen provider <namespace> <type> <version> [protocols]
```

`[protocols]` is comma separated Terraform provider API versions, with `MAJOR.MINOR`.

You should set `CITIZEN_ADDR` as citizen registry server address which you will publish your modules to. e.g. `<https://registry.example.com>`.

##### Examples

If you have ALB provider in `./utilities` directory, and your registry server is launched at `<https://registry.example.com>`, you run below command in `./utilities` directory to publish utilities provider.

```
$ CITIZEN_ADDR=https://registry.example.com \
  citizen provider dev-team utilities 0.1.0 4.1,5.0
```

Then, you can define it in your terraform file like this:

```
provider "utilities" {
}

terraform {
  required_providers {
    utilities = {
      source = "registry.example.com/dev-team/utilities"
      version = "0.1.0"
    }
  }
}
```

#### Development

Node.js 16+ required

Set environment variables, see above.

```
$ ./bin/citizen server
$ ./bin/citizen module
$ ./bin/citizen provider
```

##### Test

Set at least a storage path and the s3 bucket name variables for the tests to succeed. You need to be able to access the bucket, so you probably want to have an active aws or aws-vault profile.

Run mongodb as replica set first like:

```
$ docker-compose -f test/docker-compose-mongodb-cluster.yaml up
```

Run MySQL with docker

```
docker run --rm -p 3306:3306 --name mysql-citizen -e MYSQL_ROOT_PASSWORD=citizen -e MYSQL_DATABASE=citizen mysql
```

Run the tests:

```
$ npm test
```

Run the tests with the environment variables prefixed:

```
$ CITIZEN_STORAGE_PATH=storage CITIZEN_STORAGE_BUCKET=terraform-registry-modules npm test
```

##### Build distributions

```
$ npm run client
$ npm run build
```

It will generate prisma clients for databases.

Under `dist/`, citizen binaries for linux, darwin(amd64/arm64) and windows made.

#### License

[![FOSSA Status](https://camo.githubusercontent.com/d35bc7268e3d684fe96fb607a13b02867fd43511c082bedd92ea4cae72d51828/68747470733a2f2f6170702e666f7373612e696f2f6170692f70726f6a656374732f6769742532426769746875622e636f6d2532466f757473696465726973253246636974697a656e2e7376673f747970653d6c61726765)](https://app.fossa.io/projects/git%2Bgithub.com%2Foutsideris%2Fcitizen?ref=badge_large)

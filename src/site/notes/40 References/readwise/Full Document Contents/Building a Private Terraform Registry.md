---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/building-a-private-terraform-registry/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article2.74d541386bbf.png)

Recently, I wanted to find a way to use a custom provider in Terraform without storing in in Terraform’s official registry. I was baffled when I found out that, yes, there are ways to load custom providers in Terraform from a local file system, no way exists of distributing it that doesn’t rely on storing the provider in [registry.terraform.io](https://registry.terraform.io/).

I searched online and found two open-source registries: [citizen](https://github.com/outsideris/citizen) and [anthology](https://github.com/erikvanbrakel/anthology). None of these are usable for me because both can only serve Terraform modules and I want to serve Terraform custom providers. It seems that using private Terraform registries seems to be more common for distributing modules rather than custom providers.

Fortunately, Terraform *does* provide a specification of the protocol that we can use for distributing custom providers that Terraform can then use. With the help of [an awesome colleague](https://www.linkedin.com/in/nunoadrego/) to understand how it works I ended up implementing my own private Terraform Registry, with Python and Flask ([rekisteri](https://github.com/caramelomartins/rekisteri)).

In this article, we’ll go through Terraform’s Provider Registry Protocol and will understand how you too can build a private Terraform Registry. You’ll learn more about Terraform, Flask and Python.

#### Background

Terraform is an incredible tool to manage infrastructure. It is backed by a strong community and it has a public registry at [registry.terraform.io](https://registry.terraform.io/), where we can find tooling to fullfil almost every single need from AWS to Kubernetes, to lesser known platforms. Terraform’s registry has some very high profile providers, which is what enables Terraform to interact with such a diverse set of platforms. It also has a big collection of modules, which allows Terraform users to share and organize configuration in Terraform.

Terraform is built on a plugin architecture, which means that it allows, and encourages, developers to build their own plugins to interact with Terraform. [Provider Plugins](https://www.terraform.io/docs/plugins/provider.html), for example, allow developers to build their own custom providers to interact with their internal infrastructure or in-house tools. It is perfectly understandable that we might want to develop a custom provider to interact with in-house tooling for infrastructure - in fact, I’ve actually built two already.

Unfortunately, Terraform doesn’t provide a way to distribute these custom providers in a private way. I find this shameful because you don’t always want to open-source your custom provider, for a myriad of reasons, from business reasons to security reasons. You can have a private module registry by using Terraform Cloud but Hashicorp doesn’t provide a private registry for providers, as far as I know. From Hashicorp:

>  The Terraform open source project does not provide a server implementation, but we welcome community members to create their own private registries by following the published protocol.
> 
>  

Fortunately, Terraform *does* provide information about the protocol they use for their public registry in [Provider Registry Protocol](https://www.terraform.io/docs/internals/provider-registry-protocol.html). This means that they provide all the necessary information that allows developers to build a private Terraform registry with which Terraform can interact. Although it has very little information, it serves as an interesting baseline to implement an open-source private Terraform Registry that can be used to serve custom plugins, or simply forks of existing plugins with modifications.

#### Terraform’s Provider Registry Protocol

*Note: All of this was written considering Terraform 0.13 or higher.*

Terraform’s Provider Registry Protocol starts with service discovery, which happens through a particular endpoint. When loading up a given provider, Terraform will contact the provider’s hostname and request for the implementations of any of its protocols with `GET <hostname>/.well-known/terraform.json`. This endpoint should return a JSON response with information about where the APIs can be found. This means we can have a registry that serves both modules and providers, or it can serve only one of those.

An example from Terraform:

```
{
  "providers.v1": "/terraform/providers/v1/"
}

```

Terraform’s Provider Registry Protocol also establishes two further operations: [*List Available Versions*](https://www.terraform.io/docs/internals/provider-registry-protocol.html#list-available-versions) and [*Find a Provider Package*](https://www.terraform.io/docs/internals/provider-registry-protocol.html#find-a-provider-package).

*List Available Versions* allows Terraform to query for existing versions of a given provider based on a `namespace` and a `name` with `GET <hostname>/<namespace>/<name>/versions`. *Find a Provider Package* allows Terraform to get information about where to download a particular package of a provider based on the platform (OS and architecture) with `GET <hostname>/<namespace>/<name>/<version>/download/<os>/<arch>`.

No further information can be found from Terraform’s documentation but this is a great starting point for creating a read-only private Terraform Registry. In fairness, all that’s necessary for someone implementing the protocol is to known how Terraform interacts with the registry. All of the remaining bits of what a functional registry should do (e.g. have a way to store and manipulate metadata) can be left to the discretion of who implements it.

#### Implementation with Python and Flask

Let’s get on with the juicy bits. I built this with Python and Flask, reading metadata from a local file system, to be as quick to implement as possible, while still being (somehow) useful. So let’s start with creating a simple Flask app in a `main.py`. Inside that file, let’s add some useful Flask imports and start the application:

```
# Imports to deal with JSON, error status codes and loading files.
import json
from flask import Flask, abort
from os import path

# Starting the application.
app = Flask(__name__)

```

##### Service Discovery

To fulfill the service discovery capabilities of the protocol, we’ll add a simple route that returns the allowed protocols and where they can be found:

```
@app.route('/.well-known/terraform.json', methods=['GET'])
def discovery():
    return {"providers.v1": "/v1/providers/"}

```

Since we only want to implement the Provider’s Registry Protocol, we’ll only serve `providers.v1`, as explained in the documentation.

We now want to create a basic metadata file that has all the necessary information that we need to serve this information to Terraform. We’ll use Hashicorp’s `random` provider for this example:

```
{
    "versions": [
        {
            "version": "0.1.0",
            "protocols": [
                "4.0",
                "5.1"
            ],
            "platforms": [
                {
                    "os": "linux",
                    "arch": "amd64",
                    "filename": "terraform-provider-random_2.0.0_linux_amd64.zip",
                    "download_url": "https://releases.hashicorp.com/terraform-provider-random/2.0.0/terraform-provider-random_2.0.0_linux_amd64.zip",
                    "shasums_url": "https://releases.hashicorp.com/terraform-provider-random/2.0.0/terraform-provider-random_2.0.0_SHA256SUMS",
                    "shasums_signature_url": "https://releases.hashicorp.com/terraform-provider-random/2.0.0/terraform-provider-random_2.0.0_SHA256SUMS.sig",
                    "shasum": "5f9c7aa76b7c34d722fc9123208e26b22d60440cb47150dd04733b9b94f4541a",
                    "signing_keys": {
                        "gpg_public_keys": [
                            {
                                "key_id": "51852D87348FFC4C",
                                "ascii_armor": "-----BEGIN PGP PUBLIC KEY BLOCK-----\nVersion: GnuPG v1\n\nmQENBFMORM0BCADBRyKO1MhCirazOSVwcfTr1xUxjPvfxD3hjUwHtjsOy/bT6p9f\nW2mRPfwnq2JB5As+paL3UGDsSRDnK9KAxQb0NNF4+eVhr/EJ18s3wwXXDMjpIifq\nfIm2WyH3G+aRLTLPIpscUNKDyxFOUbsmgXAmJ46Re1fn8uKxKRHbfa39aeuEYWFA\n3drdL1WoUngvED7f+RnKBK2G6ZEpO+LDovQk19xGjiMTtPJrjMjZJ3QXqPvx5wca\nKSZLr4lMTuoTI/ZXyZy5bD4tShiZz6KcyX27cD70q2iRcEZ0poLKHyEIDAi3TM5k\nSwbbWBFd5RNPOR0qzrb/0p9ksKK48IIfH2FvABEBAAG0K0hhc2hpQ29ycCBTZWN1\ncml0eSA8c2VjdXJpdHlAaGFzaGljb3JwLmNvbT6JATgEEwECACIFAlMORM0CGwMG\nCwkIBwMCBhUIAgkKCwQWAgMBAh4BAheAAAoJEFGFLYc0j/xMyWIIAIPhcVqiQ59n\nJc07gjUX0SWBJAxEG1lKxfzS4Xp+57h2xxTpdotGQ1fZwsihaIqow337YHQI3q0i\nSqV534Ms+j/tU7X8sq11xFJIeEVG8PASRCwmryUwghFKPlHETQ8jJ+Y8+1asRydi\npsP3B/5Mjhqv/uOK+Vy3zAyIpyDOMtIpOVfjSpCplVRdtSTFWBu9Em7j5I2HMn1w\nsJZnJgXKpybpibGiiTtmnFLOwibmprSu04rsnP4ncdC2XRD4wIjoyA+4PKgX3sCO\nklEzKryWYBmLkJOMDdo52LttP3279s7XrkLEE7ia0fXa2c12EQ0f0DQ1tGUvyVEW\nWmJVccm5bq25AQ0EUw5EzQEIANaPUY04/g7AmYkOMjaCZ6iTp9hB5Rsj/4ee/ln9\nwArzRO9+3eejLWh53FoN1rO+su7tiXJA5YAzVy6tuolrqjM8DBztPxdLBbEi4V+j\n2tK0dATdBQBHEh3OJApO2UBtcjaZBT31zrG9K55D+CrcgIVEHAKY8Cb4kLBkb5wM\nskn+DrASKU0BNIV1qRsxfiUdQHZfSqtp004nrql1lbFMLFEuiY8FZrkkQ9qduixo\nmTT6f34/oiY+Jam3zCK7RDN/OjuWheIPGj/Qbx9JuNiwgX6yRj7OE1tjUx6d8g9y\n0H1fmLJbb3WZZbuuGFnK6qrE3bGeY8+AWaJAZ37wpWh1p0cAEQEAAYkBHwQYAQIA\nCQUCUw5EzQIbDAAKCRBRhS2HNI/8TJntCAClU7TOO/X053eKF1jqNW4A1qpxctVc\nz8eTcY8Om5O4f6a/rfxfNFKn9Qyja/OG1xWNobETy7MiMXYjaa8uUx5iFy6kMVaP\n0BXJ59NLZjMARGw6lVTYDTIvzqqqwLxgliSDfSnqUhubGwvykANPO+93BBx89MRG\nunNoYGXtPlhNFrAsB1VR8+EyKLv2HQtGCPSFBhrjuzH3gxGibNDDdFQLxxuJWepJ\nEK1UbTS4ms0NgZ2Uknqn1WRU1Ki7rE4sTy68iZtWpKQXZEJa0IGnuI2sSINGcXCJ\noEIgXTMyCILo34Fa/C6VCm2WBgz9zZO8/rHIiQm1J5zqz0DrDwKBUM9C\n=LYpS\n-----END PGP PUBLIC KEY BLOCK-----",
                                "trust_signature": "",
                                "source": "HashiCorp",
                                "source_url": "https://www.hashicorp.com/security.html"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}

```

This metadata structure follows Hashicorp’s metadata requirements. It has a `versions` list as the root object for the metadata. Each version needs to have a `version`, a list of accepted `protocols` and a list of `platforms` that will contain all the necessary metadata to download a specific provider’s version. For each platform, we need to specify: `os`, `arch`, `filename`, `download_url`, `shasums_url` and `shasums_signature_url`, and `signing_keys`. All of these are extensively documented in Terraform’s Provider Registry Protocol.

By executing a `GET` with each URL, we can see examples of what each URL needs to offer in order for Terraform to work properly. Notice that none of these URLs need to be served by the registry itself. They only need to be available to receive requests from when you run `terraform init`.

We store the above metadata file in a directory named `providers`, at the same level as `main.py`. Each namespace has it own sub-directory and the filename, that stores the metadata, must be the same as the name of the provider to which the metadata belongs to. As an example, again with `random`:

```
$ tree
.
├── main.py
├── providers
│   └── hashicorp
│       └── random.json

```

##### Listing Versions

To list versions of the packages we’ll add another route with the appropriate path.

```
@app.route('/v1/providers/<namespace>/<name>/versions', methods=['GET'])
def versions(namespace, name):
    filepath = 'providers/' + namespace + "/" + name + ".json"

    if not path.exists(filepath):
        abort(404)

    with open(filepath) as reader:
        data = json.load(reader)

    response = { "versions" : [] }

    for elem in data["versions"]:
        version = {"version": elem["version"], "protocols": elem["protocols"], "platforms": []}

        for platform in elem["platforms"]:
            version["platforms"].append({"os": platform["os"], "arch": platform["arch"]})

        response["versions"].append(version)
    
    return response

```

Here what we do is quite simple and inefficient. We validate the appropriate metadata file exists and we return a 404 if it doesn’t exist. If the file exists, we load it and then iterate through the data to build our response. Since the metadata file isn’t exactly the same as the response needed by Terraform, we need to build a response that is made of *only* the elements necessary - in this case *only* `os` and `arch` appear in `platforms`.

##### Find a Package

To find a package is very simple too.

```
@app.route('/v1/providers/<namespace>/<name>/<version>/download/<os>/<arch>', methods=['GET'])
def package(namespace, name, version, os, arch):
    filepath = 'providers/' + namespace + "/" + name + ".json"

    if not path.exists(filepath):
        abort(404)

    with open(filepath) as reader:
        data = json.load(reader)

    provider = None

    for elem in data["versions"]:
        if elem["version"] == version:
            for platform in elem["platforms"]:
                if platform["os"] == os and platform["arch"]:
                    provider = platform
                    provider["protocols"] = elem["protocols"]

    if provider is None:
        abort(404)

    return provider

```

We find the metadata file, as before, and return 404 if the file doesn’t exist. After ensuring that the file exists, we load it up and try to find the metadata for the specific version, OS and architecture. If the appropriate match can be found, we return the information from the metadata file plus the `protocols` properties which is also required in this response. If we can’t find an appropriate combination for version, OS and architecture, we return a 404.

#### Testing

For testing, we create a simple `main.tf` with the following contents:

```
terraform {
  required_version = "~> 0.13"
  required_providers {
    random = {
      source  = "9af044367099.ngrok.io/hashicorp/random"
      version = "~> 0.1"
    }
  }
}

```

`9af044367099.ngrok.io` refers to an `ngrok` endpoint that I created to test this out. `terraform init` requires that registries are served via HTTPS, which means that a simple development server won’t function properly for testing. I used `ngrok` to proxy requests to Flask’s development server but you can do whatever works for you. Below instructions will assume that there’s some kind of proxy to Flask.

Let’s fire up Flask’s server:

```
$ FLASK_ENV=development FLASK_APP=main.py flask run
 * Serving Flask app "main.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 199-311-940

```

Now run Terraform:

```
$ terraform init

Initializing the backend...

Initializing provider plugins...
- Finding 9af044367099.ngrok.io/hashicorp/random versions matching "~> 0.1"...
- Installing 9af044367099.ngrok.io/hashicorp/random v0.1.0...
- Installed 9af044367099.ngrok.io/hashicorp/random v0.1.0 (signed by HashiCorp)

(...)

```

In the above case, I have `https://9af044367099.ngrok.io/` redirecting all requests to `localhost:5000` which is why all requests are served properly, even though `terraform init` is sending HTTPS requests.

#### Conclusion

This is it. We’ve built a private registry that we can use with Terraform to serve custom Terraform providers that are stored somewhere outside Terraform’s official registry. Obviously, this has *very* limited functionality. It can’t even create new versions of providers or new providers dynamically but you can always simply add or update files and those will be served by this API. There are some interesting challenges for future implementations or improvements:

* Serving this with an HTTPS server instead of relying on `ngrok`.
* Implementing a way to manipulate metadata to create new providers and versions. This would mean having more endpoints for `POST` and `PUT` verbs.
* Implement more backends for metadata such as PostgreSQL, SQLite and S3.

If you are interested, you can see all of this implemented in [rekisteri@b0753040](https://github.com/caramelomartins/rekisteri/tree/b07530407b94c4e6e61fb77d1a1572952fe8ee2a). Alternatively, you can try to build your own and share the adventure! I will aim at introducing at least the above improvements in [rekisteri](https://github.com/caramelomartins/rekisteri/tree/b07530407b94c4e6e61fb77d1a1572952fe8ee2a) in order to make it more useful.

---
{"dg-publish":true,"dg-path":"Slipbox Notes/Azure Container Registry.md","permalink":"/slipbox-notes/azure-container-registry/","tags":["notes"],"created":"2023-03-24","updated":"2025-11-27"}
---


## Push Containers to ACR

Utilizing [[Docker\|Docker]] login you Tag the Container on your local machine that you wish to push to ACR.  
This tag represents the path URL that will be used in future to pull it.

Reference: [Push & pull container image - Azure Container Registry | Microsoft Learn](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-get-started-docker-cli?tabs=azure-cli)

### User Interactive Method

```bash
docker login myregistry.azurecr.io
docker tag mcr.microsoft.com/oss/nginx/nginx:1.15.5-alpine myregistry.azurecr.io/samples/nginx
docker push myregistry.azurecr.io/samples/nginx
```

### Service Principal Method

```bash
docker login myregistry.azurecr.io --username $SP_APP_ID --password $SP_PASSWD
docker tag mcr.microsoft.com/oss/nginx/nginx:1.15.5-alpine myregistry.azurecr.io/samples/nginx
docker push myregistry.azurecr.io/samples/nginx
```

### [[90_slipbox/AzCLI\|AzCLI]] Method

- If you pass the `.azurecr.io` on the login, it will automatically strip it
- Requires BuiltIn admin account to be enabled.

```bash
az acr login --name myregistry
docker tag mcr.microsoft.com/oss/nginx/nginx:1.15.5-alpine myregistry.azurecr.io/samples/nginx
docker push myregistry.azurecr.io/samples/nginx
```

### Hacky [[90_slipbox/Terraform\|Terraform]] Null Provider way

Don't do this, there are much nicer ways nowadays, things like Terraform Actions or even just CD pipelines

```Go
locals {
  images = [{
    image_name = "dotnetapi-headless"
    dockerfile = "dotnetapi-headless.dockerfile"
  }]
}
data "local_file" "file" {
  for_each = {for o in local.images : o.image_name => o}
  filename = "${path.module}/dockerfiles/${each.value.dockerfile}"
}

resource "null_resource" "docker_build_push" {
  for_each = {for o in local.images : o.image_name => o}
  triggers = {
    value = data.local_file.file[each.value.image_name].content
  }

  provisioner "local-exec" {
    command = <<-EOT
        set -e
        az acr login -n ${module.core.acr_fqdn}
        docker build - < ${data.local_file.file[each.value.image_name].filename} -t ${module.core.acr_fqdn}/${each.value.image_name}:latest
        docker push ${module.core.acr_fqdn}/${each.value.image_name}:latest
      EOT
  }

  depends_on = [
    data.local_file.file
  ]
}
```

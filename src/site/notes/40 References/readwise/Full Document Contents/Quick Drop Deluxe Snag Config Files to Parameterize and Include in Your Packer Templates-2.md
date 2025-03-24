---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/quick-drop-deluxe-snag-config-files-to-parameterize-and-include-in-your-packer-templates-2/","tags":["rw/articles"]}
---

![rw-book-cover](https://miro.medium.com/v2/da:true/resize:fit:1200/0*4KjyCMMNUDW218y9)

I was recently setting up Minecraft Dedicated Server Java Edition. Most of my work with Minecraft has been with Bedrock edition which has a similar setup. Both have a `server.properties` file but the Java Edition has some different settings that I needed to configure.

I wanted to build these settings into my Packer template so that I can bake an image that allows me to easily swap in new values at runtime. It’s not a super great experience trying to copy and paste from `vi` while in an active SSH connection. Therefore, sometimes its handy to drop a file into the Azure Storage account for easier access.

Azure provides a pretty handy feature that allows you to [execute a script](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/run-command) on the server. This can be done via the Azure Portal so it’s more of a sneakernet type operation.

The below is my first attempt:

```
az login  
  
if [ ! -f "/home/mcserver/minecraft_java/server.properties" ]; then  
    echo "File '/home/mcserver/minecraft_java/server.properties' does not exist."  
    exit 1  
fi  
  
az storage blob upload \  
  --account-name stmc54251059 \  
  --container-name drop \  
  --name server.properties \  
  --file /home/mcserver/minecraft_java/server.properties \  
  --auth-mode login \  
  --overwrite
```

I setup a managed identity on the Virtual Machine which allows the machine to impersonate the identity but you still need to perform an `az login` in order to initialize the Azure CLI to…

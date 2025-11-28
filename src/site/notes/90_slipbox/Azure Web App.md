---
{"dg-publish":true,"permalink":"/90-slipbox/azure-web-app/","tags":["notes"]}
---


## Configure Azure Web App to Use Private Endpoint

To use Azure Private Endpoint on a Web app, you need to enable VNET Integration, and configure the DNS servers.  
If you do not configure the DNS, it will use the default path, and not route this through the VNET, and therefore will not get the correct Azure Private DNS Zone

Required App Settings:

- `WEBSITE_CONTENTOVERVNET` is set to `1`
- `WEBSITE_DNS_SERVER` is set to [[90_slipbox/Azure Magic IP\|168.63.129.16]]

### AzureRM Provider Example

```go
resource "azurerm_linux_web_app" "webApp" {

# ...
# Only showing config required

  virtual_network_subnet_id = module.network.subnets_map.front.id 
  site_config {
    vnet_route_all_enabled = true 
    }

  app_settings = {
    WEBSITE_CONTENTOVERVNET = 1 
    WEBSITE_DNS_SERVER      = "168.63.129.16" 
	}
  }
}
```

> [!warning]  
> Do not use the `azurerm_app_service_virtual_network_swift_connection` resource to connect to the VNET as well as the `virtual_network_subnet_id` parameter.  
> It will create a loop every time you deploy and constantly break.

### Troubleshooting

Using `NSLookup` on the console will be the most revealing, as it will show you if you are resolving the Public or Private IP for the service.

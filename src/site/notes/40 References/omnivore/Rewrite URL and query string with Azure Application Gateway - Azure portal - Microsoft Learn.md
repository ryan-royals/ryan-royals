---
{"dg-publish":true,"permalink":"/40-references/omnivore/rewrite-url-and-query-string-with-azure-application-gateway-azure-portal-microsoft-learn/","tags":["omnivore"]}
---


- Article

This article describes how to use the Azure portal to configure an [Application Gateway v2 SKU](https://learn.microsoft.com/en-gb/azure/application-gateway/application-gateway-autoscaling-zone-redundant) instance to rewrite URL.

 Note

URL rewrite feature is available only for Standard\_v2 and WAF\_v2 SKU of Application Gateway. When URL rewrite is configured on a WAF enabled gateway, WAF evaluation will take place on the rewritten request headers and URL. [Learn more](https://learn.microsoft.com/en-gb/azure/application-gateway/rewrite-http-headers-url#using-url-rewrite-or-host-header-rewrite-with-web-application-firewall-waf%5Fv2-sku).

If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/free/?WT.mc%5Fid=A261C142F) before you begin.

## Before You Begin

You need to have an Application Gateway v2 SKU instance to complete the steps in this article. Rewriting URL isn't supported in the v1 SKU. If you don't have the v2 SKU, create an [Application Gateway v2 SKU](https://learn.microsoft.com/en-gb/azure/application-gateway/tutorial-autoscale-ps) instance before you begin.

## Sign in to Azure

Sign in to the [Azure portal](https://portal.azure.com/) with your Azure account.

## Configure URL Rewrite

In the below example whenever the request URL contains */article*, the URL path and URL query string are rewritten

`contoso.com/article/123/fabrikam` \-> `contoso.com/article.aspx?id=123&title=fabrikam`

1. Select **All resources**, and then select your application gateway.
2. Select **Rewrites** in the left pane.
3. Select **Rewrite set**:  
![Add rewrite set](https://proxy-prod.omnivore-image-cache.app/0x0,s97b2oB9FiWt0I6ZmC5UpfGoIR2yw7MBBzoOrBvMq15I/https://learn.microsoft.com/en-gb/azure/application-gateway/media/rewrite-url-portal/rewrite-url-portal-1.png)
4. Provide a name for the rewrite set and associate it with a routing rule:  
a. Enter the name for the rewrite set in the **Name** box.  
b. Select one or more of the rules listed in the **Associated routing rules** list. This is used to associate the rewrite configuration to the source listener via the routing rule. You can select only those routing rules that haven't been associated with other rewrite sets. The rules that have already been associated with other rewrite sets are greyed out.  
c. Select **Next**.  
![Associate to a rule](https://proxy-prod.omnivore-image-cache.app/0x0,sP6P6r2ajJ6LhETffDyp7jDlY_tScdaI5jHqwxUWagfg/https://learn.microsoft.com/en-gb/azure/application-gateway/media/rewrite-url-portal/rewrite-url-portal-2.png)
5. Create a rewrite rule:  
a. Select **Add rewrite rule**.  
![Screenshot that highlights Add rewrite rule.](https://proxy-prod.omnivore-image-cache.app/0x0,sNVBdhhB_cphq_FIMzLE-ePi-uZ5KwBHgOYfJ5zbravY/https://learn.microsoft.com/en-gb/azure/application-gateway/media/rewrite-url-portal/rewrite-url-portal-3.png)  
b. Enter a name for the rewrite rule in the **Rewrite rule name** box. Enter a number in the **Rule sequence** box.
6. In this example, we'll rewrite URL path and URL query string only when path contains */article*. To do this, add a condition to evaluate whether the URL path contains */article*  
a. Select **Add condition** and then select the box containing the **If** instructions to expand it.  
b. Since in this example we want to check the pattern */article* in the URL path, in the **Type of variable to check** list, select **Server variable**.  
c. In the **Server variable** list, select uri\_path  
d. Under **Case-sensitive**, select **No**.  
e. In the **Operator** list, select **equal (=)**.  
f. Enter a regular expression pattern. In this example, we'll use the pattern `.*article/(.*)/(.*)`  
( ) is used to capture the substring for later use in composing the expression for rewriting the URL path. For more information, see [here](https://learn.microsoft.com/en-gb/azure/application-gateway/rewrite-http-headers-url#capturing).  
g. Select **OK**.  
![Condition](https://proxy-prod.omnivore-image-cache.app/0x0,sZC892wLkv3IkdMplc4TO4EDfJpLklXJ9dt2evdYYIfY/https://learn.microsoft.com/en-gb/azure/application-gateway/media/rewrite-url-portal/rewrite-url-portal-4.png)
7. Add an action to rewrite the URL and URL path  
a. In the **Rewrite type** list, select **URL**.  
b. In the **Action type** list, select **Set**.  
c. Under **Components**, select **Both URL path and URL query string**  
d. In the **URL path value**, enter the new value of the path. In this example, we will use **/article.aspx**  
e. In the **URL query string value**, enter the new value of the URL query string. In this example, we will use **id={var\_uri\_path\_1}&title={var\_uri\_path\_2}**  
`{var_uri_path_1}` and `{var_uri_path_2}` are used to fetch the substrings captured while evaluating the condition in this expression `.*article/(.*)/(.*)`  
f. Select **OK**.  
![Action](https://proxy-prod.omnivore-image-cache.app/0x0,sg8t9y4bUSoqCb9CDuWd6D2c9XkDmhTVFbTMbyzME9Ag/https://learn.microsoft.com/en-gb/azure/application-gateway/media/rewrite-url-portal/rewrite-url-portal-5.png)
8. Click **Create** to create the rewrite set.
9. Verify that the new rewrite set appears in the list of rewrite sets  
![Add rewrite rule](https://proxy-prod.omnivore-image-cache.app/0x0,szLRzdcU9qF_J917KN13ouzxYH4ioKp-V0fGquqIbpRE/https://learn.microsoft.com/en-gb/azure/application-gateway/media/rewrite-url-portal/rewrite-url-portal-6.png)

## Verify URL Rewrite through Access Logs

Observe the below fields in access logs to verify if the URL rewrite happened as per your expectation.

- **originalRequestUriWithArgs**: This field contains the original request URL
- **requestUri**: This field contains the URL after the rewrite operation on Application Gateway

For more information on all the fields in the access logs, see [Access log](https://learn.microsoft.com/en-gb/azure/application-gateway/monitor-application-gateway-reference#access-log-category).

## Next Steps

To learn more about how to set up rewrites for some common use cases, see [common rewrite scenarios](https://learn.microsoft.com/en-gb/azure/application-gateway/rewrite-http-headers-url).

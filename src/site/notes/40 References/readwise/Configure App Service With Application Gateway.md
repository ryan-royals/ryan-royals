---
{"dg-publish":true,"permalink":"/40-references/readwise/configure-app-service-with-application-gateway/","tags":["rw/articles"]}
---


![rw-book-cover](https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png)

  

URL: <https://learn.microsoft.com/en-us/azure/application-gateway/configure-web-app?tabs=customdomain%2Cazure-portal#configuring-dns>  
Author: greg-lindsay

## Summary

This article provides guidance on how to configure Application Gateway with Azure App Service

## Highlights Added July 17, 2024 at 11:02 AM

> Configuring DNS  
> In the context of this scenario, DNS is relevant in two places:  
> • The DNS name, which the user or client is using towards Application Gateway and what is shown in a browser  
> • The DNS name, which Application Gateway is internally using to access the App Service in the backend ([View Highlight] (<https://read.readwise.io/read/01h1nd072p8twhsdqzdrq5g63n>))

> Use [Azure App Service static IP restrictions](https://learn.microsoft.com/en-us/azure/application-gateway/configure-web-app?tabs=customdomain%2Cazure-portal/../app-service/app-service-ip-restrictions). For example, you can restrict the web app so that it only receives traffic from the application gateway. Use the app service IP restriction feature to list the application gateway VIP as the only address with access. ([View Highlight] (<https://read.readwise.io/read/01h2ez4972565702n0r891e785>))

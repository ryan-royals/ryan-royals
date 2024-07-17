---
{"dg-publish":true,"permalink":"/40-references/readwise/overview-of-tls-termination-and-end-to-end-tls-with-application-gateway/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_6v5YQH3.png)
  
URL: https://learn.microsoft.com/en-us/azure/application-gateway/ssl-overview#tls-termination
Author: greg-lindsay

## Summary

This article is an overview of the Application Gateway end to end TLS support.

## Highlights added July 17, 2024 at 11:02 AM
>Transport Layer Security (TLS), previously known as Secure Sockets Layer (SSL), is the standard security technology for establishing an encrypted link between a web server and a browser. This link ensures that all data passed between the web server and browsers remain private and encrypted. Application gateway supports both TLS termination at the gateway as well as end to end TLS encryption. ([View Highlight] (https://read.readwise.io/read/01h1ncwptetcnygfv7jrt9qf25))


>To configure TLS termination, a TLS/SSL certificate must be added to the listener. ([View Highlight] (https://read.readwise.io/read/01h1ncwyr9afejvrw2b913rhe9))


>This allows the Application Gateway to decrypt incoming traffic and encrypt response traffic to the client. ([View Highlight] (https://read.readwise.io/read/01h1ncx1f2q597k0vpx7gdw7gh))


>The certificate provided to the Application Gateway must be in Personal Information Exchange (PFX) format, which contains both the private and public keys ([View Highlight] (https://read.readwise.io/read/01h1ncx8a2mb5xaj971mdnmfw7))


>Application gateway doesn't provide any capability to create a new certificate or send a certificate request to a certification authority. ([View Highlight] (https://read.readwise.io/read/01h1ncxea6gvzjxjz2cyht6rwx))


>Application gateway supports the following types of certificates:
>• CA (Certificate Authority) certificate: A CA certificate is a digital certificate issued by a certificate authority (CA)
>• EV (Extended Validation) certificate: An EV certificate is a certificate that conforms to industry standard certificate guidelines. This will turn the browser locator bar green and publish the company name as well.
>• Wildcard Certificate: This certificate supports any number of subdomains based on *.site.com, where your subdomain would replace the *. It doesn’t, however, support site.com, so in case the users are accessing your website without typing the leading "www", the wildcard certificate won't cover that.
>• Self-Signed certificates: Client browsers don't trust these certificates and will warn the user that the virtual service’s certificate isn't part of a trust chain. Self-signed certificates are good for testing or environments where administrators control the clients and can safely bypass the browser’s security alerts. Production workloads should never use self-signed certificates. ([View Highlight] (https://read.readwise.io/read/01h1ncxqcs3974xtftky49rteg))


>Authentication Certificates have been deprecated and replaced by Trusted Root Certificates in the Application Gateway v2 SKU. They function similarly to Authentication Certificates with a few key differences: ([View Highlight] (https://read.readwise.io/read/01h1ncykmt5hsyjc5h4gqkg8aa))


>In order for a TLS/SSL certificate to be trusted, that certificate of the backend server must have been issued by a CA that is well-known. If the certificate was not issued by a trusted CA, the application gateway will then check to see if the certificate of the issuing CA was issued by a trusted CA, and so on until either a trusted CA is found (at which point a trusted, secure connection will be established) or no trusted CA can be found (at which point the application gateway will mark the backend unhealthy). Therefore, it is recommended the backend server certificate contain both the root and intermediate CAs. ([View Highlight] (https://read.readwise.io/read/01h1ncyxmx9mzx9f0e0kh56mwr))



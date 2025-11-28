---
{"dg-publish":true,"permalink":"/90-slipbox/open-api-specification/","tags":["notes"]}
---

> The OpenAPI Specification is a specification language for HTTP APIs that provides a standardized means to define your API to others. You can quickly discover how an API works, configure infrastructure, generate client code, and create test cases for your APIs. Read more about how you can get control of your APIs now, understand the full API lifecycle and communicate with developer communities inside and outside your organization.  
> <https://www.openapis.org>

Previously known as Swagger Specification

[Example Specs to test against](https://petstore3.swagger.io/)

## Example

```yml
openapi: 3.0.0
info:
  title: My test file
  description: sometimes I write things just to figure it out
  version: 0.0.1

servers:
  - url: http://192.168.0.38
    description: kube-internal

paths:
  /productpage:
    get:
      summary: returns a page of things and stuff
      responses:
        "200":
          description: The contents of the web page
```

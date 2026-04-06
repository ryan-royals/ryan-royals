---
{"dg-publish":true,"permalink":"/90-slipbox/testing-in-terraform/","tags":["notes"],"created":"2024-07-08","updated":"2026-03-03","dg-note-properties":{"tags":"notes","related":["[[Terraform]]"],"references":["https://youtube.com/watch?v=oLRtFy6mYSg&si=8G_U7xu98RVi3x_-"],"created":"2024-07-08","modified":"2026-03-03"}}
---


A [[90_slipbox/Testing Pyramid\|Testing Pyramid]] is a concept used to build tests for your application at different scopes.  
![Testing In Terraform-1720405746383.png](/img/user/10_attachments/Testing%20In%20Terraform-1720405746383.png)![Testing In Terraform-1720405780126.png](/img/user/10_attachments/Testing%20In%20Terraform-1720405780126.png)  
![Testing In Terraform-1720405802724.png](/img/user/10_attachments/Testing%20In%20Terraform-1720405802724.png)  
Terraform tests are written in HCL iwtht he extension of `.tftest.hcl`, and are ran by `terraform test`  
Automatically cleans up the test resources.

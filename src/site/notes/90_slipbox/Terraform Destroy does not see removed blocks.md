---
{"dg-publish":true,"permalink":"/90-slipbox/terraform-destroy-does-not-see-removed-blocks/","tags":["today-i-learns"],"created":"2026-06-15T16:47:19.145+09:30","updated":"2026-08-17T11:34:05.878+09:30","dg-note-properties":{"created":"2026-06-15","modified":"2026-08-17","related":["[[Terraform]]"],"sr-due":"2026-08-15","sr-ease":218,"sr-interval":32,"tags":"today-i-learns"}}
---


Terraform Destroy does not respect removed blocks, they appear to be a Apply time operation.  
The porcelain command for Destroy must be a little different than just being a Apply.

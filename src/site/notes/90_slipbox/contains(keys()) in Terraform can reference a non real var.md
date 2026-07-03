---
{"dg-publish":true,"permalink":"/90-slipbox/contains-keys-in-terraform-can-reference-a-non-real-var/","tags":["today-i-learns"],"created":"2026-03-27T09:57:51.391+10:30","updated":"2026-06-11T09:30:38.147+09:30","dg-note-properties":{"confluenceUrl":"https://arkahna.atlassian.net/wiki/spaces/~6332438e748d1bfcb85930b7/pages/1788444673/contains+keys+in+Terraform+can+reference+a+non+real+var","created":"2026-03-12","modified":"2026-06-11","pageId":"1788444673","related":["[[Terraform]]"],"spaceId":"331808774","tags":"today-i-learns"}}
---


```go
contains(
      keys(var.not_actually_a_variable),
      "key_1"
    ),
    false
  ) ? 1 : 0
```

Wrapping a `keys()` in a `contains()` breaks Terraform logic, and will silently continue.  
This is particularly confusing when working against variables, as they can not be initialised at Plan/Apply time, meaning that they will never work, and will always do the false condition.

In the above example, `var.not_actually_a_variable` is never declared with a `variable` block, but this function will work, even though the declarative nature of Terraform should be failing this, as you usually can not Plan/Apply against a Terraform config with non existent variables / locals.

---
{"dg-publish":true,"permalink":"/90-slipbox/function-app-stuck-with-service-unavailable/","tags":["inbox/new","today-i-learns"],"created":"2026-07-03T09:52:31.502+09:30","updated":"2026-07-03T09:55:03.779+09:30","dg-note-properties":{"created":"2026-07-03","modified":"2026-07-03","related":["[[Azure Functions Apps]]","[[Azure Private Endpoint]]"],"tags":["inbox/new","today-i-learns"]}}
---


![Pasted image 20260703095322.png](/img/user/10_attachments/Pasted%20image%2020260703095322.png)

`Encountered an error (ServiceUnavailable) from host runtime` may be a symptom that there was a timing issue with Function Apps being deployed and Private Endpoint access.  
Potential solution is to set `website_run_from_package` to `0` and restart the Function App. This can help get past the first bad boot and let setup complete.

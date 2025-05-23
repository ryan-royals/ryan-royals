---
{"dg-publish":true,"permalink":"/40-references/readwise/routing-limits-azure-front-door/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_e3f1AZW.png)

## Full Document
[[40 References/readwise/Full Document Contents/Routing limits - Azure Front Door\|Readwise/Full Document Contents/Routing limits - Azure Front Door.md]]

## Highlights
Each Front Door profile has a *composite route limit*.
Your Front Door profile's composite route metric is derived from the number of routes, as well as the front end domains, protocols, and paths associated with that route.
The composite route metric for each Front Door profile can't exceed 5000. ([View Highlight] (https://read.readwise.io/read/01h4fx63z49nwatr99e5y8fcsn))


Calculate your profile's composite route metric
Follow these steps to calculate the composite route metric for your Front Door profile:
1. Select a route from your profile.
1. Multiply the number of HTTP domains by the number of HTTP paths.
2. Multiply the number of HTTPS domains by the number of HTTPS paths.
3. Add the results of steps 1a and 1b together to give the composite route metric for this individual route.
2. Repeat these steps for each route in your profile.
Add together all of the composite route metrics for each route. This is your profile's composite route metric. ([View Highlight] (https://read.readwise.io/read/01h4fx6j00xrbpbsyrgtffag2t))



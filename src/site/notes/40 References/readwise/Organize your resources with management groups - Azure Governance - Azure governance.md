---
{"dg-publish":true,"permalink":"/40-references/readwise/organize-your-resources-with-management-groups-azure-governance-azure-governance/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/media/uploaded_book_covers/profile_921743/logo-ms-social_pyD5ldb.png)

## Summary

Learn about the management groups, how their permissions work, and how to use them.

## Highlights

*Management groups* provide a governance scope above subscriptions. ([View Highlight] (https://read.readwise.io/read/01h181whwptgbh9fzkq0tj56pt))


Management groups give you enterprise-grade management at scale no matter what type of subscriptions you might have. However, all subscriptions within a single management group must trust the same Azure Active Directory (Azure AD) tenant. ([View Highlight] (https://read.readwise.io/read/01h181wrrvhwwjwxdgg7gt7s95))


![](https://learn.microsoft.com/en-us/azure/governance/media/mg-org.png) ([View Highlight] (https://read.readwise.io/read/01h181wztk3ja7fr7akgtp47tf))


10,000 management groups can be supported in a single directory. ([View Highlight] (https://read.readwise.io/read/01h0hjnmkgya8rb36q3t7kn3ma))


A management group tree can support up to six levels of depth.
• This limit doesn't include the Root level or the subscription level. ([View Highlight] (https://read.readwise.io/read/01h0hjnqm5cyjpawh38hmfprfb))


Each management group and subscription can only support one parent. ([View Highlight] (https://read.readwise.io/read/01h0hjntjb71p3shd00s4962ej))


Each management group can have many children. ([View Highlight] (https://read.readwise.io/read/01h0hjnw9trmpc560mzeqk0g4v))


By default, the root management group's display name is **Tenant root group** and operates itself as a management group. The ID is the same value as the Azure Active Directory (Azure AD) tenant ID. ([View Highlight] (https://read.readwise.io/read/01h0hjk7wwaterfsscnhnd7r5s))


**"/providers/Microsoft.Management/managementGroups/{*management-group-id*}"**. ([View Highlight] (https://read.readwise.io/read/01h0hjjf5srdw1svdb8yq515c1))



---
{"dg-publish":true,"permalink":"/40-references/readwise/build-triggers-on-azure-devops-pipelines/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)

## Full Document
[[40 References/readwise/Full Document Contents/Build triggers on Azure devops pipelines\|Readwise/Full Document Contents/Build triggers on Azure devops pipelines.md]]

## Highlights
**Pull Requests:** 
pr keyword will trigger your pipeline if a pull request is created from a branch and the destination is the noted one. For example if you create a new pull request from *mybranch* to *current* branch then the pipeline will get triggered. The pipeline will not trigger if a pull request is created from *any* branch to *uat* branch as it is excluded.
trigger: 
pr: 
branches: 
include: 
- current 
exclude: 
- uat ([View Highlight] (https://read.readwise.io/read/01hm89jxbxfpp7fsk59md0hy5p))



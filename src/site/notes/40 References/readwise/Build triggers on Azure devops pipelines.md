---
{"dg-publish":true,"permalink":"/40-references/readwise/build-triggers-on-azure-devops-pipelines/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)
  
URL: https://blog.geralexgr.com/devops/build-triggers-on-azure-devops-pipelines
Author: geralexgr

## Summary

Build triggers on Azure DevOps pipelines are a powerful tool for your build strategy. Continuous integration triggers can be set up to run a pipeline whenever there is a new commit on a specified branch or when a tag is pushed. Pull request triggers can also be used to run a pipeline when a pull request is created from a specific branch. Additionally, path triggers can be used to specify a directory or folder that will trigger the build when files within it are changed. The Microsoft documentation provides further information on build strategies.

## Highlights added July 17, 2024 at 11:02 AM
>**Pull Requests:** 
>pr keyword will trigger your pipeline if a pull request is created from a branch and the destination is the noted one. For example if you create a new pull request from *mybranch* to *current* branch then the pipeline will get triggered. The pipeline will not trigger if a pull request is created from *any* branch to *uat* branch as it is excluded.
>trigger: 
>pr: 
>branches: 
>include: 
>- current 
>exclude: 
>- uat ([View Highlight] (https://read.readwise.io/read/01hm89jxbxfpp7fsk59md0hy5p))



---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/build-triggers-on-azure-devops-pipelines/","tags":["rw/articles"]}
---

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article3.5c705a01b476.png)

Continuous integration (CI) triggers cause a pipeline to run whenever you push an update to the specified branches or you push specified tags. Build in triggers can become a powerful tool for your build strategy and the most common scenarios will be explained using the examples below.

**Continuous integration triggers:**

**Branches:**  

Those will trigger your pipeline when a new commit is performed on your branch. In the scenario below the pipeline will run if code is merged on your main branch or a branch starting from releases like *release1*, *release-1* *releases* etc. Also the pipeline **will not run** if a push is commited on *uat* branch. This is excluded through the exclude keyword.

```
trigger:  
  branches:  
    include:  
      - main  
      - release/*  
    exclude:  
      - uat
```

**Tags:**Those will trigger your pipeline only when a tag is pushed on your repository. Tags are bound with a commit on a git source control system. In the scenario below the pipeline will get triggered if a tag is pushed following the v.\* regex like *v.1* , *v.something*, *v.2* etc. Also it will not run if the tag that is pushed starts with *uat* keyword for example uat-1 will not trigger the pipeline.

```
trigger:  
  tags:  
    include:  
      - v.*  
    exclude:  
      - uat*
```

**Pull Requests:**  

pr keyword will trigger your pipeline if a pull request is created from a branch and the destination is the noted one. For example if you create a new pull request from *mybranch* to *current* branch then the pipeline will get triggered. The pipeline will not trigger if a pull request is created from *any* branch to *uat* branch as it is excluded.

```
trigger:  
pr:  
  branches:  
    include:  
    - current  
    exclude:  
      - uat
```

One powerful tool that you can combine with your build strategy is paths. When you specify paths, you must explicitly specify branches to trigger on. You can’t trigger a pipeline with only a path filter; you must also have a branch filter, and the changed files that match the path filter must be from a branch that matches the branch filter.

**Paths:**  

Using a path you specify a directory/folder which will trigger the build. For example you may want only to trigger a build when particular files are changed on your repository. In the below example the pipeline will get triggered if files inside the *docs* folder change for the branches *master* and *releases\**

```
trigger:  
  branches:  
    include:  
    - master  
    - releases/*  
  paths:  
    include:  
    - docs  
    exclude:  
    - docs/README.md
```

Microsoft documentation for build strategies:

<https://docs.microsoft.com/en-us/azure/devops/pipelines/repos/azure-repos-git?view=azure-devops&tabs=yaml#ci-triggers>

---
{"dg-publish":true,"permalink":"/90-slipbox/git-hub-responds-to-pnpm-view-package-with-nothing/","tags":["how-tos"],"created":"2026-03-27T09:57:51.531+10:30","updated":"2026-03-27T09:57:51.531+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Github Packages]]","[[PNPM]]"],"created":"2025-12-18","modified":"2026-03-03","pageId":"1645838354","spaceId":"331808774","confluenceUrl":"https://arkahna.atlassian.net/wiki/spaces/~6332438e748d1bfcb85930b7/pages/1645838354/GitHub+responds+to+pnpm+view+package+with+nothing"}}
---


## Problem

```sh
> pnpm i

The latest release of @ghorg/package is "undefined".

Other releases are:
  * canary: 0.0.0-canary-20251218022034 published at 12/18/2025 12:51:25 PM

> pnpm view @ghorg/package 

```

Even though the package is visible in the GitHub Packages, and has releases on it, it does not seem to be able to install.  
Trying to view the package using `pnpm view` results in a blank response

## Solutions

### There is no Latest Dist-tag

If the package has only ever been released with a alternate dist-tag like `canary`, then GitHub Packages may not respond with the package details.  
Releasing a un tagged version / `latest` tagged version will make it all work, with both `latest` and `canary` working, including for all previous `canary` releases.

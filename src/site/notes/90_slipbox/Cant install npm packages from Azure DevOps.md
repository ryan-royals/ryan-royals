---
{"dg-publish":true,"permalink":"/90-slipbox/cant-install-npm-packages-from-azure-dev-ops/","tags":["how-tos"],"created":"2026-03-27T09:57:51.391+10:30","updated":"2026-03-27T09:57:51.392+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Azure DevOps]]","[[PNPM]]"],"created":"2026-03-06","modified":"2026-03-06","pageId":"1783496705","spaceId":"331808774","confluenceUrl":"https://arkahna.atlassian.net/wiki/spaces/~6332438e748d1bfcb85930b7/pages/1783496705/Cant+install+npm+packages+from+Azure+DevOps"}}
---


## Problem

When working with Azure Feeds (Azure DevOps Packages), it appears that the PAT token is only good for packages and versions available at time of provision.
    
> [!note]  
> Low confidence in this, need to find documentation to match or contradict this theory

## Solutions

### Refresh the Token in the .npmrc File

Recreate the PAT token used in the .npmrc when new packages are available.

To create a Personal Access Token
1. Navigate to: <https://dev.azure.com/$>{conf.adoOrgContext}/_usersSettings/tokens
2. Click "New Token"
3. Set scope to "Packaging (Read & Write)"

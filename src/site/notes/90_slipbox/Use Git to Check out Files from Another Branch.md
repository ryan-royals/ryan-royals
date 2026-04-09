---
{"dg-publish":true,"permalink":"/90-slipbox/use-git-to-check-out-files-from-another-branch/","tags":["how-tos"],"created":"2026-03-05T13:54:38.427+10:30","updated":"2026-03-05T13:55:14.583+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Git]]"],"created":"2026-03-05","modified":"2026-03-05"}}
---


## Problem

Sometimes you just need to hard roll back a file

## Solutions

### Solution 1

```bash
git checkout <branch> -- <path>
git checkout main -- terraform/apps/app1
```

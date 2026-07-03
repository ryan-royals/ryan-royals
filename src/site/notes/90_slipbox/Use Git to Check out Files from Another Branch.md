---
{"dg-publish":true,"permalink":"/90-slipbox/use-git-to-check-out-files-from-another-branch/","tags":["how-tos"],"created":"2026-03-27T09:57:51.396+10:30","updated":"2026-06-11T09:30:38.161+09:30","dg-note-properties":{"created":"2026-03-05","modified":"2026-06-11","related":["[[Git]]"],"tags":"how-tos"}}
---


## Problem

Sometimes you just need to hard roll back a file

## Solutions

### Solution 1

```bash
git checkout <branch> -- <path>
git checkout main -- terraform/apps/app1
```

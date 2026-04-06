---
{"dg-publish":true,"permalink":"/90-slipbox/remove-local-git-branches-that-no-longer-have-a-remote/","tags":["how-tos"],"created":"2026-03-27T09:57:51.396+10:30","updated":"2026-03-27T09:57:51.396+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Git]]"],"created":"2026-03-05","modified":"2026-03-05"}}
---


## Problem

Over time merged branches accumilate on the local machine, and dont represent the remote

## Solutions

### Bash

```Bash
git fetch -p && git branch -vv | awk '/: gone]/{print $1}' | xargs git branch -d
```

### Powershell

```powershell
git fetch -p
git branch --v | ? { $_ -match "\[gone\]" } | % { -split $_ | select -First 1 } | % { git branch -D $_ }
```

---
{"dg-publish":true,"permalink":"/90-slipbox/local-git-ignore/","tags":["how-tos"],"created":"2026-03-27T09:57:51.396+10:30","updated":"2026-03-27T09:57:51.396+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Git]]"],"created":"2026-03-05","modified":"2026-03-05"}}
---


## Problem

Need a way to be certain that files wont end up in git, but you don't want to add to the git ignore.

## Solutions

### Solution 1

Use `.git/info/exclude` as a local `.gitignore` that does not update the gitignore.

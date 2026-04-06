---
{"dg-publish":true,"dg-path":"Slipbox Notes/Local Git Ignore.md","permalink":"/slipbox-notes/local-git-ignore/","tags":["how-tos"],"created":"2026-03-05","updated":"2026-03-05","dg-note-properties":{"tags":"how-tos","related":["[[Git]]"],"created":"2026-03-05","modified":"2026-03-05"}}
---


## Problem

Need a way to be certain that files wont end up in git, but you don't want to add to the git ignore.

## Solutions

### Solution 1

Use `.git/info/exclude` as a local `.gitignore` that does not update the gitignore.

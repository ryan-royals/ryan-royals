---
{"dg-publish":true,"dg-path":"Slipbox Notes/Search and Replace content in files.md","permalink":"/slipbox-notes/search-and-replace-content-in-files/","tags":["how-tos"],"dg-note-properties":{"tags":"how-tos","related":["[[RipGrep]]","[[sed]]","[[Shell|Bash]]","[[xargs]]"],"created":"2026-02-24","modified":"2026-03-03"}}
---


## Problem

Need to edit the contents across X amount of files, down directories

## Solutions

### Easy Shell search and Replace

`rg {target} -l -0 | xargs -0 sed -i 's/{target}/{replace}/'`

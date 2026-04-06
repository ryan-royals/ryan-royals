---
{"dg-publish":true,"dg-path":"Slipbox Notes/Multi line copy from a file.md","permalink":"/slipbox-notes/multi-line-copy-from-a-file/","tags":["how-tos"],"dg-note-properties":{"tags":"how-tos","related":["[[RipGrep]]","[[Shell|Bash]]"],"created":"2026-03-11","modified":"2026-03-11"}}
---


## Problem

I want to copy all matching lines out of a file, without having to move them about first

## Solutions

### RipGrep and Pipe to Wl-copy

```sh
rg -oP 'regex.*' file.txt | wl-copy
```

**-o**  
Print only the matching part  
**-P**  
Perl compatible regex, for things like `\S`

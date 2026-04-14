---
{"dg-publish":true,"permalink":"/90-slipbox/multi-file-search-and-replace-in-neovim/","tags":["how-tos"],"created":"2026-04-13T08:05:02.797+09:30","updated":"2026-04-13T08:05:03.182+09:30","dg-note-properties":{"tags":"how-tos","related":["[[NeoVim]]"],"created":"2026-04-10","modified":"2026-04-10"}}
---


## Problem

Bulk refactor lots of files where LSP tools are not doing it for you.

## Solutions

Solutions largely come down to using [[90_slipbox/Search and Replace in NeoVim\|Search and Replace in NeoVim]] on multiple files at the same time.

### Args / Argdo

You can use capture groups across multiple files:

```vim
:args **/*.tf
:argdo %s/\(resource.*\)/# Modified: \1/ge | update
```

This captures entire resource lines and adds a comment prefix across all `.tf` files.

The `e` flag suppresses errors if no matches are found, and `update` saves only if the file was modified.

### [[90_slipbox/Quick Fix in NeoVim\|Quick Fix in NeoVim]]

1. `grep *foo*`
2. `cw` to show results
   1. This opens the Cuick Window
   2. alias for `cwindow`
3. `cfdo %s/*foo*/*bar*`
   1. Cuick **File** do
   2. `cdo` operates on each line, but since we want the run `%s`, we need to target file

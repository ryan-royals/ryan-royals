---
{"dg-publish":true,"permalink":"/90-slipbox/search-and-replace-in-neo-vim/","tags":["how-tos"],"created":"2026-04-10T16:46:50.138+09:30","updated":"2026-04-15T13:34:03.713+09:30","dg-note-properties":{"tags":"how-tos","related":["[[NeoVim]]"],"created":"2026-04-10","modified":"2026-04-15","aliases":"%s"}}
---


## Getting started with Search and Replace `%s`

```
:%s/target/replacement/
```

### Swap Two Words

```vim
:%s/\(\w\+\) \(\w\+\)/\2 \1/g
```

This captures two words and swaps their positions.

### Add Quotes around a Word

```vim
:%s/\(\w\+\)/"\1"/g
```

### Extract and Reformat

```vim
:%s/name: \(.*\), age: \(.*\)/\1 is \2 years old/g
```

## Magic Mode Options

Neovim supports different "magic" modes that affect escaping:

**Very Magic Mode (`\v`)** - Less escaping needed:

```vim
:%s/\v(pattern)/\1/g
```

**No Magic Mode (`\V`)** - Literal matching:

```vim
:%s/\V\(literal.text\)/\1/g
```

## Multi File

### Args / Argdo

You can use capture groups across multiple files:

```vim
:args **/*.tf
:argdo %s/\(resource.*\)/# Modified: \1/ge | update
```

This captures entire resource lines and adds a comment prefix across all `.tf` files.

The `e` flag suppresses errors if no matches are found, and `update` saves only if the file was modified.

### Quick Fix in NeoVim

*In my config it uses ripgrep in the background as it faster and what the cool kids use*

1. Search using grep

```vim
:grep -g '*.tf' '*foo*'
```

 `-g` - Glob - Define the files to search through

2. Show the results in the Quick Window

```vim
:cw
:cwindow
```

3. Quick Fix Do to use `%s` on all files in the Quick Window

```vim
:cfdo %s/*foo*/*bar*`
```

   `cdo` operates on each line, but since we want the run `%s`, we need to target file

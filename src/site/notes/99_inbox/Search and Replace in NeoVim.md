---
{"dg-publish":true,"permalink":"/99-inbox/search-and-replace-in-neo-vim/","tags":["notes"],"created":"2026-04-10T16:46:50.138+09:30","updated":"2026-04-10T16:55:45.435+09:30","dg-note-properties":{"tags":"notes","related":["[[NeoVim]]","[[Quick Fix in NeoVim]]"],"created":"2026-04-10","modified":"2026-04-10","aliases":"%s"}}
---


Basic Capture Group Syntax

**Search pattern:**

```shell
\(pattern\)
```

**Replace with captured content:**

```shell
\1, \2, \3, etc.
```

## Practical Examples

**Example 1: Swap two words**

```vim
:%s/\(\w\+\) \(\w\+\)/\2 \1/g
```

This captures two words and swaps their positions.

**Example 2: Add quotes around a word**

```vim
:%s/\(\w\+\)/"\1"/g
```

**Example 3: Extract and reformat**

vim

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

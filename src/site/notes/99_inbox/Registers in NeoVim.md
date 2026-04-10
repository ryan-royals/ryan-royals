---
{"dg-publish":true,"permalink":"/99-inbox/registers-in-neo-vim/","tags":["notes"],"created":"2026-04-10T16:04:36.328+09:30","updated":"2026-04-10T18:13:19.536+09:30","dg-note-properties":{"tags":"notes","related":["[[NeoVim]]"],"created":"2026-04-10","modified":"2026-04-10","references":["https://kezhenxu94.me/blog/registers-in-vim","https://neovim.io/doc/user/change/#_registers"]}}
---


Nvim has a complex suite of Registers that it uses, basically a unlimited amount of clipboards.  
They can be reached with`"` in *normal* or with `ctrl+r` in *insert* mode (or command etc).  
Registers fill at different times, but users can make their own Named register by using any a-z A-Z.

`:reg` can be used to view all registers, and you can filter via `:reg {reg}`

## Unnamed Register `"`

`"` is the default unnamed register.  
When you do a `dd` , a `yy` or `ciw`, these propagate to the `"` register.  
When you do a `p`, that calls the `"` register

## Black Hole Register `_`

The `/dev/null` of registers.  
Handy for `"_dd` so that the deleted line does not write to the `"` register.

## System Clipboard `+` and `*`

Hard to find the difference, but they are both using system clipboard.

> [!note]  
> It is common to have in nvim config `vim.opt.clipboard = "unnamedplus"`, which syncs the `"` with clipboard anyway, so you can yank to clipboard without fuss

## Named Register `a-z A-Z`

User land of registers. Any letter can be used to keep custom stuff.  
Handy for "I need this for later" moments.  
`"add` to then later `"ap`

## Last Yanked `0`

`0` always has the last `y`ank in it unless you redirected it.

## Numbered `1-9`

A running log of your recent changes are kept in registers `1-9`, with `1` being the most recent.

## Small Delete `-`

If you do a `diw` or a `ciw` style change, it goes here.  
Basically anything less than a whole line.

## Last Inserted `.`

Last insert action. Repeat, like using `.` to repeat `d5k`.

## Last Command `:`

Last command ran in the command palette

## Last Search `/`

Whatever you last searched is here.

## Current File `%`

Name of the file, including the path.

## Expression `=`

Feels out of place, but basically when you call the register it opens the command palette and you can do 2+2 and it inserts 4.

## Alternative File `#`

Used in the background to power `CTRL-^`, used to jump around buffers.

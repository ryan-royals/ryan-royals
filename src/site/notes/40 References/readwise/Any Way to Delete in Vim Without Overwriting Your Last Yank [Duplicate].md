---
{"dg-publish":true,"permalink":"/40-references/readwise/any-way-to-delete-in-vim-without-overwriting-your-last-yank-duplicate/","tags":["rw/articles"]}
---

![40 References/attachments/e1a56b93cf1dbe1b46d6277544b57e33_MD5.jpg](/img/user/40%20References/attachments/e1a56b93cf1dbe1b46d6277544b57e33_MD5.jpg)
  
URL: https://stackoverflow.com/questions/3638542/any-way-to-delete-in-vim-without-overwriting-your-last-yank
Author: Stack Overflow

## Summary

I love vim, but one common gotcha is:
yank a line
go to where you would like to paste it
delete what's there
paste your yank, only to discover that it pastes what you just deleted
Obviously the

## Highlights added August 30, 2024 at 2:23 PM
>Pass to the `_` register, the black hole.
>To delete a line without sticking it in the registers:
>"_dd ([View Highlight] (https://read.readwise.io/read/01gy9fz8mm8rxty0rrajmhz2xm))



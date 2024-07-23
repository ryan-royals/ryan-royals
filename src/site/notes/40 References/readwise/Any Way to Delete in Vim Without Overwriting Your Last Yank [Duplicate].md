---
{"dg-publish":true,"permalink":"/40-references/readwise/any-way-to-delete-in-vim-without-overwriting-your-last-yank-duplicate/","tags":["rw/articles"]}
---


![rw-book-cover](https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded)

  

URL: <https://stackoverflow.com/questions/3638542/any-way-to-delete-in-vim-without-overwriting-your-last-yank>  
Author: Stack Overflow

## Summary

I love vim, but one common gotcha is:  
yank a line  
go to where you would like to paste it  
delete what's there  
paste your yank, only to discover that it pastes what you just deleted  
Obviously the

## Highlights Added July 17, 2024 at 11:02 AM

> Pass to the `_` register, the black hole.  
> To delete a line without sticking it in the registers:  
> "_dd ([View Highlight] (<https://read.readwise.io/read/01gy9fz8mm8rxty0rrajmhz2xm>))

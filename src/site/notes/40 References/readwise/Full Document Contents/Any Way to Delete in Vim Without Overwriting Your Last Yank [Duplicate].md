---
{"dg-publish":true,"permalink":"/40-references/readwise/full-document-contents/any-way-to-delete-in-vim-without-overwriting-your-last-yank-duplicate/","tags":["rw/articles"]}
---

![rw-book-cover](https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded)

I love vim, but one common gotcha is:

* yank a line
* go to where you would like to paste it
* delete what's there
* paste your yank, only to discover that it pastes what you just deleted

Obviously the workflow is delete first, yank second. But it would be reeeeeaaaaaalllly nice if I didn't *have* to. Anyone have a trick for this? Does vim have a paste buffer that works well, or is there a .vimrc setting I can change?

6 

Pass to the `_` register, the black hole.

To delete a line without sticking it in the registers:

```
"_dd

```

See also [`:help registers`](http://vimdoc.sourceforge.net/htmldoc/change.html#registers).

It's probably safest, if you want to paste something over and over again, to yank it into a "named" register.

```
"aY

```

Yanks a line into the `a` register. Paste it with `"ap`.

10 

 5 

All yank and delete operations write to the unnamed register by default. However, the most recent yank and most recent delete are always stored (separately) in the numbered registers. **The register `0` holds the most recent yank**. The registers `1-9` hold the 9 most recent deletes (with `1` being the most recent).

In other words, **a delete overwrites the most recent yank in the unnamed register, but it's still there in the `0` register.** The blackhole-register trick (`"_dd`) mentioned in the other answers works because it prevents overwriting the unnamed register, but it's not necessary.

You reference a register using double quotes, so pasting the most recently yanked text can be done like this:

```
"0p

```

This is an excellent reference:

6 

 5 

 2 

 3 

I wrote [this plugin (yankstack.vim)](https://github.com/maxbrunsfeld/vim-yankstack) to solve this problem. It gives you something like [Emacs's kill ring](http://www.gnu.org/s/libtool/manual/emacs/Kill-Ring.html) for vim. You can yank or delete multiple things, do a paste, and then cycle back and forth through your history of yanked/killed text. I find its easier than having to remember what register I yanked something into.

In my .vimrc, I have these mappings:

```
nmap <M-p> <Plug>yankstack_substitute_older_paste
nmap <M-P> <Plug>yankstack_substitute_newer_paste

```

which let me hit ALT-p or ALT-SHIFT-p to cycle back and forth through my paste history.

 2 

 1 

If you are an evil user, you may consider remapping X to do the equivalent of "\_d. However, perfecting the implementation was a little tricky for me. Nonetheless, I found that

```
(define-key evil-normal-state-map "X" 'evil-destroy)
(define-key evil-visual-state-map "X" 'evil-destroy)

(evil-define-operator evil-destroy (beg end type register yank-handler)
  "delete without yanking text"
  (evil-delete beg end type 95 yank-handler)
)

```

integrates very nicely. For example, typing XX will function analogously to dd, as will X$ to d$, X0 to d0, etc...

If you are curious as to how it works, "95" represents the "\_ register, so it simply reroutes your call to delete as if "\_ had been the register pressed.

The trick is that you know you want to grab something and move, and you are using the 'lazy' first register (which gets replaced by whatever you just deleted).

You need to learn to "cut" in vim.

Before deleting, specify any register different than the `"` one. Tip: check out your registers with `:reg`

now, you select a new register by pressing `"` before any command (in command mode, obviously)

1. select what you want to "cut" (or at step 2 specify a range)
2. Change register to anything (`1` here) and delete: `"1d` or `"1x` or even `"1c`
3. go to new place, delete some more
4. now you are ready to paste what you cut and stored in register 1: `"1p` or `"1P`

done. this also has the advantage of solving the usecase: delete 5 different things from one place, and each piece goes to a different destination... just put one in `"1` another in `"2` and so on... go to each destination and paste.

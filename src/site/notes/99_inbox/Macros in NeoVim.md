---
{"dg-publish":true,"permalink":"/99-inbox/macros-in-neo-vim/","tags":["notes"],"created":"2026-04-10T16:43:04.180+09:30","updated":"2026-04-10T18:13:20.356+09:30","dg-note-properties":{"tags":"notes","related":["[[NeoVim]]"],"created":"2026-04-10","modified":"2026-04-10"}}
---


To record a macro and save it to a register, type the key **q** followed by a letter from **a** to **z** that represents the register to save the macro, followed by all commands you want to record, and then type the key **q** again to stop the recording.

```vim
q<register><commands>q
```

For example, to record a basic macro that inserts a new line and save it to register **a**, use this sequence:

```vim
qao<ESC>q
```

Then to execute, type **@** then the macro key

```vim
@q
```

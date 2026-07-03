---
{"dg-publish":true,"permalink":"/90-slipbox/symlinking-zshrc-file-breaks-when-apps-write-to-it/","tags":["today-i-learns"],"created":"2026-03-27T09:57:51.396+10:30","updated":"2026-06-11T09:30:38.178+09:30","dg-note-properties":{"created":"2026-03-05","modified":"2026-06-11","related":["[[Kachow]]","[[ln]]","[[Shell|Bash]]","[[Shell|Zsh]]","[[Stow]]"],"tags":"today-i-learns"}}
---


When applications offer to update the .zshrc file to do thinks like autocomplete, there is a good chance that it will break any symlinking for the file.  
This is due to how it can process the write, as it most likely wont follow the link, and instead just write to the actual location of the symlink.

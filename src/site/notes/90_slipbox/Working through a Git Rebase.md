---
{"dg-publish":true,"permalink":"/90-slipbox/working-through-a-git-rebase/","tags":["how-tos"],"created":"2026-03-05T13:55:39.267+10:30","updated":"2026-03-12T16:31:49.585+10:30","dg-note-properties":{"tags":"how-tos","related":["[[Git]]"],"created":"2026-03-05","modified":"2026-03-12"}}
---


## Problem

GIt rebases are hard

## Solutions

### Working through a Git Rebase Using CLI

``` bash
git pull origin <branch> --rebase 

git status                    # see which files are conflicted
git diff                      # see the actual conflicts
git rebase --skip             # skip this commit entirely
git rebase --abort            # bail out and return to pre-rebase state
git checkout --ours <file>    # select the version of the file coming from upstream
git checkout --theirs <file>  # select the version of the file from local commits
git add <file>                # add the file completing the rebase action
git rebase --continue         # go to the next conflicting commit / finish


```

| Command    | During `merge`             | During `rebase`                            |
| ---------- | -------------------------- | ------------------------------------------ |
| `--ours`   | your current branch        | the *upstream* branch you're rebasing onto |
| `--theirs` | the branch being merged in | your *own* commits being replayed          |

### Interactive Rebase

```bash
git rebase -i <branch>
```

This will open up editor, and you can change the noun on the left to do things.  
Instructions are at the bottom of the dock

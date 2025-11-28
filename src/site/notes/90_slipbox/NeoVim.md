---
{"dg-publish":true,"permalink":"/90-slipbox/neo-vim/","tags":["notes"]}
---


## Tips

### Delete to Black Hole Register Using Vim

```vim
"_dd
```

### Macros

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

### Quick Fix

1. `grep *foo*`
2. `cw` to show results
   1. This opens the Quick Fix window
   2. alias for `cwindow`
3. `cfdo %s/*foo*/*bar*`
   1. Quick fix **File** do
   2. `cdo` operates on each line, but since we want the run `%s`, we need to target file

### Search and Replace

Basic Capture Group Syntax

**Search pattern:**

```
\(pattern\)
```

**Replace with captured content:**

```
\1, \2, \3, etc.
```

#### Practical Examples

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

#### Magic Mode Options

Neovim supports different "magic" modes that affect escaping:

**Very Magic Mode (`\v`)** - Less escaping needed:

```vim
:%s/\v(pattern)/\1/g
```

**No Magic Mode (`\V`)** - Literal matching:

```vim
:%s/\V\(literal.text\)/\1/g
```

### Multiple File Search/Replace

You can use capture groups across multiple files:

```vim
:args **/*.tf
:argdo %s/\(resource.*\)/# Modified: \1/ge | update
```

This captures entire resource lines and adds a comment prefix across all `.tf` files.

The `e` flag suppresses errors if no matches are found, and `update` saves only if the file was modified.

### Remove Consecutive Empty Lines

Condense multiple consecutive empty lines into single empty lines:

```vim
:%s/\n\n\zs\n\+//g
```

**Breakdown:**
- `\n\n` - Match two newlines (one empty line)
- `\zs` - Zero-width start match (only delete what follows)
- `\n\+` - Match additional newlines
- Result: Keeps one empty line, removes extras

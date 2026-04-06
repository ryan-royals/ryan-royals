---
{"dg-publish":true,"permalink":"/90-slipbox/bash-conditions/","tags":["how-tos"],"created":"2026-03-06","updated":"2026-03-12","dg-note-properties":{"tags":"how-tos","related":["[[Shell|Bash]]"],"references":["https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs"],"created":"2026-03-06","modified":"2026-03-12"}}
---


## If Conditions

String tests

``` bash
[ -z "$var" ]   # true if empty
[ -n "$var" ]   # true if not empty
[ "$a" = "$b" ] # equal
[ "$a" != "$b"] # not equal
```

Number tests

```bash
[ "$a" -eq "$b" ] # equal
[ "$a" -ne "$b" ] # not equal
[ "$a" -lt "$b" ] # less than
[ "$a" -gt "$b" ] # greater than
[ "$a" -le "$b" ] # less than or equal
[ "$a" -ge "$b" ] # greater than or equal
```

File tests

```bash
[ -f "$file" ]  # is a file
[ -d "$dir" ]   # is a directory
[ -e "$path" ]  # exists
[ -r "$file" ]  # readable
[ -x "$file" ]  # executable
```

Boolean logic

```bash
[ "$a" = "x" ] && [ "$b" = "y" ]  # AND
[ "$a" = "x" ] || [ "$b" = "y" ]  # OR
[ ! -f "$file" ]                   # NOT
[[ ]] (bash/zsh preferred) — supports regex and no quoting issues
[[ "$var" == "foo" ]]      # glob match
[[ "$var" =~ ^foo.* ]]    # regex match
[[ -f "$file" && -r "$file" ]]  # AND inside [[ ]]
```

Arithmetic

```bash
(( count > 5 ))
(( count % 2 == 0 ))
```

## For Loops

Over a list

```bash
for item in a b c; do
  echo "$item"
done
```

Over an array

```bash
items=("foo" "bar" "baz")
for item in "${items[@]}"; do
  echo "$item"
done
```

Over command output

```bash
for file in $(ls *.txt); do
  echo "$file"
done
```

C-style

```bash
for (( i = 0; i < 10; i++ )); do
  echo "$i"
done
```

Over a range

```bash 
for i in {1.}; do
  echo "$i"
done
```

## While Loops

Basic  

```bash
while [ "$count" -lt 10 ]; do  
  (( count++ ))  
done  
```

Reading lines from a file  

```bash
while IFS= read -r line; do  
  echo "$line"  
done < file.txt  
```

Reading command output  

```bash
while IFS= read -r line; do  
  echo "$line"  
done < <(git branch)
```

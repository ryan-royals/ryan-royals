---
{"dg-publish":true,"permalink":"/90-slipbox/types-in-terraform/","tags":["notes"]}
---


Here is a quick run through of each *type*, and how you pass inputs to the `variable` in a `.tfvars` file. These types are also used within you Terraform code in blocks such as `locals`, but those types are implied and assumed by Terraform, whilst in `variables` they are explicitly called out.

## Primitive Types

Primitive Types are the most atomic unit of input, and are used as the building blocks for more complicated Collections and Structures.

### `string`

A sequence of unicode characters. Used all the time in Terraform.  

``` hcl [2-4]
# variables.tf
variable "lettersandstuff" {
 type = string
}
```

``` hcl[2]
# dev.tfvars
lettersandstuff = "heyyyy"
```

### `number`

A number, can be fractional. Used rarely in real deployments, as Terraform is Declarative and things like sums don't always find a home when we are trying to tell a cloud platform to look like X.  

``` hcl[2-5]
# variables.tf
variable "calc_u_later" {
 type = number
}
```

``` hcl [2]
# dev.tfvars
calc_u_later = 420.69
```

### `bool`

A Boolean value (True or false). Used all the time for conditionals in deployments.

``` hcl [2-5]
# variables.tf
variable "learning_something" {
 type = bool
}
```

``` hcl [2]
# dev.tfvars
learning_something = true
```

## Collection Types

Collections are a ~~collection~~ group of the same types, used to collate information together. If you are looking to mix and match types under the same variable without nesting, that is the use case for a Structural Type.

### `list`

A ordered sequence of primitive types, which can have duplicates. Used all the time as input as it is simple to work with when we start looking at things like Loops.  

``` hcl [2-9]
# variables.tf
variable "agoodlist" {
 type = list(string)
}
variable "acomplicatedlist" {
  type = list(object({
    name = string
  }))
}
```

``` hcl[2-10]
# dev.tfvars
agoodlist = ["this", "blog", "is", "is", "is", "great"]
acomplicatedlist = [
  {
    name = "Great"
  },
  {
    name = "Awesome"
  }
]
```

### `map`

A unordered collection of values identified by a Key. Not used much as its keys are not strictly set, and Terraform is very strict about knowing keys before Plan/Apply.

```hcl [2-7]
# variables.tf
variable "pirate" {
 type = map(string)
}
```

``` hcl[2-5]
# dev.tfvars
pirate = {
 yarhar     = "fiddle dee dee",
 thisIsAKey = "thisIsAValue"
}
```

### `set`

A unordered sequence of unique values. Very rarely used as a variable, as lists are easier to work with (Since Lists are ordered, Terraform interacts with them in a simpler fashion).

```hcl[2-5]
# variables.tf
variable "agoodpun" {
 type = set(string)
}
```

``` hcl [2]
# dev.tfvars
agoodpun = ["this","blog","just","keeps","giving"]
```

## Structural Types

Structural types are similar to Collection types, but a singular Structure can have different Types all bundled together.

### `object`

A collection of named attributes, each with their own type. Used all the time by itself as a `variable`, or within a `list` as you get to define the Key up front, and know exactly what type of value you are looking up.

```hcl [2-7]
# variables.tf
variable "aobject" {
 type = object({
  name = string
  count = number
 })
}
```

```hcl [2-10]
# dev.tfvars
aobject = {
 name = "hellyeah"
 count = 20
}
```

### `tuple`

A ordered sequence of types. Each type declared must have *exactly that*. Hard to work with, not sure we have ever actually used it to have different types in any deployment. Note that `tuple` and `list` are both wrapped in square brackets `[]`, which can confuse Terraform sometimes.

``` hcl [2-5]
# variables.tf
variable "tupleware" {
 type = tuple([string, bool, number])
}
```

```hcl[2]
# dev.tfvars
["tupleCheck", false, 001]
```

## The `any` Type

For the sake of completeness, there is another type you can define being `any`. This is the same as not declaring a type on the `variable` block at all.  
I will be stern and say there is no valid use case for this type, and it is not even worth looking for exceptions or examples on when its useful, as it is almost a fundamental breach of the declarative nature of Terraform.

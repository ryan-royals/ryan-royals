---
{"dg-publish":true,"dg-path":"Slipbox Notes/JavaScript.md","permalink":"/slipbox-notes/java-script/","tags":["notes"],"created":"2023-09-04","updated":"2025-11-28"}
---


JavaScript is a dynamic language that supports being Object Oriented, Imperative and Declarative.

## Basics

*Variables* are defined using `let` or `var` and can change over time.

```js
let myFirstVariable = 1;
myFirstVariable = "Some string";
myFirstVariable = new SomeComplexClass();
```

*Constants* are defined with `const` and can not change over time.

```js
const MY_FIRST_CONSTANT = 10;
// Can not be re-assigned.
MY_FIRST_CONSTANT = 20;
// => TypeError: Assignment to constant variable.
```

*Functions* are declared many different ways, with the simplest being with the word `function`

```js
function add(num1, num2) {
  return num1 + num2;
}
add(1, 3);
// => 4
```

*Imports* and *Exports* are based on the file they are defined in.

```js
// file.js
export const MY_VALUE = 10;
export function add(num1, num2) {
  return num1 + num2;
}
// file.spec.js
import { MY_VALUE, add } from "./file";
add(MY_VALUE, 5);
// => 15
```

Type checking is typically enabled for JavaScript (Using [[TypeScript\|TypeScript]]) by adding a directive at the start of the file

```js
// @ts-check
function add(num1, num2) {
  return num1 + num2;
}
add(1, 3);
// => 4
```

- [x] [JavaScript key concepts on Exercism](https://exercism.org/tracks/javascript/exercises/lasagna/edit)

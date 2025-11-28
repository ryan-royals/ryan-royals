---
{"dg-publish":true,"permalink":"/90-slipbox/type-script-compared-to-java-script/","tags":["notes"]}
---


Typescript is a ***typed*** *superset* of [[90_slipbox/JavaScript\|JavaScript]] that adds a Static Type Checker functionality that checks for nonsensical operations among other errors.

```run-js
if ("" == 0) {
	console.log("But why?");
}
```

> [!output]  
> But why?

```run-ts
if ("" == 0) {
	console.log("Not this time")
}
```

> [!error]  
> This comparison appears to be unintentional because the types 'string' and 'number' have no overlap

## Syntax

TypeScript being a *superset* of JavaScript means that JS syntax is legal, and Typescript check for syntax errors (Missing closing brace for example). This also means that you can import any working JavaScript code into a TypeScript file and it will continue to work.

## Types

With TS being a ***typed*** *superset* of JS, it adds rules to how different kinds of values can be used.

```run-ts
console.log(4 / []);
```

> [!error]  
> The right-hand side of an arithmetic operation must be of type 'any', 'number', 'bigint' or an enum type

Typescript's type checker is designed to allow correct programs through while catching as many common errors as possible (Which can be configured).

## Runtime Behaviour

TypeScript preserves the runtime behaviour of JS, and as a general principle **never** changes the runtime behaviour of JavaScript code. Moving code from JS to TS is **guaranteed** to run the same way, even if TS thinks there are errors.

## Erased Types

Once TS compilers are done with checking the code, it erases the types to produce the resulting "compiled" code. This means that once its compiled, it results in plan JS.

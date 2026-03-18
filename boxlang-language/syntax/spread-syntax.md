---
description: Use spread syntax in literals and function calls, plus shorthand struct keys.
icon: ellipsis
---

# Spread Syntax

{% hint style="info" %}
Since BoxLang 1.12.x
{% endhint %}

Spread syntax uses `...` to expand arrays and structs into **function calls** and **literals**.

BoxLang also supports **struct shorthand keys**, which pair naturally with spread-heavy code.

## 📋 Table of Contents

* [Function call spread](spread-syntax.md#-function-call-spread)
* [Array literal spread](spread-syntax.md#-array-literal-spread)
* [Struct literal spread](spread-syntax.md#-struct-literal-spread)
* [Struct shorthand keys](spread-syntax.md#-struct-shorthand-keys)
* [Spread-only bracket literals](spread-syntax.md#-spread-only-bracket-literals)
* [Merge precedence](spread-syntax.md#-merge-precedence)
* [Common errors](spread-syntax.md#-common-errors)

## 🚀 Function call spread

Use spread in a function call to expand an array as positional arguments or a struct as named arguments.

### Spread an array into positional arguments

```js
function add( a, b, c ) {
    return a + b + c
}

args = [ 1, 2, 3 ]
result = add( ...args ) // 6
```

### Spread a struct into named arguments

```js
function greet( first, last ) {
    return "Hello, " & first & " " & last
}

person = { first: "John", last: "Doe" }
result = greet( ...person ) // "Hello, John Doe"
```

### Inline literals

```js
result = add( ...[ 10, 20, 30 ] )
result = greet( ...{ first: "Jane", last: "Smith" } )
```

### Works with more than plain function calls

Spread also works with:

* built-in functions
* member methods
* closures
* lambdas
* returned function expressions

```js
text = "a,b,c"
parts = text.listToArray( ...{ delimiter: "," } )

getGreeter = () => ( first, last ) => first & " " & last
result = getGreeter()( ...{ first: "Box", last: "Lang" } )
```

{% hint style="info" %}
Function-call spread uses the same behavior as `argumentCollection`. Arrays expand positionally. Structs expand by argument name.
{% endhint %}

## 📦 Array literal spread

Use spread inside an array literal to inline another array.

```js
left = [ 1, 2 ]
right = [ 5, 6 ]
merged = [ 0, ...left, 3, 4, ...right ]

println( merged ) // [ 0, 1, 2, 3, 4, 5, 6 ]
```

This works with inline values too.

```js
result = [ ...[ 1, 2 ], 3, 4 ]

println( result ) // [ 1, 2, 3, 4 ]
```

## 🧱 Struct literal spread

Use spread inside struct literals to merge keys from one or more sources.

### Unordered struct literals

```js
defaults = { host: "localhost", port: 5432, ssl: false }
overrides = { port: 5433 }

config = { ...defaults, ...overrides, ssl: true }

println( config )
// { "host": "localhost", "port": 5433, "ssl": true }
```

### Ordered struct literals

Ordered struct literals also support spread.

```js
base = [ one: 1, two: 2 ]
result = [ ...base, three: 3 ]

println( result ) // [ "one": 1, "two": 2, "three": 3 ]
```

### Spreading arrays into structs

When you spread an array into a struct literal, BoxLang uses **1-based numeric keys**.

```js
letters = [ "a", "b" ]
result = { ...letters }

// result[ 1 ] == "a"
// result[ 2 ] == "b"
```

That behavior also works with ordered structs.

```js
letters = [ "a", "b" ]
result = [ ...letters, tail: true ]
```

## ✨ Struct shorthand keys

Struct literals support JavaScript-style shorthand keys.

```js
host = "localhost"
port = 5432

config = { host, port }
```

That is equivalent to this:

```js
config = { "host": host, "port": port }
```

Shorthand preserves the identifier name exactly.

```js
fooBar = "value"
result = { fooBar }

println( result.keyList() )
// fooBar
```

You can mix shorthand, explicit pairs, and spread.

```js
host = "localhost"
defaults = { retries: 3 }

config = { host, ...defaults, debug: true }

println( config )
// { "host": "localhost", "retries": 3, "debug": true }
```

## 🧪 Spread-only bracket literals

Bracket literals that contain only spread entries are resolved at runtime.

### If the spread sources are arrays

The result is an array.

```js
values = [ 1, 2 ]
copy = [ ...values ]
```

### If the spread sources are structs

The result is an ordered struct.

```js
settings = { host: "localhost", port: 5432 }
ordered = [ ...settings ]
```

{% hint style="warning" %}
Spread-only bracket literals are an experimental edge case. Use explicit keyed members when you want to force ordered-struct syntax.
{% endhint %}

## 🔁 Merge precedence

Spread follows declaration order. Later entries win.

```js
left = { shared: "left", a: 1 }
right = { shared: "right", b: 2 }

result = { ...left, ...right, shared: "literal" }

// shared == "literal"
```

The same rule applies to ordered structs.

```js
left = [ shared: "left", a: 1 ]
right = [ shared: "right", b: 2 ]

result = [ ...left, ...right ]

println( result )
// [ "a": 1, "shared": "right", "b": 2 ]
```

## ⚠️ Common errors

### Non-spreadable values

You can only spread values that BoxLang can treat as arrays or structs for the target literal.

```js
// Invalid
result = [ ...123 ]
result = { ...42 }
```

### Null spread values

Spreading `null` into a literal is invalid.

```js
// Invalid
result = [ ...null ]
result = { ...null }
```

### Mixed spread-only bracket sources

A spread-only bracket literal must resolve consistently. Do not mix array and struct sources.

```js
arr = [ 1 ]
obj = { a: 2 }

// Invalid
result = [ ...arr, ...obj ]
```

## ✅ Summary

Use spread syntax when you want to:

* expand arguments into a function call
* merge arrays into arrays
* merge structs into structs
* build concise literals
* combine shorthand keys with explicit overrides

Use spread-only bracket literals carefully.\
Use explicit keyed members when you want clearer intent.

---
description: >-
  Unpack structs and arrays into variables with defaults, nesting, and rest
  captures.
icon: pallet-boxes
---

# Destructuring

{% hint style="info" %}
Since BoxLang 1.12.x
{% endhint %}

Destructuring lets you unpack values from **structs** and **arrays** into variables in a single expression.

It works in declarations like `var` and in assignments.

## 📋 Table of Contents

* [Struct destructuring](destructuring.md#-struct-destructuring)
* [Array destructuring](destructuring.md#-array-destructuring)
* [Declarations vs assignments](destructuring.md#-declarations-vs-assignments)
* [Defaults](destructuring.md#-defaults)
* [Nested patterns](destructuring.md#-nested-patterns)
* [Rest bindings](destructuring.md#-rest-bindings)
* [Scoped targets](destructuring.md#-scoped-targets)
* [Common errors](destructuring.md#-common-errors)

## 🧩 Struct destructuring

Struct destructuring binds keys by name.

```js
user = { name: "Luis", role: "admin" }
var { name, role } = user

println( name )
println( role )
```

You can also rename keys while destructuring.

```js
config = { host: "localhost", port: 5432 }
var { host, port: dbPort } = config

println( host )
println( dbPort )
```

While renaming a struct key, you can also place it into a different scope. (You may not use the `var`, `final`, or `static` keywords in these cases.)

```js
config = { host: "localhost", port: 5432 }
({ host: variables.host, port: request.dbPort } = config)

println( variables.host )
println( request.dbPort )
```

## 📚 Array destructuring

Array destructuring binds values by position.

```js
coords = [ 10, 20 ]
var [ x, y ] = coords

println( x )
println( y )
```

This also works with assignments.

```js
values = [ "BoxLang", "1.0" ]
[ productName, version ] = values
```

## 📝 Declarations vs assignments

Declarations work directly with `var`, `final`, or `static`.

```js
var { name, role } = user
var [ first, second ] = values
```

Non-declaration **struct** assignments must be wrapped in parentheses.

```js
({ name, role } = user)
({ token: authToken } = response)
```

Array assignments do not need the extra parentheses.

```js
[ first, second ] = values
```

{% hint style="info" %}
Use parentheses for struct assignments unless you are declaring with `var`, `final`, or `static`.
{% endhint %}

## 🎯 Defaults

Defaults let you provide a fallback when a value is not available.

### Struct defaults

Struct defaults apply when a key is missing.

```js
options = { size: "lg" }
var { size = "md", theme = "light", debug = false } = options

println( size ) // "lg"
println( theme ) // "light"
println( debug ) // false
```

### Array defaults

Array defaults apply when a slot is missing or `null`.

```js
values = [ 10, 20 ]
var [ first = 10, second = 0, third = 30 ] = values

println( first ) // 10
println( second ) // 20
println( third ) // 30
```

## 🪆 Nested patterns

You can destructure nested structs and arrays.

### Nested structs

```js
user = {
    name: "Luis",
    address: {
        city: "Houston"
    }
}

var { name, address: { city, zip = "77001" } } = user
println( name ) // Luis
println( city ) // Houston
println( zip ) // 77001
```

### Nested arrays

```js
points = [ [ 10, 20 ], [ 30, 40 ] ]
var [ [ x1, y1 ], [ x2, y2 ] ] = points

println( x1 ) // 10
println( y1 ) // 20
println( x2 ) // 30
println( y2 ) // 40
```

You can combine nesting with defaults.

```js
options = {}
var { coords: chartCoords = { x: 0, y: 0 } } = options

println( chartCoords ) // { x: 0, y: 0 }
```

## 🧺 Rest bindings

Rest bindings capture the remaining values.

### Struct rest

```js
data = { id: 1, name: "BoxLang", stable: true }
var { id, ...rest } = data

println( rest.keyList() ) // name, stable
```

### Array rest

```js
numbers = [ 1, 2, 3, 4, 5 ]
var [ first, ...rest ] = numbers

println( first )
println( rest )
```

Array destructuring also supports **middle rest**.

```js
numbers = [ 1, 2, 3, 4, 5, 6 ]
var [ first, ...middle, last ] = numbers

println( first )
println( middle )
println( last )
```

Short arrays still bind predictably.

```js
numbers = [ 1 ]
var [ first, ...middle, last ] = numbers

// first  = 1
// middle = []
// last   = null
```

{% hint style="warning" %}
A destructuring pattern can only contain one rest binding.
{% endhint %}

## 🎯 Scoped targets

You can explicitly destructure into scopes by renaming the binding target.

```js
result = { token: "abc123", userId: 42 }
({ token: request.authToken, userId: variables.currentUserId } = result)
```

This is useful when you want the source key and target variable to differ.

```js
payload = { id: 100 }
({ id: arguments.recordId } = payload)
```

{% hint style="warning" %}
Scoped targets are not allowed in `var`, `final`, or `static` destructuring declarations.
{% endhint %}

## ⚠️ Common errors

### Invalid shorthand keys

Some keys cannot use shorthand.

Use explicit renaming for quoted keys, spaced keys, or numeric keys.

```js
source = {
    "display name": "BoxLang",
    123: "numeric"
}

var {
    "display name": displayName,
    123: numericKey
} = source
```

### Wrong source type

Struct destructuring expects a struct-like value. Array destructuring expects an array-like value.

If a nested value does not match the pattern, BoxLang throws an error.

### Multiple rest bindings

A destructuring pattern can only contain one rest binding.

### Safer target syntax

Scoped targets must start with an explicit scope. Use `variables.foo`, `request.bar`, or another real scope.

## ✅ Summary

Destructuring gives you:

* concise assignments
* built-in renaming
* defaults
* nested extraction
* rest capture
* scoped targets when needed

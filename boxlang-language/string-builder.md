---
description: Fast, mutable string building with first-class BoxStringBuilder support, compile-time folding, and automatic runtime optimizations.
icon: bolt
---

# StringBuilder

> Available since **BoxLang 1.15.0**

String concatenation looks simple until it's on a hot path. Because Java (and therefore BoxLang) strings are **immutable**, joining two strings always creates a new object and copies both buffers. In a tight loop building a large payload—HTML fragments, JSON snippets, SQL strings, log lines—that cost compounds quickly.

BoxLang 1.15.0 addresses this with four complementary improvements that work together transparently:

1. **`BoxStringBuilder`** — a first-class, mutable string buffer type
2. **`&=` in-place append semantics** for builder values
3. **Compiler self-assignment rewrite** — `data = data & chunk` → `data &= chunk`
4. **Compile-time literal folding** & **auto-switching runtime concat strategy**

For most code you benefit automatically. For hot loops and large accumulators, reaching for `BoxStringBuilder` gives you full control.

---

## Why StringBuilder?

```js
// ❌ Every &= creates a NEW String and copies the old one
result = ""
for ( item in myList ) {
    result = result & item & ", "
}

// ✅ BoxStringBuilder appends in-place — one buffer, no copies
sb = sb{}
for ( item in myList ) {
    sb.append( item ).append( ", " )
}
result = sb.toString()
```

From 2 to 8 string segments in 100,000-iteration benchmarks:

- String concat is faster for exactly **2** strings
- Break-even is around **3** segments
- Beyond that, builder scales **~4.2×** better than plain concat
- BoxLang **automatically** uses a StringBuilder-backed path for **4 or more segments**

---

## Creating a BoxStringBuilder

There are three equivalent creation forms:

```js
// 1. BIF — optional initial value and initial buffer capacity
sbA = stringBuilderNew( "Hello", 128 )

// 2. Long literal form
sbB = stringbuilder{ "Hello" }

// 3. Short literal form (preferred)
sbC = sb{ "Hello" }
```

The `sb{ ... }` literal (and its `stringbuilder{ ... }` alias) accepts **any expression**, not just string literals. The expression is evaluated, converted to a string, and used to seed the buffer:

```js
sb{ "Hello #name#" }     // with interpolation
sb{ myVar }              // any variable
sb{ getGreeting() }      // function call
sb{ foo.bar() }          // method chain
sb{ 42 }                 // number — coerced to "42"
sb{}                     // empty buffer
```

{% hint style="info" %}
A variable named `sb` or `stringbuilder` is still just a variable when used as a plain identifier. The parser only treats them specially when immediately followed by braces: `sb{ ... }` or `stringbuilder{ ... }`.
{% endhint %}

```js
// These are ordinary variable assignments, NOT builder literals:
sb = "not a builder"
stringbuilder = "also not a builder"
```

---

## Member Method API

`BoxStringBuilder` uses **1-based positional indexing** throughout — consistent with BoxLang's array and string conventions.

### Mutation

| Method | Description |
|--------|-------------|
| `append( value )` | Append a value to the end of the buffer |
| `prepend( value )` | Insert a value at the beginning |
| `insert( position, value )` | Insert at a 1-based position |
| `delete( start, end )` | Delete characters from `start` to `end` inclusive (1-based) |
| `replace( start, end, value )` | Replace the range `[start, end]` with a new value |
| `reverse()` | Reverse the entire character sequence in place |
| `clear()` | Reset the buffer to empty |
| `trim()` | Remove leading and trailing whitespace |

### Inspection

| Method | Description |
|--------|-------------|
| `left( count )` | Return the leftmost `count` characters |
| `right( count )` | Return the rightmost `count` characters |
| `mid( start [, count ] )` | Substring from 1-based `start`, optional `count` |
| `find( substring [, start [, noCase ] ] )` | Find a substring, returns 1-based position or 0 |
| `contains( substring [, noCase ] )` | `true` if the buffer contains the substring |
| `startsWith( prefix )` | `true` if the buffer starts with the given prefix |
| `endsWith( suffix )` | `true` if the buffer ends with the given suffix |
| `length()` | Current length of the buffer in characters |
| `isEmpty()` | `true` if the buffer contains no characters |
| `toString()` | Materialize the buffer as an immutable Java `String` |

All mutation methods return **`this`** for fluent chaining:

```js
result = sb{ "Hello" }
    .append( ", " )
    .append( "World" )
    .append( "!" )
    .toString()
// → "Hello, World!"
```

### Examples

```js
// Building an HTML list
sb = sb{ "<ul>" }
for ( item in items ) {
    sb.append( "<li>" & item & "</li>" )
}
sb.append( "</ul>" )
writeOutput( sb )   // auto-coerced to String

// Reverse a string
reversed = sb{ "BoxLang" }.reverse().toString()   // "gnaLxoB"

// Find and check
buf = sb{ "Hello, World!" }
buf.find( "World" )          // 8 (1-based)
buf.startsWith( "Hello" )    // true
buf.contains( "xyz" )        // false

// Delete and replace (1-based)
buf = sb{ "Hello, World!" }
buf.delete( 1, 7 )          // removes "Hello, " → "World!"
buf.replace( 1, 5, "BoxLang" )  // → "BoxLang!"

// left / right / mid
buf = sb{ "BoxLang Rocks" }
buf.left( 7 )     // "BoxLang"
buf.right( 5 )    // "Rocks"
buf.mid( 9 )      // "Rocks"
buf.mid( 1, 3 )   // "Box"
```

---

## The `&=` Operator

When the left-hand side of `&=` is a `BoxStringBuilder` (or a raw `java.lang.StringBuilder`), BoxLang performs an **in-place append** instead of creating a new string:

```js
sb = sb{ "Hello" }
sb &= ", World"
sb &= "!"
writeOutput( sb )   // "Hello, World!"
```

This is semantically equivalent to `sb.append( ", World" ).append( "!" )` and avoids any allocation or reference change.

{% hint style="success" %}
Always prefer `&=` over `result = result & piece` for accumulators. In addition to the `BoxStringBuilder` optimization, the compiler can also rewrite the explicit self-concat form automatically (see [Compiler Optimizations](#compiler-optimizations)).
{% endhint %}

---

## Common Patterns

### Building large strings in loops

```js
// Ideal for CSV, HTML table rows, SQL IN clauses, log lines, etc.
sb = sb{}
for ( row in queryExecute( "SELECT id, name FROM users", [], { datasource: "app" } ) ) {
    sb.append( row.id )
      .append( "," )
      .append( row.name )
      .append( chr( 10 ) )   // newline
}
fileWrite( "/reports/users.csv", sb.toString() )
```

### Building JSON fragments

```js
sb = sb{ "[" }
for ( i = 1; i <= items.len(); i++ ) {
    if ( i > 1 ) sb.append( "," )
    sb.append( serializeJSON( items[ i ] ) )
}
sb.append( "]" )
jsonString = sb.toString()
```

### Stable reference identity

Because `&=` mutates `BoxStringBuilder` in place, any reference already pointing to the same buffer sees updated content:

```js
sb = sb{ "initial" }
ref = sb        // ref points to the same buffer

sb &= " content"

writeOutput( ref )   // "initial content" — same buffer, updated
```

### Template rendering

```js
function renderTemplate( string template, struct data ) {
    buf = sb{ template }
    for ( key in data ) {
        // replace {{key}} placeholders
        while ( buf.find( "{{#key#}}" ) ) {
            pos = buf.find( "{{#key#}}" )
            buf.replace( pos, pos + key.len() + 3, data[ key ] )
        }
    }
    return buf.toString()
}
```

---

## Compiler Optimizations

### Literal folding at compile time

Contiguous string literals in a concat chain are merged by the compiler **before the code runs**:

```js
// Source:
result = "foo" & "bar" & "baz" & "qux"

// Compiled as (zero runtime concat):
result = "foobarbazqux"
```

Mixed expressions are **partially folded** — adjacent literal segments are combined while dynamic segments are preserved:

```js
// Source:
result = "Hello, " & "Dear " & firstName & " " & lastName & "!"

// Compiled as:
result = "Hello, Dear " & firstName & " " & lastName & "!"
```

### Self-assignment rewrite

The compiler detects patterns where the explicit concat result is assigned back to the same target and rewrites them to the compound form:

```js
// Written as:
data = data & chunk

// Automatically rewritten to:
data &= chunk
```

This rewrite applies to identifier targets (`data`), dot-access targets (`variables.data`, `obj.field`), and array-access targets (`arr[1]`). When `data` is a `BoxStringBuilder`, the compound form triggers in-place append.

---

## Runtime Concat Strategy

At runtime, concat expressions are lowered depending on segment count:

| Segments | Strategy |
|----------|----------|
| 0–1 | Trivial return |
| 2–3 | Direct `String` concat (fastest for short chains) |
| 4 or more | `StringBuilder`-backed path with pre-computed initial capacity |

This automatic switching means you get optimal behavior with no manual tuning for expression chains and string interpolation:

```js
// 5 segments — automatically uses StringBuilder under the hood:
result = "Hello" & " " & firstName & " " & lastName

// Interpolation is treated the same way:
result = "Hello #firstName# #lastName#, your balance is #balance#."
```

Both are lowered to:

```js
sb = new StringBuilder( precomputedCapacity )
sb.append( "Hello " ).append( firstName ).append( " " ).append( lastName )
result = sb.toString()
```

---

## Java Interoperability

### Wrapping a Java StringBuilder

`BoxStringBuilder` member methods are **not injected** onto raw `java.lang.StringBuilder` instances to avoid mixing 1-based (BoxLang) and 0-based (Java) positional semantics. Wrap the Java instance first:

```js
// Create a raw Java StringBuilder
javaSB = createObject( "java", "java.lang.StringBuilder" ).init( "Hello" )

// Wrap it to get BoxStringBuilder semantics
boxSB = stringBuilderNew( javaSB )
boxSB.delete( 1, 5 )   // 1-based: removes "Hello"
writeOutput( boxSB )   // ""

// Direct Java calls still use Java semantics (0-based):
javaSB.delete( 2, 2 )  // Java no-op — start == end
```

### Silent coercion to String

Passing a `BoxStringBuilder` anywhere a `String` is required automatically calls `toString()`:

```js
sb = sb{ "Hello" }
writeOutput( sb )           // "Hello"
writeOutput( sb & " World")  // "Hello World"
len( sb )                   // 5 — works via coercion
find( "ell", sb )           // 2 — works via coercion
```

{% hint style="warning" %}
Dedicated StringBuilder BIF/member methods preserve the `BoxStringBuilder` instance and operate on it directly. Generic String BIFs will coerce the builder to a plain `String` first. Use the member method API when you want to stay in builder mode.
{% endhint %}

---

## Practical Guidance

**Use plain concat when:**
- You are joining just 2–3 values
- The code is not on a hot path or in a loop

**Use `BoxStringBuilder` when:**
- You append repeatedly inside loops
- You build large payloads incrementally (HTML, JSON, SQL, CSV, logs)
- You need stable reference identity while mutating content
- You want explicit control over buffer capacity

**Prefer compound concat:**
- Write `data &= piece` for mutable accumulation
- Legacy `data = data & piece` patterns are now automatically rewritten by the compiler in most cases

**Let the runtime handle it:**
- Any concat expression with 4+ segments is optimized automatically — no changes needed

---

## Performance Data

Benchmark setup: 100,000 iterations, comparing plain string grow versus StringBuilder append, segment count 2–8.

| Segments | Plain Concat | StringBuilder | Winner |
|----------|-------------|---------------|--------|
| 2 | ✅ Faster | — | `&` |
| 3 | ~Equal | ~Equal | Either |
| 4 | Slower | ✅ Faster | `sb` |
| 6 | Much slower | ✅ Faster | `sb` |
| 8 | ~4.2× slower | ✅ Faster | `sb` |

From 2 to 8 strings, concat growth is roughly **4.2× steeper** than builder growth. BoxLang uses the builder path automatically at 4+ segments.

---

## BIF Reference

### `stringBuilderNew( [initial], [capacity] )`

Creates a new `BoxStringBuilder`.

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `initial` | any | `""` | Initial value or a raw `java.lang.StringBuilder` to wrap |
| `capacity` | numeric | 16 | Initial buffer capacity in characters (hint, not a hard limit) |

```js
sb1 = stringBuilderNew()              // empty, default capacity
sb2 = stringBuilderNew( "Hello" )     // seeded with "Hello"
sb3 = stringBuilderNew( "Hello", 256) // seeded, with explicit capacity hint

// Wrapping an existing Java StringBuilder
javaSB = createObject( "java", "java.lang.StringBuilder" ).init( "Data" )
wrapped = stringBuilderNew( javaSB )  // shares the underlying buffer
```

### Literal Syntax

```js
sb{ expression }           // short form
stringbuilder{ expression } // long form
```

Both are parsed identically and create a `BoxStringBuilder` seeded with the evaluated expression.

---

{% hint style="success" %}
`BoxStringBuilder` is production-ready as of BoxLang 1.15.0. For the community announcement and technical deep-dive, see [StringBuilder in BoxLang: Fast Concatenation, Better &=, and Compile-Time Folding](https://community.ortussolutions.com/t/stringbuilder-in-boxlang-fast-concatenation-better-and-compile-time-folding/11123).
{% endhint %}

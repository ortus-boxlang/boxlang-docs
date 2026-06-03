---
description: A collection of unique elements with algebra operations
icon: layer-group
---

# Sets

BoxLang 1.14.0 introduces `BoxSet` as a brand-new first-class type, wrapping `java.util.Set` with full BoxLang integration including member-function dispatch, change listeners, metadata, and JSON serialization. Sets provide a powerful collection model for working with **unique values**, making them ideal for deduplication, membership testing, tagging systems, permissions, caching, filtering,  mathematics, and data comparison workflows.

Unlike arrays, sets enforce uniqueness by design and offer highly efficient lookup operations. BoxLang elevates sets to a first-class citizen with literal syntax, functional collection operations, and rich operator overloads for set algebra—including unions, intersections, differences, and symmetric differences—making complex data manipulation both expressive and concise.

Whether you're comparing datasets, managing unique identifiers, processing large collections, implementing access-control rules, or building recommendation and analytics engines, `BoxSet` provides a performant and elegant foundation for working with distinct values at scale.

Sets support three backing variants:

* `DEFAULT` — `HashSet`, fastest, no ordering
* `LINKED` — `LinkedHashSet`, preserves insertion order
* `SORTED` — `TreeSet`, natural ordering via `Compare.invoke`

```javascript
// Create a Set via function
s = setNew()

// Create a Set via literal syntax
s = set{ 1, 2, 3 }
```

{% hint style="success" %}
**Tip** Underneath the hood, all BoxLang Sets are based on the `java.util.Set` interface. So if you come from a Java background, Sets are untyped `HashSet`, `LinkedHashSet`, or `TreeSet` wrappers.
{% endhint %}

{% hint style="info" %}
**Java Set Interoperability**: Any Java `Set` implementation can be used with BoxLang set functions! BoxLang set BIFs and member functions work seamlessly with Java Sets.
{% endhint %}

## 📥 Creating Sets

BoxLang provides multiple ways to create Sets:

### setNew()

Creates a new Set with optional type, values, and case-sensitivity settings.

```javascript
// Empty default (hash) Set
s = setNew()

// Linked (insertion-ordered) Set seeded with values
s = setNew( type="linked", values=[ "c", "a", "b", "a" ] )

// Sorted Set
s = setNew( type="sorted", values=[ 9, 1, 5, 3 ] )

// Case-sensitive Set
s = setNew( values=[ "Hello", "hello", "HELLO" ], caseSensitive=true )
```

### setOf( ...values )

Creates a Set from positional varargs. Duplicates are automatically removed.

```javascript
s = setOf( 1, 2, 2, 3 )
// Result: Set with 3 elements: {1, 2, 3}
```

### Literal Syntax: set{ ... }

BoxLang supports a literal syntax for Sets using the `set` keyword followed by braces.

```javascript
// Default (hash) Set
s = set{ 1, 2, 3 }

// Empty Set
s = set{}

// Spread an array into a Set
arr = [ 3, 4, 5 ]
s = set{ 1, 2, ...arr }

// Spread another Set
other = set{ 2, 3 }
s = set{ 1, ...other, 4 }

// Spread a range
s = set{ ...(1..5) }
```

{% hint style="info" %}
The `set` token is matched as an identifier and the rule is parser-gated so it does not collide with variables named `set`. You can still use `set` as a variable name.
{% endhint %}

### From an Array

Convert an Array to a Set using the `.toSet()` member method.

```javascript
s = [ 1, 2, 2, 3 ].toSet()
s = [ "c", "a", "b", "a" ].toSet( "linked" )
s = [ 9, 1, 5, 3 ].toSet( "sorted" )
```

### From a String

Split a list-delimited string into a Set using `.listToSet()`.

```javascript
s = "a,b,c,a".listToSet()
s = "a|b|c|b".listToSet( delimiter="|", type="linked" )
```

### From a Query

Convert a Query to a Set of row structs.

```javascript
q = queryNew( "name,age", "varchar,integer", [ [ "Alice", 30 ], [ "Bob", 25 ] ] )
s = q.toSet()

// Get distinct column values as a Set
s = q.columnData( "name" ).toSet()
```

## 🔧 Set Types

BoxLang supports three Set variants:

| Type | Alias | Java Backing | Ordering |
|------|-------|--------------|----------|
| `default` | `hash` | `HashSet` | No ordering (fastest) |
| `linked` | `ordered` | `LinkedHashSet` | Preserves insertion order |
| `sorted` | `tree` | `TreeSet` | Natural ascending order |

```javascript
// Default - no ordering, fastest lookup
s = setNew()
s = set{ 1, 2, 3 }

// Linked - preserves insertion order
s = setNew( type="linked" )
s = setNew( type="linked", values=[ "c", "a", "b" ] )

// Sorted - elements kept in natural order
s = setNew( type="sorted", values=[ 9, 1, 5, 3 ] )
// toArray() produces: [1, 3, 5, 9]
```

## 🔑 Accessing Set Elements

Sets are **unordered** (except linked/sorted variants), so you don't access elements by index. Instead, you test membership or iterate.

### contains( value ) / has( value )

Test whether a value exists in the Set.

```javascript
s = [ 1, 2, 3 ].toSet()

s.contains( 2 )    // true
s.has( 2 )         // true (alias)
s.contains( 99 )   // false
```

### Iteration

```javascript
s = setOf( "apple", "banana", "cherry" )

// for loop
for ( item in s ) {
    println( item )
}

// each() closure
s.each( (item) => {
    println( item )
} )
```

## 📚 Set Built-In Functions

BoxLang provides a comprehensive set of Set BIFs organized by functionality. All Set BIFs can be called as member methods on Set objects.

### 🔨 Creation Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `setNew()` | Create new Set | `setNew( type="linked" )` |
| `setOf()` | Create from varargs | `setOf( 1, 2, 3 )` |

### ➕ Mutation Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `boxSetAdd()` | Add element | `boxSetAdd( set, value )` |
| `boxSetAddAll()` | Add multiple elements | `boxSetAddAll( set, collection )` |
| `boxSetRemove()` | Remove element | `boxSetRemove( set, value )` |
| `boxSetRemoveAll()` | Remove multiple elements | `boxSetRemoveAll( set, collection )` |
| `boxSetRetainAll()` | Keep only specified elements | `boxSetRetainAll( set, collection )` |
| `boxSetClear()` | Remove all elements | `boxSetClear( set )` |

### 🔍 Query Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `boxSetContains()` | Test membership | `boxSetContains( set, value )` → `true` |
| `boxSetContainsAll()` | Test all members | `boxSetContainsAll( set, collection )` → `true` |
| `boxSetIsEmpty()` | Check if empty | `boxSetIsEmpty( set )` → `false` |
| `boxSetEquals()` | Compare Sets | `boxSetEquals( set1, set2 )` → `true` |
| `boxSetIsSubsetOf()` | Test subset | `boxSetIsSubsetOf( a, b )` → `true` |
| `boxSetIsSupersetOf()` | Test superset | `boxSetIsSupersetOf( a, b )` → `true` |
| `boxSetIsDisjointFrom()` | Test no overlap | `boxSetIsDisjointFrom( a, b )` → `true` |

### 🔀 Algebra Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `boxSetUnion()` | Combine all elements | `boxSetUnion( a, b )` |
| `boxSetIntersection()` | Common elements | `boxSetIntersection( a, b )` |
| `boxSetDifference()` | Elements in A not in B | `boxSetDifference( a, b )` |
| `boxSetSymmetricDifference()` | Elements in either, not both | `boxSetSymmetricDifference( a, b )` |

### 🔄 Functional Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `boxSetEach()` | Iterate each element | `boxSetEach( set, callback )` |
| `boxSetMap()` | Transform elements | `boxSetMap( set, callback )` |
| `boxSetFilter()` | Filter elements | `boxSetFilter( set, callback )` |
| `boxSetReject()` | Reject elements | `boxSetReject( set, callback )` |
| `boxSetReduce()` | Reduce to single value | `boxSetReduce( set, callback, init )` |
| `boxSetEvery()` | Test all elements | `boxSetEvery( set, callback )` → `true` |
| `boxSetSome()` | Test any element | `boxSetSome( set, callback )` → `true` |
| `boxSetNone()` | Test no elements match | `boxSetNone( set, callback )` → `true` |
| `boxSetFind()` | Find first match | `boxSetFind( set, callback )` |

### 📏 Information Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `boxSetSize()` | Get element count | `boxSetSize( set )` → `5` |

### 🔄 Conversion Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `boxSetToArray()` | Convert to Array | `boxSetToArray( set )` → `[1, 2, 3]` |
| `boxSetToList()` | Convert to list string | `boxSetToList( set, "-" )` → `"1-2-3"` |

{% hint style="success" %}
**Complete Reference**: For detailed documentation of each function, visit the [Set BIF Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/set).
{% endhint %}

## ⚙️ Member Functions

All Set BIFs can be called as member functions on Set objects for cleaner, more fluent code:

```javascript
s = setNew( type="linked", values=[ "apple", "banana", "cherry" ] )

// Basic operations
s.size()              // 3
s.len()               // 3 (alias)
s.length()            // 3 (alias)
s.isEmpty()           // false

// Mutation
s.add( "date" )
s.append( "elderberry" )    // alias for add
s.addAll( [ "fig", "grape" ] )
s.remove( "apple" )
s.delete( "banana" )        // alias for remove
s.removeAll( [ "cherry", "date" ] )
s.retainAll( [ "elderberry", "fig" ] )
s.clear()

// Query
s.contains( "fig" )         // true
s.has( "fig" )              // true (alias)
s.containsAll( [ "fig", "grape" ] )
s.equals( otherSet )
s.isSubsetOf( otherSet )
s.isSupersetOf( otherSet )
s.isDisjointFrom( otherSet )

// Algebra
union = s.union( otherSet )
intersection = s.intersection( otherSet )
difference = s.difference( otherSet )
symdiff = s.symmetricDifference( otherSet )

// Functional
s.each( (item) => {
    println( item )
} )
doubled = s.map( (item) -> item.len() )
longNames = s.filter( (item) -> item.len() > 5 )
total = s.reduce( (acc, item) -> acc + item.len(), 0 )
allLong = s.every( (item) -> item.len() > 3 )
anyShort = s.some( (item) -> item.len() < 4 )
noneEmpty = s.none( (item) -> item.len() == 0 )
found = s.find( (item) -> item.startsWith("a") )

// Conversion
arr = s.toArray()
list = s.toList( "-" )
```

## 🔀 Set Algebra

Sets support four fundamental algebra operations:

### Union

Combines all unique elements from both Sets.

```javascript
a = [ 1, 2, 3 ].toSet()
b = [ 3, 4, 5 ].toSet()

u = a.union( b )
// Result: {1, 2, 3, 4, 5}
```

### Intersection

Returns elements common to both Sets.

```javascript
a = [ 1, 2, 3, 4 ].toSet()
b = [ 3, 4, 5, 6 ].toSet()

i = a.intersection( b )
// Result: {3, 4}
```

### Difference

Returns elements in the first Set that are not in the second.

```javascript
a = [ 1, 2, 3, 4 ].toSet()
b = [ 3, 4, 5 ].toSet()

d = a.difference( b )
// Result: {1, 2}
```

### Symmetric Difference

Returns elements in either Set but not in both.

```javascript
a = [ 1, 2, 3 ].toSet()
b = [ 3, 4, 5 ].toSet()

x = a.symmetricDifference( b )
// Result: {1, 2, 4, 5}
```

## 🔣 Operators

Set algebra is also available via overloaded operators:

```javascript
a = set{ 1, 2, 3 }
b = set{ 3, 4, 5 }

union     = a + b      // {1, 2, 3, 4, 5}
diff      = a - b      // {1, 2}
intersect = a * b      // {3, 4}
symdiff   = a ^ b      // {1, 2, 4, 5}
```

The right-hand operand is accepted "loose" (Array, list-delimited string, Range, etc.) when either operand is a Set.

```javascript
s = setOf( 1, 2, 3 )
result = s + [ 4, 5 ]        // Set + Array
result = s * "3,4,5"         // Set + list string
result = s - (1..2)          // Set + Range
```

{% hint style="info" %}
When neither operand is a Set, these operators fall through to standard math: `2 + 3 = 5`, `5 - 2 = 3`, `4 * 3 = 12`, `2 ^ 3 = 8`.
{% endhint %}

Compound operators are also supported:

```javascript
a = set{ 1, 2, 3 }
a *= set{ 2, 3, 4 }
// a is now {2, 3}
```

## 🔄 Functional Programming

Sets support a full functional programming pipeline:

```javascript
s = [ 1, 2, 3, 4, 5 ].toSet()

// map - transform each element
doubled = s.map( v -> v * 2 )
// Result: {2, 4, 6, 8, 10}

// filter - keep matching elements
evens = s.filter( v -> v % 2 == 0 )
// Result: {2, 4}

// reject - remove matching elements
odds = s.reject( v -> v % 2 == 0 )
// Result: {1, 3, 5}

// reduce - combine to single value
total = s.reduce( (acc, v) -> acc + v, 0 )
// Result: 15

// every - test all elements
allPositive = s.every( v -> v > 0 )
// Result: true

// some - test any element
hasLarge = s.some( v -> v > 4 )
// Result: true

// none - test no elements match
noneNegative = s.none( v -> v < 0 )
// Result: true

// find - first matching element
firstLarge = s.find( v -> v > 2 )
// Result: 3 (or another value >= 3)
```

## 🔄 Conversion

### Set to Array

```javascript
s = setNew( type="linked", values=[ "a", "b", "c" ] )
arr = s.toArray()
// Result: ["a", "b", "c"]
```

### Set to List

```javascript
s = setNew( type="linked", values=[ "a", "b", "c" ] )
list = s.toList()
// Result: "a,b,c"

list = s.toList( "-" )
// Result: "a-b-c"
```

### Array to Set

See [Arrays](arrays.md) for the `.toSet()` member method.

```javascript
arr = [ 1, 2, 2, 3 ]
s = arr.toSet()
// Result: Set{1, 2, 3}
```

## 🔤 Case Sensitivity

By default, Sets are **case-insensitive** for string elements. Different cases of the same string are treated as duplicates.

```javascript
s = setNew( values=[ "Hello", "hello", "HELLO" ] )
s.size()    // 1

s.contains( "hElLo" )    // true
```

To treat different cases as distinct elements, pass `caseSensitive=true`:

```javascript
s = setNew( values=[ "Hello", "hello", "HELLO" ], caseSensitive=true )
s.size()    // 3

s.contains( "Hello" )    // true
s.contains( "hello" )    // false
```

{% hint style="info" %}
**Numeric normalization**: Case sensitivity does not affect numeric normalization. `1`, `1L`, and `1.0` are always treated as the same numeric value regardless of case sensitivity setting.
{% endhint %}

## 🔧 Java Interop

A `java.util.Set` passed to a Set-typed BIF argument is **wrapped** (not copied) so that mutations propagate back to the underlying Java object — same contract as `Array` wrapping a Java `List`.

```javascript
import java.util.HashSet

javaSet = createObject( "java", "java.util.HashSet" ).init()
javaSet.add( "a" )
javaSet.add( "b" )

// Wrap the Java Set
s = javaSet castAs "Set"

// Mutations propagate
s.add( "c" )
javaSet.contains( "c" )    // true
```

### struct.keySet() and struct.valueSet()

Structs provide methods to extract keys or values as Sets:

```javascript
data = { name: "Luis", age: 42, email: "x@y.z" }

keys = data.keySet()
// Result: Set of struct keys

values = data.valueSet()
// Result: Set of struct values (deduplicated)
```

The keySet inherits case-sensitivity from the parent struct.

## 📦 JSON Serialization

Sets serialize to JSON arrays:

```javascript
s = setNew( type="linked", values=[ "a", "b", "c" ] )
json = jsonSerialize( s )
// Result: ["a","b","c"]
// or the member method
json = s.toJson()
```

## 🛡️ Unmodifiable Sets

Sets can be made immutable:

```javascript
s = setNew( values=[ 1, 2, 3 ] )
frozen = s.toUnmodifiable()

frozen.size()           // 3
frozen.add( 4 )         // throws UnmodifiableException

// Thaw to get a fresh mutable copy
thawed = frozen.toModifiable()
thawed.add( 4 )         // works
```

{% hint style="success" %}
**Tip**: Check out all the [Set BIF reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/set) and [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) for more capabilities.
{% endhint %}

## 🔗 Related Documentation

{% content-ref url="arrays.md" %}
[arrays.md](arrays.md)
{% endcontent-ref %}

{% content-ref url="structures.md" %}
[structures.md](structures.md)
{% endcontent-ref %}

{% content-ref url="ranges.md" %}
[ranges.md](ranges.md)
{% endcontent-ref %}

{% content-ref url="queries.md" %}
[queries.md](queries.md)
{% endcontent-ref %}

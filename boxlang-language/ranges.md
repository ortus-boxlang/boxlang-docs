---
description: Lazy, typed, iterable intervals with exclusive boundaries and custom stepping
icon: ruler-horizontal
---

# Ranges

BoxLang **Ranges** are first-class interval objects supporting lazy iteration, multiple element types, exclusive boundaries, custom stepping, and the `IRangeable` interface for custom types. Ranges are **not arrays** — they're lightweight objects that generate values on demand.

## 🚀 The Basics

### Range as a First-Class Object

Ranges are created with the `..` operator and produce a `Range` object:

```js
myRange = 1..5
// Range object — NOT immediately an array
```

Ranges are iterable and seamlessly coerce to arrays when needed:

```js
result = arrayToList( 1..5, "," )  // "1,2,3,4,5"
result = arrayLen( 1..10 )         // 10
```

But they're **not arrays** — they're lightweight objects that generate values on demand. This means huge and even infinite ranges are cheap to create and use.

## 🔢 Supported Types

### Integers and Decimals

Integer and decimal ranges work naturally with automatic direction detection:

```js
1..5             // 1, 2, 3, 4, 5
3.5..1.5         // 3.5, 2.5, 1.5 (descending auto-detected)
(0..1).step(0.25) // 0, 0.25, 0.50, 0.75, 1.00
```

### Characters

Single-character strings produce character ranges:

```js
result = []
for( c in "a".."e" ) {
    result.append( c )
}
// ["a", "b", "c", "d", "e"]

// Descending
for( c in "z".."v" ) { }
// z, y, x, w, v
```

### DateTime

DateTime ranges iterate by day by default and support unit-based stepping:

```js
start = createDate( 2024, 1, 1 )
end = createDate( 2024, 1, 5 )
r = start..end
arrayLen( r )  // 5

// Step by month
r = (createDate(2024,1,15)..createDate(2024,6,15)).step(1, "month")
arrayLen( r )  // 6

// Step by week
r = (createDate(2024,1,1)..createDate(2024,1,29)).step(1, "week")
arrayLen( r )  // 5 (Jan 1, 8, 15, 22, 29)

// Contains with string dates
r = createDate(2024,1,1)..createDate(2024,1,31)
r.contains( "2024-01-15" )  // true
r.contains( "2024-02-01" )  // false
```

### Any Comparable Type (Contains-Only)

Any two values of the same type that are naturally comparable can form a range — even if there's no way to iterate between them. Multi-character strings are a good example: they have a well-defined lexicographic ordering, so `contains()` works, but there's no natural "next" value after `"foo"`:

```js
r = "aaa".."zzz"

r.contains( "foo" )    // true — lexicographically between "aaa" and "zzz"
r.contains( "hello" )  // true
r.contains( "aaa" )    // true (inclusive boundary)
r.contains( "zzz" )    // true (inclusive boundary)
r.contains( "000" )    // false — comes before "aaa"

r.isIterable()  // false — can't step from "aaa" to "aab" automatically
r.isBounded()   // true
```

This works with any Java class that implements `Comparable` — including JDK types:

```js
import java.time.Duration

// A range representing "between 5 minutes and 2 hours"
r = Duration.ofMinutes( 5 )..Duration.ofHours( 2 )

r.contains( Duration.ofMinutes( 30 ) )  // true
r.contains( Duration.ofHours( 3 ) )     // false — exceeds 2 hours
r.contains( Duration.ofMinutes( 5 ) )   // true (boundary)

r.isIterable()  // false
```

Attempting to iterate a non-iterable range throws an error:

```js
for( s in "aaa".."zzz" ) { }  // ERROR: range is not iterable
```

This pattern works for any type with a natural ordering — use it as a bounds check without needing to enumerate values.

### Custom Types via `IRangeable`

Any BoxLang or Java class can participate in ranges by implementing the `ortus.boxlang.runtime.types.IRangeable` interface. See [Custom Rangeable Types](#custom-rangeable-types-irangeable) below for complete details.

## 🌐 Unbounded and Half-Bounded Ranges

Ranges can be open on one or both ends:

```js
1..      // open end — no upper bound
..5      // open start — no lower bound
..       // fully open — contains everything non-null
```

Half-bounded ranges are lazy — you can iterate them with a break condition:

```js
result = []
for( i in 1.. ) {
    result.append( i )
    if( i == 5 ) break
}
// [1, 2, 3, 4, 5]
```

Open-start and fully-open ranges cannot be iterated (no starting point):

```js
for( i in ..5 ) {}  // ERROR: not iterable
for( i in .. ) {}   // ERROR: not iterable
```

But they still support `contains()`:

```js
(1..).contains( 999 )       // true
(..5).contains( 3 )         // true
(..).contains( "anything" ) // true
(..).contains( null )       // false (null is never in any range)
```

### Typed Unbounded Ranges

A fully unbounded range (`..`) contains everything non-null by default. Use `.type()` to constrain it to a specific type — leveraging BoxLang's loose casting system:

```js
(..).contains( "foo" )               // true (no type constraint)
(..).type("number").contains( "foo" ) // false (wrong type)
(..).type("number").contains( "5" )   // true (coercible to number)
(..).type("integer").contains( 5.5 )  // false (not a whole integer)
(..).type("integer").contains( "5" )  // true (coercible to integer)
```

Any BoxLang type name works — string, numeric, integer, boolean, date, array, struct, etc. For custom classes, the `instanceof` operator is used:

```js
(..).type("Widget").contains( myWidget )  // true if myWidget instanceof Widget
```

For exact Java class matching with no coercion, pass a Class reference directly:

```js
import java:java.lang.Number
(..).type( Number ).contains( 42 )    // true — Integer is a Number
(..).type( Number ).contains( "5" )   // false — strict instanceof, no coercion
```

## 🔀 Exclusive Boundaries

Four boundary modes via operators:

```js
1..5     // inclusive both: 1, 2, 3, 4, 5
1>..5    // exclude start: 2, 3, 4, 5
1..<5    // exclude end:   1, 2, 3, 4
1>..<5   // exclude both:  2, 3, 4
```

These affect both iteration and `contains()`:

```js
r = 1>..5
r.contains( 1 )  // false
r.contains( 2 )  // true
r.contains( 5 )  // true
```

## 🪜 Custom Stepping

The `step()` method returns a new range (copy-on-write) with a custom step:

```js
arrayToList( (1..10).step(2), "," )   // "1,3,5,7,9"
arrayToList( (10..1).step(-3), "," )  // "10,7,4,1"
arrayToList( (1..10).step(3), "," )   // "1,4,7,10"
```

Unit-based stepping for DateTime and custom `IRangeable` types:

```js
(start..end).step( 1, "month" )
(start..end).step( 1, "week" )
(start..end).step( 1, "year" )
```

## 🌊 Lazy Iteration and Streaming

Ranges are never materialized into memory unless you ask. This means huge and even infinite ranges are cheap:

```js
// This does NOT allocate 100 billion integers
for( i in 1..100_000_000_000 ) {
    result = i
    break  // instant
}
```

Full Java Stream API integration:

```js
result = (1..100_000_000_000).stream().limit( 5 ).toList()
// [1, 2, 3, 4, 5]

result = (1..).stream().limit( 5 ).toList()
// [1, 2, 3, 4, 5]
```

Use `map`, `filter`, `takeWhile`, `anyMatch`, `limit`, and all other stream operations.

## 🔍 Contains Semantics

### Simple ranges (step = 1, no unit): Bounds Check

```js
r = 1..10
r.contains( 5 )         // true
r.contains( 0 )         // false
r.contains( "5" )       // true (numeric string coerced)
r.contains( "hello" )   // false (incompatible type)
r.contains( null )      // false (always)
```

### Stepped ranges (step > 1 or unit): Step-Reachability Check

When a range has a custom step, `contains()` verifies the value is actually reachable by the stepper — not just within bounds:

```js
r = (1..10).step(3)  // produces: 1, 4, 7, 10
r.contains( 4 )   // true  (reachable)
r.contains( 5 )   // false (within bounds but NOT reachable)
r.contains( 11 )  // false (out of bounds)
```

This follows the Python/Kotlin convention where a stepped range represents a discrete set.

For half-bounded stepped ranges, the iteration stops once the target is exceeded — so this is safe and terminates:

```js
(1..).step(3).contains( 7 )   // true (1, 4, 7 ✓)
(1..).step(3).contains( 5 )   // false (1, 4, 7 — passed 5 without hitting it)
```

### Non-iterable ranges: Always Bounds Check

Ranges that cannot be iterated (no start value, or no stepper) always fall back to a simple bounds check:

```js
r = "aaa".."zzz"   // not iterable
r.contains( "foo" ) // true (between "aaa" and "zzz" lexicographically)
```

### Range-in-Range Contains

You can check if an entire range fits within another:

```js
outer = 1..10
outer.contains( 3..7 )    // true
outer.contains( 5..15 )   // false (exceeds high end)
outer.contains( 1>..10 )  // true (exclusive inner fits in inclusive outer)
outer.contains( .. )       // false (unbounded inner can't fit in bounded outer)

// Unbounded outer contains anything
(..).contains( 1..100 )   // true
(1..).contains( 5.. )     // true
(5..).contains( 1..3 )    // false (inner starts below outer)
```

## 🗜️ Clamping Values

The `clamp()` method snaps a value to the closest boundary if it falls outside the range:

```js
(1..10).clamp( 11 )   // 10 — above high, snapped down
(1..10).clamp( 0 )    // 1  — below low, snapped up
(1..10).clamp( 5 )    // 5  — within bounds, unchanged
(1..10).clamp( "7" )  // 7  — coerced and returned
```

Half-bounded ranges snap to the one bound that exists:

```js
(5..).clamp( 2 )      // 5   — snapped up to low
(5..).clamp( 999 )    // 999 — no upper bound
(..10).clamp( 50 )    // 10  — snapped down to high
(..10).clamp( -100 )  // -100 — no lower bound
```

Fully unbounded ranges just type-check and return the value:

```js
(..).clamp( 42 )                     // 42
(..).type("numeric").clamp( "5" )    // 5 (coerced)
(..).type("numeric").clamp( "foo" )  // ERROR — incompatible type
```

## 📍 Position Checks

Check whether a value falls before or after a range without getting a full `contains()` answer:

```js
r = 1..10
r.isValueBefore( -3 )   // true — below the low bound
r.isValueBefore( 5 )    // false — inside the range
r.isValueAfter( 50 )    // true — above the high bound
r.isValueAfter( 5 )     // false — inside the range
```

Exclusive boundaries are respected:

```js
r = 5>..10
r.isValueBefore( 5 )    // true — 5 is excluded from the range
```

Incompatible types return false (same as `contains()`):

```js
(1..10).isValueBefore( "foo" )  // false
('a'..'z').isValueAfter( 42 )   // false
```

## 📋 Member Methods

### Query Methods

| Method | Description |
|--------|-------------|
| `contains(value)` | Check if value (or inner range) is within this range |
| `isValueBefore(value)` | True if value is before the low boundary |
| `isValueAfter(value)` | True if value is after the high boundary |
| `isEmpty()` | True if iteration would produce zero elements |
| `isAscending()` | True if step is positive |
| `isIterable()` | True if the range can be iterated |
| `isBounded()` | True if both start and end are present |
| `isUnbounded()` | True if both start and end are absent |
| `isHalfBounded()` | True if exactly one bound is present |
| `hasFrom()` / `hasTo()` | Check individual bounds |

### Accessors

| Method | Description |
|--------|-------------|
| `getFrom()` / `getTo()` | Get bound values |
| `getStep()` | Get current step value |

### Transformation Methods

| Method | Description |
|--------|-------------|
| `clamp(value)` | Snap value to the closest boundary if out of bounds |
| `type(typeName)` | New range constrained to a BoxLang type (uses casters for coercion) |
| `type(class)` | New range constrained to an exact Java class (strict instanceof) |
| `step(n)` | New range with numeric step |
| `step(n, unit)` | New range with unit-based step |
| `asc()` | Force ascending (empty if already descending) |
| `desc()` | Force descending (empty if already ascending) |

### Conversion Methods

| Method | Description |
|--------|-------------|
| `toArray()` | Materialize to array (requires bounded + iterable) |
| `stream()` | Get a Java Stream for functional pipelines |
| `toString()` | Human-readable representation |
| `equals(other)` | Structural equality (bounds, step, exclusivity) |

## ✅ Empty Ranges and Truthiness

Ranges are truthy if non-empty, falsy if empty:

```js
if( 1..5 ) { }           // truthy
if( (1..5).step(-1) ) { } // falsy (positive range, negative step = empty)
if( (5..1).asc() ) { }   // falsy (descending range forced ascending = empty)
if( 1>..<1 ) { }         // falsy (exclude both endpoints of single value = empty)
```

## 🔢 Operator Precedence

Arithmetic binds tighter than the range operator:

```js
1 + 3 .. 5 * 2  // evaluates as (1+3)..(5*2) = 4..10
```

You can use any expression as operands:

```js
abs(-3)..abs(-7)                    // 3..7
getStart()..getEnd()                // function calls
s.low..s.high                       // struct access
arr[1]..arr[2]                      // array index
(x ?: 1)..(x ?: 5)                  // null coalescing
" 2 ".trim().." 6 ".trim()          // chained methods
(x ? 1 : 10)..(x ? 5 : 20)          // ternary
```

## 📝 Copy-on-Write Semantics

All modifier methods return new Range instances — the original is never mutated:

```js
original = 1..10
stepped = original.step(3)
original.getStep()  // 1 (unchanged)
stepped.getStep()   // 3
```

## ⚠️ Error Cases

These throw runtime errors:

```js
[1,2]..[3,4]    // arrays can't form ranges
{a:1}..{b:2}    // structs can't form ranges
1.."hello"      // incompatible types
(() => 1)..(() => 2)  // closures can't form ranges

(..5).toArray()       // can't materialize without a start
("aaa".."zzz").toArray()  // not iterable (no stepper)
(1..10).step(5, "minutes") // unit stepping not supported on plain numbers
```

## 🧩 Custom Rangeable Types: `IRangeable`

Any Java or BoxLang class can become rangeable by implementing `ortus.boxlang.runtime.types.IRangeable`. You need to provide:

* `rangeAdvance( step )` — Return a new instance advanced by `step` positions
* `rangeCompare( other )` — Compare to another instance (negative = less, 0 = equal, positive = greater)
* `rangeCoerce( val )` — Convert arbitrary values to your type for `contains()` checks
* `rangeStepFromUnit( amount, unit )` — (Optional) Convert a unit-based step to a numeric step
* `rangeUnitStepper( unit )` — (Optional) Return a custom stepper closure for non-uniform stepping

### Example 1: Fibonacci — Infinite Non-Linear Sequences

Not all sequences advance linearly. The Fibonacci sequence is a perfect example — each value depends on the previous two, so `rangeAdvance(1)` produces values that grow exponentially. BoxLang's range system handles this naturally.

```js
class Fib implements="java:ortus.boxlang.runtime.types.IRangeable" {
    property name="prev" type="integer" default=0
    property name="current" type="integer" default=1

    // Advance by N steps in the Fibonacci sequence
    function rangeAdvance( step ) {
        var result = this
        for( var i = 1; i <= step; i++ ) {
            result = new Fib(
                prev: result.getCurrent(),
                current: result.getPrev() + result.getCurrent()
            )
        }
        return result
    }

    // Compare by current value (defines ordering)
    function rangeCompare( other ) {
        return variables.current - other.getCurrent()
    }

    // Convert integers to Fib instances for contains() checks
    function rangeCoerce( val ) {
        if( val instanceof "Fib" ) return val
        if( isNumeric( val ) ) return new Fib( current: int(val) )
        return null
    }
}
```

**Usage:**

```js
// First 10 Fibonacci numbers
(new Fib()..).stream().limit(10).map( .getCurrent() ).toList()
// [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

// Is this a Fibonacci number?
(new Fib()..).contains( 13 )   // true — 13 is a Fibonacci number
(new Fib()..).contains( 14 )   // false — 14 is not
(new Fib()..).contains( 144 )  // true
```

### Example 2: Roman Numerals

A Roman numeral class that stores an integer internally and converts to/from Roman notation. This demonstrates iteration, stepping, and coercion-based contains.

```js
class Roman implements="java:ortus.boxlang.runtime.types.IRangeable" {
    property name="value" type="integer" default=0

    static {
        VALUES = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        SYMBOLS = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    }

    // Construct from integer or Roman numeral string
    function init( input ) {
        variables.value = isNumeric( input ) ? int( input ) : static.fromRoman( input )
        return this
    }

    // Parse a Roman numeral string into its integer value
    static function fromRoman( s ) {
        s = uCase( s )
        return static.VALUES.reduce( ( acc, val, idx ) => {
            var sym = static.SYMBOLS[ idx ]
            while( mid( s, acc.pos, sym.len() ) == sym ) {
                acc.result += val
                acc.pos += sym.len()
            }
            return acc
        }, { result: 0, pos: 1 } ).result
    }

    // Convert an integer to its Roman numeral string representation
    static function toRoman( num ) {
        return static.VALUES.reduce( ( result, val, idx ) => {
            var count = int( num / val )
            num -= count * val
            return result & repeatString( static.SYMBOLS[ idx ], count )
        }, "" )
    }

    function toString() { return static.toRoman( variables.value ) }
    function rangeAdvance( step ) { return new Roman( variables.value + step ) }
    function rangeCompare( other ) { return variables.value - other.getValue() }

    // Convert integers or Roman numeral strings to Roman instances
    function rangeCoerce( val ) {
        if( val instanceof "Roman" ) return val
        if( isNumeric( val ) ) return new Roman( val )
        if( isSimpleValue( val ) ) return new Roman( val )
        return null
    }
}
```

**Usage:**

```js
result = []
for( r in new Roman("I")..new Roman("X") ) {
    result.append( r.toString() )
}
// ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

// Contains with multiple input types
range = new Roman("I")..new Roman("C")  // 1 to 100
range.contains( new Roman("V") )   // true
range.contains( 5 )                // true
range.contains( "V" )              // true
```

### Example 3: Musical Notes with Unit Stepping

This is where it gets interesting. A Musical Note class that supports chromatic, whole-step, major-third, octave, major scale, and minor scale stepping — plus stream composition for infinite sequences.

```js
class Note implements="java:ortus.boxlang.runtime.types.IRangeable" {
    property name="midi" type="integer" default=60

    static {
        NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        MAJOR = [2, 2, 1, 2, 2, 2, 1]
        MINOR = [2, 1, 2, 2, 1, 2, 2]
    }

    function init( input ) {
        variables.midi = isNumeric( input ) ? int( input ) : static.parseName( input )
        return this
    }

    static function parseName( name ) {
        name = uCase( name )
        var hasSharp = name.len() > 2 && mid( name, 2, 1 ) == "#"
        var notePart = hasSharp ? left( name, 2 ) : left( name, 1 )
        var octave = int( right( name, name.len() - notePart.len() ) )
        var idx = arrayFind( static.NOTES, notePart )
        return ( octave + 1 ) * 12 + idx - 1
    }

    function toString() {
        return static.NOTES[ variables.midi mod 12 + 1 ] & ( int( variables.midi / 12 ) - 1 )
    }

    function rangeAdvance( step ) { return new Note( variables.midi + step ) }
    function rangeCompare( other ) { return variables.midi - other.getMidi() }

    function rangeCoerce( val ) {
        if( val instanceof "Note" ) return val
        if( isNumeric( val ) ) return new Note( val )
        if( isSimpleValue( val ) ) return new Note( val )
        return null
    }

    // Convert named units to a fixed semitone count
    function rangeStepFromUnit( amount, unit ) {
        switch( unit ) {
            case "chromatic": return amount
            case "whole": return amount * 2
            case "third": return amount * 4
            case "octave": return amount * 12
        }
        throw( message: "Unsupported unit: " & unit )
    }

    // Return a closure for non-uniform scale stepping (major/minor)
    function rangeUnitStepper( unit ) {
        if( unit != "major" && unit != "minor" ) return null
        var root = variables.midi
        var intervals = ( unit == "major" ) ? static.MAJOR : static.MINOR
        var cumulative = [0]
        for( var i = 1; i <= 7; i++ ) {
            cumulative.append( cumulative[ i ] + intervals[ i ] )
        }
        return ( current, amount ) => {
            var offset = current.getMidi() - root
            var octaves = int( offset / 12 )
            var remainder = offset mod 12
            var degree = 0
            for( var i = 2; i <= cumulative.len(); i++ ) {
                if( cumulative[ i ] <= remainder ) degree = i - 1
            }
            var newDegree = octaves * 7 + degree + amount
            var newOctaves = int( newDegree / 7 )
            var newDegreeInOctave = newDegree mod 7
            return new Note( root + ( newOctaves * 12 ) + cumulative[ newDegreeInOctave + 1 ] )
        }
    }
}
```

**Usage:**

```js
// Chromatic scale
result = []
for( n in (new Note("C4")..new Note("D4")).step( 1, "chromatic" ) ) {
    result.append( n.toString() )
}
// ["C4", "C#4", "D4"]

// C Major scale
result = []
for( n in (new Note("C4")..new Note("C5")).step( 1, "major" ) ) {
    result.append( n.toString() )
}
// ["C4", "D4", "E4", "F4", "G4", "A4", "B4", "C5"]

// Half-bounded + stream: Full chromatic octave
chromaticScale = (new Note("C4")..).step( 1, "chromatic" )
    .stream()
    .limit( 13 )
    .map( n => n.toString() )
    .toList()
// ["C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4", "C5"]
```

### Implementation Checklist

1. `rangeAdvance( step )` — Return a new instance moved by `step` positions. This is your "next value" generator.
2. `rangeCompare( other )` — Return negative/zero/positive like Java's `compareTo()`. This defines ordering for contains checks and iteration bounds.
3. `rangeCoerce( val )` — Convert foreign values to your type. Return `null` if the value can't be converted. This enables `contains()` to accept multiple input types.
4. `rangeStepFromUnit( amount, unit )` (optional) — Convert named units to numeric step values. Only needed if your type supports unit-based stepping with uniform intervals.
5. `rangeUnitStepper( unit )` (optional) — Return a closure `(current, amount) => nextValue` for non-uniform stepping patterns. Return `null` to fall through to `rangeStepFromUnit()`.

{% hint style="success" %}
**Key Insight:** The key insight is that `IRangeable` types always use step-reachability for `contains()` — the range iterates through actual values produced by `rangeAdvance()` rather than doing a simple bounds check. This is essential for sequences like Fibonacci where the "distance" between values is non-uniform.
{% endhint %}

## 📚 Additional Resources

* [BoxLang Ranges: Supercharged](https://community.ortussolutions.com/t/boxlang-ranges-supercharged/11106) — Community blog post covering all range features
* [BoxLang Ranges Part 2: Custom Types with IRangeable](https://community.ortussolutions.com/t/boxlang-ranges-part-2-custom-types-with-irangeable/11107) — Deep dive into `IRangeable` with complete examples

{% hint style="info" %}
**Available in BoxLang 1.14.0+**
{% endhint %}

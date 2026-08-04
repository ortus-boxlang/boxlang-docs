---
description: Collection of key-value pairs; a data dictionary
icon: book
---

# Structures

A structure is a collection of data where each element of data is addressed by a **name or key** and it can hold a value of any type. Like a dictionary but on steroids:

```javascript
// Create a struct via function
myStruct = structnew()

// Create a struct via literal syntax
myStruct = {}
```

{% hint style="success" %}
**Tip** Underneath the hood, all BoxLang structures are based on the `java.util.Map` interface. So if you come from a Java background, structures are untyped `HashMaps`.
{% endhint %}

{% hint style="info" %}
**Java Map Interoperability**: Any Java `Map` implementation can be used with BoxLang struct functions! This includes `HashMap`, `LinkedHashMap`, `TreeMap`, `ConcurrentHashMap`, `Properties`, and any other class implementing `java.util.Map`. BoxLang struct BIFs and member functions work seamlessly with Java Maps.
{% endhint %}

As an analogy, think about a refrigerator. If we’re keeping track of the produce inside the fridge, we don’t really care about where the produce is in, or basically: **order doesn’t matter**. Instead, we organize things by name, which are unique, and each name can have any value. The name _grapes_ might have the value 2, then the name _lemons_ might have the value 1, and _eggplants_ the value 6.

{% hint style="info" %}
All BoxLang structures are passed to functions as memory references, not values. Keep that in mind when working with structures. There is also the `passby=reference|value` attribute to function arguments where you can decide whether to pass by reference or value.
{% endhint %}

## 📋 Table of Contents

* [Key-Value Pairs](structures.md#key-value-pairs)
* [Creating Structures](structures.md#creating-structures)
* [Accessing Structure Elements](structures.md#accessing-structure-elements)
* [Struct Shorthand Keys](structures.md#-struct-shorthand-keys)
* [Struct Spread](structures.md#-struct-spread)
* [Struct Destructuring](structures.md#-struct-destructuring)
* [Structure Built-In Functions](structures.md#structure-built-in-functions)
* [Member Functions](structures.md#member-functions)
* [Looping Over Structures](structures.md#looping-over-structures)
* [Sorting Structures](structures.md#sorting-structures)
* [Struct Streams](structures.md#struct-streams)
* [Advanced Patterns](structures.md#advanced-patterns)

## 🔑 Key-Value Pairs

A structure is an _unordered collection_ where the data gets organized as a key and value pair. BoxLang syntax for structures follows the following syntax:

```javascript
produce = {
    grapes     = 2,
    lemons     = 1,
    eggplants  = 6
};
```

{% hint style="success" %}
**Tip** Please note that `=` sign and `:` are interchangeable in BoxLang. So you can use any to define your structures.
{% endhint %}

Since BoxLang is a case-insensitive language, the above structure will store all keys in uppercase. If you want the **exact casing** to be preserved in the structure, then surround the keys with quotes (`"`).

{% hint style="info" %}
The exact casing is extremely important if you will be converting these structures into JSON in the future.
{% endhint %}

```javascript
produce = {
    "grapes"     = 2,
    "lemons"     = 1,
    "eggplants"  = 6
};
```

The _key_ is the address, and the _value_ is the data at that address. Please note that the _value_ can be ANYTHING. It can be an array, an object, a simple value, or even an embedded structure. It doesn't matter.

## 📥 Retrieving Values

Retrieving values from structures can be done via dot or array notation or the `structFind()` function. Let's explore these approaches:

### 🔢 Array Notation

```javascript
writeOutput( "I have #produce[ "grapes" ]# grapes in my fridge!" );
writeOutput( "I have #produce[ "eggplants" ]# eggplants in my fridge!" );
```

### ⚫ Dot Notation

```javascript
writeOutput( "I have #produce.grapes# grapes in my fridge!" );
writeOutput( "I have #produce.eggplants# eggplants in my fridge!" );
```

### structFind( structure, key, \[defaultValue ] )

[https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structfind](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structfind)

<pre class="language-javascript"><code class="lang-javascript"><strong>// Member Function
</strong><strong>writeOutput( "I have #produce.find( "grapes" )# grapes in my fridge!" );
</strong>writeOutput( "I have #produce.find( "eggplants" )# eggplants in my fridge!" );

// Global Function
writeOutput( "I have #structFind( produce, "grapes" )# grapes in my fridge!" );
writeOutput( "I have #structFind( produce, "eggplants" ) eggplants in my fridge!" );
</code></pre>

{% hint style="warning" %}
However, please be aware that when dealing with native Java hashmaps, we recommend using array notation as the case is preserved in array notation, while in dot notation, it does not.
{% endhint %}

{% hint style="success" %}
BoxLang offers also the `structGet()` function which will search for a key or a key path. If there is no structure or array present in the path, this function creates structures or arrays to make it a valid variable path. [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structget](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structget)
{% endhint %}

### 🛡️ Safe Navigation

BoxLang also supports the concept of [safe navigation](operators.md#safe-navigation-operator) when dealing with structures. Sometimes it can be problematic when using dot notation on nested structures since some keys might not exist or be `null`. You can avoid this pain by using the safe navigation operator `?.` instead of the traditional `.` , and combine it with the elvis operator `?:` so if null, then returning a value.

```javascript
user = { age : 40 }

echo( user.age ) // 40
echo( user.salary ) // throws exception
echo( user?.salary ) // nothing, no exception
echo( user?.salary ?: 0 ) // 0
```

## 📤 Setting Values

I can also set new or override structure values a la carte. You can do so via array/dot notation or via the `structInsert(), structUpdate()` functions ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structinsert](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structinsert), [https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structupdate](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structupdate))

```javascript
// new key using default uppercase notation
produce.apples = 3;
// new key using case sensitive key
produce[ "apples" ] = 3;

// I just ate one grape, let's reduce it
produce[ "grapes" ] = 1; // or
produce.grapes--;

produce.insert( "newVeggie", 2 )
produce.update( "newVeggie", 1 )

structInsert( produce, "carrots", 5 )
structUpdate( produce, "carrots", 2 )
```

{% hint style="success" %}
**Tip** You can use the `toString()` call on any structure to get a string representation of its keys+values: `produce.toString()`
{% endhint %}

## ✨ Struct Shorthand Keys

Struct literals support JavaScript-style shorthand keys.

```javascript
host = "localhost"
port = 5432

config = { host, port }
```

That is equivalent to:

```javascript
config = { host: host, port: port }
```

Shorthand keeps the identifier name as the key.

```javascript
fooBar = "value"
result = { fooBar }
```

## 🌟 Struct Spread

Struct literals support spread syntax for merging one or more sources.

```javascript
defaults = { retries: 2, ssl: false }
overrides = { ssl: true }

config = { host: "localhost", ...defaults, ...overrides }
```

Ordered struct literals support spread as well.

```javascript
base = [ first: 1, second: 2 ]
result = [ ...base, third: 3 ]
```

Later entries win.

```javascript
result = { ...left, ...right, shared: "literal" }
```

## 🧩 Struct Destructuring

Struct destructuring lets you bind keys directly into variables.

```javascript
user = { name: "Luis", role: "admin" }
var { name, role } = user
```

You can rename keys, provide defaults, and capture the rest.

```javascript
options = { host: "localhost" }
var { host, port = 5432, ...rest } = options
```

Nested patterns are supported.

```javascript
user = { profile: { email: "box@lang.io" } }
var { profile: { email } } = user
```

Non-declaration struct assignments must be wrapped in parentheses.

```javascript
({ name, role } = user)
```

{% hint style="info" %}
Quoted, spaced, or numeric keys cannot use shorthand destructuring. Use explicit renaming instead.
{% endhint %}

See [Destructuring](syntax/destructuring.md) for full syntax and scoped-target behavior.

## 📚 Struct Built-In Functions (BIFs)

BoxLang provides a comprehensive set of struct BIFs organized by functionality. All struct BIFs can be called as member methods on Struct objects.

### 🔨 Creation & Configuration Functions

| Function           | Purpose             | Example                            |
| ------------------ | ------------------- | ---------------------------------- |
| `structNew()`      | Create new struct   | `structNew("ordered")` → `[:]`     |
| `structCopy()`     | Create shallow copy | `structCopy(myStruct)`             |
| `structToSorted()` | Create sorted copy  | `structToSorted(myStruct, "text")` |

### ➕ Modification Functions

| Function         | Purpose               | Example                                   |
| ---------------- | --------------------- | ----------------------------------------- |
| `structInsert()` | Insert key-value pair | `structInsert(struct, "key", "value")`    |
| `structUpdate()` | Update existing key   | `structUpdate(struct, "key", "newValue")` |
| `structAppend()` | Merge structs         | `structAppend(struct1, struct2)`          |
| `structDelete()` | Remove key            | `structDelete(struct, "key")`             |
| `structClear()`  | Remove all keys       | `structClear(struct)`                     |

### 🔍 Search & Filter Functions

| Function            | Purpose                       | Example                                        |
| ------------------- | ----------------------------- | ---------------------------------------------- |
| `structFind()`      | Find value by key             | `structFind(struct, "key")` → value            |
| `structGet()`       | Get with dot notation         | `structGet("struct.nested.key")`               |
| `structFindKey()`   | Find keys matching value      | `structFindKey(struct, "searchValue")`         |
| `structFindValue()` | Find values matching criteria | `structFindValue(struct, "pattern")`           |
| `structKeyExists()` | Check if key exists           | `structKeyExists(struct, "key")` → `true`      |
| `structFilter()`    | Filter by condition           | `structFilter(struct, (k,v) -> v > 5)`         |
| `structEvery()`     | Test all entries              | `structEvery(struct, (k,v) -> v > 0)` → `true` |
| `structSome()`      | Test any entry                | `structSome(struct, (k,v) -> v > 10)` → `true` |
| `structNone()`      | Test no entries match         | `structNone(struct, (k,v) -> v < 0)` → `true`  |

### 🔄 Transformation Functions

| Function                | Purpose                 | Example                                                 |
| ----------------------- | ----------------------- | ------------------------------------------------------- |
| `structMap()`           | Transform values        | `structMap(struct, (k,v) -> v * 2)`                     |
| `structReduce()`        | Reduce to single value  | `structReduce(struct, (acc,k,v) -> acc + v, 0)`         |
| `structKeyTranslate()`  | Translate keys          | `structKeyTranslate(struct, mapping)`                   |
| `structToQueryString()` | Convert to query string | `structToQueryString(struct)` → `"key1=val1&key2=val2"` |

### 📊 Sorting Functions

| Function       | Purpose            | Example                                           |
| -------------- | ------------------ | ------------------------------------------------- |
| `structSort()` | Sort keys to array | `structSort(struct, "text")` → `["key1", "key2"]` |

### 📏 Information Functions

| Function                  | Purpose                | Example                                       |
| ------------------------- | ---------------------- | --------------------------------------------- |
| `structCount()`           | Get key count          | `structCount(struct)` → `5`                   |
| `structIsEmpty()`         | Check if empty         | `structIsEmpty(struct)` → `false`             |
| `structKeyArray()`        | Get keys as array      | `structKeyArray(struct)` → `["key1", "key2"]` |
| `structKeyList()`         | Get keys as list       | `structKeyList(struct)` → `"key1,key2"`       |
| `structValueArray()`      | Get values as array    | `structValueArray(struct)` → `[val1, val2]`   |
| `structEquals()`          | Compare structs        | `structEquals(struct1, struct2)` → `true`     |
| `structIsCaseSensitive()` | Check case sensitivity | `structIsCaseSensitive(struct)` → `false`     |
| `structIsOrdered()`       | Check if ordered       | `structIsOrdered(struct)` → `true`            |
| `structGetMetadata()`     | Get struct metadata    | `structGetMetadata(struct)`                   |

### 🔗 Iteration Functions

| Function       | Purpose            | Example                                             |
| -------------- | ------------------ | --------------------------------------------------- |
| `structEach()` | Iterate each entry | `structEach(struct, (k,v) => println(k & ":" & v))` |

{% hint style="success" %}
**Complete Reference**: For detailed documentation of each function, visit the [Struct BIF Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct).
{% endhint %}

## ⚙️ Member Functions

All struct BIFs can be called as member functions on Struct objects for cleaner, more fluent code:

```js
inventory = {
    "banana": 12,
    "apple": 20,
    "cherry": 15,
    "date": 8
}

// Basic operations
inventory.count()          // 4
inventory.isEmpty()        // false
inventory.keyArray()       // ["banana", "apple", "cherry", "date"]
inventory.keyList()        // "banana,apple,cherry,date"

// Modification
inventory.insert("grape", 10)
inventory.update("apple", 25)
inventory.delete("date")
inventory.append({"kiwi": 5, "mango": 3})

// Search
inventory.keyExists("banana")   // true
inventory.find("apple")         // 25

// Transformation
doubled = inventory.map((k,v) -> v * 2)
expensive = inventory.filter((k,v) -> v > 10)
total = inventory.reduce((acc,k,v) -> acc + v, 0)

// Sorting
sortedKeys = inventory.sort("text")

// Information
inventory.isCaseSensitive()     // false
inventory.isOrdered()           // false

// Iteration
inventory.each((key, value) => {
    println("#key#: #value#")
})

// Chaining operations
result = inventory
    .filter((k,v) -> v > 10)
    .map((k,v) -> v * 2)
    .keyArray()
```

## 🔧 Java Map Methods

Since BoxLang structs implement the `java.util.Map` interface, you have access to all Java Map methods:

```js
import java.util.Collections
import java.util.Comparator

data = {"name": "BoxLang", "version": "1.0", "type": "JVM"}

// Size and capacity
data.size()                  // 3
data.isEmpty()               // false

// Adding/updating elements
data.put("author", "Ortus")  // Add or update
data.putIfAbsent("license", "Apache")  // Only if key doesn't exist
data.putAll({"year": 2024, "platform": "Multi"})

// Removing elements
data.remove("type")          // Remove by key
data.remove("version", "1.0") // Remove if value matches
data.clear()                 // Remove all

// Accessing elements
data.get("name")             // Get value
data.getOrDefault("missing", "default")  // With default
data.getRaw("name")          // Get without unwrapping NullValue

// Checking
data.containsKey("name")     // true/false
data.containsValue("BoxLang") // true/false

// Keys and values
keys = data.keySet()         // Set of keys
values = data.values()       // Collection of values
entries = data.entrySet()    // Set of Map.Entry objects

// Iteration
data.forEach((k, v) => println("#k#: #v#"))

// Compute operations
data.compute("count", (k, v) -> v == null ? 1 : v + 1)
data.computeIfAbsent("id", (k) -> createUniqueId())
data.computeIfPresent("count", (k, v) -> v + 1)

// Merge operation
data.merge("count", 1, (oldVal, newVal) -> oldVal + newVal)

// Replace operations
data.replace("version", "2.0")  // Replace if exists
data.replace("version", "1.0", "2.0")  // Replace if old value matches
data.replaceAll((k, v) -> v.toString().toUpperCase())
```

## 🌊 Struct Streams

Structs provide first-class Java Stream support through three members: `stream()`, `keyStream()`, and `valueStream()`.

* `stream()` returns a stream of `java.util.Map.Entry` objects.
* `keyStream()` returns a stream of the struct's keys.
* `valueStream()` returns a stream of the struct's values.

```js
inventory = {
    widgets: 42,
    gadgets: 7,
    sprockets: 0,
    gizmos: 118
}

// Keys with zero stock
outOfStock = inventory.stream()
    .filter(entry -> entry.getValue() == 0)
    .map(entry -> entry.getKey())
    .toList()

// Total units on hand
totalUnits = inventory.valueStream()
    .mapToInt(qty -> qty)
    .sum()

// Sorted key listing
sortedKeys = inventory.keyStream()
    .sorted()
    .toList()
```

You can also use the streams with standard Java Stream terminal operations:

```js
data = { name: "BoxLang", version: "1.0", type: "JVM" }

data.stream()
    .filter(entry -> entry.getValue() != null)
    .forEach(entry -> println(entry.getKey()))
```

## 🎯 BoxLang Struct Native Methods

The BoxLang `Struct` type provides additional methods beyond standard Java Map operations:

```js
config = {"debug": true, "timeout": 30, "retries": 3}

// ===== Type Information =====

// Get struct type
type = config.getType()           // TYPES.DEFAULT
typeName = config.getBoxTypeName() // "Struct"

// Type checks
isCaseSensitive = config.isCaseSensitive()  // false
isSoftRef = config.isSoftReferenced()       // false

// ===== Key Operations =====

// Get keys as various types
keyList = config.getKeys()           // List<Key> objects
keyStrings = config.getKeysAsStrings() // List<String>

// Access with Key objects
config.containsKey(Key.of("debug")) // true
config.get(Key.of("timeout"))       // 30
config.put(Key.of("maxConns"), 100)

// ===== Advanced Get Methods =====

// Type-safe getters (no casting needed)
config.getAsBoolean(Key.of("debug"))   // true
config.getAsInteger(Key.of("timeout")) // 30
config.getAsString(Key.of("mode"))     // "production"
config.getAsArray(Key.of("hosts"))     // Array object
config.getAsStruct(Key.of("nested"))   // IStruct object
config.getAsDateTime(Key.of("created")) // DateTime object
config.getAsFunction(Key.of("callback")) // Function object
config.getAsQuery(Key.of("results"))   // Query object

// Generic typed getter
config.getAs(Integer.class, Key.of("timeout")) // 30

// Optional and Attempt wrappers
optional = config.getAsOptional(Key.of("missing"))  // Optional.empty()
attempt = config.getAsAttempt(Key.of("timeout"))    // Attempt<Object>
attempt = config.getAsAttempt(Key.of("timeout"), Integer.class) // Attempt<Integer>

// ===== Bulk Operations =====

// Add all from another map
config.addAll({"compression": true, "logging": "verbose"})

// Get wrapped underlying Map
wrapped = config.getWrapped()  // Map<Key, Object>

// ===== Conversion Operations =====

// Convert to string representation
str = config.asString()        // Formatted multi-line string
str = config.toString()        // Same as asString()

// Convert to unmodifiable
immutable = config.toUnmodifiable()  // UnmodifiableStruct

// ===== Metadata Operations =====

// Get BoxLang metadata
meta = config.getBoxMeta()     // BoxMeta object
meta = config.$bx              // Same via property

// ===== Static Factory Methods =====

// Create from key-value pairs
struct = Struct.of("key1", "value1", "key2", "value2")
struct = Struct.ofNonConcurrent("k1", "v1")  // Non-thread-safe

// Create linked (ordered) structs
ordered = Struct.linkedOf("first", 1, "second", 2)
ordered = Struct.linkedOfNonConcurrent("a", 1)

// Create sorted structs with comparator
sorted = Struct.sortedOf(comparator, "z", 1, "a", 2)
sorted = Struct.sortedOf(Struct.KEY_LENGTH_LONGEST_FIRST_COMPARATOR, map)

// Create from Java Map
struct = Struct.fromMap(javaMap)
struct = Struct.fromMap(TYPES.LINKED, javaMap)

// ===== Equality and Hashing =====

config1.equals(config2)        // Deep equality check
hash = config.hashCode()       // Hash code
```

### 🔑 Key Differences: String Keys vs Key Objects

| Operation       | String Key                   | Key Object                           |
| --------------- | ---------------------------- | ------------------------------------ |
| Get value       | `struct.get("name")`         | `struct.get(Key.of("name"))`         |
| Check existence | `struct.containsKey("name")` | `struct.containsKey(Key.of("name"))` |
| Set value       | `struct.put("name", val)`    | `struct.put(Key.of("name"), val)`    |
| Remove          | `struct.remove("name")`      | `struct.remove(Key.of("name"))`      |
| Case handling   | Always case-insensitive\*    | Respects struct type                 |

\*Unless the struct is case-sensitive type

{% hint style="info" %}
**BoxLang Key Objects**: The `Key` class is a special BoxLang type that simulates a case-insensitive string by default. When working with case-sensitive structs, use `KeyCased` for exact case matching.
{% endhint %}

## 🗂️ Structure Types

In BoxLang, not only can you create case-insensitive unordered structures but also the following types using the `structNew()` function ([https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structnew](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct/structnew))

* case-sensitive
* normal
* ordered or linked
* ordered-case-sensitive
* soft
* synchronized
* weak

Here is the signature for the `structnew()` function:

```javascript
structNew( [type[[,sortType][,sortOrder][,localeSensitive]|[,callback]]] )
```

```
structNew( [type, [onMissingKey] ] )
```

Now let's create some different types of structures

```javascript
produce = structNew();
pickyProduce = structNew( "casesensitive" )

queue = structNew( "ordered" )
pickyQueue = structNew( "ordered-casesensitive" )
linkedList = structnew( 'ordered' );
cache = structnew( 'soft' );
```

### 💻 Literal Syntax

You can also use literal syntax for some of these types:

```javascript
// ordered struct
myStruct = [:] or [=]
```

{% hint style="success" %}
**Tip**: Check out all the [structure BIF reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/struct) and [member functions](https://boxlang.ortusbooks.com/getting-started/overview/syntax-style-guide#member-functions) for more capabilities.
{% endhint %}

## 🔁 Looping Over Structures

You can use different constructs for looping over structures:

* `for` loops
* `loop` constructs
* `each()` closures

```javascript
// Simple iteration (key only)
for( var key in produce ){
 systemOutput( "I just had #produce[ key ]# #key#" );
}

// Destructuring syntax - get both key and value
for( key, value in produce ){
 systemOutput( "I just had #value# #key#" );
}

// Each closure with key and value
produce.each( function( key, value ){
  systemOutput( "I just had #value# #key#" );
} );
```

{% hint style="success" %}
**New in 1.10.0**: Loop destructuring syntax `for (key, value in struct)` allows you to get both the key and value in a single, clean declaration without needing array notation lookups.
{% endhint %}

### ⚡ Multi-Threaded Looping

BoxLang allows you to leverage the `each()` operations in a multi-threaded fashion. The `structEach()` or `each()` functions allow for a `parallel` and `maxThreads` arguments so the iteration can happen concurrently on as many `maxThreads` as supported by your JVM.

```java
structEach( struct, callback, parallel:boolean, maxThreads:numeric );
each( collection, callback, parallel:boolean, maxThreads:numeric );
```

This is incredibly awesome as now your callback will be called concurrently! However, please note that once you enter concurrency land, you should shiver and tremble. Thread concurrency will be of the utmost importance, and you must ensure that var scoping is done correctly and that appropriate locking strategies are in place.

```java
myStruct.each( function( key, value ){
   myservice.process( value );
}, true, 20 );
```

Even though this approach to multi-threaded looping is easy, it is not performant and/or flexible. Under the hood, the BoxLang uses a single thread executor for each execution, do not allow you to deal with exceptions, and if an exception occurs in an element processor, good luck; you will never know about it. This approach can be verbose and error-prone, but it's easy. You also don't control where the processing thread runs and are at the mercy of the engine.

### 🚀 ColdBox Futures Parallel Programming

If you would like a functional and much more flexible approach to multi-threaded or parallel programming, consider using the ColdBox Futures approach (usable in ANY framework or non-framework code). You can use it by installing ColdBox or WireBox into any BoxLang application and leveraging our `async` programming constructs, which behind the scenes, leverage the entire Java Concurrency and Completable Futures frameworks.

{% embed url="https://coldbox.ortusbooks.com/digging-deeper/promises-async-programming/parallel-computations" %}
ColdBox Futures and Async Programming
{% endembed %}

Here are some methods that will allow you to do parallel computations:

* `all( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures to execute them in parallel. When you call on it, it will return a future that will retrieve an array of the results of all the operations.
* `allApply( items, fn, executor ):array` : This function can accept an array of items or a struct of items of any type and apply a function to each of the items in parallel. The `fn` argument receives the appropriate item and must return a result. Consider this a parallel `map()` operation.
* `anyOf( a1, a2, ... ):Future` : This method accepts an infinite amount of future objects, closures, or an array of closures/futures and will execute them in parallel. However, instead of returning all of the results in an array like `all()`, this method will return the future that executes the fastest! Race Baby!
* `withTimeout( timeout, timeUnit )` : Apply a timeout to `all()` or `allApply()` operations. The `timeUnit` can be days, hours, microseconds, milliseconds, minutes, nanoseconds, and seconds. The default is milliseconds.

## ✨ Trailing Commas

BoxLang supports trailing commas when defining array and struct literals. Just in case you miss a dangling comma, we won't shout at you!

```groovy
myArray = [
    "BoxLang",
    "ColdBox",
    "TestBox",
    "CommandBox",
]
println( myArray )

myStruct = {
    name: "BoxLang",
    type: "JVM Dynamic Language",
    version: "1.0.0",
}
println( myStruct )
```

## 👂 Change Listeners

All arrays and structures offer the ability to listen to changes to themselves. This is all done via our `$bx` metadata object available on all arrays/structures. You will call the `registerChangeListener()` function to register a closure/lambda that will listen to changes on the struct. You can listen:

* To all changes in the structure
* To a specific key in the structure

However, you must EXPLICITLY return the value that will be stored in the change.

```java
// Listen to all changes in the array
myStruct.$bx.registerChangeListener( closure/lambda )

// Listen to a specific index in the array
myStruct.$bx.registerChangeListener( index, closure/lambda )
```

{% hint style="warning" %}
Please note that this change listener will fire on every struct access, so ensure it's performant.
{% endhint %}

The signature of the closure/lambda is the following

```groovy
( Key key, any newValue, any oldValue, struct ) => {}
```

{% hint style="success" %}
Please note that the Key is a BoxLang Key object, which simulates a case-insensitive string. You can use methods on it like:\\

* `getName()`
* `getNameNoCase()`
* `toString()`
{% endhint %}

Here are a few simple examples:

{% embed url="https://try.boxlang.io/?code=eJxlUU1PhDAQvfdXvHAwkJBdJSExbNbLHjV682I8VBh3m%2B2WpgwQYva%2FWywg0fbQ6Zs3b76U6chw7Qbs8SXgT%2FQhjb9RgbssDYiVVg4jcj8BZ9WrkZBPf2mtJg9kt%2BIqxHaLJ9UwGXANqTXKkzRHalB%2Fgk%2BEhl1bcgFZVSkcXeqOxtdqWXqDuNwINZe1cXQctdzhRyPokosRn2lIYah%2Flbr1YbWuJivIJ9g%2FTB1ZpwxrEyN6pKFAhBv4YCS7P95n6tGNGoEza%2F8nvuhqTZxTz0RH3DqzxO%2FEFYlYtWRb9iJWGQpzS5F7wq%2B%2FIk1M8bKJtfNtmvW731eWC7EUtTCQfANtnZDm" %}

```java
inventory = {
    "banana": 12,
    "papaya": 8,
    "kiwi": 15,
    "apple": 20
}

// Listen to all changes of the struct: add, remove, replace, etc.
inventory.registerChangeListener( (key, newValue, oldValue, struct) => {
    println( "Key: " & key );
    println( "New value: " & newValue );
    println( "Old value: " & oldValue );
    return newValue;
} )

inventory.put( "pineapple", 5 )
inventory.delete( "banana" )
inventory["apple"] = 25

println( inventory )
```

Here is another example when listening to a specific index:

{% embed url="https://try.boxlang.io/?code=eJxlkTFrwzAQhXf9ioeHEoNI0pRASUiXji3t1qV0UO1LckTIQpZjTMl%2FrxxZjmnlRX73vXd3NpszGV%2B5Djv8CISTfSsTnmyD%2B5WMilVWdb3yOAgnbrkH1sO7slZTEFZLcRFiscAr154MfIXiqMyBauwrB4XaUsF7LnCiDhyAI6H2rim84DTJ3NGht7vnqzVGkZuNk0nMgl3CUPuhdEMSlS6HWwzLsXsa1rGOjdcmuF%2Bo2yDD3bV3vv1TfaMW5z4jMin7P%2FiuyymYWifQkW%2BcGf1bcUEuJsvZxocQy4biR5NYB%2BBWL0mTp9uy0%2BJnEr%2FC33pYCjFONSLIfwF%2Fs5BH" %}

```java
inventory = {
    "banana": 12,
    "papaya": 8,
    "kiwi": 15,
    "apple": 20
}

// Listen to changes for a specific key in the struct
inventory.registerChangeListener( "banana", (key, newValue, oldValue, struct) => {
    println( "Key: " & key );
    println( "New value: " & newValue );
    println( "Old value: " & oldValue );
    return newValue;
} )

inventory.put( "pineapple", 5 )
inventory.delete( "banana" )
inventory["banana"] = 30

println( inventory )
```

## 🔗 Related Documentation

{% content-ref url="arrays.md" %}
[arrays.md](arrays.md)
{% endcontent-ref %}

{% content-ref url="sets.md" %}
[sets.md](sets.md)
{% endcontent-ref %}

{% content-ref url="ranges.md" %}
[ranges.md](ranges.md)
{% endcontent-ref %}

{% content-ref url="queries.md" %}
[queries.md](queries.md)
{% endcontent-ref %}

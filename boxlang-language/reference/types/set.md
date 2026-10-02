
# Type: `Set`

The primary Set class in BoxLang.

This class wraps a <code>java.util.Set</code> and provides
 full BoxLang integration: member-function dispatch via <code>FunctionService</code>, change
 listeners, metadata, and JSON serialization.

 <p>
 BoxSet supports three backing variants chosen at construction:
 <ul>
 <li><code>Type#DEFAULT</code> — <code>HashSet</code>, fastest, no order guarantee</li>
 <li><code>Type#LINKED</code> — <code>LinkedHashSet</code>, preserves insertion order</li>
 <li><code>Type#SORTED</code> — <code>TreeSet</code>, natural ordering (uses <code>Compare</code>)</li>
 </ul>

 <p>
 This class is named <code>BoxSet</code> (rather than <code>Set</code>) to avoid collision with
 <code>java.util.Set</code> throughout the BoxLang codebase.

## Set Methods

<details>
<summary><code>add(value=[any])</code></summary>

Add an element to a Set, deduplicating automatically.

If the value is already present, the call is a
 no-op. The Set is modified in place and returned to support method chaining.

### Method Signature

```
add(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to add. Duplicates are silently ignored. |  |
</details>
<details>
<summary><code>addAll(values=[any])</code></summary>

Add every element of a collection into a Set, deduplicating automatically.

The source collection can be
 an Array, another Set, a list-delimited String, or any value castable to a Set. The Set is modified in
 place and returned to support method chaining.

### Method Signature

```
addAll(values=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `values` | `any` | `true` | The collection of values to add. Accepts an Array, Set, list-delimited String, or any castable collection. |  |
</details>
<details>
<summary><code>any(callback=[function:Predicate])</code></summary>

Test whether at least one element of a Set satisfies a predicate.

Iteration short-circuits on the first
 element for which the predicate returns true. Returns false for an empty Set. The predicate receives the
 element value, its 1-based ordinal position, and the Set itself.

### Method Signature

```
any(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Short-circuits on the first <code>true</code> result. |  |
</details>
<details>
<summary><code>append(value=[any])</code></summary>

Add an element to a Set, deduplicating automatically.

If the value is already present, the call is a
 no-op. The Set is modified in place and returned to support method chaining.

### Method Signature

```
append(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to add. Duplicates are silently ignored. |  |
</details>
<details>
<summary><code>clear()</code></summary>

Remove all elements from a Set, leaving it empty.

The Set is modified in place and returned to support
 method chaining.

### Method Signature

```
clear()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>contains(value=[any])</code></summary>

Test whether a Set contains a given value using BoxLang value equality.

Returns true if the value is
 present, false otherwise.

### Method Signature

```
contains(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to look for. |  |
</details>
<details>
<summary><code>containsAll(values=[any])</code></summary>

Test whether a Set contains every element of a given collection.

The collection can be an Array, another
 Set, a list-delimited String, or any value castable to a Set. Returns true only if all elements are present.

### Method Signature

```
containsAll(values=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `values` | `any` | `true` | The collection of values to check for. Accepts an Array, Set, list-delimited String, or any castable collection. |  |
</details>
<details>
<summary><code>delete(value=[any])</code></summary>

Remove an element from a Set.

If the value is not present the call is a no-op. The Set is modified in
 place and returned to support method chaining.

### Method Signature

```
delete(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to remove. If the value is not present, the call is a no-op. |  |
</details>
<details>
<summary><code>difference(otherSet=[any])</code></summary>

Compute the relative complement (A − B) of two Sets.

Returns a new Set containing all elements that are in
 A but not in B. The result is a new Set of the same variant as A; neither input is modified.

### Method Signature

```
difference(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The set to subtract (B). Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>duplicate(deep=[boolean])</code></summary>

Duplicates an object - either shallow or deep

### Method Signature

```
duplicate(deep=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `deep` | `boolean` | `false` | Whether to deep copy the object or make a shallow copy (e.g. only the top level keys in a struct) | `true` |
</details>
<details>
<summary><code>each(callback=[function:Consumer])</code></summary>

Invoke a callback for every element of a Set.

The callback receives the element value, its 1-based ordinal
 position, and the Set itself; single-argument callbacks receive only the value. Iteration follows the natural
 order of the underlying variant. Use setMap() if you need a transformed result.

### Method Signature

```
each(callback=[function:Consumer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Consumer` | `true` | Invoked for each element. Receives <code>(value, ordinal, set)</code>; single-argument callbacks<br>                    receive only the value. |  |
</details>
<details>
<summary><code>equals(otherSet=[any])</code></summary>

Test whether two Sets contain exactly the same elements.

The comparison is variant-agnostic: a hash Set and
 a linked Set with identical elements are considered equal. Returns true if both sets have the same size and
 every element of one is present in the other.

### Method Signature

```
equals(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The second set to compare. Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>every(callback=[function:Predicate])</code></summary>

Test whether every element of a Set satisfies a predicate.

Iteration short-circuits on the first element
 for which the predicate returns false. Returns true for an empty Set (vacuous truth). The predicate receives
 the element value, its 1-based ordinal position, and the Set itself.

### Method Signature

```
every(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Short-circuits on the first <code>false</code> result. |  |
</details>
<details>
<summary><code>filter(callback=[function:Predicate])</code></summary>

Return a new Set containing only the elements of the source Set for which the predicate returns true.

The
 result is a new Set of the same variant as the source; the source is not modified. The predicate receives
 the element value, its 1-based ordinal position, and the Set itself.

### Method Signature

```
filter(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Elements for which this returns <code>true</code> are included in the result. |  |
</details>
<details>
<summary><code>find(callback=[function:Predicate])</code></summary>

Return the first element of a Set for which the predicate returns true, or null if no element matches.

Iteration follows the natural order of the underlying variant and stops at the first match. The predicate
 receives the element value, its 1-based ordinal position, and the Set itself.

### Method Signature

```
find(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Iteration stops at the first element for which this returns <code>true</code>. |  |
</details>
<details>
<summary><code>has(value=[any])</code></summary>

Test whether a Set contains a given value using BoxLang value equality.

Returns true if the value is
 present, false otherwise.

### Method Signature

```
has(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to look for. |  |
</details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

### Method Signature

```
hash(algorithm=[string], encoding=[string], numIterations=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `algorithm` | `string` | `false` | The supported <code>java.security.MessageDigest</code> algorithm (case-insensitive) or "quick" for an insecure 64-bit hash | `MD5` |
| `encoding` | `string` | `false` | Applicable to strings ( default "utf-8" ) | `utf-8` |
| `numIterations` | `integer` | `false` | The number of iterations to re-digest the object ( default 1 ); | `1` |
</details>
<details>
<summary><code>intersection(otherSet=[any])</code></summary>

Compute the intersection (A ∩ B) of two Sets, returning a new Set that contains only the elements present
 in both A and B.

The result is a new Set of the same variant as A; neither input is modified.

### Method Signature

```
intersection(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The second set (B). Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>isDisjointFrom(otherSet=[any])</code></summary>

Test whether two Sets share no common elements, i.e.

their intersection is empty. Returns true if the two
 Sets are disjoint, false if they have at least one element in common.

### Method Signature

```
isDisjointFrom(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The second set to compare against. Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>isEmpty()</code></summary>

Test whether a Set contains no elements.

Returns true for an empty Set, false if it has one or more elements.

### Method Signature

```
isEmpty()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>isSubsetOf(otherSet=[any])</code></summary>

Test whether every element of set A is also contained in set B, i.e.

A ⊆ B. An empty set is always a
 subset of any set. Returns true if A is a subset of B, false otherwise.

### Method Signature

```
isSubsetOf(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The candidate superset (B). Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>isSupersetOf(otherSet=[any])</code></summary>

Test whether every element of set B is also contained in set A, i.e.

A ⊇ B. A set is always a superset
 of the empty set. Returns true if A is a superset of B, false otherwise.

### Method Signature

```
isSupersetOf(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The candidate subset (B). Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>len()</code></summary>

Returns the absolute value of a number

### Method Signature

```
len()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>length()</code></summary>

Returns the absolute value of a number

### Method Signature

```
length()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>map(callback=[function:Function])</code></summary>

Apply a transform function to every element of a Set and collect the deduplicated results into a new Set
 of the same variant.

The source Set is not modified. The callback receives the element value, its 1-based
 ordinal position, and the original Set.

### Method Signature

```
map(callback=[function:Function])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Function` | `true` | Receives <code>(value, ordinal, set)</code> and returns the transformed value. |  |
</details>
<details>
<summary><code>none(callback=[function:Predicate])</code></summary>

Test whether no element of a Set satisfies a predicate.

Iteration short-circuits on the first element for
 which the predicate returns true. Returns true for an empty Set. The predicate receives the element value,
 its 1-based ordinal position, and the Set itself.

### Method Signature

```
none(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Short-circuits on the first <code>true</code> result. |  |
</details>
<details>
<summary><code>parallelStream()</code></summary>

No description available

### Method Signature

```
parallelStream()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

Left-fold a Set with an accumulator function, reducing it to a single value.

The callback receives the
 current accumulator, the element value, its 1-based ordinal position, and the Set itself, and returns the
 new accumulator. Iteration follows the natural order of the underlying variant.

### Method Signature

```
reduce(callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | Receives <code>(accumulator, value, ordinal, set)</code> and returns the new accumulator. |  |
| `initialValue` | `any` | `false` | The starting accumulator value. If omitted, the first element is used as the initial value. |  |
</details>
<details>
<summary><code>reject(callback=[function:Predicate])</code></summary>

Return a new Set containing only the elements of the source Set for which the predicate returns false
 (the inverse of setFilter).

The result is a new Set of the same variant as the source; the source is not
 modified. The predicate receives the element value, its 1-based ordinal position, and the Set itself.

### Method Signature

```
reject(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Elements for which this returns <code>false</code> are included in the result. |  |
</details>
<details>
<summary><code>remove(value=[any])</code></summary>

Remove an element from a Set.

If the value is not present the call is a no-op. The Set is modified in
 place and returned to support method chaining.

### Method Signature

```
remove(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to remove. If the value is not present, the call is a no-op. |  |
</details>
<details>
<summary><code>removeAll(values=[any])</code></summary>

Remove every element of a collection from a Set, leaving only the elements that are not in the collection.

The Set is modified in place and returned to support method chaining. Elements not present in the Set are
 silently skipped.

### Method Signature

```
removeAll(values=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `values` | `any` | `true` | The collection of values to remove. Accepts an Array, Set, list-delimited String, or any castable collection. |  |
</details>
<details>
<summary><code>retainAll(values=[any])</code></summary>

Retain only the elements of a Set that are also present in the given collection, removing everything else.

This is the in-place equivalent of computing an intersection. The Set is modified in place and returned to
 support method chaining.

### Method Signature

```
retainAll(values=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `values` | `any` | `true` | The collection whose membership determines which elements are kept. Accepts an Array, Set,<br>                  list-delimited String, or any castable collection. |  |
</details>
<details>
<summary><code>size()</code></summary>

Returns the absolute value of a number

### Method Signature

```
size()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>some(callback=[function:Predicate])</code></summary>

Test whether at least one element of a Set satisfies a predicate.

Iteration short-circuits on the first
 element for which the predicate returns true. Returns false for an empty Set. The predicate receives the
 element value, its 1-based ordinal position, and the Set itself.

### Method Signature

```
some(callback=[function:Predicate])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | Predicate invoked for each element. Receives <code>(value, ordinal, set)</code>.<br>                    Short-circuits on the first <code>true</code> result. |  |
</details>
<details>
<summary><code>stream()</code></summary>

No description available

### Method Signature

```
stream()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>symmetricDifference(otherSet=[any])</code></summary>

Compute the symmetric difference (A △ B) of two Sets, returning the elements that are in exactly one of
 the two Sets but not in both.

Equivalent to <code>(A ∪ B) − (A ∩ B)</code>. The result is a new Set of the same
 variant as A; neither input is modified.

### Method Signature

```
symmetricDifference(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The second set (B). Accepts any value castable to a Set. |  |
</details>
<details>
<summary><code>toArray()</code></summary>

Convert a Set to an Array, preserving the iteration order of the underlying variant.

For a LINKED Set the
 insertion order is preserved; for a SORTED Set the natural ordering applies; for a default hash Set the
 order is undefined. The source Set is not modified.

### Method Signature

```
toArray()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>Query Format Options</h2>
 The <code>queryFormat</code> argument determines how queries are serialized:
 <ul>
 <li><code>row</code> or <code>false</code>: Serializes the query as a top-level struct with two keys:
 <code>columns</code> (an array of column names) and <code>data</code> (an array of arrays representing
 each row's data).</li>
 <li><code>column</code> or <code>true</code>: Serializes the query as a top-level struct with three keys:
 <code>rowCount</code> (the number of rows), <code>columns</code> (an array of column names), and
 <code>data</code> (a struct where each key is a column name and the value is an array of values for that column).</li>
 <li><code>struct</code>: Serializes the query as an array of structs, where each struct represents a row of data.</li>
 </ul>

 <h2>Usage</h2>

 <pre>
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 </pre>

### Method Signature

```
toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `queryFormat` | `string` | `false` | If the variable is a query, specifies whether to serialize the query by rows or by columns. Valid values are:<br>                       <code>row</code> same as <code>false</code>, <code>column</code> same as <code>true</code>, or <code>struct</code>. Defaults to <code>row</code>. |  |
| `useSecureJSONPrefix` | `string` | `false` | If true, the JSON string is prefixed with a secure JSON prefix. (Not implemented yet) | `false` |
| `useCustomSerializer` | `boolean` | `false` | If true, the JSON string is serialized using a custom serializer. (Not implemented yet) |  |
| `pretty` | `boolean` | `false` | If true, the JSON string is formatted with indentation and line breaks for readability. Defaults to false. | `false` |
</details>
<details>
<summary><code>toList(delimiter=[string])</code></summary>

Join the elements of a Set into a delimited string.

Each element is cast to a String before joining.
 For LINKED Sets the insertion order is preserved; for SORTED Sets the natural ordering applies; for
 default hash Sets the order is undefined.

### Method Signature

```
toList(delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | The delimiter to place between elements. Defaults to <code>","</code>. | `,` |
</details>
<details>
<summary><code>toModifiable()</code></summary>

Convert an array, struct, query or set to its Modifiable counterpart.

### Method Signature

```
toModifiable()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct, query or set to its Unmodifiable counterpart.

### Method Signature

```
toUnmodifiable()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>union(otherSet=[any])</code></summary>

Compute the union (A ∪ B) of two Sets, returning a new Set that contains all elements from both.

Duplicates are automatically deduplicated. The result is a new Set of the same variant as A; neither
 input is modified.

### Method Signature

```
union(otherSet=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `otherSet` | `any` | `true` | The second set (B). Accepts any value castable to a Set. |  |
</details>




## Examples

### Creating sets using the function `setNew`

```java
// Create a default set (hash-based, no ordering)
mySet = setNew();

// Create a linked set which will maintain insertion order
mySet = setNew( type="linked" );

// Create a sorted set which will keep elements in natural order
mySet = setNew( type="sorted" );

// Create a set seeded with values (duplicates removed)
mySet = setNew( values=[ 1, 2, 2, 3 ] );

// Create a case-sensitive set
mySet = setNew( values=[ "Hello", "hello", "HELLO" ], caseSensitive=true );
```


### Creating sets using literal syntax

```java
// Create a set with values
mySet = set{ 1, 2, 3 };

// Create an empty set
emptySet = set{};

// Spread an array into a set
arr = [ 3, 4, 5 ];
s = set{ 1, 2, ...arr };

// Spread another set
other = set{ 2, 3 };
s = set{ 1, ...other, 4 };

// Spread a range
s = set{ ...(1..5) };
```

### Creating sets from varargs

```java
// setOf deduplicates automatically
s = setOf( 1, 2, 2, 3 );
// Result: Set with 3 elements
```

### Converting arrays to sets

```java
// Convert array to default set
s = [ 1, 2, 2, 3 ].toSet();

// Convert to linked (insertion-ordered) set
s = [ "c", "a", "b", "a" ].toSet( "linked" );

// Convert to sorted set
s = [ 9, 1, 5, 3 ].toSet( "sorted" );
```

### Converting strings to sets

```java
// Split comma-delimited string to set
s = "a,b,c,a".listToSet();

// Custom delimiter with type
s = "a|b|c|b".listToSet( delimiter="|", type="linked" );
```

### Set membership and mutation

```java
s = setNew();

// Add elements (add and append are aliases)
s.add( "apple" );
s.append( "banana" );

// Test membership (contains and has are aliases)
s.contains( "apple" );    // true
s.has( "banana" );        // true

// Remove elements (remove and delete are aliases)
s.remove( "apple" );
s.delete( "banana" );

// Size (size, len, length are aliases)
s.size();
s.len();
s.length();
```

### Set algebra

```java
a = set{ 1, 2, 3 };
b = set{ 3, 4, 5 };

// Union - all unique elements
u = a.union( b );        // {1, 2, 3, 4, 5}
u = a + b;               // operator shorthand

// Intersection - common elements
i = a.intersection( b ); // {3}
i = a * b;               // operator shorthand

// Difference - in A but not B
d = a.difference( b );   // {1, 2}
d = a - b;               // operator shorthand

// Symmetric difference - in either but not both
x = a.symmetricDifference( b ); // {1, 2, 4, 5}
x = a ^ b;                      // operator shorthand
```

### Functional operations

```java
s = [ 1, 2, 3, 4, 5 ].toSet();

// Map - transform elements
doubled = s.map( v -> v * 2 );

// Filter - keep matching
evens = s.filter( v -> v % 2 == 0 );

// Reduce - combine to single value
total = s.reduce( (acc, v) -> acc + v, 0 );

// Predicates
s.every( v -> v > 0 );     // true
s.some( v -> v > 4 );      // true
s.none( v -> v < 0 );      // true

// Find first match
found = s.find( v -> v > 2 );
```

### Converting sets back

```java
s = setNew( type="linked", values=[ "a", "b", "c" ] );

// To array
arr = s.toArray();

// To list string
list = s.toList();
list = s.toList( "-" );    // custom delimiter
```

### Struct key/value sets

```java
data = { name: "Luis", age: 42, email: "x@y.z" };

// Get keys as a set
keys = data.keySet();

// Get values as a set (deduplicated)
values = data.valueSet();
```

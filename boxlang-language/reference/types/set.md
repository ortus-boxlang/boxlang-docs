[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Set`



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

## Set Methods

<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</details>
<details>
<summary><code>duplicate(deep=[boolean])</code></summary>

Duplicates an object - either shallow or deep

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `deep` | `boolean` | `false` | `true` |

</details>
<details>
<summary><code>size()</code></summary>

Returns the absolute value of a number
</details>
<details>
<summary><code>len()</code></summary>

Returns the absolute value of a number
</details>
<details>
<summary><code>length()</code></summary>

Returns the absolute value of a number
</details>
<details>
<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct, query or set to its Unmodifiable counterpart.
</details>
<details>
<summary><code>toModifiable()</code></summary>

Convert an array, struct, query or set to its Modifiable counterpart.
</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>,Query Format Options,</h2>,
 The ,<code>,queryFormat,</code>, argument determines how queries are serialized:
 ,<ul>,
 ,<li>,<code>,row,</code>, or ,<code>,false,</code>,: Serializes the query as a top-level struct with two keys:
 ,<code>,columns,</code>, (an array of column names) and ,<code>,data,</code>, (an array of arrays representing
 each row's data).,</li>,
 ,<li>,<code>,column,</code>, or ,<code>,true,</code>,: Serializes the query as a top-level struct with three keys:
 ,<code>,rowCount,</code>, (the number of rows), ,<code>,columns,</code>, (an array of column names), and
 ,<code>,data,</code>, (a struct where each key is a column name and the value is an array of values for that column).,</li>,
 ,<li>,<code>,struct,</code>,: Serializes the query as an array of structs, where each struct represents a row of data.,</li>,
 ,</ul>,

 ,<h2>,Usage,</h2>,

 ,<pre>,
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `null` |
| `useSecureJSONPrefix` | `string` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `null` |
| `pretty` | `boolean` | `false` | `false` |

</details>
<details>
<summary><code>isEmpty()</code></summary>

Test whether a Set contains no elements.

Returns true for an empty Set, false if it has one or more elements.
</details>
<details>
<summary><code>isSupersetOf(otherSet=[any])</code></summary>

Test whether every element of set B is also contained in set A, i.e.

A \u2287 B. A set is always a superset
 of the empty set. Returns true if A is a superset of B, false otherwise.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>reject(callback=[function:Predicate])</code></summary>

Return a new Set containing only the elements of the source Set for which the predicate returns false
 (the inverse of setFilter).

The result is a new Set of the same variant as the source; the source is not
 modified. The predicate receives the element value, its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>isDisjointFrom(otherSet=[any])</code></summary>

Test whether two Sets share no common elements, i.e.

their intersection is empty. Returns true if the two
 Sets are disjoint, false if they have at least one element in common.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>retainAll(values=[any])</code></summary>

Retain only the elements of a Set that are also present in the given collection, removing everything else.

This is the in-place equivalent of computing an intersection. The Set is modified in place and returned to
 support method chaining.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `values` | `any` | `true` | `null` |

</details>
<details>
<summary><code>union(otherSet=[any])</code></summary>

Compute the union (A \u222a B) of two Sets, returning a new Set that contains all elements from both.

Duplicates are automatically deduplicated. The result is a new Set of the same variant as A; neither
 input is modified.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>each(callback=[function:Consumer])</code></summary>

Invoke a callback for every element of a Set.

The callback receives the element value, its 1-based ordinal
 position, and the Set itself; single-argument callbacks receive only the value. Iteration follows the natural
 order of the underlying variant. Use setMap() if you need a transformed result.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Consumer` | `true` | `null` |

</details>
<details>
<summary><code>toList(delimiter=[string])</code></summary>

Join the elements of a Set into a delimited string.

Each element is cast to a String before joining.
 For LINKED Sets the insertion order is preserved; for SORTED Sets the natural ordering applies; for
 default hash Sets the order is undefined.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |

</details>
<details>
<summary><code>filter(callback=[function:Predicate])</code></summary>

Return a new Set containing only the elements of the source Set for which the predicate returns true.

The
 result is a new Set of the same variant as the source; the source is not modified. The predicate receives
 the element value, its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>symmetricDifference(otherSet=[any])</code></summary>

Compute the symmetric difference (A \u25b3 B) of two Sets, returning the elements that are in exactly one of
 the two Sets but not in both.

Equivalent to ,{@code (A \u222a B) \u2212 (A \u2229 B)},. The result is a new Set of the same
 variant as A; neither input is modified.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

Left-fold a Set with an accumulator function, reducing it to a single value.

The callback receives the
 current accumulator, the element value, its 1-based ordinal position, and the Set itself, and returns the
 new accumulator. Iteration follows the natural order of the underlying variant.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:BiFunction` | `true` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>difference(otherSet=[any])</code></summary>

Compute the relative complement (A \u2212 B) of two Sets.

Returns a new Set containing all elements that are in
 A but not in B. The result is a new Set of the same variant as A; neither input is modified.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>addAll(values=[any])</code></summary>

Add every element of a collection into a Set, deduplicating automatically.

The source collection can be
 an Array, another Set, a list-delimited String, or any value castable to a Set. The Set is modified in
 place and returned to support method chaining.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `values` | `any` | `true` | `null` |

</details>
<details>
<summary><code>intersection(otherSet=[any])</code></summary>

Compute the intersection (A \u2229 B) of two Sets, returning a new Set that contains only the elements present
 in both A and B.

The result is a new Set of the same variant as A; neither input is modified.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>equals(otherSet=[any])</code></summary>

Test whether two Sets contain exactly the same elements.

The comparison is variant-agnostic: a hash Set and
 a linked Set with identical elements are considered equal. Returns true if both sets have the same size and
 every element of one is present in the other.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>
<details>
<summary><code>toArray()</code></summary>

Convert a Set to an Array, preserving the iteration order of the underlying variant.

For a LINKED Set the
 insertion order is preserved; for a SORTED Set the natural ordering applies; for a default hash Set the
 order is undefined. The source Set is not modified.
</details>
<details>
<summary><code>containsAll(values=[any])</code></summary>

Test whether a Set contains every element of a given collection.

The collection can be an Array, another
 Set, a list-delimited String, or any value castable to a Set. Returns true only if all elements are present.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `values` | `any` | `true` | `null` |

</details>
<details>
<summary><code>clear()</code></summary>

Remove all elements from a Set, leaving it empty.

The Set is modified in place and returned to support
 method chaining.
</details>
<details>
<summary><code>remove(value=[any])</code></summary>

Remove an element from a Set.

If the value is not present the call is a no-op. The Set is modified in
 place and returned to support method chaining.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>delete(value=[any])</code></summary>

Remove an element from a Set.

If the value is not present the call is a no-op. The Set is modified in
 place and returned to support method chaining.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>some(callback=[function:Predicate])</code></summary>

Test whether at least one element of a Set satisfies a predicate.

Iteration short-circuits on the first
 element for which the predicate returns true. Returns false for an empty Set. The predicate receives the
 element value, its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>any(callback=[function:Predicate])</code></summary>

Test whether at least one element of a Set satisfies a predicate.

Iteration short-circuits on the first
 element for which the predicate returns true. Returns false for an empty Set. The predicate receives the
 element value, its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>find(callback=[function:Predicate])</code></summary>

Return the first element of a Set for which the predicate returns true, or null if no element matches.

Iteration follows the natural order of the underlying variant and stops at the first match. The predicate
 receives the element value, its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>contains(value=[any])</code></summary>

Test whether a Set contains a given value using BoxLang value equality.

Returns true if the value is
 present, false otherwise.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>has(value=[any])</code></summary>

Test whether a Set contains a given value using BoxLang value equality.

Returns true if the value is
 present, false otherwise.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>map(callback=[function:Function])</code></summary>

Apply a transform function to every element of a Set and collect the deduplicated results into a new Set
 of the same variant.

The source Set is not modified. The callback receives the element value, its 1-based
 ordinal position, and the original Set.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Function` | `true` | `null` |

</details>
<details>
<summary><code>removeAll(values=[any])</code></summary>

Remove every element of a collection from a Set, leaving only the elements that are not in the collection.

The Set is modified in place and returned to support method chaining. Elements not present in the Set are
 silently skipped.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `values` | `any` | `true` | `null` |

</details>
<details>
<summary><code>add(value=[any])</code></summary>

Add an element to a Set, deduplicating automatically.

If the value is already present, the call is a
 no-op. The Set is modified in place and returned to support method chaining.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>append(value=[any])</code></summary>

Add an element to a Set, deduplicating automatically.

If the value is already present, the call is a
 no-op. The Set is modified in place and returned to support method chaining.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `any` | `true` | `null` |

</details>
<details>
<summary><code>every(callback=[function:Predicate])</code></summary>

Test whether every element of a Set satisfies a predicate.

Iteration short-circuits on the first element
 for which the predicate returns false. Returns true for an empty Set (vacuous truth). The predicate receives
 the element value, its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>none(callback=[function:Predicate])</code></summary>

Test whether no element of a Set satisfies a predicate.

Iteration short-circuits on the first element for
 which the predicate returns true. Returns true for an empty Set. The predicate receives the element value,
 its 1-based ordinal position, and the Set itself.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |

</details>
<details>
<summary><code>isSubsetOf(otherSet=[any])</code></summary>

Test whether every element of set A is also contained in set B, i.e.

A \u2286 B. An empty set is always a
 subset of any set. Returns true if A is a subset of B, false otherwise.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `otherSet` | `any` | `true` | `null` |

</details>


## Examples

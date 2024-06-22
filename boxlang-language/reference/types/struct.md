[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Struct`

This type provides the core map class for Boxlang.

Structs are highly versatile and are used for organizing and managing related data.

 Types of Structs in BoxLang:

 * Basic Structs: These are the basic structures where each key is associated with a single value. Keys are case-insensitive and can be strings or symbols.
 * Nested Structs: Structs can contain other structs as values, allowing for a hierarchical organization of data.
 * Case-Sensitive Structs: By default, BoxLang structs are case-insensitive. However, you can create case-sensitive structs if needed.
 * Ordered Structs: This implementation of a Struct maintains keys in the order they were added.
 * Sorted Structs: This implementation of a Struct maintains keys in specified sorted order.

## Examples

### Creating structs using the function `structNew`

```java
// Create a default struct ( unordered )
myStruct = structNew();

// Create an ordered struct which will maintain key order of insertion
myStruct = structNew( "ordered" );

// Create a case-sensitive struct which will require key access to use the exact casing
myStruct = structNew( "casesenstive" );
myStruct[ "cat" ] = "pet";
myStruct[ "Cat" ] = "wild";

// Create a sorted struct 
myStruct = structNew( "sorted", "textAsc" )
```


### Creating structs using object literal syntax

```java
// Create an empty default struct ( unordered )
myStruct = {};

// Create an empty struct and populate it with values
animals = {
  cow: "moo",
  pig: "oink"
};

// Create an ordered struct which will maintain key order of insertion
// Note that you must provide the ordered struct with data to prevent confusion as to whether it is an array or struct
orderedAnimals = [
  cow: "moo",
  pig: "oink"
];
```


## Struct Methods

<details>
<summary><code>append(struct2=[structloose], overwrite=[boolean])</code></summary>

Appends the contents of a second struct to the first struct either with or without overwrite

Examples:
*Append One Struct to Another:*

```java
animals = {
  cow: "moo",
  pig: "oink"
};

// Show current animals
animals.dump( label ="Current animals" );

// Create a new animal
newAnimal = {
  cat: "meow"
};

// Append the newAnimal to animals
animals.append( newAnimal );

animals.dump( label="Updated animals" );
```


 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `struct2` | `struct` | `true` | `null` |
| `overwrite` | `boolean` | `false` | `true` |


</details>
<details>
<summary><code>clear()</code></summary>

Clear all items from struct

</details>
<details>
<summary><code>copy()</code></summary>

Creates a shallow copy of a struct.

Copies top-level keys, values, and arrays in the structure by value; copies nested structures by reference.

</details>
<details>
<summary><code>count()</code></summary>

Returns the absolute value of a number

</details>
<details>
<summary><code>delete(key=[string], indicateNotExists=[boolean])</code></summary>

Deletes a key from a struct

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |
| `indicateNotExists` | `boolean` | `false` | `false` |


</details>
<details>
<summary><code>each(callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean])</code></summary>

Used to iterate over a struct and run the function closure for each key/value pair.

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `ordered` | `boolean` | `false` | `false` |


</details>
<details>
<summary><code>equals(struct2=[structloose])</code></summary>

Tests equality between two structs

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `struct2` | `struct` | `true` | `null` |


</details>
<details>
<summary><code>every(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>

Used to iterate over a struct and test whether every item in the struct meets the test.

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |


</details>
<details>
<summary><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>

Used to filter a struct and return a new struct containing the result

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |


</details>
<details>
<summary><code>find(key=[string], defaultValue=[any])</code></summary>

Finds and retrieves a top-level key from a string in a struct

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |
| `defaultValue` | `any` | `false` | `null` |


</details>
<details>
<summary><code>findKey(key=[string], scope=[string])</code></summary>

Searches a struct for a given key and returns an array of values

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |
| `scope` | `string` | `false` | `one` |


</details>
<details>
<summary><code>findValue(value=[string], scope=[string])</code></summary>

Searches a struct for a given value and returns an array of results

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `null` |
| `scope` | `string` | `false` | `one` |


</details>
<details>
<summary><code>getFromPath(path=[string])</code></summary>

Retrieves the value from a struct using a path based expression

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `path` | `string` | `true` | `null` |


</details>
<details>
<summary><code>getMetadata()</code></summary>

Gets Struct-specific metadata of the requested struct.

</details>
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
<summary><code>insert(key=[string], value=[any], overwrite=[boolean])</code></summary>

Inserts a key/value pair in to a struct - with an optional overwrite argument

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |
| `value` | `any` | `true` | `null` |
| `overwrite` | `boolean` | `false` | `false` |


</details>
<details>
<summary><code>isCaseSensitive()</code></summary>

Returns whether the give struct is case sensitive

</details>
<details>
<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty

</details>
<details>
<summary><code>isOrdered()</code></summary>

Tests whether a struct is ordered ( e.g.

linked )

</details>
<details>
<summary><code>keyArray()</code></summary>

Get keys of a struct as an array

</details>
<details>
<summary><code>keyExists(key=[string])</code></summary>

Tests whether a key exists in a struct and returns a boolean value

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |


</details>
<details>
<summary><code>keyList(delimiter=[string])</code></summary>

Get keys of a struct as a string list

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |


</details>
<details>
<summary><code>len()</code></summary>

Returns the absolute value of a number

</details>
<details>
<summary><code>map(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>

Used to map a struct to a new struct of the same type containing the result

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |


</details>
<details>
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>

Run the provided udf against struct to reduce the values to a single output

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `initialValue` | `any` | `false` | `null` |


</details>
<details>
<summary><code>some(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>

Used to iterate over a struct and test whether any items meet the test callback.

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |


</details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], path=[string], callback=[function])</code></summary>

Sorts a struct according to the specified arguments and returns an array of struct keys

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `text` |
| `sortOrder` | `string` | `false` | `asc` |
| `path` | `string` | `false` | `null` |
| `callback` | `function` | `false` | `null` |


</details>
<details>
<summary><code>toImmutable()</code></summary>

Convert an array, struct or query to its immutable counterpart.

</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></summary>

Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `null` |


</details>
<details>
<summary><code>toMutable()</code></summary>

Convert an array, struct or query to its mutable counterpart.

</details>
<details>
<summary><code>toQueryString(delimiter=[string])</code></summary>

Converts a struct to a query string using the specified delimiter.

<p>,
 The default delimiter is ,{@code "&"}

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `&` |


</details>
<details>
<summary><code>toSorted(sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function])</code></summary>

Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `text` |
| `sortOrder` | `string` | `false` | `asc` |
| `localeSensitive` | `any` | `false` | `false` |
| `callback` | `function` | `false` | `null` |


</details>
<details>
<summary><code>translateKeys(deep=[boolean], retainKeys=[boolean])</code></summary>

Converts a struct with dot-notated keys in to an unflattened version

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `deep` | `boolean` | `false` | `false` |
| `retainKeys` | `boolean` | `false` | `false` |


</details>
<details>
<summary><code>update(key=[string], value=[any])</code></summary>

Updates or sets a key/value pair in to a struct

 Arguments:


| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |
| `value` | `any` | `true` | `null` |


</details>
<details>
<summary><code>valueArray()</code></summary>

Returns an array of all values of top level keys in a struct

</details>


## Examples

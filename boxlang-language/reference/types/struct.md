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
<p>Appends the contents of a second struct to the first struct either with or without overwrite

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
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`struct2`</td>
<td>`structloose`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`overwrite`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`true`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>clear()</code></summary>
<p>Clear all items from struct
</p></details>
<details>
<summary><code>copy()</code></summary>
<p>Creates a shallow copy of a struct.

Copies top-level keys, values, and arrays in the structure by value; copies nested structures by reference.
</p></details>
<details>
<summary><code>count()</code></summary>
<p>Returns the absolute value of a number
</p></details>
<details>
<summary><code>delete(key=[string], indicateNotExists=[boolean])</code></summary>
<p>Deletes a key from a struct

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`indicateNotExists`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>each(callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean])</code></summary>
<p>Used to iterate over a struct and run the function closure for each key/value pair.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`ordered`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>equals(struct2=[structloose])</code></summary>
<p>Tests equality between two structs

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`struct2`</td>
<td>`structloose`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>every(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Used to iterate over a struct and test whether every item in the struct meets the test.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Used to filter a struct and return a new struct containing the result

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>find(key=[string], defaultValue=[any])</code></summary>
<p>Finds and retrieves a top-level key from a string in a struct

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`defaultValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findKey(key=[string], scope=[string])</code></summary>
<p>Searches a struct for a given key and returns an array of values

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`false`</td>
<td>`one`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>findValue(value=[string], scope=[string])</code></summary>
<p>Searches a struct for a given value and returns an array of results

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`value`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`scope`</td>
<td>`string`</td>
<td>`false`</td>
<td>`one`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>getFromPath(path=[string])</code></summary>
<p>Retrieves the value from a struct using a path based expression

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`path`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>getMetadata()</code></summary>
<p>Gets Struct-specific metadata of the requested struct.
</p></details>
<details>
<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>
<p>Creates an algorithmic hash of an object

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`algorithm`</td>
<td>`string`</td>
<td>`false`</td>
<td>`MD5`</td>
</tr>

<tr>
<td>`encoding`</td>
<td>`string`</td>
<td>`false`</td>
<td>`utf-8`</td>
</tr>

<tr>
<td>`numIterations`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`1`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>insert(key=[string], value=[any], overwrite=[boolean])</code></summary>
<p>Inserts a key/value pair in to a struct - with an optional overwrite argument

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`overwrite`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>isCaseSensitive()</code></summary>
<p>Returns whether the give struct is case sensitive
</p></details>
<details>
<summary><code>isEmpty()</code></summary>
<p>Determine whether a given value is empty
</p></details>
<details>
<summary><code>isOrdered()</code></summary>
<p>Tests whether a struct is ordered ( e.g.

linked )
</p></details>
<details>
<summary><code>keyArray()</code></summary>
<p>Get keys of a struct as an array
</p></details>
<details>
<summary><code>keyExists(key=[string])</code></summary>
<p>Tests whether a key exists in a struct and returns a boolean value

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>keyList(delimiter=[string])</code></summary>
<p>Get keys of a struct as a string list

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`,`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>len()</code></summary>
<p>Returns the absolute value of a number
</p></details>
<details>
<summary><code>map(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Used to map a struct to a new struct of the same type containing the result

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>
<p>Run the provided udf against struct to reduce the values to a single output

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>some(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Used to iterate over a struct and test whether any items meet the test callback.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parallel`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`maxThreads`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], path=[string], callback=[function])</code></summary>
<p>Sorts a struct according to the specified arguments and returns an array of struct keys

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`sortType`</td>
<td>`any`</td>
<td>`false`</td>
<td>`text`</td>
</tr>

<tr>
<td>`sortOrder`</td>
<td>`string`</td>
<td>`false`</td>
<td>`asc`</td>
</tr>

<tr>
<td>`path`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toImmutable()</code></summary>
<p>Convert an array, struct or query to its immutable counterpart.
</p></details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></summary>
<p>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`queryFormat`</td>
<td>`string`</td>
<td>`false`</td>
<td>`row`</td>
</tr>

<tr>
<td>`useSecureJSONPrefix`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`useCustomSerializer`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toMutable()</code></summary>
<p>Convert an array, struct or query to its mutable counterpart.
</p></details>
<details>
<summary><code>toQueryString(delimiter=[string])</code></summary>
<p>Converts a struct to a query string using the specified delimiter.

<p>,
 The default delimiter is ,{@code "&"}

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`delimiter`</td>
<td>`string`</td>
<td>`false`</td>
<td>`&`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toSorted(sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function])</code></summary>
<p>Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`sortType`</td>
<td>`any`</td>
<td>`false`</td>
<td>`text`</td>
</tr>

<tr>
<td>`sortOrder`</td>
<td>`string`</td>
<td>`false`</td>
<td>`asc`</td>
</tr>

<tr>
<td>`localeSensitive`</td>
<td>`any`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`callback`</td>
<td>`function`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>translateKeys(deep=[boolean], retainKeys=[boolean])</code></summary>
<p>Converts a struct with dot-notated keys in to an unflattened version

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`deep`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr>

<tr>
<td>`retainKeys`</td>
<td>`boolean`</td>
<td>`false`</td>
<td>`false`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>update(key=[string], value=[any])</code></summary>
<p>Updates or sets a key/value pair in to a struct

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`key`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`value`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>valueArray()</code></summary>
<p>Returns an array of all values of top level keys in a struct
</p></details>


## Examples

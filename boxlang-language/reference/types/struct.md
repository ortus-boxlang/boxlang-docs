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

## Struct Methods

<dl>
<dt><code>append(struct2=[structloose], overwrite=[boolean])</code></dt><dd>Appends the contents of a second struct to the first struct either with or without overwrite

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `struct2` | `structloose` | `true` | `` |
| `overwrite` | `boolean` | `false` | `true` |

</dd>
<dt><code>clear()</code></dt><dd>Clear all items from struct</dd>
<dt><code>copy()</code></dt><dd>Creates a shallow copy of a struct.

Copies top-level keys, values, and arrays in the structure by value; copies nested structures by reference.</dd>
<dt><code>count()</code></dt><dd>Returns the absolute value of a number</dd>
<dt><code>delete(key=[string], indicateNotExists=[boolean])</code></dt><dd>Deletes a key from a struct

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |
| `indicateNotExists` | `boolean` | `false` | `false` |

</dd>
<dt><code>each(callback=[function], parallel=[boolean], maxThreads=[integer], ordered=[boolean])</code></dt><dd>Used to iterate over a struct and run the function closure for each key/value pair.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `ordered` | `boolean` | `false` | `false` |

</dd>
<dt><code>equals(struct2=[structloose])</code></dt><dd>Tests equality between two structs

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `struct2` | `structloose` | `true` | `` |

</dd>
<dt><code>every(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Used to iterate over a struct and test whether every item in the struct meets the test.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Used to filter a struct and return a new struct containing the result

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>find(key=[string], defaultValue=[any])</code></dt><dd>Finds and retrieves a top-level key from a string in a struct

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |
| `defaultValue` | `any` | `false` | `` |

</dd>
<dt><code>findKey(key=[string], scope=[string])</code></dt><dd>Searches a struct for a given key and returns an array of values

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |
| `scope` | `string` | `false` | `one` |

</dd>
<dt><code>findValue(value=[string], scope=[string])</code></dt><dd>Searches a struct for a given value and returns an array of results

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `string` | `true` | `` |
| `scope` | `string` | `false` | `one` |

</dd>
<dt><code>getFromPath(path=[string])</code></dt><dd>Retrieves the value from a struct using a path based expression

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `path` | `string` | `true` | `` |

</dd>
<dt><code>getMetadata()</code></dt><dd>Gets Struct-specific metadata of the requested struct.</dd>
<dt><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></dt><dd>Creates an algorithmic hash of an object

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `algorithm` | `string` | `false` | `MD5` |
| `encoding` | `string` | `false` | `utf-8` |
| `numIterations` | `integer` | `false` | `1` |

</dd>
<dt><code>insert(key=[string], value=[any], overwrite=[boolean])</code></dt><dd>Inserts a key/value pair in to a struct - with an optional overwrite argument

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |
| `value` | `any` | `true` | `` |
| `overwrite` | `boolean` | `false` | `false` |

</dd>
<dt><code>isCaseSensitive()</code></dt><dd>Returns whether the give struct is case sensitive</dd>
<dt><code>isEmpty()</code></dt><dd>Determine whether a given value is empty</dd>
<dt><code>isOrdered()</code></dt><dd>Tests whether a struct is ordered ( e.g.

linked )</dd>
<dt><code>keyArray()</code></dt><dd>Get keys of a struct as an array</dd>
<dt><code>keyExists(key=[string])</code></dt><dd>Tests whether a key exists in a struct and returns a boolean value

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |

</dd>
<dt><code>keyList(delimiter=[string])</code></dt><dd>Get keys of a struct as a string list

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |

</dd>
<dt><code>len()</code></dt><dd>Returns the absolute value of a number</dd>
<dt><code>map(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Used to map a struct to a new struct of the same type containing the result

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>reduce(callback=[function], initialValue=[any])</code></dt><dd>Run the provided udf against struct to reduce the values to a single output

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>some(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Used to iterate over a struct and test whether any items meet the test callback.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>sort(sortType=[any], sortOrder=[string], path=[string], callback=[function])</code></dt><dd>Sorts a struct according to the specified arguments and returns an array of struct keys

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `text` |
| `sortOrder` | `string` | `false` | `asc` |
| `path` | `string` | `false` | `` |
| `callback` | `function` | `false` | `` |

</dd>
<dt><code>toImmutable()</code></dt><dd>Convert an array, struct or query to its immutable counterpart.</dd>
<dt><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></dt><dd>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `` |

</dd>
<dt><code>toMutable()</code></dt><dd>Convert an array, struct or query to its mutable counterpart.</dd>
<dt><code>toQueryString(delimiter=[string])</code></dt><dd>Converts a struct to a query string using the specified delimiter.

<p>,
 The default delimiter is ,{@code "&"}

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `&` |

</dd>
<dt><code>toSorted(sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function])</code></dt><dd>Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortType` | `any` | `false` | `text` |
| `sortOrder` | `string` | `false` | `asc` |
| `localeSensitive` | `any` | `false` | `false` |
| `callback` | `function` | `false` | `` |

</dd>
<dt><code>translateKeys(deep=[boolean], retainKeys=[boolean])</code></dt><dd>Converts a struct with dot-notated keys in to an unflattened version

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `deep` | `boolean` | `false` | `false` |
| `retainKeys` | `boolean` | `false` | `false` |

</dd>
<dt><code>update(key=[string], value=[any])</code></dt><dd>Updates or sets a key/value pair in to a struct

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |
| `value` | `any` | `true` | `` |

</dd>
<dt><code>valueArray()</code></dt><dd>Returns an array of all values of top level keys in a struct</dd>

</dl>

## Examples

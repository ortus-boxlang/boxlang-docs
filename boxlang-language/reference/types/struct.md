
# Type: `Struct`

This type provides the core map class for Boxlang.

Structs are highly versatile and are used for organizing and managing related data.

 Types of Structs in BoxLang: <code>DEFAULT, CASE_SENSITIVE, LINKED, LINKED_CASE_SENSITIVE, SORTED, WEAK, SOFT</code>

 - DEFAULT: These are the basic structures where each key is associated with a single value. Keys are case-insensitive and can be strings or symbols.
 - Nested Structs: Structs can contain other structs as values, allowing for a hierarchical organization of data.
 - CASE_SENSITIVE: By default, BoxLang structs are case-insensitive. However, you can create case-sensitive structs if needed.
 - LINKED, LINKED_CASE_SENSITIVE (Ordered Structs): This implementation of a Struct maintains keys in the order they were added.
 - SORTED: This implementation of a Struct maintains keys in specified sorted order.
 - WEAK: This implementation of a Struct uses weak references for keys.
 - SOFT: This implementation of a Struct uses a default struct with values wrapped in a SoftReference.

## Struct Methods

<details>
<summary><code>append(struct2=[structloose], overwrite=[boolean])</code></summary>

Appends the contents of a second struct to the first struct either with or
 without overwrite

### Method Signature

```
append(struct2=[structloose], overwrite=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct2` | `struct` | `true` | The struct containing the values to be appended |  |
| `overwrite` | `boolean` | `false` | Default true. Whether to overwrite existing values found<br>                     in struct1 from the values in struct2 | `true` |

### Examples

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
</details>
<details>
<summary><code>bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

<p>
 The available <code>output</code> locations are:
 - <strong>buffer</strong>: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser.
 - <strong>console</strong>: The output is printed to the System console.
 - <strong>Absolute File Path</strong> The output is written to a file with the specified absolute file path.
 </p>
 
 The output `format` can be either HTML or plain text.
 
 The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

### Method Signature

```
bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `label` | `string` | `false` | A custom label to display above the dump (Only in HTML output) |  |
| `depth` | `numeric` | `false` | The recursion depth to display when dumping nested collections. 1-based: -1 (default) is unlimited, 0 shows nothing,<br>                 1 shows the top level with no recursion, 2 recurses once, etc. (Only in HTML output) |  |
| `maxRows` | `numeric` | `false` | The maximum number of keys/rows/items to display per level of a collection, array, or query. 1-based: -1 (default)<br>                   is unlimited, 0 shows nothing, 1 shows a single row, etc. (Only in HTML output) |  |
| `top` | `numeric` | `false` | Deprecated: use maxRows instead. When maxRows is not also passed, top's value is used as maxRows.<br>               Kept for backwards compatibility with existing BoxLang code. (Only in HTML output) |  |
| `expand` | `boolean` | `false` | Whether to expand the dump. Be default, we try to expand as much as possible. (Only in HTML output) | `true` |
| `abort` | `boolean` | `false` | Whether to do a hard abort the request after dumping. Default is false | `false` |
| `output` | `string` | `false` | The output format which can be "buffer", "console", or "{absolute file path}". The default is "buffer". |  |
| `format` | `string` | `false` | The format of the output to a <strong>filename</strong>. Can be "html" or "text". The default is according to the output location. |  |
| `showUDFs` | `boolean` | `false` | Show UDFs or not. Default is true. (Only in HTML output) | `true` |
</details>
<details>
<summary><code>clear()</code></summary>

Clear all items from struct

### Method Signature

```
clear()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>copy()</code></summary>

Creates a shallow copy of a struct.

Copies top-level keys, values, and arrays in the structure by value; copies nested structures by reference.

### Method Signature

```
copy()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>count()</code></summary>

Returns the absolute value of a number

### Method Signature

```
count()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>delete(key=[any])</code></summary>

Deletes a key from a struct

### Method Signature

```
delete(key=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The key to delete |  |
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
<summary><code>each(callback=[function:BiConsumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])</code></summary>

Used to iterate over a struct and run the function closure for each key/value pair.

<p>
 The function will be passed 3 arguments: the key, the value, and the struct.
 You can alternatively pass a Java BiConsumer which will only receive the first 2 args (key and value).
 <p>
 This BIF is useful for performing side effects on each item in the struct, such as logging or modifying external state.
 <p>

 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
each(callback=[function:BiConsumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiConsumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiConsumer which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `ordered` | `boolean` | `false` | Whether parallel operations should execute and maintain order | `false` |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>equals(struct2=[structloose])</code></summary>

Tests equality between two structs

### Method Signature

```
equals(struct2=[structloose])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `struct2` | `struct` | `true` | The struct to test for equality |  |
</details>
<details>
<summary><code>every(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a struct and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the struct.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large structs, especially when the test function is computationally expensive or the struct is large.

### Method Signature

```
every(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiPredicate` | `true` | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If parallel is true and maxThreads is not passed, it will use the common ForkJoinPool. |  |
| `virtual` | `boolean` | `false` | Whether to use a virtual thread for each task when running in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>filter(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters a struct and returns a new struct with the values that pass the filter criteria.

This BIF will invoke the callback function for each entry in the struct, passing the key, value, and the struct itself.
 <ul>
 <li>If the callback returns true, the entry will be included in the new struct.</li>
 <li>If the callback returns false, the entry will be excluded from the new struct.</li>
 <li>If the callback requires strict arguments, it will only receive the key and value.</li>
 <li>If the callback does not require strict arguments, it will receive the key, value, and the original struct.</li>
 </ul>
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
filter(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiPredicate` | `true` | The function used to filter. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>find(key=[any], defaultValue=[any])</code></summary>

Finds and retrieves a top-level key from a string in a struct

### Method Signature

```
find(key=[any], defaultValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The key to search |  |
| `defaultValue` | `any` | `false` | An optional value to be returned if the struct does not contain the key |  |
</details>
<details>
<summary><code>findKey(key=[any], scope=[string])</code></summary>

Searches a struct for a given key and returns an array of values

### Method Signature

```
findKey(key=[any], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The key to search for |  |
| `scope` | `string` | `false` | Either one (default), which finds the first instance or all to return all values | `one` |
</details>
<details>
<summary><code>findValue(value=[string], scope=[string])</code></summary>

Searches a struct for a given value and returns an array of results

### Method Signature

```
findValue(value=[string], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `string` | `true` | The value to search for |  |
| `scope` | `string` | `false` | Either one (default), which finds the first instance or all to return all values | `one` |
</details>
<details>
<summary><code>getFromPath(path=[string])</code></summary>

Retrieves the value from a struct using a path based expression

### Method Signature

```
getFromPath(path=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The string path to the object requested in the struct |  |
</details>
<details>
<summary><code>getMetadata()</code></summary>

Gets Struct-specific metadata of the requested struct.

### Method Signature

```
getMetadata()
```

### Arguments

This function does not accept any arguments
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
<summary><code>insert(key=[any], value=[any], overwrite=[boolean])</code></summary>

Inserts a key/value pair in to a struct - with an optional overwrite argument

### Method Signature

```
insert(key=[any], value=[any], overwrite=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The struct key |  |
| `value` | `any` | `true` | The value to assign for the specified key |  |
| `overwrite` | `boolean` | `false` | Whether to overwrite the existing value if the key exists ( default: false ) | `false` |
</details>
<details>
<summary><code>isCaseSensitive()</code></summary>

Returns whether the give struct is case sensitive

### Method Signature

```
isCaseSensitive()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of
 anything that can be casted to: Array, Struct, Query, or String.

### Method Signature

```
isEmpty()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>isOrdered()</code></summary>

Tests whether a struct is ordered ( e.g.

linked )

### Method Signature

```
isOrdered()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>keyArray()</code></summary>

Get keys of a struct as an array

### Method Signature

```
keyArray()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>keyExists(key=[any])</code></summary>

Tests whether a key exists in a struct and returns a boolean value

### Method Signature

```
keyExists(key=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The key within the struct to test for existence |  |
</details>
<details>
<summary><code>keyList(delimiter=[string])</code></summary>

Get keys of a struct as a string list

### Method Signature

```
keyList(delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | The delimiter to use between the keys in the returned list. Defaults to a comma. | `,` |
</details>
<details>
<summary><code>keySet(type=[string])</code></summary>

Build a Set containing the keys of a Struct.

Key names are extracted as plain Strings via Key.getName(),
 so the resulting Set always holds String values. The backing variant can be configured; use "linked" to
 preserve the Struct's iteration order.

### Method Signature

```
keySet(type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet,<br>                preserves Struct iteration order), or "sorted" / "tree" (TreeSet, alphabetical order). | `default` |
</details>
<details>
<summary><code>keyTranslate(deep=[boolean], retainKeys=[boolean])</code></summary>

Converts a struct with dot-notated keys in to an unflattened version

### Method Signature

```
keyTranslate(deep=[boolean], retainKeys=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `deep` | `boolean` | `false` | Whether to recurse in to nested keys - default false | `false` |
| `retainKeys` | `boolean` | `false` | Whether to retain the original dot-notated keys - default false | `false` |
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
<summary><code>map(callback=[function:BiFunction], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

This BIF will iterate over each key-value pair in the struct and invoke the callback function for each item so you can do
 any operation on the key-value pair and return a new value that will be set in a new struct.

The callback function will be passed the key, the value, and the original struct.
 <ul>
 <li>If the callback requires strict arguments, it will only receive the key and value.</li>
 <li>If the callback does not require strict arguments, it will receive the key, value, and the original struct.</li>
 </ul>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
map(callback=[function:BiFunction], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function used to produce the right-hand value assignment in the new struct. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiFunction which will only receive the<br>                    first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>none(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a struct and test whether <strong>NONE</strong> item meets the test callback.

This is the opposite of <code>StructSome</code>.
 <p>
 The function will be passed 3 arguments: the value, the index, and the struct.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large structs, especially when the test function is computationally expensive or the struct is large.

### Method Signature

```
none(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiPredicate` | `true` | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If parallel is true and maxThreads is not passed, it will use the common ForkJoinPool. |  |
| `virtual` | `boolean` | `false` | Whether to use a virtual thread for each task when running in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>

Run the provided udf against struct to reduce the values to a single output

### Method Signature

```
reduce(callback=[function], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function` | `true` | The function to invoke for each entry in the struct. The function will be passed 4 arguments: the accumulator, they entry key,<br>                    the<br>                    current index, and the original struct. The function should return the new accumulator value. |  |
| `initialValue` | `any` | `false` | The initial value of the accumulator |  |
</details>
<details>
<summary><code>some(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a struct and test whether <strong>ANY</strong> items meet the test callback.

The function will be passed 3 arguments: the key, the value, and the struct.
 You can alternatively pass a Java BiPredicate which will only receive the first 2 args.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.
 <p>

### Method Signature

```
some(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiPredicate` | `true` | The function used to test. The function will be passed 3 arguments: the key, the value, the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If parallel is true and maxThreads is not passed, it will use the common ForkJoinPool. |  |
| `virtual` | `boolean` | `false` | Whether to use a virtual thread for each task when running in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], path=[string], callback=[function:Comparator])</code></summary>

Sorts a struct according to the specified arguments and returns an array of struct keys

### Method Signature

```
sort(sortType=[any], sortOrder=[string], path=[string], callback=[function:Comparator])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sortType` | `any` | `false` | An optional sort type to apply to that type - if a callback is given in this position it will be used as that argument | `text` |
| `sortOrder` | `string` | `false` | The sort order applicable to the sortType argument | `asc` |
| `path` | `string` | `false` | An optional key path used to sort by a nested value within each struct entry (e.g. "address.city"). |  |
| `callback` | `function:Comparator` | `false` | An optional callback to use as the sorting function. You can alternatively pass a Java Comparator. |  |
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
<summary><code>toQueryString(delimiter=[string])</code></summary>

Converts a struct to a query string using the specified delimiter.

<p>
 The default delimiter is <code>"&amp;"</code>

### Method Signature

```
toQueryString(delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `string` | `false` | The delimiter to use in the query string. Default is "&" | `&` |
</details>
<details>
<summary><code>toSorted(sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function:Comparator])</code></summary>

Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

### Method Signature

```
toSorted(sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function:Comparator])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sortType` | `any` | `false` | An optional sort type to apply to that type - if a callback is given in this position it will be used as that argument | `text` |
| `sortOrder` | `string` | `false` | The sort order applicable to the sortType argument | `asc` |
| `localeSensitive` | `any` | `false` | Sort based on local rules | `false` |
| `callback` | `function:Comparator` | `false` | An optional callback to use as the sorting function. You can alternatively pass a Java Comparator. |  |
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
<summary><code>update(key=[any], value=[any])</code></summary>

Updates or sets a key/value pair in to a struct

### Method Signature

```
update(key=[any], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The struct key |  |
| `value` | `any` | `true` | The value to assign for the specified key |  |
</details>
<details>
<summary><code>valueArray()</code></summary>

Returns an array of all values of top level keys in a struct

### Method Signature

```
valueArray()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>valueSet(type=[string])</code></summary>

Build a Set containing the values of a Struct, deduplicating automatically.

The backing variant can be
 configured; use "linked" to preserve the Struct's value iteration order.

### Method Signature

```
valueSet(type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet,<br>                preserves Struct iteration order), or "sorted" / "tree" (TreeSet). | `default` |
</details>




## Examples

### Creating structs using the function `structNew`

```java
// Create a default struct ( unordered )
myStruct = structNew();

// Create an ordered struct which will maintain key order of insertion
myStruct = structNew( "ordered" );

// Create a case-sensitive struct which will require key access to use the exact casing
myStruct = structNew( "casesensitive" );
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

// JavaScript-style key shorthand
sound = "moo";
animal = { sound }; // same as { sound: sound }

// Create an ordered struct which will maintain key order of insertion
// Note that you must provide the ordered struct with data to prevent confusion as to whether it is an array or struct
orderedAnimals = [
  cow: "moo",
  pig: "oink"
];
```

### Object destructuring assignment

```java
data = { a: 10, b: 20, c: { d: 40, e: 50 }, f: 60 };

// Basic destructuring into the default assignment scope
({ a, b } = data);

// Scoped assignment via explicit rename
({ a: variables.a, b: request.b } = data);

// Defaults, nested destructuring, and rest
({ a, z = 999, c: { d }, ...rest } = data);
```

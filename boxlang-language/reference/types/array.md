
# Type: `Array`

The primary array class in BoxLang.

This class wraps a Java List and provides additional functionality for BoxLang.

 BoxLang indices are one-based, so the first element is at index 1, not 0.

## Array Methods

<details>
<summary><code>append(value=[any], merge=[boolean])</code></summary>

Append a value to an array

### Method Signature

```
append(value=[any], merge=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The element to append. Can be any type. |  |
| `merge` | `boolean` | `false` | If true, the value is assumed to be an array and the elements of the array are appended to the array. If false, the value is<br>                 appended as a single element. | `false` |
</details>
<details>
<summary><code>avg()</code></summary>

Return length of array

### Method Signature

```
avg()
```

### Arguments

This function does not accept any arguments
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
<summary><code>chunk(length=[integer])</code></summary>

Chunks the array into an array of arrays of the specified size.

The final chunk may be shorter if the array does not divide evenly.

 <pre>
 numbers = [ 1, 2, 3, 4, 5 ];
 numbers.chunk( 2 ); // [ [ 1, 2 ], [ 3, 4 ], [ 5 ] ]
 </pre>

### Method Signature

```
chunk(length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `length` | `integer` | `true` | The size of each chunk. |  |
</details>
<details>
<summary><code>clear()</code></summary>

Clear all items from array

### Method Signature

```
clear()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>contains(value=[any], substringMatch=[boolean])</code></summary>

This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

### Method Signature

```
contains(value=[any], substringMatch=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to find or a closure to be used as a search function. |  |
| `substringMatch` | `boolean` | `false` | If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>                          that just use a function filter. | `false` |
</details>
<details>
<summary><code>containsNoCase(value=[any], substringMatch=[boolean])</code></summary>

This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

### Method Signature

```
containsNoCase(value=[any], substringMatch=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to find or a closure to be used as a search function. |  |
| `substringMatch` | `boolean` | `false` | If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>                          that just use a function filter. | `false` |
</details>
<details>
<summary><code>delete(value=[any], scope=[string])</code></summary>

Delete first occurance of item in array case sensitive

### Method Signature

```
delete(value=[any], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to deleted. |  |
| `scope` | `string` | `false` | Which matches to delete: "one" (default) deletes the first matching value, "all" deletes every matching value. | `one` |
</details>
<details>
<summary><code>deleteAt(index=[integer])</code></summary>

Delete item at specified index in array

### Method Signature

```
deleteAt(index=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `integer` | `true` | The index to deleted. |  |
</details>
<details>
<summary><code>deleteNoCase(value=[any], scope=[string])</code></summary>

Delete first occurance of item in array case sensitive

### Method Signature

```
deleteNoCase(value=[any], scope=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to deleted. |  |
| `scope` | `string` | `false` | Which matches to delete: "one" (default) deletes the first matching value, "all" deletes every matching value. | `one` |
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
<summary><code>each(callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

This BIF is used to perform an operation on each item in the array, similar to Java's forEach method.
 It can also be used to perform operations in parallel if the `parallel` argument is set to true.

 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the iterator will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the iterator in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
each(callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Comparator which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `ordered` | `boolean` | `false` | whether parallel operations should execute and maintain order | `false` |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>equals(obj=[any])</code></summary>

Verifies equality with the following rules:
 - Same object
 - Super class

### Method Signature

```
equals(obj=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `obj` | `any` | `true` |  |  |
</details>
<details>
<summary><code>every(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over an array and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the array.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large arrays, especially when the test function is computationally expensive or the array is large.

### Method Signature

```
every(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters an array and returns a new array containing the result
 This BIF will invoke the callback function for each item in the array, passing the item, its index, and the array itself.

<ul>
 <li>If the callback returns true, the item will be included in the new array.</li>
 <li>If the callback returns false, the item will be excluded from the new array.</li>
 <li>If the callback requires strict arguments, it will only receive the item and its index.</li>
 <li>If the callback does not require strict arguments, it will receive the item, its index, and the array itself.</li>
 </ul>

 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>find(value=[any], substringMatch=[boolean])</code></summary>

This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

### Method Signature

```
find(value=[any], substringMatch=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to find or a closure to be used as a search function. |  |
| `substringMatch` | `boolean` | `false` | If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>                          that just use a function filter. | `false` |
</details>
<details>
<summary><code>findAll(value=[any])</code></summary>

Return an array containing the indexes of matched values

### Method Signature

```
findAll(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to found. |  |
</details>
<details>
<summary><code>findAllNoCase(value=[any])</code></summary>

Return an array containing the indexes of matched values

### Method Signature

```
findAllNoCase(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to found. |  |
</details>
<details>
<summary><code>findFirst(callback=[function], defaultValue=[any], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Return first item in array that matches the predicate function.

<pre>
 users = [ { name: "Ada" }, { name: "Grace" } ];
 users.findFirst( ( user ) => user.name == "Grace" ); // { name: "Grace" }
 users.findFirst( ( user ) => user.name == "Linus", "Unknown" ); // "Unknown"
 </pre>

### Method Signature

```
findFirst(callback=[function], defaultValue=[any], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `defaultValue` | `any` | `false` | The default value to use if the array is empty or no value is returned from the predicate function. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>findNoCase(value=[any], substringMatch=[boolean])</code></summary>

This function searches the array for the specified value. Returns the index in the array of the first match, or 0 if there is
                     no match.

### Method Signature

```
findNoCase(value=[any], substringMatch=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to find or a closure to be used as a search function. |  |
| `substringMatch` | `boolean` | `false` | If true, the search will be a substring match. Default is false. This only works on simple values, not complex ones. For<br>                          that just use a function filter. | `false` |
</details>
<details>
<summary><code>first(defaultValue=[any])</code></summary>

Return first item in array

### Method Signature

```
first(defaultValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `defaultValue` | `any` | `false` | The value to return when the array is empty. If omitted, an exception is thrown for an empty array. |  |
</details>
<details>
<summary><code>flatMap(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Maps each element and flattens the result one level.

<pre>
 values = [ 1, 2, 3 ];
 values.flatMap( ( value ) => [ value, value * 10 ] );
 // [ 1, 10, 2, 20, 3, 30 ]
 </pre>

### Method Signature

```
flatMap(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the current item, and the<br>                    current index, and the original array. You can alternatively pass a Java Function which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | If true, the function will be invoked in parallel using multiple threads. Defaults to false. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when parallel is true. If not provided the common thread pool will be used. If a boolean value is passed, it will be assigned as the virtual argument. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual thread. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>flatten(depth=[integer])</code></summary>

Flattens nested arrays to the specified depth.

When depth is omitted, the array is flattened completely.

 <pre>
 nested = [ 1, [ 2, [ 3 ] ] ];
 nested.flatten(); // [ 1, 2, 3 ]
 nested.flatten( 1 ); // [ 1, 2, [ 3 ] ]
 </pre>

### Method Signature

```
flatten(depth=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `depth` | `integer` | `false` | The depth to flatten. If omitted, flatten all nested arrays. |  |
</details>
<details>
<summary><code>getMetadata()</code></summary>

Gets metadata for items of an array and indicates the array type.

### Method Signature

```
getMetadata()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>groupBy(callback=[function])</code></summary>

Returns a struct of keys returned from the predicate function and values of arrays of matching rows.

<pre>
 values = [ 1, 2, 3, 4 ];
 values.groupBy( ( value ) => value % 2 ? "odd" : "even" );
 // { odd: [ 1, 3 ], even: [ 2, 4 ] }
 </pre>

### Method Signature

```
groupBy(callback=[function])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
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
<summary><code>indexExists(index=[any])</code></summary>

Returns whether there exists an item in the array at the selected index.

### Method Signature

```
indexExists(index=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `any` | `true` | The index to check. |  |
</details>
<details>
<summary><code>insertAt(position=[integer], value=[any])</code></summary>

Append a value to an array

### Method Signature

```
insertAt(position=[integer], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position` | `integer` | `true` | The position to insert at |  |
| `value` | `any` | `true` | The value to insert |  |
</details>
<details>
<summary><code>isDefined(index=[any])</code></summary>

Returns whether there exists an item in the array at the selected index.

### Method Signature

```
isDefined(index=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `any` | `true` | The index to check. |  |
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
<summary><code>join(delimiter=[String], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

### Method Signature

```
join(delimiter=[String], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `String` | `false` | The character to use as a separator | `,` |
| `initialValue` | `any` | `false` |  |  |
</details>
<details>
<summary><code>last()</code></summary>

Return first item in array

### Method Signature

```
last()
```

### Arguments

This function does not accept any arguments
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
<summary><code>map(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Iterates over every entry of the array and calls the closure function to work on the element of the array.

The returned value will be set at the
 same index in a new array and the new array will be returned

### Method Signature

```
map(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the current item, and the<br>                    current index, and the original array. You can alternatively pass a Java Function which will only receive the 1st arg. The function should return the value that will be set at the same index in the new array. |  |
| `parallel` | `boolean` | `false` | If true, the function will be invoked in parallel using multiple threads. Defaults to false. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when parallel is true. If not provided the common thread pool will be used. If a boolean value is passed, it will be assigned as the virtual argument. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual thread. Defaults to false. Ingored if parallel is false. | `false` |
</details>
<details>
<summary><code>max()</code></summary>

Get the max value from an array

### Method Signature

```
max()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>median()</code></summary>

Return the median value of an array.

Will only work on arrays that contain only numeric values.

### Method Signature

```
median()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>merge(array2=[array], leaveIndex=[boolean])</code></summary>

This function creates a new array with data from the two passed arrays.

To add all the data from one array into another without creating a new
 array see the built in function ArrayAppend(arr1, arr2, true).

### Method Signature

```
merge(array2=[array], leaveIndex=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array2` | `array` | `true` | The second array to merge |  |
| `leaveIndex` | `boolean` | `true` | Set to true maintain value indexes - if two values have the same index it will keep values from array1 | `false` |
</details>
<details>
<summary><code>mid(start=[integer], length=[integer])</code></summary>

Extracts a sub array from an existing array.

### Method Signature

```
mid(start=[integer], length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` | The position to start the slice from. Negative values count from the end of the array. | `1` |
| `length` | `integer` | `false` | The number of elements to return. 0 (default) returns all elements from start to the end of the array. | `0` |
</details>
<details>
<summary><code>min()</code></summary>

Return length of array

### Method Signature

```
min()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>none(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over an array and test whether <strong>NONE</strong> item meets the test callback.

This is the opposite of <code>ArraySome</code>.
 <p>
 The function will be passed 3 arguments: the value, the index, and the array.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large arrays, especially when the test function is computationally expensive or the array is large.

### Method Signature

```
none(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>parallelStream()</code></summary>

Returns a parallel stream of the array

### Method Signature

```
parallelStream()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>pop(defaultValue=[any])</code></summary>

Remove last item in array and return it

### Method Signature

```
pop(defaultValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `defaultValue` | `any` | `false` | The value to return when the array is empty. If omitted, an exception is thrown for an empty array. |  |
</details>
<details>
<summary><code>prepend(value=[any])</code></summary>

Append a value to the start an array

### Method Signature

```
prepend(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to prepend |  |
</details>
<details>
<summary><code>push(value=[any])</code></summary>

Adds an element or an object to the end of an array, then returns the size of the modified array.

### Method Signature

```
push(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The element to append. Can be any type. |  |
</details>
<details>
<summary><code>range(to=[numeric])</code></summary>

Build an array out of a range of numbers or using our range syntax: {start}..{end}
 or using the from and to arguments

<p>
 You can also build negative ranges
 <p>

 <pre>
 arrayRange( "1..5" )
 arrayRange( "-10..5" )
 arrayRange( 1, 500 )
 </pre>

### Method Signature

```
range(to=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `to` | `numeric` | `false` | The last index item, or defaults to the from value |  |
</details>
<details>
<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

Run the provided udf over the array to reduce the values to a single output

### Method Signature

```
reduce(callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the accumulator, the current item, and the<br>                    current index. You can alternatively pass a Java BiFunction which will only receive the first 2 args. The function should return the new accumulator value. |  |
| `initialValue` | `any` | `false` | The initial value of the accumulator |  |
</details>
<details>
<summary><code>reduceRight(callback=[function:BiFunction], initialValue=[any])</code></summary>

This function iterates over every element of the array and calls the closure to work on that element.

It will reduce the array to a single value,
 from the right to the left, and return it.

### Method Signature

```
reduceRight(callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the accumulator, the current item, and the<br>                    current index. You can alternatively pass a Java BiFunction which will only receive the first 2 args. The function should return the new accumulator value. |  |
| `initialValue` | `any` | `false` | The initial value of the accumulator |  |
</details>
<details>
<summary><code>reject(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters an array and returns a new array containing the result.

This is the inverse of <code>ArrayFilter</code>.

 <pre>
 values = [ 1, 2, 3, 4 ];
 values.reject( ( value ) => value % 2 == 0 ); // [ 1, 3 ]
 </pre>
 
 This BIF will invoke the callback function for each item in the array, passing the item, its index, and the array itself.
 <ul>
 <li>If the callback returns false, the item will be included in the new array.</li>
 <li>If the callback returns true, the item will be excluded from the new array.</li>
 <li>If the callback requires strict arguments, it will only receive the item and its index.</li>
 <li>If the callback does not require strict arguments, it will receive the item, its index, and the array itself.</li>
 </ul>

 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
reject(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual threads. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>resize(size=[integer])</code></summary>

Resets an array to a specified minimum number of elements.

This can improve performance, if used to size an array to its
 expected maximum. For more than 500 elements, use arrayResize
 immediately after using the ArrayNew BIF.

### Method Signature

```
resize(size=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `size` | `integer` | `true` | The new minimum size of the array |  |
</details>
<details>
<summary><code>reverse()</code></summary>

Returns an array with all of the elements reversed.

The value in [0] within the input array will then exist in [n] in the output array, where n is
 the amount of elements in the array minus one.

### Method Signature

```
reverse()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>set(start=[any], end=[any], value=[any])</code></summary>

In a one-dimensional array, sets the elements in a specified
 index range to a value.

Useful for initializing an array after
 a call to arrayNew.

### Method Signature

```
set(start=[any], end=[any], value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `any` | `true` | The starting index |  |
| `end` | `any` | `true` | The ending index |  |
| `value` | `any` | `true` | The value to set |  |
</details>
<details>
<summary><code>shift(defaultValue=[any])</code></summary>

Removes the first element from an array and returns the removed element.

This method changes the length of the array. If used on an empty array, an
 exception will be thrown.

### Method Signature

```
shift(defaultValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `defaultValue` | `any` | `false` | The value to return when the array is empty. If omitted, an exception is thrown for an empty array. |  |
</details>
<details>
<summary><code>slice(start=[integer], length=[integer])</code></summary>

Extracts a sub array from an existing array.

### Method Signature

```
slice(start=[integer], length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `start` | `integer` | `true` | The position to start the slice from. Negative values count from the end of the array. | `1` |
| `length` | `integer` | `false` | The number of elements to return. 0 (default) returns all elements from start to the end of the array. | `0` |
</details>
<details>
<summary><code>some(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over an array and test whether <strong>ANY</strong> items meet the test callback.

The function will be passed 3 arguments: the value, the index, and the array.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
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
some(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the value, the index, the array. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is provided it will be assigned to the virtual argument instead. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual thread. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[function:Comparator])</code></summary>

Sorts array elements.

### Method Signature

```
sort(sortType=[any], sortOrder=[string], localeSensitive=[boolean], callback=[function:Comparator])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sortType` | `any` | `false` | Options are text, numeric, or textnocase | `textnocase` |
| `sortOrder` | `string` | `false` | Options are asc or desc | `asc` |
| `localeSensitive` | `boolean` | `false` | Sort based on local rules | `false` |
| `callback` | `function:Comparator` | `false` | Function to sort by |  |
</details>
<details>
<summary><code>splice(index=[Integer], elementCountForRemoval=[Integer], replacements=[array])</code></summary>

Modifies an array by removing elements and adding new elements.

It starts from the index, removes as many elements as specified by
 elementCountForRemoval, and puts the replacements starting from index position.

### Method Signature

```
splice(index=[Integer], elementCountForRemoval=[Integer], replacements=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `index` | `Integer` | `true` | The initial position to remove or insert from |  |
| `elementCountForRemoval` | `Integer` | `false` | The number of elemetns to remove | `0` |
| `replacements` | `array` | `false` | An array of elements to insert |  |
</details>
<details>
<summary><code>stream()</code></summary>

Returns a stream of the array

### Method Signature

```
stream()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>sum()</code></summary>

Returns the sum of all values in an array

### Method Signature

```
sum()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>swap(position1=[any], position2=[any])</code></summary>

Swaps array values of an array at specified positions.

This function is more efficient than multiple assignment statements

### Method Signature

```
swap(position1=[any], position2=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `position1` | `any` | `true` | The first position to swap |  |
| `position2` | `any` | `true` | The second position to swap |  |
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
<summary><code>toList(delimiter=[String], initialValue=[any])</code></summary>

Used to iterate over an array and run the function closure for each item in the array.

### Method Signature

```
toList(delimiter=[String], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `delimiter` | `String` | `false` | The character to use as a separator | `,` |
| `initialValue` | `any` | `false` |  |  |
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
<summary><code>toSet(type=[string], delimiter=[string])</code></summary>

Convert a collection into a Set, deduplicating automatically.

Accepts an Array, a list-delimited String,
 an existing Set, a QueryColumn, an XML node, a bounded Range, or any value castable to a Set. When the
 value is already of the requested variant it is returned as-is; otherwise a new Set of the specified
 variant is created and populated.

### Method Signature

```
toSet(type=[string], delimiter=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The backing variant: "default" / "hash" (HashSet), "linked" / "ordered" (LinkedHashSet),<br>                or "sorted" / "tree" (TreeSet). When omitted, the caster defaults to LINKED for ordered<br>                collections like Arrays. |  |
| `delimiter` | `string` | `false` | When <code>value</code> is a String, the list delimiter to split on. Defaults to <code>","</code>. | `,` |
</details>
<details>
<summary><code>toStruct()</code></summary>

Transform the array to a struct, the index of the array is the key of the struct

### Method Signature

```
toStruct()
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
<summary><code>transpose()</code></summary>

Returns a transposed array based on all passed in arrays.

<pre>
 arrayTranspose(
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
 );
 // [ [ 1, 4, 7 ], [ 2, 5, 8 ], [ 3, 6, 9 ] ]
 </pre>

### Method Signature

```
transpose()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>unique(caseSensitive=[boolean])</code></summary>

Returns a new array with duplicate items removed.

<pre>
 values = [ 1, 1, 2, 3, 3 ];
 values.unique(); // [ 1, 2, 3 ]
 </pre>

### Method Signature

```
unique(caseSensitive=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `caseSensitive` | `boolean` | `false` | Whether string element comparisons are case-sensitive. Defaults to false. | `false` |
</details>
<details>
<summary><code>unshift(object=[any])</code></summary>

This function adds one or more elements to the beginning of the original array and returns the length of the modified array.

### Method Signature

```
unshift(object=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` | The value to add |  |
</details>
<details>
<summary><code>zip(array2=[array], callback=[function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Returns a zipped array.

<pre>
 arrayZip( [ 1, 2 ], [ "a", "b" ] );
 // [ [ 1, "a" ], [ 2, "b" ] ]

 arrayZip( [ 1, 2 ], [ 10, 20 ], ( a, b ) => a + b );
 // [ 11, 22 ]
 </pre>

### Method Signature

```
zip(array2=[array], callback=[function], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `array2` | `array` | `true` | The second array to zip |  |
| `callback` | `function` | `false` | An optional callback function to receive the item and the current index from both zipped arrays and return a new value. |  |
| `parallel` | `boolean` | `false` | If true, the function will be invoked in parallel using multiple threads. Defaults to false. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when parallel is true. If not provided the common thread pool will be used. If a boolean value is passed, it will be assigned as the virtual argument. |  |
| `virtual` | `boolean` | `false` | If true, the function will be invoked using virtual thread. Defaults to false. Ignored if parallel is false. | `false` |
</details>







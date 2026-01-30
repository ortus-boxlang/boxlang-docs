# struct

This type provides the core map class for Boxlang.

Structs are highly versatile and are used for organizing and managing related data.

Types of Structs in BoxLang: `DEFAULT, CASE_SENSITIVE, LINKED, LINKED_CASE_SENSITIVE, SORTED, WEAK, SOFT`

* DEFAULT: These are the basic structures where each key is associated with a single value. Keys are case-insensitive and can be strings or symbols.
* Nested Structs: Structs can contain other structs as values, allowing for a hierarchical organization of data.
* CASE\_SENSITIVE: By default, BoxLang structs are case-insensitive. However, you can create case-sensitive structs if needed.
* LINKED, LINKED\_CASE\_SENSITIVE (Ordered Structs): This implementation of a Struct maintains keys in the order they were added.
* SORTED: This implementation of a Struct maintains keys in specified sorted order.
* WEAK: This implementation of a Struct uses weak references for keys.
* SOFT: This implementation of a Struct uses a default struct with values wrapped in a SoftReference.

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

Arguments:

| Argument    | Type      | Required | Default |
| ----------- | --------- | -------- | ------- |
| `struct2`   | `struct`  | `true`   | `null`  |
| `overwrite` | `boolean` | `false`  | `true`  |

Examples: _Append One Struct to Another:_

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

<summary><code>bxDump(label=[string], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

, The available ,`,output,`, locations are: - ,**,buffer,**,: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser. - ,**,console,**,: The output is printed to the System console. - ,**,Absolute File Path,**, The output is written to a file with the specified absolute file path. ,

,

The output `format` can be either HTML or plain text.

The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

Arguments:

| Argument   | Type      | Required | Default |
| ---------- | --------- | -------- | ------- |
| `label`    | `string`  | `false`  | `null`  |
| `top`      | `numeric` | `false`  | `null`  |
| `expand`   | `boolean` | `false`  | `true`  |
| `abort`    | `boolean` | `false`  | `false` |
| `output`   | `string`  | `false`  | `null`  |
| `format`   | `string`  | `false`  | `null`  |
| `showUDFs` | `boolean` | `false`  | `true`  |

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

<summary><code>delete(key=[any])</code></summary>

Deletes a key from a struct

Arguments:

| Argument | Type  | Required | Default |
| -------- | ----- | -------- | ------- |
| `key`    | `any` | `true`   | `null`  |

</details>

<details>

<summary><code>duplicate(deep=[boolean])</code></summary>

Duplicates an object - either shallow or deep

Arguments:

| Argument | Type      | Required | Default |
| -------- | --------- | -------- | ------- |
| `deep`   | `boolean` | `false`  | `true`  |

</details>

<details>

<summary><code>each(callback=[function:BiConsumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])</code></summary>

Used to iterate over a struct and run the function closure for each key/value pair.

, The function will be passed 3 arguments: the key, the value, and the struct. You can alternatively pass a Java BiConsumer which will only receive the first 2 args (key and value). ,

, This BIF is useful for performing side effects on each item in the struct, such as logging or modifying external state. ,

,

,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument     | Type                  | Required | Default |
| ------------ | --------------------- | -------- | ------- |
| `callback`   | `function:BiConsumer` | `true`   | `null`  |
| `parallel`   | `boolean`             | `false`  | `false` |
| `maxThreads` | `any`                 | `false`  | `null`  |
| `ordered`    | `boolean`             | `false`  | `false` |
| `virtual`    | `boolean`             | `false`  | `false` |

</details>

<details>

<summary><code>equals(struct2=[structloose])</code></summary>

Tests equality between two structs

Arguments:

| Argument  | Type     | Required | Default |
| --------- | -------- | -------- | ------- |
| `struct2` | `struct` | `true`   | `null`  |

</details>

<details>

<summary><code>every(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a struct and test whether **every** item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the struct. You can alternatively pass a Java Predicate which will only receive the 1st arg. The function should return true if the item meets the test, and false otherwise. ,

, ,**,Note:,**, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. This allows for efficient processing of large structs, especially when the test function is computationally expensive or the struct is large.

Arguments:

| Argument     | Type                   | Required | Default |
| ------------ | ---------------------- | -------- | ------- |
| `callback`   | `function:BiPredicate` | `true`   | `null`  |
| `parallel`   | `boolean`              | `false`  | `false` |
| `maxThreads` | `any`                  | `false`  | `null`  |
| `virtual`    | `boolean`              | `false`  | `false` |

</details>

<details>

<summary><code>filter(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters a struct and returns a new struct with the values that pass the filter criteria.

This BIF will invoke the callback function for each entry in the struct, passing the key, value, and the struct itself. ,

* , ,
* ,If the callback returns true, the entry will be included in the new struct.,
* , ,
* ,If the callback returns false, the entry will be excluded from the new struct.,
* , ,
* ,If the callback requires strict arguments, it will only receive the key and value.,
* , ,
* ,If the callback does not require strict arguments, it will receive the key, value, and the original struct.,
* , ,

, ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument     | Type                   | Required | Default |
| ------------ | ---------------------- | -------- | ------- |
| `callback`   | `function:BiPredicate` | `true`   | `null`  |
| `parallel`   | `boolean`              | `false`  | `false` |
| `maxThreads` | `any`                  | `false`  | `null`  |
| `virtual`    | `boolean`              | `false`  | `false` |

</details>

<details>

<summary><code>find(key=[any], defaultValue=[any])</code></summary>

Finds and retrieves a top-level key from a string in a struct

Arguments:

| Argument       | Type  | Required | Default |
| -------------- | ----- | -------- | ------- |
| `key`          | `any` | `true`   | `null`  |
| `defaultValue` | `any` | `false`  | `null`  |

</details>

<details>

<summary><code>findKey(key=[any], scope=[string])</code></summary>

Searches a struct for a given key and returns an array of values

Arguments:

| Argument | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `key`    | `any`    | `true`   | `null`  |
| `scope`  | `string` | `false`  | `one`   |

</details>

<details>

<summary><code>findValue(value=[string], scope=[string])</code></summary>

Searches a struct for a given value and returns an array of results

Arguments:

| Argument | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `value`  | `string` | `true`   | `null`  |
| `scope`  | `string` | `false`  | `one`   |

</details>

<details>

<summary><code>getFromPath(path=[string])</code></summary>

Retrieves the value from a struct using a path based expression

Arguments:

| Argument | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `path`   | `string` | `true`   | `null`  |

</details>

<details>

<summary><code>getMetadata()</code></summary>

Gets Struct-specific metadata of the requested struct.

</details>

<details>

<summary><code>hash(algorithm=[string], encoding=[string], numIterations=[integer])</code></summary>

Creates an algorithmic hash of an object

Arguments:

| Argument        | Type      | Required | Default |
| --------------- | --------- | -------- | ------- |
| `algorithm`     | `string`  | `false`  | `MD5`   |
| `encoding`      | `string`  | `false`  | `utf-8` |
| `numIterations` | `integer` | `false`  | `1`     |

</details>

<details>

<summary><code>insert(key=[any], value=[any], overwrite=[boolean])</code></summary>

Inserts a key/value pair in to a struct - with an optional overwrite argument

Arguments:

| Argument    | Type      | Required | Default |
| ----------- | --------- | -------- | ------- |
| `key`       | `any`     | `true`   | `null`  |
| `value`     | `any`     | `true`   | `null`  |
| `overwrite` | `boolean` | `false`  | `false` |

</details>

<details>

<summary><code>isCaseSensitive()</code></summary>

Returns whether the give struct is case sensitive

</details>

<details>

<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of anything that can be casted to: Array, Struct, Query, or String.

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

<summary><code>keyExists(key=[any])</code></summary>

Tests whether a key exists in a struct and returns a boolean value

Arguments:

| Argument | Type  | Required | Default |
| -------- | ----- | -------- | ------- |
| `key`    | `any` | `true`   | `null`  |

</details>

<details>

<summary><code>keyList(delimiter=[string])</code></summary>

Get keys of a struct as a string list

Arguments:

| Argument    | Type     | Required | Default |
| ----------- | -------- | -------- | ------- |
| `delimiter` | `string` | `false`  | `,`     |

</details>

<details>

<summary><code>keyTranslate(deep=[boolean], retainKeys=[boolean])</code></summary>

Converts a struct with dot-notated keys in to an unflattened version

Arguments:

| Argument     | Type      | Required | Default |
| ------------ | --------- | -------- | ------- |
| `deep`       | `boolean` | `false`  | `false` |
| `retainKeys` | `boolean` | `false`  | `false` |

</details>

<details>

<summary><code>len()</code></summary>

Returns the absolute value of a number

</details>

<details>

<summary><code>map(callback=[function:BiFunction], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

This BIF will iterate over each key-value pair in the struct and invoke the callback function for each item so you can do any operation on the key-value pair and return a new value that will be set in a new struct.

The callback function will be passed the key, the value, and the original struct. ,

* , ,
* ,If the callback requires strict arguments, it will only receive the key and value.,
* , ,
* ,If the callback does not require strict arguments, it will receive the key, value, and the original struct.,
* , ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument     | Type                  | Required | Default |
| ------------ | --------------------- | -------- | ------- |
| `callback`   | `function:BiFunction` | `true`   | `null`  |
| `parallel`   | `boolean`             | `false`  | `false` |
| `maxThreads` | `any`                 | `false`  | `null`  |
| `virtual`    | `boolean`             | `false`  | `false` |

</details>

<details>

<summary><code>none(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a struct and test whether **NONE** item meets the test callback.

This is the opposite of ,{@link StructSome},. ,

, The function will be passed 3 arguments: the value, the index, and the struct. You can alternatively pass a Java Predicate which will only receive the 1st arg. The function should return true if the item meets the test, and false otherwise. ,

, ,**,Note:,**, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. This allows for efficient processing of large structs, especially when the test function is computationally expensive or the struct is large.

Arguments:

| Argument     | Type                   | Required | Default |
| ------------ | ---------------------- | -------- | ------- |
| `callback`   | `function:BiPredicate` | `true`   | `null`  |
| `parallel`   | `boolean`              | `false`  | `false` |
| `maxThreads` | `any`                  | `false`  | `null`  |
| `virtual`    | `boolean`              | `false`  | `false` |

</details>

<details>

<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>

Run the provided udf against struct to reduce the values to a single output

Arguments:

| Argument       | Type       | Required | Default |
| -------------- | ---------- | -------- | ------- |
| `callback`     | `function` | `true`   | `null`  |
| `initialValue` | `any`      | `false`  | `null`  |

</details>

<details>

<summary><code>some(callback=[function:BiPredicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a struct and test whether **ANY** items meet the test callback.

The function will be passed 3 arguments: the key, the value, and the struct. You can alternatively pass a Java BiPredicate which will only receive the first 2 args. The function should return true if the item meets the test, and false otherwise. ,

, ,**,Note:,**, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance. ,

Arguments:

| Argument     | Type                   | Required | Default |
| ------------ | ---------------------- | -------- | ------- |
| `callback`   | `function:BiPredicate` | `true`   | `null`  |
| `parallel`   | `boolean`              | `false`  | `false` |
| `maxThreads` | `any`                  | `false`  | `null`  |
| `virtual`    | `boolean`              | `false`  | `false` |

</details>

<details>

<summary><code>sort(sortType=[any], sortOrder=[string], path=[string], callback=[function:Comparator])</code></summary>

Sorts a struct according to the specified arguments and returns an array of struct keys

Arguments:

| Argument    | Type                  | Required | Default |
| ----------- | --------------------- | -------- | ------- |
| `sortType`  | `any`                 | `false`  | `text`  |
| `sortOrder` | `string`              | `false`  | `asc`   |
| `path`      | `string`              | `false`  | `null`  |
| `callback`  | `function:Comparator` | `false`  | `null`  |

</details>

<details>

<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

### ,Query Format Options,

, The ,`,queryFormat,`, argument determines how queries are serialized: ,

* , ,
* ,`,row,`, or ,`,false,`,: Serializes the query as a top-level struct with two keys: ,`,columns,`, (an array of column names) and ,`,data,`, (an array of arrays representing each row's data).,
* , ,
* ,`,column,`, or ,`,true,`,: Serializes the query as a top-level struct with three keys: ,`,rowCount,`, (the number of rows), ,`,columns,`, (an array of column names), and ,`,data,`, (a struct where each key is a column name and the value is an array of values for that column).,
* , ,
* ,`,struct,`,: Serializes the query as an array of structs, where each struct represents a row of data.,
* , ,

,

,

### ,Usage,

,

,

```
,
// Convert a query to JSON
myQuery = ...;
json = jsonSerialize( myQuery, queryFormat="row" );
// Convert a list to JSON
myList = "foo,bar,baz";
jsonList = jsonSerialize( myList );
,
```

Arguments:

| Argument              | Type      | Required | Default |
| --------------------- | --------- | -------- | ------- |
| `queryFormat`         | `string`  | `false`  | `row`   |
| `useSecureJSONPrefix` | `string`  | `false`  | `false` |
| `useCustomSerializer` | `boolean` | `false`  | `null`  |
| `pretty`              | `boolean` | `false`  | `false` |

</details>

<details>

<summary><code>toModifiable()</code></summary>

Convert an array, struct or query to its Modifiable counterpart.

</details>

<details>

<summary><code>toQueryString(delimiter=[string])</code></summary>

Converts a struct to a query string using the specified delimiter.

, The default delimiter is ,{@code "&"}

Arguments:

| Argument    | Type     | Required | Default |
| ----------- | -------- | -------- | ------- |
| `delimiter` | `string` | `false`  | `&`     |

</details>

<details>

<summary><code>toSorted(sortType=[any], sortOrder=[string], localeSensitive=[any], callback=[function:Comparator])</code></summary>

Converts a struct to a sorted struct - using either a callback comparator or textual directives as the sort option

Arguments:

| Argument          | Type                  | Required | Default |
| ----------------- | --------------------- | -------- | ------- |
| `sortType`        | `any`                 | `false`  | `text`  |
| `sortOrder`       | `string`              | `false`  | `asc`   |
| `localeSensitive` | `any`                 | `false`  | `false` |
| `callback`        | `function:Comparator` | `false`  | `null`  |

</details>

<details>

<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct or query to its Unmodifiable counterpart.

</details>

<details>

<summary><code>update(key=[any], value=[any])</code></summary>

Updates or sets a key/value pair in to a struct

Arguments:

| Argument | Type  | Required | Default |
| -------- | ----- | -------- | ------- |
| `key`    | `any` | `true`   | `null`  |
| `value`  | `any` | `true`   | `null`  |

</details>

<details>

<summary><code>valueArray()</code></summary>

Returns an array of all values of top level keys in a struct

</details>

## Examples

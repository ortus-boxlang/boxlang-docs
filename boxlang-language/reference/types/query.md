# query

Represents a BoxLang Query object that stores tabular data.

This class implements multiple interfaces:

* IType: for BoxLang type system integration
* IReferenceable: for dynamic property/method access
* Collection: for Java collection operations
* Serializable: for persistence support

The Query object stores data as a list of row arrays, with column metadata maintained separately. It provides thread-safe operations for manipulating the data and supports JDBC ResultSet integration.

Key features:

* Dynamic column addition/removal
* Row manipulation (add, delete, swap)
* Conversion to/from other data structures
* Query metadata support
* Collection interface implementation
* Optimized data storage with lazy initialization

## Query Methods

<details>

<summary><code>addColumn(columnName=[string], datatype=[any], array=[array])</code></summary>

Adds a column to a query and populates its rows with the contents of a one-dimensional array.

Arguments:

| Argument     | Type     | Required | Default  |
| ------------ | -------- | -------- | -------- |
| `columnName` | `string` | `true`   | `null`   |
| `datatype`   | `any`    | `false`  | `object` |
| `array`      | `array`  | `false`  | `[]`     |

</details>

<details>

<summary><code>addRow(rowData=[any])</code></summary>

Return new query

Arguments:

| Argument  | Type  | Required | Default |
| --------- | ----- | -------- | ------- |
| `rowData` | `any` | `false`  | `null`  |

</details>

<details>

<summary><code>append(query2=[query])</code></summary>

This function clears the query

Arguments:

| Argument | Type    | Required | Default |
| -------- | ------- | -------- | ------- |
| `query2` | `query` | `true`   | `null`  |

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

This function clears the query

</details>

<details>

<summary><code>columnArray()</code></summary>

This function returns the column array of a query.

</details>

<details>

<summary><code>columnCount()</code></summary>

This function returns the number of columns in a query

</details>

<details>

<summary><code>columnData(columnName=[string])</code></summary>

Returns the data in a query column.

Arguments:

| Argument     | Type     | Required | Default |
| ------------ | -------- | -------- | ------- |
| `columnName` | `string` | `true`   | `null`  |

</details>

<details>

<summary><code>columnExists(column=[string])</code></summary>

This function returns true if the column exists in the query

Arguments:

| Argument | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `column` | `string` | `true`   | `null`  |

</details>

<details>

<summary><code>columnList()</code></summary>

This function returns the delimited column list of a query.

</details>

<details>

<summary><code>currentRow()</code></summary>

Returns the current row number

</details>

<details>

<summary><code>deleteColumn(column=[string])</code></summary>

Deletes a column within a query object.

Arguments:

| Argument | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `column` | `string` | `true`   | `null`  |

</details>

<details>

<summary><code>deleteRow(row=[integer])</code></summary>

This function deletes a row from the query

Arguments:

| Argument | Type      | Required | Default |
| -------- | --------- | -------- | ------- |
| `row`    | `integer` | `true`   | `null`  |

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

<summary><code>each(callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])</code></summary>

Iterates over query rows and passes each row per iteration to a callback function.

This function is used to perform an action for each row in the query. It does not return a value, but rather allows you to perform side effects such as printing or modifying data. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument     | Type                | Required | Default |
| ------------ | ------------------- | -------- | ------- |
| `callback`   | `function:Consumer` | `true`   | `null`  |
| `parallel`   | `boolean`           | `false`  | `false` |
| `maxThreads` | `any`               | `false`  | `null`  |
| `ordered`    | `boolean`           | `false`  | `false` |
| `virtual`    | `boolean`           | `false`  | `false` |

</details>

<details>

<summary><code>every(closure=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a Query and test whether **every** item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the Query. You can alternatively pass a Java Predicate which will only receive the 1st arg. The function should return true if the item meets the test, and false otherwise. ,

, ,**,Note:,**, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. This allows for efficient processing of large Queries, especially when the test function is computationally expensive or the Query is large.

Arguments:

| Argument     | Type                 | Required | Default |
| ------------ | -------------------- | -------- | ------- |
| `closure`    | `function:Predicate` | `true`   | `null`  |
| `parallel`   | `boolean`            | `false`  | `false` |
| `maxThreads` | `any`                | `false`  | `null`  |
| `virtual`    | `boolean`            | `false`  | `false` |

</details>

<details>

<summary><code>filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters query rows specified in filter criteria This BIF will invoke the callback function for each row in the query, passing the row as a struct.

* , ,
* ,If the callback returns true, the row will be included in the new query.,
* , ,
* ,If the callback returns false, the row will be excluded from the new query.,
* , ,
* ,If the callback requires strict arguments, it will only receive the row as a struct.,
* , ,
* ,If the callback does not require strict arguments, it will receive the row as a struct, the row number (1-based), and the query itself.,
* , ,

, ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to filter, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument     | Type                 | Required | Default |
| ------------ | -------------------- | -------- | ------- |
| `callback`   | `function:Predicate` | `true`   | `null`  |
| `parallel`   | `boolean`            | `false`  | `false` |
| `maxThreads` | `any`                | `false`  | `null`  |
| `virtual`    | `boolean`            | `false`  | `false` |

</details>

<details>

<summary><code>getCell(column_name=[string], row_number=[integer])</code></summary>

This function maps the query to a new query.

Arguments:

| Argument      | Type      | Required | Default |
| ------------- | --------- | -------- | ------- |
| `column_name` | `string`  | `true`   | `null`  |
| `row_number`  | `integer` | `false`  | `null`  |

</details>

<details>

<summary><code>getResult()</code></summary>

Returns the metadata of a query.

</details>

<details>

<summary><code>getRow(rowNumber=[integer])</code></summary>

Returns the cells of a query row as a structure

Arguments:

| Argument    | Type      | Required | Default |
| ----------- | --------- | -------- | ------- |
| `rowNumber` | `integer` | `true`   | `null`  |

</details>

<details>

<summary><code>insertAt(value=[query], position=[numeric])</code></summary>

Inserts a query data into another query at a specific position

Arguments:

| Argument   | Type      | Required | Default |
| ---------- | --------- | -------- | ------- |
| `value`    | `query`   | `true`   | `null`  |
| `position` | `numeric` | `true`   | `null`  |

</details>

<details>

<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of anything that can be casted to: Array, Struct, Query, or String.

</details>

<details>

<summary><code>keyExists(key=[string])</code></summary>

This function returns true if the key exists in the query

Arguments:

| Argument | Type     | Required | Default |
| -------- | -------- | -------- | ------- |
| `key`    | `string` | `true`   | `null`  |

</details>

<details>

<summary><code>len()</code></summary>

Returns the absolute value of a number

</details>

<details>

<summary><code>map(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

This BIF will iterate over each row in the query and invoke the callback function for each item so you can do any operation on the row and return a new value that will be set at the same index in a new query.

The callback function will be passed the row as a struct, the current row number (1-based), and the query itself. ,

* , ,
* ,If the callback requires strict arguments, it will only receive the row as a struct.,
* , ,
* ,If the callback does not require strict arguments, it will receive the row as a struct, the row number (1-based), and the query itself.,
* , ,

, ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

Arguments:

| Argument     | Type                | Required | Default |
| ------------ | ------------------- | -------- | ------- |
| `callback`   | `function:Function` | `true`   | `null`  |
| `parallel`   | `boolean`           | `false`  | `false` |
| `maxThreads` | `any`               | `false`  | `null`  |
| `virtual`    | `boolean`           | `false`  | `false` |

</details>

<details>

<summary><code>none(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a Query and test whether **NONE** item meets the test callback.

This is the opposite of ,{@link QuerySome},. ,

, The function will be passed 3 arguments: the value, the index, and the Query. You can alternatively pass a Java Predicate which will only receive the 1st arg. The function should return true if the item meets the test, and false otherwise. ,

, ,**,Note:,**, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. This allows for efficient processing of large Queries, especially when the test function is computationally expensive or the Query is large.

Arguments:

| Argument     | Type                 | Required | Default |
| ------------ | -------------------- | -------- | ------- |
| `callback`   | `function:Predicate` | `true`   | `null`  |
| `parallel`   | `boolean`            | `false`  | `false` |
| `maxThreads` | `any`                | `false`  | `null`  |
| `virtual`    | `boolean`            | `false`  | `false` |

</details>

<details>

<summary><code>prepend(query2=[query])</code></summary>

Adds a query to the beginning of another query

Arguments:

| Argument | Type    | Required | Default |
| -------- | ------- | -------- | ------- |
| `query2` | `query` | `true`   | `null`  |

</details>

<details>

<summary><code>recordCount()</code></summary>

This function returns the number of records in a query

</details>

<details>

<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

This function reduces the query to a single value.

Arguments:

| Argument       | Type                  | Required | Default |
| -------------- | --------------------- | -------- | ------- |
| `callback`     | `function:BiFunction` | `true`   | `null`  |
| `initialValue` | `any`                 | `true`   | `null`  |

</details>

<details>

<summary><code>reverse()</code></summary>

This function reverses the query data

</details>

<details>

<summary><code>rowData(rowNumber=[integer])</code></summary>

Returns the cells of a query row as a structure

Arguments:

| Argument    | Type      | Required | Default |
| ----------- | --------- | -------- | ------- |
| `rowNumber` | `integer` | `true`   | `null`  |

</details>

<details>

<summary><code>rowSwap(source=[numeric], destination=[numeric])</code></summary>

In a query object, swap the record in the sourceRow with the record from the destinationRow.

Arguments:

| Argument      | Type      | Required | Default |
| ------------- | --------- | -------- | ------- |
| `source`      | `numeric` | `true`   | `null`  |
| `destination` | `numeric` | `true`   | `null`  |

</details>

<details>

<summary><code>setCell(column=[string], value=[any], row=[integer])</code></summary>

Sets a cell to a value.

Arguments:

| Argument | Type      | Required | Default |
| -------- | --------- | -------- | ------- |
| `column` | `string`  | `true`   | `null`  |
| `value`  | `any`     | `true`   | `null`  |
| `row`    | `integer` | `false`  | `null`  |

</details>

<details>

<summary><code>setRow(rowNumber=[integer], rowData=[any])</code></summary>

Adds or updates a row in a query based on the provided row data and position.

Arguments:

| Argument    | Type      | Required | Default |
| ----------- | --------- | -------- | ------- |
| `rowNumber` | `integer` | `false`  | `0`     |
| `rowData`   | `any`     | `true`   | `null`  |

</details>

<details>

<summary><code>slice(offset=[integer], length=[integer])</code></summary>

Returns a subset of rows from an existing query

Arguments:

| Argument | Type      | Required | Default |
| -------- | --------- | -------- | ------- |
| `offset` | `integer` | `true`   | `null`  |
| `length` | `integer` | `false`  | `0`     |

</details>

<details>

<summary><code>some(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a query and test whether **ANY** items meet the test callback.

The function will be passed 3 arguments: the row, the currentRow, and the query. You can alternatively pass a Java Predicate which will only receive the 1st arg. The function should return true if the item meets the test, and false otherwise. ,

, ,**,Note:,**, This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that meets the test condition. ,

, ,

### ,Parallel Execution,

, If the ,`,parallel,`, argument is set to true, and no ,`,max_threads,`, are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams. If ,`,max_threads,`, is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete. Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance. ,

Arguments:

| Argument     | Type                 | Required | Default |
| ------------ | -------------------- | -------- | ------- |
| `callback`   | `function:Predicate` | `true`   | `null`  |
| `parallel`   | `boolean`            | `false`  | `false` |
| `maxThreads` | `any`                | `false`  | `null`  |
| `virtual`    | `boolean`            | `false`  | `false` |

</details>

<details>

<summary><code>sort(sortFunc=[function:Comparator])</code></summary>

Sorts array elements.

Arguments:

| Argument   | Type                  | Required | Default |
| ---------- | --------------------- | -------- | ------- |
| `sortFunc` | `function:Comparator` | `true`   | `null`  |

</details>

<details>

<summary><code>toArrayOfStructs()</code></summary>

Convert this query to an array of structs.

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

<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct or query to its Unmodifiable counterpart.

</details>

## Examples

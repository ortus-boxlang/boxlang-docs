
# Type: `Query`

Represents a BoxLang Query object that stores tabular data.

This class implements multiple interfaces:
 - IType: for BoxLang type system integration
 - IReferenceable: for dynamic property/method access
 - Collection<IStruct>: for Java collection operations
 - Serializable: for persistence support

 The Query object stores data as a list of row arrays, with column metadata maintained
 separately. It provides thread-safe operations for manipulating the data and
 supports JDBC ResultSet integration.

 Key features:
 - Dynamic column addition/removal
 - Row manipulation (add, delete, swap)
 - Conversion to/from other data structures
 - Query metadata support
 - Collection interface implementation
 - Optimized data storage with lazy initialization

## Query Methods

<details>
<summary><code>addColumn(columnName=[string], datatype=[any], array=[array])</code></summary>

Adds a column to a query and populates its rows with the contents of a one-dimensional array.

### Method Signature

```
addColumn(columnName=[string], datatype=[any], array=[array])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `columnName` | `string` | `true` | The name of the column to add. |  |
| `datatype` | `any` | `false` | The column data type of the new column or the array to populate the column with a generic type of anything. | `object` |
| `array` | `array` | `false` |  | `[]` |
</details>
<details>
<summary><code>addRow(rowData=[any])</code></summary>

Return new query

### Method Signature

```
addRow(rowData=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `rowData` | `any` | `false` | Data to populate the query. Can be a struct (with keys matching column names), an array of structs, or an array of arrays (in<br>                   same order as columnList) |  |
</details>
<details>
<summary><code>append(query2=[query])</code></summary>

This function clears the query

### Method Signature

```
append(query2=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query2` | `query` | `true` |  |  |
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

This function clears the query

### Method Signature

```
clear()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>columnArray()</code></summary>

This function returns the column array of a query.

### Method Signature

```
columnArray()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>columnCount()</code></summary>

This function returns the number of columns in a query

### Method Signature

```
columnCount()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>columnData(columnName=[string])</code></summary>

Returns the data in a query column.

### Method Signature

```
columnData(columnName=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `columnName` | `string` | `true` | The name of the column to get the data from. |  |
</details>
<details>
<summary><code>columnExists(column=[string])</code></summary>

This function returns true if the column exists in the query

### Method Signature

```
columnExists(column=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `column` | `string` | `true` | The column to check for |  |
</details>
<details>
<summary><code>columnList()</code></summary>

This function returns the delimited column list of a query.

### Method Signature

```
columnList()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>currentRow()</code></summary>

Returns the current row number

### Method Signature

```
currentRow()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>deleteColumn(column=[string])</code></summary>

Deletes a column within a query object.

### Method Signature

```
deleteColumn(column=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `column` | `string` | `true` | The name of the column to delete. |  |
</details>
<details>
<summary><code>deleteRow(row=[integer])</code></summary>

This function deletes a row from the query

### Method Signature

```
deleteRow(row=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `row` | `integer` | `true` | The row index to delete |  |
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

Iterates over query rows and passes each row per iteration to a callback function.

This function is used to perform an action for each row in the query.
 It does not return a value, but rather allows you to perform side effects such as printing or modifying data.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to iterate, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
each(callback=[function:Consumer], parallel=[boolean], maxThreads=[any], ordered=[boolean], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Consumer` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Consumer which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual argument |  |
| `ordered` | `boolean` | `false` |  | `false` |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ingored if parallel is false | `false` |
</details>
<details>
<summary><code>every(closure=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a Query and test whether <strong>every</strong> item meets the test callback.

The function will be passed 3 arguments: the value, the index, and the Query.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large Queries, especially when the test function is computationally expensive or the Query is large.

### Method Signature

```
every(closure=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `closure` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Filters query rows specified in filter criteria
 This BIF will invoke the callback function for each row in the query, passing the row as a struct.

<ul>
 <li>If the callback returns true, the row will be included in the new query.</li>
 <li>If the callback returns false, the row will be excluded from the new query.</li>
 <li>If the callback requires strict arguments, it will only receive the row as a struct.</li>
 <li>If the callback does not require strict arguments, it will receive the row as a struct, the row number (1-based), and the query itself.</li>
 </ul>
 <p>
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
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the query row as a struct, the row number, the query. You can alternatively pass a Java Predicate which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>getCell(column_name=[string], row_number=[integer])</code></summary>

This function maps the query to a new query.

### Method Signature

```
getCell(column_name=[string], row_number=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `column_name` | `string` | `true` |  |  |
| `row_number` | `integer` | `false` |  |  |
</details>
<details>
<summary><code>getResult()</code></summary>

Returns the metadata of a query.

### Method Signature

```
getResult()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>getRow(rowNumber=[integer])</code></summary>

Returns the cells of a query row as a structure

### Method Signature

```
getRow(rowNumber=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `rowNumber` | `integer` | `true` | Position of the query row to return. |  |
</details>
<details>
<summary><code>insertAt(value=[query], position=[numeric])</code></summary>

Inserts a query data into another query at a specific position

### Method Signature

```
insertAt(value=[query], position=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `query` | `true` | The query that will be inserted |  |
| `position` | `numeric` | `true` | The position where the query will be inserted |  |
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
<summary><code>keyExists(key=[string])</code></summary>

This function returns true if the key exists in the query

### Method Signature

```
keyExists(key=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `string` | `true` | The key to check for |  |
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

This BIF will iterate over each row in the query and invoke the callback function for each item so you can do
 any operation on the row and return a new value that will be set at the same index in a new query.

The callback function will be passed the row as a struct, the current row number (1-based), and the query itself.
 <ul>
 <li>If the callback requires strict arguments, it will only receive the row as a struct.</li>
 <li>If the callback does not require strict arguments, it will receive the row as a struct, the row number (1-based), and the query itself.</li>
 </ul>
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the map will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the map in parallel, and destroy it after the operation is complete.
 Please note that this may not be the most efficient way to map, as it will create a new ForkJoinPool for each invocation of the BIF. You may want to consider using a shared ForkJoinPool for better performance.

### Method Signature

```
map(callback=[function:Function], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Function` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. You can alternatively pass a Java Function which will only receive the 1st arg. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>none(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a Query and test whether <strong>NONE</strong> item meets the test callback.

This is the opposite of <code>QuerySome</code>.
 <p>
 The function will be passed 3 arguments: the value, the index, and the Query.
 You can alternatively pass a Java Predicate which will only receive the 1st arg.
 The function should return true if the item meets the test, and false otherwise.
 <p>
 <strong>Note:</strong> This operation is a short-circuit operation, meaning it will stop iterating as soon as it finds the first item that does not meet the test condition.
 <p>
 <h2>Parallel Execution</h2>
 If the <code>parallel</code> argument is set to true, and no <code>max_threads</code> are sent, the filter will be executed in parallel using a ForkJoinPool with parallel streams.
 If <code>max_threads</code> is specified, it will create a new ForkJoinPool with the specified number of threads to run the filter in parallel, and destroy it after the operation is complete.
 This allows for efficient processing of large Queries, especially when the test function is computationally expensive or the Query is large.

### Method Signature

```
none(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:Predicate` | `true` |  |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>prepend(query2=[query])</code></summary>

Adds a query to the beginning of another query

### Method Signature

```
prepend(query2=[query])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query2` | `query` | `true` |  |  |
</details>
<details>
<summary><code>recordCount()</code></summary>

This function returns the number of records in a query

### Method Signature

```
recordCount()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

This function reduces the query to a single value.

### Method Signature

```
reduce(callback=[function:BiFunction], initialValue=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `callback` | `function:BiFunction` | `true` | The function to invoke for each item. The function will be passed 4 arguments: the accumulator, the current item, the current index, and the query. You can alternatively pass a Java Predicate which will only receive the first 2<br>                    args. |  |
| `initialValue` | `any` | `true` | The initial value to use for the reduction |  |
</details>
<details>
<summary><code>reverse()</code></summary>

This function reverses the query data

### Method Signature

```
reverse()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>rowData(rowNumber=[integer])</code></summary>

Returns the cells of a query row as a structure

### Method Signature

```
rowData(rowNumber=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `rowNumber` | `integer` | `true` | Position of the query row to return. |  |
</details>
<details>
<summary><code>rowSwap(source=[numeric], destination=[numeric])</code></summary>

In a query object, swap the record in the sourceRow with the record from the destinationRow.

### Method Signature

```
rowSwap(source=[numeric], destination=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `source` | `numeric` | `true` | The row to swap from |  |
| `destination` | `numeric` | `true` | The row to swap to |  |
</details>
<details>
<summary><code>setCell(column=[string], value=[any], row=[integer])</code></summary>

Sets a cell to a value.

### Method Signature

```
setCell(column=[string], value=[any], row=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `column` | `string` | `true` | The column name to set the cell in |  |
| `value` | `any` | `true` | The value to set the cell to |  |
| `row` | `integer` | `false` | The row number to set the cell in. If no row number is specified, the cell on the last row is set. |  |
</details>
<details>
<summary><code>setRow(rowNumber=[integer], rowData=[any])</code></summary>

Adds or updates a row in a query based on the provided row data and position.

### Method Signature

```
setRow(rowNumber=[integer], rowData=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `rowNumber` | `integer` | `false` | Optional position of the row to update; if omitted or zero, a new row will be added. | `0` |
| `rowData` | `any` | `true` | A struct or array containing data for the row. |  |
</details>
<details>
<summary><code>slice(offset=[integer], length=[integer])</code></summary>

Returns a subset of rows from an existing query

### Method Signature

```
slice(offset=[integer], length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `offset` | `integer` | `true` | The first row to include in the new query. |  |
| `length` | `integer` | `false` | The number of rows to include, defaults to all remaining rows. | `0` |
</details>
<details>
<summary><code>some(callback=[function:Predicate], parallel=[boolean], maxThreads=[any], virtual=[boolean])</code></summary>

Used to iterate over a query and test whether <strong>ANY</strong> items meet the test callback.

The function will be passed 3 arguments: the row, the currentRow, and the query.
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
| `callback` | `function:Predicate` | `true` | The function to invoke for each item. The function will be passed 3 arguments: the row, the currentRow, the query. |  |
| `parallel` | `boolean` | `false` | Whether to run the filter in parallel. Defaults to false. If true, the filter will be run in parallel using a ForkJoinPool. | `false` |
| `maxThreads` | `any` | `false` | The maximum number of threads to use when running the filter in parallel. If not passed it will use the default number of threads for the ForkJoinPool.<br>                      If parallel is false, this argument is ignored. If a boolean is passed it will be used as the virtual thread argument |  |
| `virtual` | `boolean` | `false` | Whether to use virtual threads when running the filter in parallel. Defaults to false. Ignored if parallel is false. | `false` |
</details>
<details>
<summary><code>sort(sortFunc=[function:Comparator])</code></summary>

Sorts array elements.

### Method Signature

```
sort(sortFunc=[function:Comparator])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `sortFunc` | `function:Comparator` | `true` | Sort function to use. You can alternatively pass a Java Comparator. |  |
</details>
<details>
<summary><code>toArrayOfStructs()</code></summary>

Convert this query to an array of structs.

### Method Signature

```
toArrayOfStructs()
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
<summary><code>toUnmodifiable()</code></summary>

Convert an array, struct, query or set to its Unmodifiable counterpart.

### Method Signature

```
toUnmodifiable()
```

### Arguments

This function does not accept any arguments
</details>







[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Query`

This type represents a representation of a database query result set.

It provides language specific methods to access columnar data, both as value lists and within iterative loops

## Query Methods

<details>
<summary><code>addColumn(columnName=[string], datatype=[any], array=[array])</code></summary>

Adds a column to a query and populates its rows with the contents of a one-dimensional array.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `columnName` | `string` | `true` | `null` |
| `datatype` | `any` | `false` | `Varchar` |
| `array` | `array` | `false` | `[]` |

</details>
<details>
<summary><code>addRow(rowData=[any])</code></summary>

Return new query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowData` | `any` | `false` | `null` |

</details>
<details>
<summary><code>append(query2=[query])</code></summary>

This function clears the query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query2` | `query` | `true` | `null` |

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

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `columnName` | `string` | `true` | `null` |

</details>
<details>
<summary><code>columnExists(column=[string])</code></summary>

This function returns true if the column exists in the query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `null` |

</details>
<details>
<summary><code>currentRow()</code></summary>

Returns the current row number
</details>
<details>
<summary><code>deleteColumn(column=[string])</code></summary>

Deletes a column within a query object.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `null` |

</details>
<details>
<summary><code>deleteRow(row=[integer])</code></summary>

This function deletes a row from the query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `row` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>each(callback=[function:Consumer], parallel=[boolean], maxThreads=[integer])</code></summary>

Iterates over query rows and passes each row per iteration to a callback function

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Consumer` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>every(closure=[function:Predicate], parallel=[boolean], maxThreads=[integer])</code></summary>

Executes a callback/closure against every row in a query and returns true if the callback/closure returned true for every row.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `closure` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>filter(callback=[function:Predicate], parallel=[boolean], maxThreads=[integer])</code></summary>

Filters query rows specified in filter criteria

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>getCell(column_name=[string], row_number=[integer])</code></summary>

This function maps the query to a new query.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column_name` | `string` | `true` | `null` |
| `row_number` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>getResult()</code></summary>

Returns the metadata of a query.
</details>
<details>
<summary><code>getRow(rowNumber=[integer])</code></summary>

Returns the cells of a query row as a structure

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>insertAt(value=[query], position=[numeric])</code></summary>

Inserts a query data into another query at a specific position

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `value` | `query` | `true` | `null` |
| `position` | `numeric` | `true` | `null` |

</details>
<details>
<summary><code>isEmpty()</code></summary>

Determine whether a given value is empty.

We check for emptiness of
 anything that can be casted to: Array, Struct, Query, or String.
</details>
<details>
<summary><code>keyExists(key=[string])</code></summary>

This function returns true if the key exists in the query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `null` |

</details>
<details>
<summary><code>map(callback=[function:Function], parallel=[boolean], maxThreads=[integer])</code></summary>

This function maps the query to a new query.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Function` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>prepend(query2=[query])</code></summary>

Adds a query to the beginning of another query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query2` | `query` | `true` | `null` |

</details>
<details>
<summary><code>recordCount()</code></summary>

This function returns the number of records in a query
</details>
<details>
<summary><code>reduce(callback=[function:BiFunction], initialValue=[any])</code></summary>

This function reduces the query to a single value.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:BiFunction` | `true` | `null` |
| `initialValue` | `any` | `true` | `null` |

</details>
<details>
<summary><code>reverse()</code></summary>

This function reverses the query data
</details>
<details>
<summary><code>rowData(rowNumber=[integer])</code></summary>

Returns the cells of a query row as a structure

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>rowSwap(source=[numeric], destination=[numeric])</code></summary>

In a query object, swap the record in the sourceRow with the record from the destinationRow.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `source` | `numeric` | `true` | `null` |
| `destination` | `numeric` | `true` | `null` |

</details>
<details>
<summary><code>setCell(column=[string], value=[any], row=[integer])</code></summary>

Sets a cell to a value.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `null` |
| `value` | `any` | `true` | `null` |
| `row` | `integer` | `false` | `null` |

</details>
<details>
<summary><code>setRow(rowNumber=[integer], rowData=[any])</code></summary>

Adds or updates a row in a query based on the provided row data and position.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `false` | `0` |
| `rowData` | `any` | `true` | `null` |

</details>
<details>
<summary><code>slice(offset=[integer], length=[integer])</code></summary>

Returns a subset of rows from an existing query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `offset` | `integer` | `true` | `null` |
| `length` | `integer` | `false` | `0` |

</details>
<details>
<summary><code>some(callback=[function:Predicate], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>

This function calls a given closure/function with every element in a given query and returns true, if one of the closure calls returns true

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function:Predicate` | `true` | `null` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `null` |
| `initialValue` | `any` | `false` | `null` |

</details>
<details>
<summary><code>sort(sortFunc=[function:Comparator])</code></summary>

Sorts array elements.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortFunc` | `function:Comparator` | `true` | `null` |

</details>
<details>
<summary><code>toImmutable()</code></summary>

Convert an array, struct or query to its immutable counterpart.
</details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `string` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `null` |

</details>
<details>
<summary><code>toMutable()</code></summary>

Convert an array, struct or query to its mutable counterpart.
</details>


## Examples

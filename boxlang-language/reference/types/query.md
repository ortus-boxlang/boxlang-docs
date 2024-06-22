[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Query`

This type represents a representation of a database query result set.

It provides language specific methods to access columnar data, both as value lists and within iterative loops

## Query Methods

<details>
<summary><code>addColumn(columnName=[string], datatype=[any], array=[array])</code></summary>
<p>Adds a column to a query and populates its rows with the contents of a one-dimensional array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `columnName` | `string` | `true` | `` |
| `datatype` | `any` | `false` | `Varchar` |
| `array` | `array` | `false` | `[]` |

</p></details>
<details>
<summary><code>addRow(rowData=[any])</code></summary>
<p>Return new query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowData` | `any` | `false` | `` |

</p></details>
<details>
<summary><code>append(query2=[query])</code></summary>
<p>This function clears the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query2` | `query` | `true` | `` |

</p></details>
<details>
<summary><code>clear()</code></summary>
<p>This function clears the query
</p></details>
<details>
<summary><code>columnArray()</code></summary>
<p>This function returns the column array of a query.
</p></details>
<details>
<summary><code>columnCount()</code></summary>
<p>This function returns the number of columns in a query
</p></details>
<details>
<summary><code>columnData(columnName=[string])</code></summary>
<p>Returns the data in a query column.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `columnName` | `string` | `true` | `` |

</p></details>
<details>
<summary><code>columnExists(column=[string])</code></summary>
<p>This function returns true if the column exists in the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `` |

</p></details>
<details>
<summary><code>currentRow()</code></summary>
<p>Returns the current row number
</p></details>
<details>
<summary><code>deleteColumn(column=[string])</code></summary>
<p>Deletes a column within a query object.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `` |

</p></details>
<details>
<summary><code>deleteRow(row=[integer])</code></summary>
<p>This function deletes a row from the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `row` | `integer` | `true` | `` |

</p></details>
<details>
<summary><code>each(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Iterates over query rows and passes each row per iteration to a callback function

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</p></details>
<details>
<summary><code>every(closure=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Executes a callback/closure against every row in a query and returns true if the callback/closure returned true for every row.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `closure` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</p></details>
<details>
<summary><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Filters query rows specified in filter criteria

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</p></details>
<details>
<summary><code>getCell(column_name=[string], row_number=[integer])</code></summary>
<p>This function maps the query to a new query.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column_name` | `string` | `true` | `` |
| `row_number` | `integer` | `false` | `` |

</p></details>
<details>
<summary><code>getResult()</code></summary>
<p>Returns the metadata of a query.
</p></details>
<details>
<summary><code>keyExists(key=[string])</code></summary>
<p>This function returns true if the key exists in the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |

</p></details>
<details>
<summary><code>map(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>This function maps the query to a new query.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</p></details>
<details>
<summary><code>prepend(query2=[query])</code></summary>
<p>Adds a query to the beginning of another query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query2` | `query` | `true` | `` |

</p></details>
<details>
<summary><code>recordCount()</code></summary>
<p>This function returns the number of records in a query
</p></details>
<details>
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>
<p>This function reduces the query to a single value.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `true` | `` |

</p></details>
<details>
<summary><code>rowData(rowNumber=[integer])</code></summary>
<p>Returns the cells of a query row as a structure

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `true` | `` |

</p></details>
<details>
<summary><code>setCell(column=[string], value=[any], row=[integer])</code></summary>
<p>Sets a cell to a value.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `` |
| `value` | `any` | `true` | `` |
| `row` | `integer` | `false` | `` |

</p></details>
<details>
<summary><code>setRow(rowNumber=[integer], rowData=[any])</code></summary>
<p>Adds or updates a row in a query based on the provided row data and position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `false` | `0` |
| `rowData` | `any` | `true` | `` |

</p></details>
<details>
<summary><code>slice(offset=[integer], length=[integer])</code></summary>
<p>Returns a subset of rows from an existing query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `offset` | `integer` | `true` | `` |
| `length` | `integer` | `false` | `0` |

</p></details>
<details>
<summary><code>some(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>
<p>This function calls a given closure/function with every element in a given query and returns true, if one of the closure calls returns true

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `initialValue` | `any` | `false` | `` |

</p></details>
<details>
<summary><code>sort(sortFunc=[function])</code></summary>
<p>Sorts array elements.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortFunc` | `function` | `true` | `` |

</p></details>
<details>
<summary><code>toImmutable()</code></summary>
<p>Convert an array, struct or query to its immutable counterpart.
</p></details>
<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])</code></summary>
<p>Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `boolean` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `` |

</p></details>
<details>
<summary><code>toMutable()</code></summary>
<p>Convert an array, struct or query to its mutable counterpart.
</p></details>


## Examples

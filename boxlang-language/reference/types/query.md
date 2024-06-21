[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Query`

This type represents a representation of a database query result set.

It provides language specific methods to access columnar data, both as value lists and within iterative loops

## Query Methods

<dl>
<dt><code>addColumn(columnName=[string], datatype=[any], array=[array])</code></dt><dd>Adds a column to a query and populates its rows with the contents of a one-dimensional array.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `columnName` | `string` | `true` | `` |
| `datatype` | `any` | `false` | `Varchar` |
| `array` | `array` | `false` | `[]` |

</dd>
<dt><code>addRow(rowData=[any])</code></dt><dd>Return new query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowData` | `any` | `false` | `` |

</dd>
<dt><code>append(query2=[query])</code></dt><dd>This function clears the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query2` | `query` | `true` | `` |

</dd>
<dt><code>clear()</code></dt><dd>This function clears the query</dd>
<dt><code>columnArray()</code></dt><dd>This function returns the column array of a query.</dd>
<dt><code>columnCount()</code></dt><dd>This function returns the number of columns in a query</dd>
<dt><code>columnData(columnName=[string])</code></dt><dd>Returns the data in a query column.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `columnName` | `string` | `true` | `` |

</dd>
<dt><code>columnExists(column=[string])</code></dt><dd>This function returns true if the column exists in the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `` |

</dd>
<dt><code>currentRow()</code></dt><dd>Returns the current row number</dd>
<dt><code>deleteColumn(column=[string])</code></dt><dd>Deletes a column within a query object.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `` |

</dd>
<dt><code>deleteRow(row=[integer])</code></dt><dd>This function deletes a row from the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `row` | `integer` | `true` | `` |

</dd>
<dt><code>each(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Iterates over query rows and passes each row per iteration to a callback function

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>every(closure=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Executes a callback/closure against every row in a query and returns true if the callback/closure returned true for every row.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `closure` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>filter(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>Filters query rows specified in filter criteria

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>getCell(column_name=[string], row_number=[integer])</code></dt><dd>This function maps the query to a new query.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column_name` | `string` | `true` | `` |
| `row_number` | `integer` | `false` | `` |

</dd>
<dt><code>getResult()</code></dt><dd>Returns the metadata of a query.</dd>
<dt><code>keyExists(key=[string])</code></dt><dd>This function returns true if the key exists in the query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `string` | `true` | `` |

</dd>
<dt><code>map(callback=[function], parallel=[boolean], maxThreads=[integer])</code></dt><dd>This function maps the query to a new query.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |

</dd>
<dt><code>prepend(query2=[query])</code></dt><dd>Adds a query to the beginning of another query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query2` | `query` | `true` | `` |

</dd>
<dt><code>recordCount()</code></dt><dd>This function returns the number of records in a query</dd>
<dt><code>reduce(callback=[function], initialValue=[any])</code></dt><dd>This function reduces the query to a single value.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `initialValue` | `any` | `true` | `` |

</dd>
<dt><code>rowData(rowNumber=[integer])</code></dt><dd>Returns the cells of a query row as a structure

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `true` | `` |

</dd>
<dt><code>setCell(column=[string], value=[any], row=[integer])</code></dt><dd>Sets a cell to a value.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `column` | `string` | `true` | `` |
| `value` | `any` | `true` | `` |
| `row` | `integer` | `false` | `` |

</dd>
<dt><code>setRow(rowNumber=[integer], rowData=[any])</code></dt><dd>Adds or updates a row in a query based on the provided row data and position.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `rowNumber` | `integer` | `false` | `0` |
| `rowData` | `any` | `true` | `` |

</dd>
<dt><code>slice(offset=[integer], length=[integer])</code></dt><dd>Returns a subset of rows from an existing query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `offset` | `integer` | `true` | `` |
| `length` | `integer` | `false` | `0` |

</dd>
<dt><code>some(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></dt><dd>This function calls a given closure/function with every element in a given query and returns true, if one of the closure calls returns true

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `callback` | `function` | `true` | `` |
| `parallel` | `boolean` | `false` | `false` |
| `maxThreads` | `integer` | `false` | `` |
| `initialValue` | `any` | `false` | `` |

</dd>
<dt><code>sort(sortFunc=[function])</code></dt><dd>Sorts array elements.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `sortFunc` | `function` | `true` | `` |

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

</dl>

## Examples

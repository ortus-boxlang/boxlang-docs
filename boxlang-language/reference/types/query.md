[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Query`

This type represents a representation of a database query result set.

It provides language specific methods to access columnar data, both as value lists and within iterative loops

## Query Methods

<details>
<summary><code>addColumn(columnName=[string], datatype=[any], array=[array])</code></summary>
<p>Adds a column to a query and populates its rows with the contents of a one-dimensional array.

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
<td>`columnName`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`datatype`</td>
<td>`any`</td>
<td>`false`</td>
<td>`Varchar`</td>
</tr>

<tr>
<td>`array`</td>
<td>`array`</td>
<td>`false`</td>
<td>`[]`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>addRow(rowData=[any])</code></summary>
<p>Return new query

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
<td>`rowData`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>append(query2=[query])</code></summary>
<p>This function clears the query

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
<td>`query2`</td>
<td>`query`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

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
<td>`columnName`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>columnExists(column=[string])</code></summary>
<p>This function returns true if the column exists in the query

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
<td>`column`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>currentRow()</code></summary>
<p>Returns the current row number
</p></details>
<details>
<summary><code>deleteColumn(column=[string])</code></summary>
<p>Deletes a column within a query object.

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
<td>`column`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>deleteRow(row=[integer])</code></summary>
<p>This function deletes a row from the query

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
<td>`row`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>each(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Iterates over query rows and passes each row per iteration to a callback function

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
<summary><code>every(closure=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>Executes a callback/closure against every row in a query and returns true if the callback/closure returned true for every row.

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
<td>`closure`</td>
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
<p>Filters query rows specified in filter criteria

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
<summary><code>getCell(column_name=[string], row_number=[integer])</code></summary>
<p>This function maps the query to a new query.

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
<td>`column_name`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`row_number`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>getResult()</code></summary>
<p>Returns the metadata of a query.
</p></details>
<details>
<summary><code>keyExists(key=[string])</code></summary>
<p>This function returns true if the key exists in the query

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
<summary><code>map(callback=[function], parallel=[boolean], maxThreads=[integer])</code></summary>
<p>This function maps the query to a new query.

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
<summary><code>prepend(query2=[query])</code></summary>
<p>Adds a query to the beginning of another query

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
<td>`query2`</td>
<td>`query`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>recordCount()</code></summary>
<p>This function returns the number of records in a query
</p></details>
<details>
<summary><code>reduce(callback=[function], initialValue=[any])</code></summary>
<p>This function reduces the query to a single value.

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
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>rowData(rowNumber=[integer])</code></summary>
<p>Returns the cells of a query row as a structure

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
<td>`rowNumber`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>setCell(column=[string], value=[any], row=[integer])</code></summary>
<p>Sets a cell to a value.

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
<td>`column`</td>
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
<td>`row`</td>
<td>`integer`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>setRow(rowNumber=[integer], rowData=[any])</code></summary>
<p>Adds or updates a row in a query based on the provided row data and position.

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
<td>`rowNumber`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`0`</td>
</tr>

<tr>
<td>`rowData`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>slice(offset=[integer], length=[integer])</code></summary>
<p>Returns a subset of rows from an existing query

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
<td>`offset`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`length`</td>
<td>`integer`</td>
<td>`false`</td>
<td>`0`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>some(callback=[function], parallel=[boolean], maxThreads=[integer], initialValue=[any])</code></summary>
<p>This function calls a given closure/function with every element in a given query and returns true, if one of the closure calls returns true

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
<td>`initialValue`</td>
<td>`any`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>sort(sortFunc=[function])</code></summary>
<p>Sorts array elements.

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
<td>`sortFunc`</td>
<td>`function`</td>
<td>`true`</td>
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


## Examples

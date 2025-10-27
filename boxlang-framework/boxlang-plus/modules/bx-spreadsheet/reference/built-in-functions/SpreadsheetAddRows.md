[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SpreadsheetAddRows`

Adds multiple rows from a query to an Excel spreadsheet object.

## Method Signature

```
SpreadsheetAddRows(spreadsheetObj=[any], data=[any], row=[any], column=[any], insert=[any], datatype=[any], includeColumnNames=[any])
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|----------|
| `spreadsheetObj` | `ANY` | `true` | The spreadsheet object. |  |
| `data` | `ANY` | `true` | An array of arrays or a query object to add as rows. |  |

## Examples

Add multiple rows from array of arrays:

```js
// Add multiple rows at once
var spreadsheet = SpreadsheetNew();
var data = [
    [ "John", "Sales", 75000 ],
    [ "Alice", "Marketing", 65000 ],
    [ "Bob", "IT", 80000 ]
];
SpreadsheetAddRows( spreadsheet, data );
```

Add a query as spreadsheet rows:

```js
// Convert query results to spreadsheet rows
var spreadsheet = SpreadsheetNew();
var employees = queryExecute( "SELECT name, department, salary FROM employees" );
SpreadsheetAddRows( spreadsheet, employees );
```

Batch import data:

```js
// Import from external data source
var spreadsheet = SpreadsheetNew();

// Add headers
SpreadsheetAddRow( spreadsheet, [ "ID", "Product", "Price", "Stock" ] );

// Add bulk data
var products = [
    [ 1, "Widget", 19.99, 100 ],
    [ 2, "Gadget", 29.99, 50 ],
    [ 3, "Gizmo", 39.99, 75 ]
];
SpreadsheetAddRows( spreadsheet, products );
```

## Related

- [SpreadsheetAddRow()](./SpreadsheetAddRow.md) - Add a single row
- [SpreadsheetDeleteRows()](./SpreadsheetDeleteRows.md) - Delete multiple rows
- [SpreadsheetRead()](./SpreadsheetRead.md) - Read spreadsheet data
- [Query Operations Guide](../../query-operations.md) - Working with queries
- [Batch Operations](../../batch-operations.md) - Bulk data operations

| `row` | `NUMERIC` | `false` | The row number where to start inserting the data (1-based). If not specified, adds to the end. |  |
| `column` | `NUMERIC` | `false` | The column number where to start inserting the data (1-based). Default is 1. |  |
| `insert` | `BOOLEAN` | `false` | Whether to insert new rows or overwrite existing rows. Default is false. | true |
| `datatype` | `BOOLEAN` | `false` | The data type to apply to the cells (not implemented in this version). | false |
| `includeColumnNames` | `any` | `false` | Whether to include column names as the first row. Default is false. |  |


## Examples



## Related

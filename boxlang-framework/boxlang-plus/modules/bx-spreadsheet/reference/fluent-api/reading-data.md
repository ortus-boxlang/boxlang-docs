---
description: Methods for reading cell values, rows, columns, and ranges from spreadsheets
icon: book-open
---

# 📖 Reading Data

Methods for retrieving data from spreadsheet cells, rows, columns, and ranges.

---

## getCellValue()

Gets the value from a specific cell.

**Signature:**
```js
getCellValue( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number (1-based)
- `column` (required) - Column number (1-based)

**Returns:** Cell value (string, numeric, date, or null)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get cell value
value = sheet.getCellValue( 1, 1 );

// Get multiple cells
firstName = sheet.getCellValue( 2, 1 );
lastName = sheet.getCellValue( 2, 2 );
```

---

## getCellFormula()

Gets the formula from a cell (if it contains a formula).

**Signature:**
```js
getCellFormula( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** Formula string (without leading =) or empty string

**Examples:**

```js
sheet = Spreadsheet( "calculations.xlsx", load = true );

// Get formula
formula = sheet.getCellFormula( 2, 3 );
// Returns: "A2*B2"

// Get calculated value
value = sheet.getCellValue( 2, 3 );
// Returns: 150
```

---

## getCellType()

Gets the data type of a cell.

**Signature:**
```js
getCellType( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** String - "blank", "numeric", "string", "formula", "boolean", "error"

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true );

type = sheet.getCellType( 1, 1 );

switch ( type ) {
    case "numeric":
        writeOutput( "Cell contains a number" );
        break;
    case "formula":
        writeOutput( "Cell contains a formula" );
        break;
    case "string":
        writeOutput( "Cell contains text" );
        break;
}
```

---

## getRow()

Gets all values from a specific row as an array.

**Signature:**
```js
getRow( numeric rowNumber )
```

**Parameters:**
- `rowNumber` (required) - Row number to retrieve

**Returns:** Array of cell values

**Examples:**

```js
sheet = Spreadsheet( "employees.xlsx", load = true );

// Get first row (headers)
headers = sheet.getRow( 1 );
// Returns: ["Name", "Department", "Salary"]

// Get data row
employee = sheet.getRow( 2 );
// Returns: ["John Doe", "Engineering", 95000]
```

---

## getRows()

Gets multiple rows as an array of arrays.

**Signature:**
```js
getRows( numeric startRow, numeric endRow )
```

**Parameters:**
- `startRow` (required) - Starting row number
- `endRow` (required) - Ending row number

**Returns:** Array of arrays (each inner array is a row)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get rows 2-5
rows = sheet.getRows( 2, 5 );
// Returns: [
//     ["Row 2 data"],
//     ["Row 3 data"],
//     ["Row 4 data"],
//     ["Row 5 data"]
// ]

// Process rows
for ( row in rows ) {
    writeOutput( row[1] );
}
```

---

## getColumn()

Gets all values from a specific column as an array.

**Signature:**
```js
getColumn( numeric columnNumber )
```

**Parameters:**
- `columnNumber` (required) - Column number to retrieve

**Returns:** Array of cell values

**Examples:**

```js
sheet = Spreadsheet( "sales.xlsx", load = true );

// Get first column
products = sheet.getColumn( 1 );

// Get sales column
sales = sheet.getColumn( 2 );

// Calculate total
total = sales.sum();
```

---

## getColumns()

Gets multiple columns as an array of arrays.

**Signature:**
```js
getColumns( numeric startColumn, numeric endColumn )
```

**Parameters:**
- `startColumn` (required) - Starting column number
- `endColumn` (required) - Ending column number

**Returns:** Array of arrays (each inner array is a column)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Get columns 1-3
columns = sheet.getColumns( 1, 3 );
```

---

## getCellComment()

Gets the comment from a specific cell.

**Signature:**
```js
getCellComment( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** Struct with `text` and `author` keys, or null if no comment

**Examples:**

```js
sheet = Spreadsheet( "reviewed.xlsx", load = true );

comment = sheet.getCellComment( 2, 3 );

if ( !isNull( comment ) ) {
    writeOutput( "Comment: #comment.text#" );
    writeOutput( "Author: #comment.author#" );
}
```

---

## toArray()

Converts the entire spreadsheet (or current sheet) to an array of structs.

**Signature:**
```js
toArray( [boolean includeHeaderRow=true] )
```

**Parameters:**
- `includeHeaderRow` (optional) - Whether to use first row as keys (default: true)

**Returns:** Array of structs (if includeHeaderRow=true) or array of arrays (if false)

**Examples:**

```js
sheet = Spreadsheet( "employees.xlsx", load = true );

// Array of structs (uses first row as keys)
employees = sheet.toArray();
// Returns: [
//     { "Name": "John", "Department": "Engineering" },
//     { "Name": "Jane", "Department": "Marketing" }
// ]

// Array of arrays
data = sheet.toArray( includeHeaderRow = false );
// Returns: [
//     ["John", "Engineering"],
//     ["Jane", "Marketing"]
// ]
```

---

## toQuery()

Converts the spreadsheet to a BoxLang query object.

**Signature:**
```js
toQuery()
```

**Returns:** Query object (uses first row as column names)

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true );

qry = sheet.toQuery();

// Use query functions
for ( row in qry ) {
    writeOutput( row.Name );
}

// Query of queries
result = queryExecute(
    "SELECT * FROM qry WHERE Department = ?",
    [ "Engineering" ],
    { dbtype: "query" }
);
```

---

## toJson()

Converts the spreadsheet to JSON format.

**Signature:**
```js
toJson()
```

**Returns:** JSON string (array of objects)

**Examples:**

```js
sheet = Spreadsheet( "products.xlsx", load = true );

json = sheet.toJson();

// Save to file
fileWrite( "products.json", json );

// Or return in API
return json;
```

---

## toCSV()

Converts the spreadsheet to CSV format.

**Signature:**
```js
toCSV( [string delimiter=","] )
```

**Parameters:**
- `delimiter` (optional) - Field delimiter (default: ",")

**Returns:** CSV string

**Examples:**

```js
sheet = Spreadsheet( "data.xlsx", load = true );

// Standard CSV
csv = sheet.toCSV();

// Tab-delimited
tsv = sheet.toCSV( delimiter = chr(9) );

// Semicolon-delimited
csv = sheet.toCSV( delimiter = ";" );

fileWrite( "export.csv", csv );
```

---

## toHtml()

Converts the spreadsheet to an HTML table.

**Signature:**
```js
toHtml()
```

**Returns:** HTML table string

**Examples:**

```js
sheet = Spreadsheet( "report.xlsx", load = true );

html = sheet.toHtml();

// Embed in page
writeOutput( "<h1>Report</h1>" );
writeOutput( html );
```

---

## 💡 Usage Patterns

### Read Single Values

```js
sheet = Spreadsheet( "data.xlsx", load = true );

value = sheet.getCellValue( 1, 1 );
```

### Read Entire Sheet

```js
// As array of structs
data = Spreadsheet( "employees.xlsx", load = true ).toArray();

for ( employee in data ) {
    writeOutput( "#employee.Name# - #employee.Department#" );
}
```

### Read and Export

```js
sheet = Spreadsheet( "source.xlsx", load = true );

// Export to multiple formats
fileWrite( "export.csv", sheet.toCSV() );
fileWrite( "export.json", sheet.toJson() );
fileWrite( "export.html", sheet.toHtml() );
```

### Read Specific Range

```js
sheet = Spreadsheet( "large-file.xlsx", load = true );

// Read only rows 100-200
data = sheet.getRows( 100, 200 );
```

---

## 📚 See Also

- [Writing Data](writing-data.md)
- [Data Export Guide](../../data-export.md)
- [Formulas](formulas.md)

---
description: Methods for getting spreadsheet information and metadata
icon: info-circle
---

# ℹ️ Utility Methods

Methods for retrieving information about spreadsheet structure, cells, and metadata.

---

## getRowCount()

Gets the number of rows in the current sheet.

**Signature:**
```js
getRowCount()
```

**Returns:** Numeric

**Examples:**

```js
rowCount = sheet.getRowCount();
writeOutput( "Sheet has #rowCount# rows" );
```

---

## getColumnCount()

Gets the number of columns in the current sheet.

**Signature:**
```js
getColumnCount()
```

**Returns:** Numeric

**Examples:**

```js
colCount = sheet.getColumnCount();
writeOutput( "Sheet has #colCount# columns" );
```

---

## getCellInfo()

Gets detailed information about a specific cell.

**Signature:**
```js
getCellInfo( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** Struct with cell information

**Return Keys:**
```js
{
    value: any,          // Cell value
    formula: string,     // Formula (if cell contains formula)
    type: string,        // "numeric", "string", "boolean", "blank", "formula"
    dataFormat: string,  // Excel format code
    comment: string,     // Cell comment
    row: numeric,
    column: numeric
}
```

**Examples:**

```js
info = sheet.getCellInfo( 2, 3 );

writeOutput( "Value: #info.value#<br>" );
writeOutput( "Type: #info.type#<br>" );

if ( info.formula.len() > 0 ) {
    writeOutput( "Formula: #info.formula#" );
}
```

---

## getSheetInfo()

Gets information about the current sheet.

**Signature:**
```js
getSheetInfo()
```

**Returns:** Struct with sheet information

**Return Keys:**
```js
{
    name: string,        // Sheet name
    rowCount: numeric,   // Number of rows
    columnCount: numeric, // Number of columns
    isProtected: boolean, // Protection status
    sheetIndex: numeric  // Sheet position (1-based)
}
```

**Examples:**

```js
info = sheet.getSheetInfo();

writeOutput( "Sheet: #info.name#<br>" );
writeOutput( "Size: #info.rowCount# x #info.columnCount#<br>" );
writeOutput( "Protected: #info.isProtected#" );
```

---

## getColumnName()

Converts a column number to its Excel letter name.

**Signature:**
```js
getColumnName( numeric columnNumber )
```

**Parameters:**
- `columnNumber` (required) - Column number (1-based)

**Returns:** String (column letter)

**Examples:**

```js
name = sheet.getColumnName( 1 );  // "A"
name = sheet.getColumnName( 27 ); // "AA"
name = sheet.getColumnName( 702 ); // "ZZ"
```

---

## getColumnNumber()

Converts an Excel column letter to its numeric index.

**Signature:**
```js
getColumnNumber( string columnName )
```

**Parameters:**
- `columnName` (required) - Column letter (e.g., "A", "AA")

**Returns:** Numeric (1-based column number)

**Examples:**

```js
num = sheet.getColumnNumber( "A" );   // 1
num = sheet.getColumnNumber( "AA" );  // 27
num = sheet.getColumnNumber( "ZZ" );  // 702
```

---

## isFormula()

Checks if a cell contains a formula.

**Signature:**
```js
isFormula( numeric row, numeric column )
```

**Parameters:**
- `row` (required) - Row number
- `column` (required) - Column number

**Returns:** Boolean

**Examples:**

```js
if ( sheet.isFormula( 2, 3 ) ) {
    formula = sheet.getCellFormula( 2, 3 );
    writeOutput( "Cell contains formula: #formula#" );
}
```

---

## 💡 Usage Patterns

### Sheet Summary

```js
info = sheet.getSheetInfo();

writeOutput( "
    <h2>#info.name#</h2>
    <ul>
        <li>Rows: #info.rowCount#</li>
        <li>Columns: #info.columnCount#</li>
        <li>Protected: #info.isProtected#</li>
    </ul>
" );
```

### Data Range Detection

```js
sheet = Spreadsheet( "data.xlsx", load = true );

rowCount = sheet.getRowCount();
colCount = sheet.getColumnCount();

writeOutput( "Data range: A1 to #sheet.getColumnName(colCount)##rowCount#" );
```

### Cell Inspector

```js
function inspectCell( required sheet, required numeric row, required numeric column ) {
    info = sheet.getCellInfo( row, column );

    writeOutput( "Cell #sheet.getColumnName(column)##row#:<br>" );
    writeOutput( "Value: #info.value#<br>" );
    writeOutput( "Type: #info.type#<br>" );

    if ( info.formula.len() > 0 ) {
        writeOutput( "Formula: #info.formula#<br>" );
    }

    if ( info.comment.len() > 0 ) {
        writeOutput( "Comment: #info.comment#<br>" );
    }
}
```

### Process All Sheets

```js
sheet = Spreadsheet( "workbook.xlsx", load = true );

names = sheet.getSheetNames();

for ( name in names ) {
    sheet.selectSheet( name );
    info = sheet.getSheetInfo();

    writeOutput( "
        Sheet: #info.name#
        Size: #info.rowCount# x #info.columnCount#
        <hr>
    " );
}
```

---

## 📚 See Also

- [Reading Data](reading-data.md)
- [Sheet Operations](sheet-operations.md)

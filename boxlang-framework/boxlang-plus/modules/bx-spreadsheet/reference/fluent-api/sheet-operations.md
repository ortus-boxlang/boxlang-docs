---
description: Methods for creating, selecting, and managing worksheets
icon: table
---

# 📊 Sheet Operations

Methods for working with multiple worksheets within a spreadsheet workbook.

---

## createSheet()

Creates a new worksheet.

**Signature:**
```js
createSheet( [string sheetName] )
```

**Parameters:**
- `sheetName` (optional) - Name for the new sheet (auto-generated if not provided)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Create with auto-generated name
sheet.createSheet();

// Create with custom name
sheet.createSheet( "Sales Data" );
```

---

## createAndSelectSheet()

Creates a new worksheet and immediately selects it.

**Signature:**
```js
createAndSelectSheet( [string sheetName] )
```

**Parameters:**
- `sheetName` (optional) - Name for the new sheet

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
Spreadsheet( "workbook.xlsx" )
    .createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Summary Data" ] )
    .createAndSelectSheet( "Details" )
    .setRowData( 1, [ "Detailed Data" ] )
    .save();
```

---

## selectSheet()

Selects an existing worksheet for subsequent operations.

**Signature:**
```js
selectSheet( any sheet )
```

**Parameters:**
- `sheet` (required) - Sheet name (string) or sheet number (numeric, 1-based)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Select by name
sheet.selectSheet( "Sales Data" );

// Select by number
sheet.selectSheet( 1 );

// Switch between sheets
sheet.selectSheet( "Data" )
    .addRow( [ "Data row" ] )
    .selectSheet( "Summary" )
    .addRow( [ "Summary row" ] );
```

---

## renameSheet()

Renames a worksheet.

**Signature:**
```js
renameSheet( string oldName, string newName )
```

**Parameters:**
- `oldName` (required) - Current sheet name
- `newName` (required) - New sheet name

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet.renameSheet( "Sheet1", "Sales Report" );
```

---

## deleteSheet()

Deletes a worksheet from the workbook.

**Signature:**
```js
deleteSheet( string sheetName )
```

**Parameters:**
- `sheetName` (required) - Name of sheet to delete

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet.deleteSheet( "Temporary" );
```

---

## getSheetNames()

Gets an array of all sheet names in the workbook.

**Signature:**
```js
getSheetNames()
```

**Returns:** Array of sheet names

**Examples:**

```js
names = sheet.getSheetNames();
// Returns: ["Sheet1", "Sales", "Summary"]

// Loop through all sheets
for ( name in names ) {
    writeOutput( "Sheet: #name#" );
}
```

---

## clearSheet()

Clears all content from the current sheet.

**Signature:**
```js
clearSheet()
```

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
sheet.selectSheet( "Data" )
    .clearSheet()
    .save();
```

---

## 💡 Usage Patterns

### Multi-Sheet Workbook

```js
Spreadsheet( "quarterly-report.xlsx" )
    // Summary sheet
    .createAndSelectSheet( "Summary" )
    .setRowData( 1, [ "Quarter", "Revenue" ] )
    .addRow( [ "Q1", "=SUM(Q1!B:B)" ] )
    .addRow( [ "Q2", "=SUM(Q2!B:B)" ] )

    // Q1 detail sheet
    .createAndSelectSheet( "Q1" )
    .setRowData( 1, [ "Month", "Amount" ] )
    .addRow( [ "Jan", 10000 ] )
    .addRow( [ "Feb", 12000 ] )
    .addRow( [ "Mar", 11000 ] )

    // Q2 detail sheet
    .createAndSelectSheet( "Q2" )
    .setRowData( 1, [ "Month", "Amount" ] )
    .addRow( [ "Apr", 13000 ] )
    .addRow( [ "May", 14000 ] )
    .addRow( [ "Jun", 12500 ] )

    .save();
```

### Export All Sheets

```js
sheet = Spreadsheet( "workbook.xlsx", load = true );

names = sheet.getSheetNames();

for ( name in names ) {
    sheet.selectSheet( name );
    csv = sheet.toCSV();
    fileWrite( "#name#.csv", csv );
}
```

### Clean Up Workbook

```js
sheet = Spreadsheet( "workbook.xlsx", load = true );

// Delete temporary sheets
sheet.deleteSheet( "Temp1" )
    .deleteSheet( "Temp2" );

// Rename remaining
sheet.renameSheet( "Sheet1", "Final Data" );

sheet.save();
```

---

## 📚 See Also

- [User Guide - Multiple Sheets](../../user-guide.md#multiple-sheets)
- [Formulas](formulas.md) - Cross-sheet formulas

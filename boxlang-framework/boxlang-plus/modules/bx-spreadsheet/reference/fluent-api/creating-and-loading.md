---
description: Methods for creating new spreadsheets and loading existing files
icon: file-circle-plus
---

# 📄 Creating and Loading

Methods for creating new `SpreadsheetFile` objects and loading existing spreadsheet files.

---

## Spreadsheet()

Creates a new `SpreadsheetFile` object.

**Signature:**
```js
Spreadsheet( [string filename], [boolean load=false] )
```

**Parameters:**
- `filename` (optional) - Path to spreadsheet file
- `load` (optional) - Whether to load the file (default: false)

**Returns:** `SpreadsheetFile` object

**Examples:**

```js
// Create empty spreadsheet
sheet = Spreadsheet();

// Create with filename
sheet = Spreadsheet( "output.xlsx" );

// Load existing file
sheet = Spreadsheet( "existing.xlsx", load = true );
```

---

## load()

Loads an existing spreadsheet file into the `SpreadsheetFile` object.

**Signature:**
```js
load( string filepath )
```

**Parameters:**
- `filepath` (required) - Full path to the spreadsheet file

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Load file
sheet = Spreadsheet().load( "data.xlsx" );

// Load and chain operations
sheet = Spreadsheet()
    .load( "data.xlsx" )
    .addRow( [ "New data" ] )
    .save();
```

---

## toBinary()

Gets the spreadsheet as a binary object for saving or serving.

**Signature:**
```js
toBinary()
```

**Returns:** Binary data

**Examples:**

```js
sheet = Spreadsheet()
    .setRowData( 1, [ "Data" ] );

// Get as binary
binary = sheet.toBinary();

// Save binary
fileWrite( "output.xlsx", binary );

// Serve as download
cfheader( name="Content-Type", value="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" );
cfheader( name="Content-Disposition", value='attachment; filename="export.xlsx"' );
cfcontent( variable=binary, reset=true );
```

---

## 💡 Usage Patterns

### Create New File

```js
// Create and work with new spreadsheet
sheet = Spreadsheet( "report.xlsx" )
    .setRowData( 1, [ "Headers" ] )
    .addRow( [ "Data" ] )
    .save();
```

### Load Existing File

```js
// Load, modify, save
Spreadsheet( "existing.xlsx", load = true )
    .addRow( [ "New row" ] )
    .save();
```

### Create In-Memory

```js
// Create without filename, save later
sheet = Spreadsheet();
sheet.setRowData( 1, [ "Data" ] );
sheet.save( "output.xlsx" );
```

### Binary Export

```js
// Create and export as binary
binary = Spreadsheet()
    .setRowData( 1, [ "Export" ] )
    .toBinary();

fileWrite( "export.xlsx", binary );
```

---

## 📚 See Also

- [Saving and Exporting](saving-and-exporting.md)
- [Reading Data](reading-data.md)
- [Writing Data](writing-data.md)

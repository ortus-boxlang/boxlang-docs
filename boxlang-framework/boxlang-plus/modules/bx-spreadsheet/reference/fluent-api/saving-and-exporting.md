---
description: Methods for saving spreadsheets to files and exporting to various formats
icon: floppy-disk
---

# 💾 Saving and Exporting

Methods for saving spreadsheets to disk and exporting data to various formats.

---

## save()

Saves the spreadsheet to a file.

**Signature:**
```js
save( [string filepath], [boolean overwrite=false] )
```

**Parameters:**
- `filepath` (optional) - Full path to save file (uses initial filename if not provided)
- `overwrite` (optional) - Whether to overwrite existing file (default: false)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Save to initial filename
Spreadsheet( "output.xlsx" )
    .setRowData( 1, [ "Data" ] )
    .save();

// Save to different filename
sheet = Spreadsheet()
    .setRowData( 1, [ "Data" ] )
    .save( "export.xlsx" );

// Overwrite existing file
sheet.save( "existing.xlsx", overwrite = true );
```

---

## 📚 See Also

- [Creating and Loading](creating-and-loading.md)
- [Reading Data](reading-data.md) - Export methods (toCSV, toJson, etc.)
- [Data Export Guide](../../data-export.md)

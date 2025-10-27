---
description: Methods for protecting and unprotecting worksheets
icon: lock
---

# 🔒 Protection

Methods for securing worksheets with password protection.

---

## protectSheet()

Protects a worksheet with an optional password.

**Signature:**
```js
protectSheet( [string password], [string sheetName] )
```

**Parameters:**
- `password` (optional) - Password to protect sheet (no password if omitted)
- `sheetName` (optional) - Sheet to protect (current sheet if omitted)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Protect current sheet with password
sheet.protectSheet( "secret123" );

// Protect without password
sheet.protectSheet();

// Protect specific sheet
sheet.protectSheet( password = "abc", sheetName = "Data" );
```

{% hint style="info" %}
**Protection Capabilities:**
When a sheet is protected, users cannot:
- Modify cell values
- Insert/delete rows or columns
- Change formatting
- Modify formulas

Users can still:
- View all data
- Scroll and navigate
- Copy data
- Use filters (if enabled)
{% endhint %}

---

## unprotectSheet()

Removes protection from a worksheet.

**Signature:**
```js
unprotectSheet( [string password], [string sheetName] )
```

**Parameters:**
- `password` (optional) - Password if sheet was password-protected
- `sheetName` (optional) - Sheet to unprotect (current sheet if omitted)

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Unprotect current sheet
sheet.unprotectSheet( "secret123" );

// Unprotect specific sheet
sheet.unprotectSheet(
    password = "abc",
    sheetName = "Data"
);
```

---

## 💡 Usage Patterns

### Protect Template

```js
Spreadsheet( "template.xlsx" )
    .setRowData( 1, [ "Name", "Value" ] )
    .formatRow( 1, { bold: true, fgcolor: "lightgray" } )
    .protectSheet( "admin123" )
    .save();
```

### Multi-Sheet Protection

```js
sheet = Spreadsheet( "workbook.xlsx" )
    .createAndSelectSheet( "Read-Only Data" )
    .setRowData( 1, [ "Protected Data" ] )
    .protectSheet( "password" )

    .createAndSelectSheet( "Editable" )
    .setRowData( 1, [ "Editable Data" ] )
    // Don't protect this sheet

    .save();
```

### Temporary Protection

```js
// Load, protect, modify specific cells, save
sheet = Spreadsheet( "data.xlsx", load = true );

// Unprotect to make changes
sheet.unprotectSheet( "admin123" );

// Update data
sheet.setCellValue( 1, 1, "Updated" );

// Re-protect
sheet.protectSheet( "admin123" );

sheet.save();
```

### Form Template

```js
Spreadsheet( "form.xlsx" )
    .setRowData( 1, [ "Field", "Value" ] )
    .setRowData( 2, [ "Name:", "" ] )
    .setRowData( 3, [ "Email:", "" ] )
    .setRowData( 4, [ "Phone:", "" ] )

    // Format labels
    .formatColumn( 1, { bold: true, fgcolor: "lightblue" } )

    // Protect so only column 2 is editable
    .protectSheet()

    .save();
```

{% hint style="warning" %}
**Security Note:**
Excel sheet protection is NOT encryption. It prevents accidental changes but is not a security mechanism. For true security, use workbook encryption at the file level.
{% endhint %}

---

## 📚 See Also

- [Advanced Features Guide](../../advanced-features.md#protection)
- [Sheet Operations](sheet-operations.md)

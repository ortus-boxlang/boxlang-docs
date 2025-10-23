---
description: Premium spreadsheet module for reading, writing, styling, and transforming XLSX documents in BoxLang+ applications.
icon: file-spreadsheet
---

# 📊 `bx-spreadsheet` Module

The `bx-spreadsheet` module enables efficient creation and manipulation of spreadsheet (XLSX) documents: generating reports, importing data, and applying styles programmatically.

## 🚀 Features

* Read existing XLSX files
* Create multi-sheet workbooks
* Apply cell styles (fonts, colors, alignment)
* Auto-size columns & freeze panes
* Write formulas
* Export to file or binary stream
* Large dataset streaming patterns

## 📦 Installation

### Via CommandBox

```bash
box install bx-spreadsheet
```

### Via BoxLang

```bash
install-bx-module bx-spreadsheet
```

## ⚙ Basic Workbook Creation

```js
sheetData = [
    ["ID", "Name", "Score"],
    [1, "Alice", 92],
    [2, "Bob", 85],
    [3, "Chris", 78]
];

workbook = spreadsheetNew();
sheet    = spreadsheetAddSheet( workbook, "Results" );

spreadsheetAddRows( sheet, sheetData );
spreadsheetAutoSize( sheet );

binary = spreadsheetWriteBinary( workbook );
fileWrite( expandPath( "results.xlsx" ), binary );
```

## 🎨 Styling Example

```js
headerStyle = {
  bold: true,
  backgroundColor: "#2c3e50",
  fontColor: "#ffffff",
  horizontalAlign: "center"
};

spreadsheetApplyStyleRow( sheet, row = 1, style = headerStyle );
```

## 📥 Reading Data

```js
incoming = fileReadBinary( expandPath( "import.xlsx" ) );
wb       = spreadsheetRead( incoming );
rows     = spreadsheetGetSheetData( wb, "Sheet1" );

for ( r in rows ) {
    // Process each row
}
```

## 🧪 Formulas

```js
spreadsheetSetCell( sheet, row = 5, column = 4, value = "=SUM(D2:D4)" );
```

## 🔐 Entitlement

Requires active BoxLang+ subscription. Fallback: throw descriptive exception if entitlement invalid.

## 🛡 Error Handling

```js
try {
    wb = spreadsheetRead( incoming );
} catch ( e ) {
    writeLog( text = "Spreadsheet read failed: " & e.message, type = "error" );
}
```

## 📏 Performance Tips

* Stream large datasets in batches
* Minimize style operations inside tight loops
* Prefer binary output for direct HTTP streaming

## 📎 Related Modules

{% content-ref url="bx-csv.md" %}
CSV Module
{% endcontent-ref %}

{% content-ref url="bx-plus.md" %}
Subscription Bootstrap
{% endcontent-ref %}

---
Next: Handle delimited data with the [`bx-csv` module](bx-csv.md).

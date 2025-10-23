---
description: Premium CSV processing module for high-performance parsing and generation of delimited datasets in BoxLang+ applications.
icon: table
---

# 📄 `bx-csv` Module

The `bx-csv` module streamlines working with delimited data (CSV/TSV). It emphasizes performance, streaming, and memory efficiency for large datasets.

## 🚀 Features

* Streaming CSV parsing (low memory footprint)
* Custom delimiters (comma, tab, pipe, etc.)
* Quoted value & escape character handling
* Header row detection & mapping to structs
* Generate CSV from arrays, queries, or iterators
* Optional type coercion (numeric, boolean)

## 📦 Installation

### Via CommandBox

```bash
box install bx-csv
```

### Via BoxLang

```bash
install-bx-module bx-csv
```

## 📥 Parsing Example

```js
csvText = fileRead( expandPath( "users.csv" ) );
records  = csvParse( csvText, hasHeader = true );

for ( r in records ) {
    // r is a struct keyed by header names
    writeOutput( r.name & "<br>" );
}
```

## 🌊 Streaming Parse (Conceptual)

```js
stream = fileOpen( expandPath( "large.csv" ), "read" );
parser = csvParserNew( stream, hasHeader = true );

while ( parser.hasNext() ) {
    row = parser.next();
    // process row
}

fileClose( stream );
```

## 📤 Generation Example

```js
rows = [
  { id: 1, name: "Alice", active: true },
  { id: 2, name: "Bob", active: false }
];

csvOut = csvGenerate( rows, headers = ["id","name","active" ] );
fileWrite( expandPath( "export.csv" ), csvOut );
```

## ⚙ Options Overview

| Option | Purpose | Default |
| ------ | ------- | ------- |
| `delimiter` | Field separator | `,` |
| `quoteChar` | Quote character | `"` |
| `escapeChar` | Escape sequence | `\\` |
| `hasHeader` | Treat first row as header | `false` |
| `coerceTypes` | Attempt to cast numeric/boolean values | `false` |

## 🔐 Entitlement

Requires BoxLang+ subscription. Entitlement failures surface as descriptive exceptions.

## 🛡 Error Handling

```js
try {
    records = csvParse( csvText, hasHeader = true );
} catch ( e ) {
    writeLog( text = "CSV parse failed: " & e.message, type = "error" );
}
```

## 🧪 Performance Tips

* Prefer streaming for files > 5MB
* Disable coercion when raw text needed
* Reuse parser instances when feasible

## 📎 Related Modules

{% content-ref url="bx-spreadsheet.md" %}
Spreadsheet Module
{% endcontent-ref %}

{% content-ref url="bx-plus.md" %}
Subscription Bootstrap
{% endcontent-ref %}

---
Next: Scale distributed operations with the [`bx-couchbase` module](bx-couchbase.md).

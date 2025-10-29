---
description: Memory-efficient processing of large Excel files using the streaming API with Consumer callbacks
icon: rocket
---

# 🚀 Large File Streaming

The Spreadsheet Module provides **true streaming capabilities** for processing large Excel files without loading the entire workbook into memory. This is essential when working with spreadsheets containing thousands of rows that would otherwise cause memory issues.

{% hint style="success" %}
**Memory Efficient**: The streaming API processes files row-by-row, keeping only ~100 rows in memory at any given time. This allows you to process spreadsheets with millions of rows on standard hardware.
{% endhint %}

---

## 🎯 Why Use Streaming?

### Traditional Loading vs. Streaming

**Traditional Approach (Loads Entire File):**

```js
// ⚠️ Loads ALL rows into memory at once
sheet = Spreadsheet( "huge-file.xlsx" );
data = sheet.toArray();  // Could consume gigabytes of RAM

for ( row in data ) {
    // Process each row
}
```

**Streaming Approach (Memory Efficient):**

```js
// ✅ Processes rows one at a time
Spreadsheet().process( "huge-file.xlsx", ( row ) => {
    // Process row immediately, then discard from memory
    println( row );
});
```

### When to Use Streaming

Use streaming for:

- **Large files** with thousands of rows (> 10,000 rows)
- **Import operations** where you process data sequentially
- **Memory-constrained environments** where RAM is limited
- **Data transformation** that doesn't require random access to all rows
- **Export to databases** or other formats where you process row-by-row

Use traditional loading for:

- **Small files** (< 10,000 rows)
- **Random access** where you need to jump between rows
- **Modification operations** where you need to write back to the file
- **Complex operations** requiring multiple passes over the data

---

## 🔧 How It Works

### Technology Stack

The streaming implementation uses different approaches based on file format:

| Format | Technology | Memory Usage | Notes |
|--------|------------|--------------|-------|
| `.xlsx` | excel-streaming-reader | ~100 rows | True streaming with Apache POI wrapper |
| `.xls` | Apache POI (HSSF) | Full file | Legacy format requires full load |

{% hint style="info" %}
**XLSX Recommended**: For large file processing, always use `.xlsx` format. The legacy `.xls` format does not support streaming due to its binary structure.
{% endhint %}

### Streaming Configuration

The streaming reader is configured with optimal defaults:

```java
// Internal configuration (you don't need to set this)
StreamingReader.builder()
    .rowCacheSize( 100 )      // Keep 100 rows in memory
    .bufferSize( 4096 )       // 4KB read buffer
    .open( inputStream );
```

---

## 📚 API Methods

The streaming API provides three `process()` methods that accept **Consumer callbacks**:

### Method 1: Process File by Path

Process all rows from the first sheet in a file:

```js
Spreadsheet().process( filePath, consumer );
```

**Parameters:**

- `filePath` (String) - Absolute or relative path to Excel file
- `consumer` (Consumer<Array>) - Callback function receiving each row as an Array

### Method 2: Process Specific Sheet

Process rows from a named sheet:

```js
Spreadsheet().process( filePath, sheetName, consumer );
```

**Parameters:**

- `filePath` (String) - Absolute or relative path to Excel file
- `sheetName` (String) - Name of the sheet to process
- `consumer` (Consumer<Array>) - Callback function receiving each row as an Array

### Method 3: Process Loaded Workbook

Process an already-loaded workbook (still memory-efficient for active sheet):

```js
sheet = Spreadsheet( "file.xlsx" );
sheet.process( consumer );
```

**Parameters:**

- `consumer` (Consumer<Array>) - Callback function receiving each row as an Array

{% hint style="warning" %}
**Method 3 Note**: This method processes the currently active sheet from a workbook already loaded into memory. For truly large files, prefer Methods 1 or 2 which stream directly from disk.
{% endhint %}

---

## 💡 Examples

### Basic Row Processing

Process each row and print its contents:

```js
Spreadsheet().process( "sales-data.xlsx", ( row ) => {
    println( "Row: #row.toString()#" );
});
```

### Data Import to Database

Stream large file directly into a database:

```js
Spreadsheet().process( "customers.xlsx", ( row ) => {
    // Skip header row
    if ( row[1] == "Name" ) return;

    // Insert into database
    queryExecute(
        "INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)",
        [ row[1], row[2], row[3] ]
    );
});
```

### Processing Specific Sheet

Stream data from a named sheet:

```js
Spreadsheet().process(
    "multi-sheet-report.xlsx",
    "Sales Data",
    ( row ) => {
        // Process only "Sales Data" sheet
        processOrder( row );
    }
);
```

### Type-Safe Data Processing

Handle different cell value types:

```js
Spreadsheet().process( "data.xlsx", ( row ) => {
    // Access cells by index (1-based)
    productName = row[1];        // String
    quantity = row[2];           // Number (always Double)
    price = row[3];              // Number (always Double)
    inStock = row[4];            // Boolean
    lastUpdated = row[5];        // LocalDateTime

    // Calculate total
    total = quantity * price;

    println( "#productName#: #total#" );
});
```

### Filtering During Streaming

Filter rows during processing to reduce memory:

```js
results = [];

Spreadsheet().process( "orders.xlsx", ( row ) => {
    // Only keep high-value orders
    if ( row[3] > 10000 ) {
        results.append({
            orderId: row[1],
            customer: row[2],
            amount: row[3]
        });
    }
});

println( "Found #results.len()# high-value orders" );
```

### Streaming with Row Counter

Track progress while processing:

```js
rowCount = 0;

Spreadsheet().process( "large-file.xlsx", ( row ) => {
    rowCount++;

    // Log progress every 1000 rows
    if ( rowCount % 1000 == 0 ) {
        println( "Processed #rowCount# rows..." );
    }

    processRow( row );
});

println( "Total rows processed: #rowCount#" );
```

### Error Handling in Streaming

Gracefully handle errors during streaming:

```js
errorCount = 0;

try {
    Spreadsheet().process( "data.xlsx", ( row ) => {
        try {
            // Attempt to process row
            processBusinessLogic( row );
        } catch ( any e ) {
            // Log error but continue processing
            errorCount++;
            writeLog( "Error processing row: #e.message#" );
        }
    });
} catch ( any e ) {
    writeLog( "Fatal error reading file: #e.message#" );
}

println( "Processing complete. Errors: #errorCount#" );
```

### Chaining with Fluent API

Combine streaming with other fluent operations:

```js
// Create summary spreadsheet from streamed data
summary = [];

Spreadsheet()
    .process( "source-data.xlsx", ( row ) => {
        // Aggregate data during streaming
        summary.append( summarizeRow( row ) );
    });

// Create new spreadsheet from aggregated data
Spreadsheet()
    .addRow( [ "Summary", "Count", "Total" ] )
    .formatRow( 1, { bold: true, fgcolor: "blue" } )
    .addRows( summary )
    .autoSizeColumns()
    .save( "summary-report.xlsx" );
```

---

## 🎭 Cell Value Types

The streaming API returns strongly-typed values based on Excel cell types:

| Excel Type | BoxLang Type | Example |
|------------|--------------|---------|
| String | `String` | `"Hello World"` |
| Numeric | `Double` | `123.45` (always Double, even for integers) |
| Boolean | `Boolean` | `true` or `false` |
| Date/Time | `LocalDateTime` | `2025-01-15T10:30:00` |
| Formula | Evaluated Result | Returns the cached formula result value |
| Blank | `""` (empty string) | `""` |
| Error | `String` | Error code like `"#DIV/0!"` |

{% hint style="info" %}
**Numeric Values**: All numeric cells return `Double` type for consistency, even if the Excel cell contains an integer like `42`. This matches the behavior of `SpreadsheetUtil` and ensures predictable type handling.
{% endhint %}

### Formula Handling

Formulas are automatically evaluated using cached results:

```js
// Excel cell contains formula: =A1*B1
Spreadsheet().process( "formulas.xlsx", ( row ) => {
    result = row[3];  // Returns calculated Double value, not formula string
});
```

---

## ⚡ Performance Considerations

### Memory Usage

| File Size | Traditional Loading | Streaming API |
|-----------|---------------------|---------------|
| 10 MB / 50K rows | ~150 MB RAM | ~5 MB RAM |
| 50 MB / 250K rows | ~750 MB RAM | ~5 MB RAM |
| 200 MB / 1M rows | ~3 GB RAM | ~5 MB RAM |

### Processing Speed

- **Streaming is slightly slower** than traditional loading due to on-demand parsing
- **Tradeoff**: Slightly longer processing time for dramatically reduced memory usage
- **Best Practice**: Use streaming for files > 10,000 rows where memory is a concern

### Optimization Tips

**DO:**

- ✅ Process data directly in the Consumer callback
- ✅ Write to database or file immediately
- ✅ Aggregate/summarize data during streaming
- ✅ Use filtering to reduce memory accumulation

**DON'T:**

- ❌ Store all rows in an array during streaming (defeats the purpose)
- ❌ Make blocking I/O calls in the callback (slows processing)
- ❌ Modify the source file during streaming
- ❌ Use streaming for small files (< 10K rows)

---

## 🔄 Streaming vs. Traditional Loading

### Comparison Table

| Feature | Streaming | Traditional Loading |
|---------|-----------|---------------------|
| Memory Usage | Constant (~5 MB) | Scales with file size |
| Random Access | ❌ Sequential only | ✅ Full random access |
| Modification | ❌ Read-only | ✅ Read and write |
| XLSX Support | ✅ True streaming | ✅ Full support |
| XLS Support | ⚠️ Full load required | ✅ Full support |
| Best For | Large imports | Small files, editing |

### Decision Matrix

**Use Streaming when:**

- File size > 10,000 rows
- Sequential processing is sufficient
- Memory is limited
- Read-only operations
- Format is `.xlsx`

**Use Traditional Loading when:**

- File size < 10,000 rows
- Need to modify cells
- Random access to rows required
- Multiple passes over data needed
- Format is `.xls` (no streaming available)

---

## 🔐 Best Practices

### 1. Always Use XLSX for Large Files

```js
// ✅ Good: XLSX supports streaming
Spreadsheet().process( "large-data.xlsx", processor );

// ❌ Bad: XLS requires full load
Spreadsheet().process( "large-data.xls", processor );  // Loads entire file
```

### 2. Process Data Immediately

```js
// ✅ Good: Process and discard
Spreadsheet().process( "data.xlsx", ( row ) => {
    saveToDatabase( row );  // Immediate processing
});

// ❌ Bad: Defeats streaming purpose
allRows = [];
Spreadsheet().process( "data.xlsx", ( row ) => {
    allRows.append( row );  // Accumulates in memory!
});
```

### 3. Handle Errors Gracefully

```js
// ✅ Good: Error handling per row
Spreadsheet().process( "data.xlsx", ( row ) => {
    try {
        processRow( row );
    } catch ( any e ) {
        logError( e );  // Continue processing
    }
});
```

### 4. Use Filtering Early

```js
// ✅ Good: Filter during streaming
Spreadsheet().process( "data.xlsx", ( row ) => {
    if ( row[1] != "Invalid" ) {  // Filter early
        processValid( row );
    }
});
```

### 5. Monitor Progress for Large Files

```js
// ✅ Good: Progress tracking
counter = 0;
Spreadsheet().process( "huge-file.xlsx", ( row ) => {
    if ( ++counter % 10000 == 0 ) {
        println( "Processed #counter# rows" );
    }
});
```

---

## 🐛 Troubleshooting

### Issue: OutOfMemoryError

**Cause**: Accumulating rows in memory during streaming

**Solution**: Process rows immediately without storing

```js
// ❌ Wrong
results = [];
Spreadsheet().process( "data.xlsx", ( row ) => results.append(row) );

// ✅ Correct
Spreadsheet().process( "data.xlsx", ( row ) => saveToDatabase(row) );
```

### Issue: Slow Processing

**Cause**: Blocking I/O or expensive operations in callback

**Solution**: Optimize callback logic

```js
// ❌ Slow: Multiple database calls per row
Spreadsheet().process( "data.xlsx", ( row ) => {
    queryExecute( "INSERT..." );  // Slow per-row insert
});

// ✅ Fast: Batch inserts
batch = [];
Spreadsheet().process( "data.xlsx", ( row ) => {
    batch.append( row );
    if ( batch.len() >= 1000 ) {
        bulkInsert( batch );
        batch = [];
    }
});
bulkInsert( batch );  // Insert remaining
```

### Issue: XLS Files Not Streaming

**Cause**: Legacy `.xls` format doesn't support streaming

**Solution**: Convert to `.xlsx` or accept full loading

```js
// Convert XLS to XLSX first
Spreadsheet( "old-file.xls" ).save( "new-file.xlsx" );

// Now stream the XLSX version
Spreadsheet().process( "new-file.xlsx", processor );
```

---

## 📖 Related Documentation

- [Fluent API Reference](reference/fluent-api/) - Complete API documentation
- [Data Export](data-export.md) - Exporting data to various formats
- [User Guide](user-guide.md) - General usage patterns
- [Examples](examples.md) - More code examples

---

## 🎓 Summary

The streaming API provides:

✅ **Memory-efficient** processing of large files
✅ **Simple Consumer callback** pattern
✅ **True streaming** for `.xlsx` files via excel-streaming-reader
✅ **Type-safe** cell value handling
✅ **Production-ready** for files with millions of rows

Remember: Use streaming for large files, traditional loading for small files or when you need to modify data.

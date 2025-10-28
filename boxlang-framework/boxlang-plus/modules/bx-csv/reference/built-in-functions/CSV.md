[comment]: # (Note: This documentation is generated dynamically in the build process. To modify the contents, change the javadoc on the BIF class)

# Function: `CSV`

Returns a fluent CSVFile object for creating or manipulating CSV files.

## Method Signature

```
CSV( [path], [delimiter], [hasHeaders], [trim], [ignoreEmptyLines], [skipHeaderRecord] )
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | string | No | Path to the CSV file | `null` |
| `delimiter` | char | No | Delimiter character | `,` |
| `hasHeaders` | boolean | No | Whether the CSV has headers | `true` |
| `trim` | boolean | No | Whether to trim whitespace from values | `true` |
| `ignoreEmptyLines` | boolean | No | Whether to ignore empty lines | `true` |
| `skipHeaderRecord` | boolean | No | Whether to skip the header record when parsing | `false` |

## Examples

```javascript
// Create new
csv = CSV();

// Load existing
csv = CSV( "data.csv" );

// Load with custom delimiter
csv = CSV( path="data.txt", delimiter="|" );

// Load with full configuration
csv = CSV(
    path="data.csv",
    delimiter=",",
    hasHeaders=true,
    trim=true,
    ignoreEmptyLines=true,
    skipHeaderRecord=true
);
```

## Related

- [File I/O Functions](../../../../../boxlang-language/reference/built-in-functions/io/) - File reading and writing operations
- [Array Functions](../../../../../boxlang-language/reference/built-in-functions/arrays.md) - Array manipulation for CSV data processing
- [Query Functions](../../../../../boxlang-language/reference/built-in-functions/queries.md) - Working with query objects and CSV data
- [String Functions](../../../../../boxlang-language/reference/built-in-functions/strings.md) - String manipulation for CSV processing
- [JSON Functions](../../../../../boxlang-language/reference/built-in-functions/json.md) - Converting between CSV and JSON formats

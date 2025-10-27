---
description: Methods for adding data validation rules to cells and ranges
icon: shield-check
---

# ✅ Data Validation

Methods for adding dropdown lists, numeric restrictions, and custom validation rules to cells.

---

## addDataValidation()

Adds data validation rules to a cell or range.

**Signature:**
```js
addDataValidation(
    numeric row,
    numeric column,
    string validationType,
    any value1,
    [any value2],
    [boolean allowBlank=true],
    [boolean showDropdown=true],
    [string errorTitle],
    [string errorMessage]
)
```

**Parameters:**
- `row` (required) - Starting row
- `column` (required) - Starting column
- `validationType` (required) - Type of validation (see types below)
- `value1` (required) - First constraint value
- `value2` (optional) - Second constraint value (for ranges)
- `allowBlank` (optional) - Allow blank cells (default: true)
- `showDropdown` (optional) - Show dropdown arrow (default: true)
- `errorTitle` (optional) - Error dialog title
- `errorMessage` (optional) - Error dialog message

**Validation Types:**
- `"LIST"` - Dropdown list of values
- `"DECIMAL"` - Decimal number constraints
- `"INTEGER"` - Whole number constraints
- `"DATE"` - Date constraints
- `"TIME"` - Time constraints
- `"TEXT_LENGTH"` - Text length constraints
- `"CUSTOM"` - Custom formula validation

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Dropdown list
sheet.addDataValidation(
    row = 2,
    column = 3,
    validationType = "LIST",
    value1 = "Small,Medium,Large"
);

// Numeric range
sheet.addDataValidation(
    row = 2,
    column = 4,
    validationType = "DECIMAL",
    value1 = 0,
    value2 = 100,
    errorTitle = "Invalid Value",
    errorMessage = "Must be between 0 and 100"
);

// Date validation
sheet.addDataValidation(
    row = 2,
    column = 5,
    validationType = "DATE",
    value1 = createDate( 2024, 1, 1 ),
    value2 = createDate( 2024, 12, 31 )
);

// Text length
sheet.addDataValidation(
    row = 2,
    column = 2,
    validationType = "TEXT_LENGTH",
    value1 = 1,
    value2 = 50
);
```

---

## addDataValidationRange()

Adds data validation to a range of cells.

**Signature:**
```js
addDataValidationRange(
    numeric startRow,
    numeric startColumn,
    numeric endRow,
    numeric endColumn,
    string validationType,
    any value1,
    [any value2],
    [boolean allowBlank=true],
    [boolean showDropdown=true],
    [string errorTitle],
    [string errorMessage]
)
```

**Parameters:**
Same as `addDataValidation()` with row/column range

**Returns:** `SpreadsheetFile` (chainable)

**Examples:**

```js
// Dropdown for entire column
sheet.addDataValidationRange(
    startRow = 2,
    startColumn = 3,
    endRow = 100,
    endColumn = 3,
    validationType = "LIST",
    value1 = "Pending,Approved,Rejected"
);

// Numeric constraints for range
sheet.addDataValidationRange(
    startRow = 2,
    startColumn = 5,
    endRow = 50,
    endColumn = 5,
    validationType = "INTEGER",
    value1 = 1,
    value2 = 10
);
```

---

## 💡 Common Validation Patterns

### Status Dropdown

```js
sheet.setRowData( 1, [ "Task", "Status" ] )
    .addDataValidationRange(
        startRow = 2,
        startColumn = 2,
        endRow = 100,
        endColumn = 2,
        validationType = "LIST",
        value1 = "Not Started,In Progress,Complete"
    );
```

### Percentage Validation

```js
sheet.addDataValidation(
    row = 2,
    column = 3,
    validationType = "DECIMAL",
    value1 = 0,
    value2 = 1,
    errorTitle = "Invalid Percentage",
    errorMessage = "Enter a value between 0 and 1"
);
```

### Date Range

```js
startDate = createDate( 2024, 1, 1 );
endDate = createDate( 2024, 12, 31 );

sheet.addDataValidationRange(
    startRow = 2,
    startColumn = 4,
    endRow = 100,
    endColumn = 4,
    validationType = "DATE",
    value1 = startDate,
    value2 = endDate,
    errorTitle = "Invalid Date",
    errorMessage = "Must be in 2024"
);
```

### Priority Levels

```js
sheet.addDataValidation(
    row = 2,
    column = 5,
    validationType = "LIST",
    value1 = "Low,Medium,High,Critical",
    showDropdown = true,
    allowBlank = false
);
```

---

## 📚 See Also

- [Advanced Features Guide](../../advanced-features.md#data-validation)
- [User Guide - Data Validation](../../user-guide.md#data-validation)

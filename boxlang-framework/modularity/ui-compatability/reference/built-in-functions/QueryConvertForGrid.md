
# Function: `QueryConvertForGrid`

Converts a query object to a format suitable for grid display with pagination and sorting capabilities.

## Method Signature

```
QueryConvertForGrid(query, page, pagesize)
```

### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `query` | `query` | `true` | The query object to convert |  |
| `page` | `numeric` | `false` | The page number (1-based) | `1` |
| `pagesize` | `numeric` | `false` | The number of rows per page | `25` |

## Examples

```boxlang
// Convert a query for grid display
myQuery = QueryNew("id,name,email", "integer,varchar,varchar");
QueryAddRow(myQuery, [
    {id: 1, name: "John Doe", email: "john@example.com"},
    {id: 2, name: "Jane Smith", email: "jane@example.com"}
]);

// Convert with pagination
gridData = QueryConvertForGrid(myQuery, 1, 10);

// The result contains:
// gridData.QUERY - The paginated query data
// gridData.TOTALROWCOUNT - Total number of rows
// gridData.PAGE - Current page number
// gridData.PAGESIZE - Rows per page
// gridData.TOTALPAGES - Total number of pages
// gridData.STARTROW - First row index of current page
// gridData.ENDROW - Last row index of current page
```

## Related

* [AjaxLink](./AjaxLink.md)
* [AjaxOnLoad](./AjaxOnLoad.md)

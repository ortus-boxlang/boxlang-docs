# Component: `Grid`

Generates a data grid with sorting, editing, and pagination capabilities.

## Syntax

```boxlang
<bx:grid 
    name="string"
    query="query"
    pageSize="numeric"
    sortable="boolean"
    editable="boolean"
    height="string"
    width="string">
    <!-- Optional gridcolumn children -->
</bx:grid>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | **Yes** | Grid control name | |
| `query` | `query` | No | Query object to populate the grid | |
| `pageSize` | `numeric` | No | Number of rows per page | `25` |
| `sortable` | `boolean` | No | Enable column sorting | `true` |
| `editable` | `boolean` | No | Enable cell editing | `false` |
| `autoWidth` | `boolean` | No | Auto-size columns to fit content | `false` |
| `height` | `string` | No | Grid height (CSS value) | |
| `width` | `string` | No | Grid width (CSS value) | |
| `stripeRows` | `boolean` | No | Alternate row colors | `true` |
| `showHeaders` | `boolean` | No | Show column headers | `true` |
| `selectMode` | `string` | No | Row selection mode: none, single, multi | `"single"` |
| `onLoad` | `string` | No | JavaScript function called when grid loads | |
| `onEdit` | `string` | No | JavaScript function called when cell is edited | |
| `onSort` | `string` | No | JavaScript function called when column is sorted | |
| `id` | `string` | No | HTML element ID | Auto-generated |
| `class` | `string` | No | Additional CSS classes | |
| `style` | `string` | No | Additional CSS styles | |

## Examples

### Basic grid with query data

```boxlang
<bx:grid name="userGrid" query="#getUserQuery()#" pageSize="10">
    <bx:gridcolumn name="id" header="ID" width="80" />
    <bx:gridcolumn name="name" header="Name" width="200" />
    <bx:gridcolumn name="email" header="Email" width="250" />
</bx:grid>
```

### Editable grid with event handlers

```boxlang
<bx:grid 
    name="editableGrid" 
    query="#myQuery#" 
    editable="true"
    onEdit="handleEdit"
    onSort="handleSort">
    <bx:gridcolumn name="name" header="Name" editable="true" />
    <bx:gridcolumn name="status" header="Status" editable="true" />
</bx:grid>

<script>
function handleEdit(grid, row, col, oldValue, newValue) {
    console.log("Cell edited:", oldValue, "->", newValue);
}

function handleSort(grid, column, direction) {
    console.log("Column sorted:", column, direction);
}
</script>
```

### Grid with custom styling

```boxlang
<bx:grid 
    name="styledGrid" 
    query="#myQuery#"
    height="400px" 
    width="100%"
    stripeRows="true"
    selectMode="multi"
    class="custom-grid">
</bx:grid>
```

## Usage Notes

- The `name` attribute is required and must be unique on the page
- Use `<bx:gridcolumn>` child components to define columns
- If no columns are defined, all query columns are displayed automatically
- The grid supports AJAX loading and updating of data
- Requires BoxLang AJAX JavaScript files (use `<bx:ajaximport>`)

## Related Components

- [GridColumn](GridColumn.md) - Define grid columns
- [GridRow](GridRow.md) - Define grid rows
- [GridUpdate](GridUpdate.md) - Update grid data
- [AjaxImport](AjaxImport.md) - Import required AJAX files

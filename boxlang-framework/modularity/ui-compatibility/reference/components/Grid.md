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
    autoWidth="boolean"
    height="string"
    width="string"
    stripeRows="boolean"
    showHeaders="boolean"
    selectMode="string"
    onLoad="string"
    onEdit="string"
    onSort="string"
    id="string"
    class="string"
    style="string"
    appendKey="boolean"
    bgColor="string"
    bind="string"
    bindOnLoad="boolean"
    bold="boolean"
    colHeaderBold="boolean"
    colHeaderFont="string"
    colHeaderFontSize="number"
    colHeaderItalic="boolean"
    colHeaderTextColor="string"
    collapsible="boolean"
    delete="boolean"
    deleteButton="boolean"
    enabled="boolean"
    font="string"
    fontSize="number"
    format="string"
    gridDataAlign="string"
    groupfield="string"
    href="string"
    hrefKey="string"
    hSpace="number"
    insert="boolean"
    insertButton="boolean"
    italic="boolean"
    maxRows="number"
    multirowselect="boolean"
    notSupported="string"
    onBlur="string"
    onChange="string"
    onError="string"
    onFocus="string"
    onValidate="string"
    preservePageOnSort="boolean"
    resetHead="boolean"
    rowHeight="number"
    selectColor="string"
    selectOnLoad="boolean"
    stripeRowColor="string"
    target="string"
    textColor="string"
    title="string"
    tooltip="string"
    visible="boolean">
    <!-- Optional gridcolumn children -->
</bx:grid>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | **Yes** | Grid control name | |
| `query` | `any` | No | Query object to populate the grid | `""` |
| `pageSize` | `number` | No | Number of rows per page | `25` |
| `sortable` | `boolean` | No | Enable column sorting | `true` |
| `editable` | `boolean` | No | Enable cell editing | `false` |
| `autoWidth` | `boolean` | No | Auto-size columns to fit content | `false` |
| `height` | `string` | No | Grid height (CSS value) | `""` |
| `width` | `string` | No | Grid width (CSS value) | `""` |
| `stripeRows` | `boolean` | No | Alternate row colors | `true` |
| `showHeaders` | `boolean` | No | Show column headers | `true` |
| `selectMode` | `string` | No | Selection mode: `edit`, `row`, `single`, `column`, `browse`, `all` | `all` |
| `onLoad` | `string` | No | JavaScript function called when grid loads | `""` |
| `onEdit` | `string` | No | JavaScript function called when cell is edited | `""` |
| `onSort` | `string` | No | JavaScript function called when column is sorted | `""` |
| `id` | `string` | No | HTML element ID | Auto-generated |
| `class` | `string` | No | Additional CSS classes | `""` |
| `style` | `string` | No | Additional CSS styles | `""` |
| `appendKey` | `boolean` | No | Append key field to form data | `false` |
| `bgColor` | `string` | No | Background color for grid | `""` |
| `bind` | `string` | No | Data binding expression for AJAX | `""` |
| `bindOnLoad` | `boolean` | No | Whether to bind data on initial load | `true` |
| `bold` | `boolean` | No | Bold text formatting | `false` |
| `colHeaderBold` | `boolean` | No | Bold column headers | `false` |
| `colHeaderFont` | `string` | No | Column header font family | `""` |
| `colHeaderFontSize` | `number` | No | Column header font size | `""` |
| `colHeaderItalic` | `boolean` | No | Italic column headers | `false` |
| `colHeaderTextColor` | `string` | No | Column header text color | `""` |
| `collapsible` | `boolean` | No | Whether grid is collapsible | `false` |
| `delete` | `boolean` | No | Allow delete operations | `false` |
| `deleteButton` | `boolean` | No | Show delete button | `false` |
| `enabled` | `boolean` | No | Enable/disable grid | `true` |
| `font` | `string` | No | Text font family | `""` |
| `fontSize` | `number` | No | Text font size | `""` |
| `format` | `string` | No | Output format (only `html` supported) | `html` |
| `gridDataAlign` | `string` | No | Data alignment: `left`, `center`, `right` | `left` |
| `groupfield` | `string` | No | Field to group by | `""` |
| `href` | `string` | No | URL for links in grid | `""` |
| `hrefKey` | `string` | No | Key field for href links | `""` |
| `hSpace` | `number` | No | Horizontal spacing | `0` |
| `insert` | `boolean` | No | Allow insert operations | `false` |
| `insertButton` | `boolean` | No | Show insert button | `false` |
| `italic` | `boolean` | No | Italic text formatting | `false` |
| `maxRows` | `number` | No | Maximum rows to display (`0` = no limit) | `0` |
| `multirowselect` | `boolean` | No | Multiple row selection | `false` |
| `notSupported` | `string` | No | Message when grid format not supported | `""` |
| `onBlur` | `string` | No | Blur event handler | `""` |
| `onChange` | `string` | No | Change event handler | `""` |
| `onError` | `string` | No | Error event handler | `""` |
| `onFocus` | `string` | No | Focus event handler | `""` |
| `onValidate` | `string` | No | Validation event handler | `""` |
| `preservePageOnSort` | `boolean` | No | Preserve page when sorting | `false` |
| `resetHead` | `boolean` | No | Reset column headers | `false` |
| `rowHeight` | `number` | No | Height of rows in pixels | `""` |
| `selectColor` | `string` | No | Selection highlight color | `""` |
| `selectOnLoad` | `boolean` | No | Select first row on load | `false` |
| `stripeRowColor` | `string` | No | Alternate row color | `""` |
| `target` | `string` | No | Target for href links | `""` |
| `textColor` | `string` | No | Text color | `""` |
| `title` | `string` | No | Grid title | `""` |
| `tooltip` | `string` | No | Tooltip text | `""` |
| `visible` | `boolean` | No | Grid visibility | `true` |

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

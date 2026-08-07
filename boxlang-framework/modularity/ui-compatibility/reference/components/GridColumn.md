# Component: `GridColumn`

Defines a column in a data grid component.

## Syntax

```boxlang
<bx:gridcolumn 
    name="string"
    header="string"
    width="string"
    sortable="boolean"
    editable="boolean"
    dataAlign="string"
    headerAlign="string"
    display="boolean"
    type="string"
    numberFormat="string"
    dateFormat="string"
    values="string"
    valuesDisplay="string"
    href="string"
    target="string" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | Yes | Column data field name | |
| `header` | `string` | No | Column header text | `name` |
| `width` | `string` | No | Column width (CSS value) | |
| `sortable` | `boolean` | No | Enable sorting for this column | `true` |
| `editable` | `boolean` | No | Enable editing for this column | `false` |
| `dataAlign` | `string` | No | Data alignment: `left`, `center`, `right` | `left` |
| `headerAlign` | `string` | No | Header alignment: `left`, `center`, `right` | `left` |
| `display` | `boolean` | No | Whether to display this column | `true` |
| `type` | `string` | No | Data type: `string`, `html`, `numeric`, `date`, `boolean`. If `html`, the content will not be HTML-encoded | `string` |
| `numberFormat` | `string` | No | Number format mask for numeric columns | |
| `dateFormat` | `string` | No | Date format mask for date columns | |
| `values` | `string` | No | Comma-delimited list of values for dropdown editing | |
| `valuesDisplay` | `string` | No | Display values corresponding to `values` list | |
| `href` | `string` | No | URL pattern for making column data into links | |
| `target` | `string` | No | Link target (`_blank`, `_self`, etc.) | |

## Usage Notes

- Must be used within a `<bx:grid>` component
- The `name` attribute should match a field in the grid's query data

## Related Components

- [Grid](Grid.md) - Parent grid component
- [GridRow](GridRow.md) - Grid row component

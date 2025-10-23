# Component: `GridColumn`

Defines a column in a data grid component.

## Syntax

```boxlang
<bx:gridcolumn 
    name="string"
    header="string"
    width="string"
    editable="boolean"
    sortable="boolean"
    display="boolean" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | Yes | Column field name from query | |
| `header` | `string` | No | Column header text | Column name |
| `width` | `string` | No | Column width (CSS value) | Auto |
| `editable` | `boolean` | No | Enable cell editing | `false` |
| `sortable` | `boolean` | No | Enable column sorting | `true` |
| `display` | `boolean` | No | Show/hide column | `true` |

## Usage Notes

- Must be used within a `<bx:grid>` component
- The `name` attribute should match a field in the grid's query data

## Related Components

- [Grid](Grid.md) - Parent grid component
- [GridRow](GridRow.md) - Grid row component

# Component: `GridRow`

Defines individual rows within a Grid component when not using query data. This component allows you to manually define row data and customize row appearance with styling and selection capabilities.

## Syntax

```html
<bx:gridrow 
    data="struct"
    bgcolor="string"
    textColor="string"
    selected="boolean"
    id="string"
    class="string"
    style="string">
</bx:gridrow>
```

## Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `data` | struct | No | `{}` | Struct containing row data with column names as keys |
| `bgcolor` | string | No | `""` | Background color for the row (CSS color value) |
| `textColor` | string | No | `""` | Text color for the row (CSS color value) |
| `selected` | boolean | No | `false` | Whether this row is initially selected |
| `id` | string | No | auto-generated | HTML element ID for the row |
| `class` | string | No | `""` | Additional CSS classes for the row |
| `style` | string | No | `""` | Additional inline CSS styles for the row |

## Usage Notes

- Must be used within a `<bx:grid>` component
- Useful for defining static data rows when not using query data
- Supports both struct data and delimited string formats
- Row data is mapped to columns defined by GridColumn components
- Automatically generates unique IDs if not provided

## Examples

### Basic Row Definition

```html
<bx:grid name="employeeGrid">
    <bx:gridcolumn name="id" header="Employee ID" />
    <bx:gridcolumn name="name" header="Full Name" />
    <bx:gridcolumn name="department" header="Department" />
    
    <bx:gridrow data="#{ id: 1, name: 'John Doe', department: 'Engineering' }#" />
    <bx:gridrow data="#{ id: 2, name: 'Jane Smith', department: 'Marketing' }#" />
    <bx:gridrow data="#{ id: 3, name: 'Bob Johnson', department: 'Sales' }#" />
</bx:grid>
```

### Styled Rows

```html
<bx:grid name="statusGrid">
    <bx:gridcolumn name="task" header="Task" />
    <bx:gridcolumn name="status" header="Status" />
    <bx:gridcolumn name="priority" header="Priority" />
    
    <!-- Normal priority row -->
    <bx:gridrow 
        data="#{ task: 'Update documentation', status: 'In Progress', priority: 'Normal' }#" />
    
    <!-- High priority row with red background -->
    <bx:gridrow 
        data="#{ task: 'Fix critical bug', status: 'Pending', priority: 'High' }#"
        bgcolor="##ffebee"
        textColor="##d32f2f" />
    
    <!-- Completed task with green background -->
    <bx:gridrow 
        data="#{ task: 'Deploy to production', status: 'Complete', priority: 'High' }#"
        bgcolor="##e8f5e8"
        textColor="##2e7d32"
        class="completed-task" />
</bx:grid>
```

### Pre-selected Rows

```html
<bx:grid name="selectionGrid" selectmode="multi">
    <bx:gridcolumn name="item" header="Item" />
    <bx:gridcolumn name="quantity" header="Quantity" />
    
    <bx:gridrow 
        data="#{ item: 'Widget A', quantity: 5 }#" 
        selected="true" />
    <bx:gridrow 
        data="#{ item: 'Widget B', quantity: 3 }#" />
    <bx:gridrow 
        data="#{ item: 'Widget C', quantity: 8 }#" 
        selected="true" />
</bx:grid>
```

### Using Delimited String Data

```html
<bx:grid name="csvGrid">
    <bx:gridcolumn name="product" header="Product" />
    <bx:gridcolumn name="price" header="Price" />
    <bx:gridcolumn name="stock" header="Stock" />
    
    <!-- Data can be provided as comma-delimited string -->
    <bx:gridrow data="Laptop,999.99,25" />
    <bx:gridrow data="Mouse,29.99,100" />
    <bx:gridrow data="Keyboard,79.99,50" />
</bx:grid>
```

### Custom Styling and IDs

```html
<bx:grid name="customGrid">
    <bx:gridcolumn name="code" header="Code" />
    <bx:gridcolumn name="description" header="Description" />
    
    <bx:gridrow 
        id="row_001"
        data="#{ code: 'A001', description: 'Primary Item' }#"
        class="primary-row highlight"
        style="border-left: 4px solid ##007bff; font-weight: bold;" />
        
    <bx:gridrow 
        id="row_002"
        data="#{ code: 'B001', description: 'Secondary Item' }#"
        class="secondary-row"
        style="font-style: italic;" />
</bx:grid>
```

## Generated HTML

The GridRow component generates HTML table rows with the following structure:

```html
<tr id="gridrow_abc123" class="bx-grid-row" data-selected="false">
    <td class="bx-grid-select-cell">
        <input type="radio" name="myGrid_select" value="gridrow_abc123" />
    </td>
    <td class="bx-grid-cell" data-column="id">1</td>
    <td class="bx-grid-cell" data-column="name">John Doe</td>
    <td class="bx-grid-cell" data-column="department">Engineering</td>
</tr>
```

## CSS Classes

- `.bx-grid-row` - Applied to all grid rows
- `.bx-grid-row-selected` - Added when `selected="true"`
- `.bx-grid-cell` - Applied to individual cells
- `.bx-grid-select-cell` - Applied to selection cells (when grid supports selection)

## Related Components

- [Grid](Grid.md) - Parent grid component
- [GridColumn](GridColumn.md) - Defines columns for the grid
- [GridUpdate](GridUpdate.md) - Handles grid data updates

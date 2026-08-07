# Component: `GridUpdate`

Handles AJAX-based updates for Grid components, enabling real-time synchronization with databases or web services. This component tracks changes to grid data and provides automatic update functionality without full page refreshes.

## Syntax

```html
<bx:gridupdate 
    grid="string"
    dataSource="string"
    tableName="string"
    tableOwner="string"
    tableQualifier="string"
    keyOnly="boolean"
    username="string"
    password="string"
    url="string"
    method="string"
    onSuccess="string"
    onError="string">
</bx:gridupdate>
```

## Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `grid` | string | **Yes** | - | Name of the grid component to update |
| `dataSource` | string | No* | `""` | Data source name for database updates |
| `tableName` | string | No* | `""` | Database table name to update |
| `tableOwner` | string | No | `""` | Database table owner/schema |
| `tableQualifier` | string | No | `""` | Database table qualifier |
| `keyOnly` | boolean | No | `false` | Only update key fields |
| `username` | string | No | `""` | Database username |
| `password` | string | No | `""` | Database password |
| `url` | string | No* | `""` | URL endpoint for HTTP-based updates |
| `method` | string | No | `"POST"` | HTTP method for URL updates: `POST`, `PUT` |
| `onSuccess` | string | No | `""` | JavaScript function to call on successful update |
| `onError` | string | No | `""` | JavaScript function to call on update error |

**Note:** Either `dataSource` + `tableName` OR `url` is required to specify the update destination.

## Usage Notes

- Automatically tracks grid changes (cell edits, row deletions, new rows)
- Supports both database and HTTP endpoint updates
- Generates JavaScript handlers for grid interaction
- Provides event-driven update notifications
- Maintains change tracking until successful update

## Examples

### Database Updates

```html
<bx:grid name="employeeGrid" query="#getEmployees()#">
    <bx:gridcolumn name="id" header="ID" />
    <bx:gridcolumn name="firstName" header="First Name" editable="true" />
    <bx:gridcolumn name="lastName" header="Last Name" editable="true" />
    <bx:gridcolumn name="department" header="Department" editable="true" />
</bx:grid>

<bx:gridupdate 
    grid="employeeGrid"
    dataSource="employeeDB"
    tableName="employees"
    onSuccess="handleUpdateSuccess"
    onError="handleUpdateError" />

<script>
function handleUpdateSuccess(message) {
    alert('Employee data updated successfully!');
}

function handleUpdateError(error) {
    alert('Update failed: ' + error);
}

// Manual update trigger
function saveChanges() {
    updateGrid_employeeGrid();
}
</script>

<button onclick="saveChanges()">Save Changes</button>
```

### HTTP Endpoint Updates

```html
<bx:grid name="productGrid" query="#getProducts()#">
    <bx:gridcolumn name="id" header="Product ID" />
    <bx:gridcolumn name="name" header="Product Name" editable="true" />
    <bx:gridcolumn name="price" header="Price" editable="true" />
    <bx:gridcolumn name="category" header="Category" editable="true" />
</bx:grid>

<bx:gridupdate 
    grid="productGrid"
    url="/api/products/batch-update"
    method="PUT"
    onSuccess="showNotification"
    onError="showError" />

<script>
function showNotification(result) {
    document.getElementById('status').innerHTML = 
        '<div class="alert alert-success">Products updated successfully!</div>';
}

function showError(error) {
    document.getElementById('status').innerHTML = 
        '<div class="alert alert-danger">Update failed: ' + error + '</div>';
}
</script>

<div id="status"></div>
<button onclick="updateGrid_productGrid()">Update Products</button>
```

### Database Updates with Authentication

```html
<bx:grid name="secureGrid" query="#getSecureData()#">
    <bx:gridcolumn name="id" header="ID" />
    <bx:gridcolumn name="confidential" header="Confidential Data" editable="true" />
    <bx:gridcolumn name="lastModified" header="Last Modified" />
</bx:grid>

<bx:gridupdate 
    grid="secureGrid"
    dataSource="secureDB"
    tableName="confidential_data"
    tableOwner="security"
    username="#session.dbUser#"
    password="#session.dbPassword#"
    keyOnly="true" />
```

### Custom Update Endpoint with Error Handling

```html
<bx:grid name="inventoryGrid">
    <bx:gridcolumn name="sku" header="SKU" />
    <bx:gridcolumn name="quantity" header="Quantity" editable="true" />
    <bx:gridcolumn name="location" header="Location" editable="true" />
</bx:grid>

<bx:gridupdate 
    grid="inventoryGrid"
    url="/inventory/update"
    method="PATCH"
    onSuccess="inventoryUpdateSuccess"
    onError="inventoryUpdateError" />

<script>
function inventoryUpdateSuccess(result) {
    // Show detailed success information
    console.log('Updated:', result.updatedRows);
    console.log('Added:', result.insertedRows);
    console.log('Deleted:', result.deletedRows);
    
    // Refresh related displays
    refreshInventoryReport();
    updateStockLevels();
}

function inventoryUpdateError(error) {
    // Log error for debugging
    console.error('Inventory update failed:', error);
    
    // Show user-friendly message
    showDialog('Update Failed', 
        'Unable to update inventory. Please try again or contact support.');
    
    // Optionally revert changes
    revertGridChanges('inventoryGrid');
}

// Auto-save functionality
setInterval(function() {
    if (hasGridChanges('inventoryGrid')) {
        updateGrid_inventoryGrid();
    }
}, 30000); // Auto-save every 30 seconds
</script>
```

## Update Data Format

The GridUpdate component sends update data in the following JSON format:

```json
{
    "grid": "myGrid",
    "modified": {
        "row_1": {
            "firstName": "John",
            "lastName": "Smith"
        },
        "row_2": {
            "department": "Engineering"
        }
    },
    "deleted": ["row_5", "row_8"],
    "added": [
        {
            "firstName": "New",
            "lastName": "Employee",
            "department": "Sales"
        }
    ],
    "timestamp": "2023-10-23T14:30:00.000Z"
}
```

## Server-Side Response Format

For HTTP endpoints, the expected response format is:

```json
{
    "success": true,
    "message": "Update completed successfully",
    "updatedRows": 2,
    "deletedRows": 2,
    "insertedRows": 1
}
```

Error responses should include:

```json
{
    "success": false,
    "message": "Update failed: Invalid data format",
    "error": "Detailed error information"
}
```

## Event Handling

The component fires custom events that can be listened to:

```javascript
// Listen for successful updates
document.querySelector('#myGrid').addEventListener('gridUpdateSuccess', function(e) {
    console.log('Update successful:', e.detail);
});

// Listen for update errors
document.querySelector('#myGrid').addEventListener('gridUpdateError', function(e) {
    console.log('Update error:', e.detail.error);
});

// Listen for individual cell changes
document.querySelector('#myGrid').addEventListener('gridCellEdit', function(e) {
    console.log('Cell changed:', e.detail.column, e.detail.value);
});
```

## JavaScript API

The component creates a global update function that can be called programmatically:

```javascript
// Trigger update for specific grid
updateGrid_myGridName();

// Check if grid has unsaved changes
if (hasGridChanges('myGridName')) {
    updateGrid_myGridName();
}

// Access change tracking (if exposed)
var changes = getGridChanges('myGridName');
console.log('Modified rows:', changes.modified);
console.log('Deleted rows:', changes.deleted);
console.log('New rows:', changes.added);
```

## Security Considerations

- Database credentials should be handled securely
- Use HTTPS endpoints for sensitive data
- Validate all incoming update data on the server
- Implement proper authentication and authorization
- Consider rate limiting for update endpoints

## Related Components

- [Grid](Grid.md) - Parent grid component that this updates
- [GridColumn](GridColumn.md) - Defines editable columns
- [GridRow](GridRow.md) - Individual row data that can be modified

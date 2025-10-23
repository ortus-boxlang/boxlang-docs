# Component: `Div`

Generates a dynamic HTML div element that can be updated asynchronously via AJAX.

## Syntax

```boxlang
<bx:div 
    bind="string"
    bindOnLoad="boolean"
    id="string"
    onBindError="string"
    tagName="string"
    class="string"
    style="string">
    <!-- Optional body content -->
</bx:div>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `bind` | `string` | No | Bind expression that provides content for the div via AJAX | `""` |
| `bindOnLoad` | `boolean` | No | Whether to execute bind expression when tag first loads | `true` |
| `id` | `string` | No | HTML ID attribute of the generated div tag | Auto-generated |
| `onBindError` | `string` | No | JavaScript function to handle bind expression errors | `""` |
| `tagName` | `string` | No | HTML tag name to generate | `"div"` |
| `class` | `string` | No | Additional CSS classes | `""` |
| `style` | `string` | No | Additional CSS styles | `""` |

## Examples

### Basic div with static content

```boxlang
<bx:div id="myDiv" class="content-area">
    <p>This is static content</p>
</bx:div>
```

### AJAX-enabled div with bind expression

```boxlang
<bx:div id="dynamicDiv" bind="cfc:myComponent.getData()" bindOnLoad="true" />
```

### Custom tag name

```boxlang
<bx:div tagName="section" class="main-section">
    <h2>Section Content</h2>
</bx:div>
```

### With error handling

```boxlang
<bx:div bind="url:data.bxm" onBindError="handleError" />

<script>
function handleError(error) {
    console.log("AJAX error:", error);
}
</script>
```

## Usage Notes

- When using the `bind` attribute, the component cannot have body content
- Valid `tagName` values: div, span, p, section, article, aside, header, footer, main, nav
- If `bindOnLoad` is true, the div will show a loading indicator until AJAX content loads
- The component automatically adds CSS classes for styling and JavaScript functionality

## Related Components

- [AjaxImport](AjaxImport.md) - Import required AJAX files
- [Layout](Layout.md) - Layout containers
- [Grid](Grid.md) - Data grids

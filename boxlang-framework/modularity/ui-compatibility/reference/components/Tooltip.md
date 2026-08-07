# Component: `Tooltip`

Provides interactive tooltips that appear on hover over HTML elements.

## Syntax

```boxlang
<bx:tooltip 
    tooltip="string"
    autoDismissDelay="number"
    hideDelay="number"
    preventOverlap="boolean"
    showDelay="number"
    sourceForTooltip="string"
    style="string"
    id="string"
    class="string">
    <!-- Body content that triggers the tooltip -->
</bx:tooltip>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `tooltip` | `string` | No* | Text displayed in the tooltip; can include HTML | `""` |
| `autoDismissDelay` | `number` | No | Time in milliseconds after which tooltip auto-disappears | `0` |
| `hideDelay` | `number` | No | Delay time before tooltip hides after mouse moves away | `300` |
| `preventOverlap` | `boolean` | No | Prevent tooltip from overlapping the component | `false` |
| `showDelay` | `number` | No | Delay before tooltip appears after hovering | `500` |
| `sourceForTooltip` | `string` | No* | URL for dynamic content to display in tooltip | `""` |
| `style` | `string` | No | CSS styles for custom tooltip appearance | `""` |
| `id` | `string` | No | HTML element ID | Auto-generated |
| `class` | `string` | No | Additional CSS classes | `""` |

**Note:** Either `tooltip` or `sourceForTooltip` is required.

## Examples

### Basic tooltip with text

```boxlang
<bx:tooltip tooltip="This is a helpful tooltip" showDelay="500">
    Hover over me!
</bx:tooltip>
```

### Tooltip with dynamic content

```boxlang
<bx:tooltip sourceForTooltip="tooltip-content.bxm" hideDelay="200">
    <button>More Info</button>
</bx:tooltip>
```

### Styled tooltip

```boxlang
<bx:tooltip 
    tooltip="<b>Important:</b> This action cannot be undone"
    autoDismissDelay="5000"
    preventOverlap="true"
    style="background-color: #fff3cd; color: #856404; border: 1px solid #ffc107;">
    <span class="warning-icon">⚠️</span>
</bx:tooltip>
```

## Usage Notes

- The tooltip is triggered by hovering over the body content of the component
- Tooltip content wraps around the element it should trigger on
- Supports both static text and dynamic content via `sourceForTooltip`
- Requires BoxLang AJAX JavaScript files (use `<bx:ajaximport>`)

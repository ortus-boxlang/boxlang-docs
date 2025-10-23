# Component: `Tooltip`

Adds tooltip functionality to elements.

## Syntax

```boxlang
<bx:tooltip 
    for="string"
    text="string"
    delay="numeric"
    position="string">
</bx:tooltip>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `for` | `string` | Yes | ID of element to attach tooltip to | |
| `text` | `string` | Yes | Tooltip text content | |
| `delay` | `numeric` | No | Show delay in milliseconds | `500` |
| `position` | `string` | No | Tooltip position (top, bottom, left, right) | `"top"` |

## Examples

```boxlang
<input type="text" id="username" name="username" />
<bx:tooltip for="username" text="Enter your username" position="right" />
```

## Usage Notes

- Requires an existing element with the specified ID
- Tooltip appears on hover and disappears on mouse leave

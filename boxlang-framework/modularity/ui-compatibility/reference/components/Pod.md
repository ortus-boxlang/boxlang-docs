# Component: `Pod`

Generates a pod (content container with title bar).

## Syntax

```boxlang
<bx:pod 
    title="string"
    height="string"
    width="string"
    style="string"
    class="string">
    <!-- Content -->
</bx:pod>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | `string` | No | Pod title displayed in header | |
| `height` | `string` | No | CSS height value | |
| `width` | `string` | No | CSS width value | |
| `style` | `string` | No | Additional CSS styles | |
| `class` | `string` | No | Additional CSS classes | |

## Examples

```boxlang
<bx:pod title="User Information" width="300px">
    <p>User profile content goes here</p>
</bx:pod>
```

## Usage Notes

- Creates a bordered container with optional title bar
- Useful for organizing content into discrete sections

# Component: `Pod`

Generates a pod (content container with title bar).

## Syntax

```boxlang
<bx:pod 
    title="string"
    name="string"
    height="string"
    width="string"
    bodyStyle="string"
    headerStyle="string"
    overflow="string"
    source="string"
    onBindError="string"
    id="string"
    class="string"
    style="string">
    <!-- Content -->
</bx:pod>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | `string` | No | Text to display in the pod's title bar | `""` |
| `name` | `string` | No | The name assigned to the pod control | `""` |
| `height` | `string` | No | Height of the control in pixels | `""` |
| `width` | `string` | No | Width of the control in pixels | `""` |
| `bodyStyle` | `string` | No | CSS style specification for the pod body | `""` |
| `headerStyle` | `string` | No | CSS style specification for the pod header | `""` |
| `overflow` | `string` | No | How to display child content that overflows: `auto`, `hidden`, `scroll`, `visible` | `auto` |
| `source` | `string` | No | URL that returns the content of the pod | `""` |
| `onBindError` | `string` | No | JavaScript function to execute if evaluating bind expression results in error | `""` |
| `id` | `string` | No | HTML element ID | Auto-generated |
| `class` | `string` | No | Additional CSS classes | `""` |
| `style` | `string` | No | Additional CSS styles | `""` |

## Examples

```boxlang
<bx:pod title="User Information" width="300px">
    <p>User profile content goes here</p>
</bx:pod>
```

## Usage Notes

- Creates a bordered container with optional title bar
- Useful for organizing content into discrete sections

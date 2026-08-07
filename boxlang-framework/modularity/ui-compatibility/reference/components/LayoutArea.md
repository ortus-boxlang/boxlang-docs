# Component: `LayoutArea`

Defines areas within a layout container component.

## Syntax

```boxlang
<bx:layoutarea 
    title="string"
    align="string"
    collapsible="boolean"
    initcollapsed="boolean"
    source="string"
    position="string"
    size="string"
    splitter="boolean"
    minsize="string"
    maxsize="string"
    id="string">
    <!-- Content -->
</bx:layoutarea>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | `string` | No | Area title (used for tabs/accordion headers) | `""` |
| `align` | `string` | No | Content alignment within the area | `""` |
| `collapsible` | `boolean` | No | Whether area can be collapsed (accordion) | `false` |
| `initcollapsed` | `boolean` | No | Start in collapsed state | `false` |
| `source` | `string` | No | URL to load content from | `""` |
| `position` | `string` | No | Position for border layout: `bottom`, `center`, `left`, `right`, `top` | `""` |
| `size` | `string` | No | CSS size for border layout regions | `""` |
| `splitter` | `boolean` | No | Show splitter for border layout | `false` |
| `minsize` | `string` | No | Minimum size constraint | `""` |
| `maxsize` | `string` | No | Maximum size constraint | `""` |
| `id` | `string` | No | HTML element ID | Auto-generated |

## Usage Notes

- Must be used within a `<bx:layout>` component
- Different attributes are relevant for different layout types

## Related Components

- [Layout](Layout.md) - Parent layout component

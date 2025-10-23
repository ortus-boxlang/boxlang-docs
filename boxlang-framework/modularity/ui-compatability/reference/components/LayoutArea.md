# Component: `LayoutArea`

Defines areas within a layout container component.

## Syntax

```boxlang
<bx:layoutarea 
    title="string"
    position="string"
    selected="boolean"
    collapsed="boolean"
    collapsible="boolean"
    height="string"
    width="string"
    flex="numeric">
    <!-- Content -->
</bx:layoutarea>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `title` | `string` | No | Area title (for tabs/accordion) | |
| `position` | `string` | No | Position for border layouts (north, south, east, west, center) | |
| `selected` | `boolean` | No | Initially selected (for tabs) | `false` |
| `collapsed` | `boolean` | No | Initially collapsed (for accordion) | `false` |
| `collapsible` | `boolean` | No | Allow collapse/expand | `true` |
| `height` | `string` | No | CSS height value | |
| `width` | `string` | No | CSS width value | |
| `flex` | `numeric` | No | Flex grow factor (for hbox/vbox) | `1` |

## Usage Notes

- Must be used within a `<bx:layout>` component
- Different attributes are relevant for different layout types

## Related Components

- [Layout](Layout.md) - Parent layout component

# Component: `Layout`

Generates layout containers supporting various layout types including tab, accordion, border, hbox, and vbox.

## Syntax

```boxlang
<bx:layout 
    type="string"
    align="string"
    fillHeight="boolean"
    fitToWindow="boolean"
    height="string"
    width="string"
    style="string"
    id="string"
    class="string"
    name="string">
    <!-- layoutarea children -->
</bx:layout>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `type` | `string` | **Yes** | Layout type: tab, accordion, border, hbox, vbox | |
| `align` | `string` | No | Content alignment: left, center, right, justify | |
| `fillHeight` | `boolean` | No | Fill available height | `false` |
| `fitToWindow` | `boolean` | No | Fill entire window viewport | `false` |
| `height` | `string` | No | CSS height value | |
| `width` | `string` | No | CSS width value | |
| `style` | `string` | No | Additional CSS styles | |
| `id` | `string` | No | HTML element ID | Auto-generated |
| `class` | `string` | No | Additional CSS classes | |
| `name` | `string` | No | Component name identifier | |

## Examples

### Tab Layout

```boxlang
<bx:layout type="tab" height="400px">
    <bx:layoutarea title="Tab 1" selected="true">
        <p>Content for the first tab</p>
    </bx:layoutarea>
    <bx:layoutarea title="Tab 2">
        <p>Content for the second tab</p>
    </bx:layoutarea>
</bx:layout>
```

### Accordion Layout

```boxlang
<bx:layout type="accordion" width="300px">
    <bx:layoutarea title="Section 1" collapsible="true">
        <p>Collapsible section content</p>
    </bx:layoutarea>
    <bx:layoutarea title="Section 2" collapsed="false">
        <p>Another section of content</p>
    </bx:layoutarea>
</bx:layout>
```

### Border Layout

```boxlang
<bx:layout type="border" fitToWindow="true">
    <bx:layoutarea position="north" height="60px">
        Header content
    </bx:layoutarea>
    <bx:layoutarea position="center">
        Main content area
    </bx:layoutarea>
    <bx:layoutarea position="south" height="30px">
        Footer content
    </bx:layoutarea>
</bx:layout>
```

### Horizontal Box Layout

```boxlang
<bx:layout type="hbox" align="center">
    <bx:layoutarea flex="1">
        <p>Left panel</p>
    </bx:layoutarea>
    <bx:layoutarea flex="2">
        <p>Center panel (wider)</p>
    </bx:layoutarea>
    <bx:layoutarea flex="1">
        <p>Right panel</p>
    </bx:layoutarea>
</bx:layout>
```

## Layout Types

- **tab**: Tabbed interface with clickable tab headers
- **accordion**: Collapsible sections that expand/collapse
- **border**: Five-region layout (north, south, east, west, center)
- **hbox**: Horizontal box layout with flexible widths
- **vbox**: Vertical box layout with flexible heights

## Usage Notes

- Must contain `<bx:layoutarea>` child components
- Each layout type has specific requirements for layoutarea attributes
- Requires BoxLang AJAX JavaScript files for interactive functionality
- The `type` attribute is required and determines the layout behavior

## Related Components

- [LayoutArea](LayoutArea.md) - Define areas within layouts
- [AjaxImport](AjaxImport.md) - Import required AJAX files

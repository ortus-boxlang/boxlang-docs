---
description: Creates an in-page pop-up window backed by the native HTML dialog element.
icon: browser
---

# Component: `Window`

Creates an in-page pop-up window backed by a native `<dialog>` element. The component generates the required HTML/JS bootstrap and delegates all interactive behaviour to the `cfwindow.js` ES module.

## Syntax

```boxlang
<bx:window 
    name="string"
    title="string"
    source="string"
    bodyStyle="string"
    headerStyle="string"
    width="number"
    height="number"
    minWidth="number"
    minHeight="number"
    x="number"
    y="number"
    center="boolean"
    initShow="boolean"
    modal="boolean"
    closable="boolean"
    draggable="boolean"
    resizable="boolean"
    destroyOnClose="boolean"
    refreshOnShow="boolean"
    onBindError="string"
    id="string">
    <!-- Body content -->
</bx:window>
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | **Yes** | Unique name of the window on the page | |
| `title` | `string` | No | Text displayed in the window title bar (supports HTML) | `""` |
| `source` | `string` | No | URL whose response becomes the window body (overrides body content) | `""` |
| `bodyStyle` | `string` | No | CSS style specification for the window body | `""` |
| `headerStyle` | `string` | No | CSS style specification for the window header | `""` |
| `width` | `number` | No | Width of the window in pixels | `500` |
| `height` | `number` | No | Height of the window in pixels | `300` |
| `minWidth` | `number` | No | Minimum width users can resize the window to | `0` |
| `minHeight` | `number` | No | Minimum height users can resize the window to | `0` |
| `x` | `number` | No | Horizontal pixel coordinate of the window upper-left corner | `""` |
| `y` | `number` | No | Vertical pixel coordinate of the window upper-left corner | `""` |
| `center` | `boolean` | No | Center the window over the browser viewport | `false` |
| `initShow` | `boolean` | No | Show the window when the page loads | `false` |
| `modal` | `boolean` | No | Prevent interaction with the page while window is open | `false` |
| `closable` | `boolean` | No | Show a close button on the title bar | `true` |
| `draggable` | `boolean` | No | Allow the user to drag the window | `true` |
| `resizable` | `boolean` | No | Allow the user to resize the window | `true` |
| `destroyOnClose` | `boolean` | No | Remove the window from the DOM when closed | `false` |
| `refreshOnShow` | `boolean` | No | Re-fetch the source URL each time the window is shown | `false` |
| `onBindError` | `string` | No | JavaScript function name called when a bind expression errors | `""` |
| `id` | `string` | No | HTML id for the root dialog element | Auto-generated |

## Examples

### Basic window

```boxlang
<bx:window name="myWindow" title="Hello World" width="400" height="300" initShow="true">
    <p>Body content here</p>
</bx:window>
```

### Modal window with external source

```boxlang
<bx:window 
    name="detailsWindow" 
    title="User Details" 
    source="user-details.bxm"
    width="600" 
    height="400"
    modal="true"
    center="true">
</bx:window>
```

### Configurable window

```boxlang
<bx:window 
    name="settingsWindow" 
    title="<b>Settings</b>" 
    width="500"
    height="350"
    minWidth="300"
    minHeight="200"
    closable="true"
    draggable="true"
    resizable="true"
    center="true"
    bodyStyle="padding: 1rem;">
    <h3>Application Settings</h3>
    <p>Configure your preferences below.</p>
</bx:window>
```

## Usage Notes

- Backed by the native HTML `<dialog>` element for accessibility
- The `source` attribute overrides any body content when provided
- Use `refreshOnShow="true"` to re-fetch source content each time the window opens
- The window can be controlled via JavaScript using the `ColdFusion.Window` API
- Requires BoxLang AJAX JavaScript files (use `<bx:ajaximport>`)

## Related Components

- [AjaxImport](AjaxImport.md) - Import required AJAX files
- [Pod](Pod.md) - Simpler container with optional title bar

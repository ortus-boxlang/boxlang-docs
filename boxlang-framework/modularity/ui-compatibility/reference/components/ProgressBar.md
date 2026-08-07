---
description: Creates an animated progress bar driven by a timer or bind expression.
icon: chart-bar
---

# Component: `ProgressBar`

Generates an animated progress bar that can be driven by a timer (`duration`) or by a bind expression (CFC / JavaScript function) returning `{ status, message }`.

## Syntax

```boxlang
<bx:progressbar 
    name="string"
    bind="string"
    duration="numeric"
    interval="numeric"
    width="numeric"
    height="numeric"
    autoDisplay="boolean"
    onComplete="string"
    onError="string"
    style="string"
    class="string"
    id="string" />
```

## Attributes

| Attribute | Type | Required | Description | Default |
|-----------|------|----------|-------------|---------|
| `name` | `string` | **Yes** | The control identifier used by `ColdFusion.ProgressBar.*` | |
| `bind` | `string` | No* | Bind expression (`cfc:component.method()`) that returns `{ status: 0-1, message: "" }` | `""` |
| `duration` | `numeric` | No* | Total duration in milliseconds for automatic progress | `""` |
| `interval` | `numeric` | No | Polling/update interval in milliseconds | `1000` |
| `width` | `numeric` | No | Width in pixels | `400` |
| `height` | `numeric` | No | Height in pixels | `""` |
| `autoDisplay` | `boolean` | No | Whether to display the bar immediately | `true` |
| `onComplete` | `string` | No | JavaScript function name to call on completion | `""` |
| `onError` | `string` | No | JavaScript function name to call on error (bind mode only) | `""` |
| `style` | `string` | No | Style spec: `bgcolor`, `textcolor`, `progresscolor` (hex without `#`) | `""` |
| `class` | `string` | No | Additional CSS classes | `""` |
| `id` | `string` | No | HTML element ID (defaults to `name`) | |

**Note:** Either `duration` (timer-based) or `bind` (poll-based) is required. They are mutually exclusive.

## Examples

### Timer-based progress bar

```boxlang
<bx:progressbar name="uploadBar" duration="5000" onComplete="handleUploadDone" />
```

### Bind-based progress bar

```boxlang
<bx:progressbar name="processBar" bind="cfc:status.getProgress()" interval="2000" onComplete="handleDone" onError="handleError" />
```

### Styled progress bar

```boxlang
<bx:progressbar 
    name="styledBar" 
    duration="3000" 
    width="600"
    height="30"
    style="bgcolor:#eee,textcolor:#333,progresscolor:#4caf50" />
```

## Usage Notes

- Integrates with the `ColdFusion.ProgressBar` JavaScript API (`start`, `stop`, `show`, `hide`) for runtime control
- In bind mode, the bound method must return a struct with `status` (0-1) and `message` keys
- The `style` attribute uses comma-delimited key:value pairs without `#` prefixes for hex colors
- Requires BoxLang AJAX JavaScript files (use `<bx:ajaximport>`)

## Related Components

- [AjaxImport](AjaxImport.md) - Import required AJAX files

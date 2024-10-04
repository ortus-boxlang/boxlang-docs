[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Abort`

Tests for a parameter's existence, tests its data type, and, if a default value is not assigned, optionally provides one.

## Component Signature

```
<bx:Abort showerror=[string]
type=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `showerror` | `string` | `false` | Whether to show an error |  |
| `type` | `string` | `false` | The type of the abort (request or page) | `request` |

## Examples

```
<bx:Abort showerror=[string]
type=[string] />
```

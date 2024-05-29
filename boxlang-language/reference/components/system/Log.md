[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Log`

Logs information to the specified log file

## Component Signature

```
<bx:Log text=[string]
file=[string]
log=[string]
type=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `text` | `string` | `false` | The text to log |  |
| `file` | `string` | `false` | An optional explicit file to log to |  |
| `log` | `string` | `false` | The log category to write to | `Application` |
| `type` | `string` | `false` | The log level of the entry. One of "Information", "Warning", "Error", "Debug", "Trace" | `Information` |

## Examples

```
<bx:Log text=[string]
file=[string]
log=[string]
type=[string] />
```

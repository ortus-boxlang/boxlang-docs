[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Param`

Tests for a parameter's existence, tests its data type, and, if a default value is not assigned, optionally provides one.

## Component Signature

```
<bx:Param name=[string]
type=[string]
default=[any]
max=[numeric]
min=[numeric]
pattern=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The name of the parameter |  |
| `type` | `string` | `false` | The data type of the parameter |  |
| `default` | `any` | `false` | The default value of the parameter |  |
| `max` | `numeric` | `false` | The maximum value of the parameter |  |
| `min` | `numeric` | `false` | The minimum value of the parameter |  |
| `pattern` | `string` | `false` | The pattern of the parameter |  |

## Examples

```
<bx:Param name=[string]
type=[string]
default=[any]
max=[numeric]
min=[numeric]
pattern=[string] />
```

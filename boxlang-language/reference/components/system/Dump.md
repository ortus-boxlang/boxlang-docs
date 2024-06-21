[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Dump`

Outputs the contents of a variable of any type for debugging purposes.

## Component Signature

```
<bx:Dump var=[any]
label=[string]
top=[numeric]
expand=[boolean]
abort=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `var` | `any` | `false` | The variable to dump |  |
| `label` | `string` | `false` | A label to display before the dump |  |
| `top` | `numeric` | `false` | The number of levels to display | `0` |
| `expand` | `boolean` | `false` | Whether to expand the dump | `true` |
| `abort` | `boolean` | `false` |  | `false` |

## Examples

```
<bx:Dump var=[any]
label=[string]
top=[numeric]
expand=[boolean]
abort=[boolean] />
```

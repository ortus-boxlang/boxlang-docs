[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `ProcParam`

Provide a paramater to a stored procudure.

## Component Signature

```
<bx:ProcParam type=[string]
value=[any]
sqltype=[string]
maxLength=[integer]
scale=[integer]
null=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The type of stored procedure paramter. One of in | out | inout | `in` |
| `value` | `any` | `false` | The value to pass |  |
| `sqltype` | `string` | `false` | The sql type the value | `string` |
| `maxLength` | `integer` | `false` |  |  |
| `scale` | `integer` | `false` |  |  |
| `null` | `boolean` | `false` | If the value should be counted as null |  |

## Examples

```
<bx:ProcParam type=[string]
value=[any]
sqltype=[string]
maxLength=[integer]
scale=[integer]
null=[boolean] />
```

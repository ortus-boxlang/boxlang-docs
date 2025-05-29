
# Component: `ProcResult`

Register a result set variable for a stored procedure.

## Component Signature

```
<bx:ProcResult name=[string]
resultSet=[integer]
maxRows=[integer] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The variable name to place the result set in. |  |
| `resultSet` | `integer` | `false` | The index of the resultset to access. Required if there is more than one ProcResult component. |  |
| `maxRows` | `integer` | `false` | The maximum number of rows to fetch per resultset. | `-1` |

## Examples



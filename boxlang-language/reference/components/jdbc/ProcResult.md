[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `ProcResult`

Register a result set variable for a stored procedure.

## Component Signature

```
<bx:ProcResult name=[string]
resultSet=[numeric]
maxRows=[numeric] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `name` | `string` | `true` | The variable name to place the result set in. |  |
| `resultSet` | `numeric` | `false` | The index of the resultset to access. Required if there is more than one ProcResult component. |  |
| `maxRows` | `numeric` | `false` | The maximum number of rows to fetch per resultset. | `-1` |

## Examples

```
<bx:ProcResult name=[string]
resultSet=[numeric]
maxRows=[numeric] />
```

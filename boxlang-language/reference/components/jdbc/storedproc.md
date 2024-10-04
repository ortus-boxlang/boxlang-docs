[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `StoredProc`

Execute a stored procedure.

## Component Signature

```
<bx:StoredProc procedure=[string]
datasource=[string]
username=[string]
password=[string]
blockfactor=[integer]
debug=[boolean]
returnCode=[boolean]
result=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `procedure` | `string` | `true` | The name of the procedure to execute. |  |
| `datasource` | `string` | `false` | The name of the datasource where the stored procedure is registered. |  |
| `username` | `string` | `false` |  |  |
| `password` | `string` | `false` |  |  |
| `blockfactor` | `integer` | `false` |  |  |
| `debug` | `boolean` | `false` |  | `false` |
| `returnCode` | `boolean` | `false` |  | `false` |
| `result` | `string` | `false` |  |  |

## Examples

```
<bx:StoredProc procedure=[string]
datasource=[string]
username=[string]
password=[string]
blockfactor=[integer]
debug=[boolean]
returnCode=[boolean]
result=[string] />
```

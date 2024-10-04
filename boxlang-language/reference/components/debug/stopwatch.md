[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Stopwatch`

Used to time a block of code and assigns the result to a variable

## Component Signature

```
<bx:Stopwatch label=[string]
unit=[string]
variable=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `label` | `string` | `false` | The label to use for the output. |  |
| `unit` | `string` | `false` | The unit of time to use for the output. One of `nano`, `micro`, `milli`, or `second`. | `milli` |
| `variable` | `string` | `false` | The name of the variable to store the result in. |  |

## Examples

```
<bx:Stopwatch label=[string]
unit=[string]
variable=[string] />
```

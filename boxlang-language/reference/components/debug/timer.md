[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Timer`

Times a block of code and outputs the result in a specified format.

## Component Signature

```
<bx:Timer type=[string]
label=[string]
unit=[string]
variable=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `false` | The type of output to generate. One of `debug`, `comment`, `inline`, or `outline`. |  |
| `label` | `string` | `false` | The label to use for the output. |  |
| `unit` | `string` | `false` | The unit of time to use for the output. One of `nano`, `micro`, `milli`, or `second`. | `milli` |
| `variable` | `string` | `false` | The name of the variable to store the result in. |  |

## Examples

```
<bx:Timer type=[string]
label=[string]
unit=[string]
variable=[string] />
```

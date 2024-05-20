[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Execute`

Component variation of Execute function

## Component Signature
```
<bx:Execute variable=[string]
name=[string]
arguments=[any]
timeout=[long]
terminateOnTimeout=[boolean]
directory=[string]
outputFile=[string]
errorFile=[string]
errorVariable=[string] />
```
### Attributes

| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `variable` | `string` | `true` | The variable name to produce |  |
| `name` | `string` | `true` | The process name or binary path ( e.g. bash or /bin/sh ) |  |
| `arguments` | `any` | `false` | The process arguments ( e.g. for `java --version` this would be `--version` ) |  |
| `timeout` | `long` | `false` | The timeout to wait for the command, in seconds ( default unlimited ) |  |
| `terminateOnTimeout` | `boolean` | `false` | Whether to terminate the process/command if a timeout is reached | `false` |
| `directory` | `string` | `false` | A working directory to execute the command from |  |
| `outputFile` | `string` | `false` |  |  |
| `errorFile` | `string` | `false` | An optional file path to write errors to |  |
| `errorVariable` | `string` | `false` | Optional variable to produce for error output |  |

## Examples

```
<bx:Execute variable=[string]
name=[string]
arguments=[any]
timeout=[long]
terminateOnTimeout=[boolean]
directory=[string]
outputFile=[string]
errorFile=[string]
errorVariable=[string] />
```

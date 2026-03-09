
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
errorVariable=[string]
exitCode=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `variable` | `string` | `false` | The variable name to produce |  |
| `name` | `string` | `true` | The process name or binary path ( e.g. bash or /bin/sh ) |  |
| `arguments` | `any` | `false` | The process arguments ( e.g. for `java --version` this would be `--version` ) |  |
| `timeout` | `long` | `false` | The timeout to wait for the command, in seconds ( default unlimited ) |  |
| `terminateOnTimeout` | `boolean` | `false` | Whether to terminate the process/command if a timeout is reached | `false` |
| `directory` | `string` | `false` | A working directory to execute the command from |  |
| `outputFile` | `string` | `false` |  |  |
| `errorFile` | `string` | `false` | An optional file path to write errors to |  |
| `errorVariable` | `string` | `false` | Optional variable to produce for error output |  |
| `exitCode` | `string` | `false` | An optional variable to set the exit code into |  |

## Examples

### Script syntax

If you want to execute a script (.sh,.cmd,.bat), use bash (linux) or cmd.exe (windows) as the command and the script as argument for the shell interpreter.


```java
bx:execute name="bash" arguments="/opt/jq.sh #cmdArgs#" variable="standardOut" errorVariable="errorOut" timeout="10";

```


### Script syntax with terminateOnTimeout

Printing a PDF using lpr


```java
bx:execute name="lpr" arguments="-P 'My Print Job Name' 'C:/Users/devguy/Documents/server/mynewfile.pdf'" timeout="5" terminateOnTimeout="true";

```



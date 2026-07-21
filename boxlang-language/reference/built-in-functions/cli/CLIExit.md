[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CLIExit`

Exits the CLI with the specified exit code.

## Method Signature

```
CLIExit(exitCode=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `exitCode` | `numeric` | `false` | By convention, a nonzero status code, indicates abnormal termination. Deault code is 0. | `0` |

## Examples

### Exit the CLI/REPL session

```java
// This will exit the current CLI session
// cliExit();
writeOutput( "would exit" );

```

Result: would exit

## Related

  * [CLIClear](./CLIClear.md)
  * [CLIGetArgs](./CLIGetArgs.md)
  * [CLIRead](./CLIRead.md)

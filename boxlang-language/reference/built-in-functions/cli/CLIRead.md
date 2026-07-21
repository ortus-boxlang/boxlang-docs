[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CLIRead`

Reads a line of text from the CLI.

You can optionally provide a prompt string to display before reading the input.

## Method Signature

```
CLIRead(prompt=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `prompt` | `string` | `false` | An optional prompt string to display before reading input. |  |

## Examples

### Read input from the CLI

```java
// In a CLI context, reads a line from stdin
// value = cliRead( "Enter name: " );
writeOutput( "reads stdin" );

```

Result: reads stdin

## Related

  * [CLIClear](./CLIClear.md)
  * [CLIExit](./CLIExit.md)
  * [CLIGetArgs](./CLIGetArgs.md)

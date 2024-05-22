[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `File`

Manages interactions with server files.

## Component Signature
```
<bx:File action=[string]
file=[string]
mode=[string]
output=[string]
addnewline=[boolean]
attributes=[string]
charset=[string]
source=[string]
destination=[string]
variable=[string]
filefield=[string]
nameconflict=[string]
accept=[string]
result=[string]
fixnewline=[boolean]
cachedwithin=[numeric] />
```
### Attributes

| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `true` | The action to take. One of: append, copy, delete, move, read, readbinary, rename, upload, uploadall, write |  |
| `file` | `string` | `false` | The file to act on |  |
| `mode` | `string` | `false` | The mode to open the file in |  |
| `output` | `string` | `false` | The output of the action |  |
| `addnewline` | `boolean` | `false` | Add a newline to the end of the file | `false` |
| `attributes` | `string` | `false` | Attributes to set on the file |  |
| `charset` | `string` | `false` | The character set to use | `utf-8` |
| `source` | `string` | `false` | The source file |  |
| `destination` | `string` | `false` | The destination file |  |
| `variable` | `string` | `false` | The variable to store the result in |  |
| `filefield` | `string` | `false` | The file field to use |  |
| `nameconflict` | `string` | `false` | What to do if there is a name conflict |  |
| `accept` | `string` | `false` | The accept header |  |
| `result` | `string` | `false` | The result of the action |  |
| `fixnewline` | `boolean` | `false` | Fix newlines | `false` |
| `cachedwithin` | `numeric` | `false` | The time to cache the file within |  |

## Examples

```
<bx:File action=[string]
file=[string]
mode=[string]
output=[string]
addnewline=[boolean]
attributes=[string]
charset=[string]
source=[string]
destination=[string]
variable=[string]
filefield=[string]
nameconflict=[string]
accept=[string]
result=[string]
fixnewline=[boolean]
cachedwithin=[numeric] />
```

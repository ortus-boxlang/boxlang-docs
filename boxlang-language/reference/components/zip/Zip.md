[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Zip`

The BoxLang Zip component is a powerful component that allows you to interact with zip/gzip files.

## Component Signature

```
<bx:Zip action=[string]
file=[string]
destination=[string]
filter=[any]
entryPath=[any]
charset=[string]
result=[string]
overwrite=[boolean]
prefix=[string]
recurse=[boolean]
flatList=[boolean]
source=[string]
variable=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `false` | The action to take: delete, list, read, readBinary, unzip, zip | `zip` |
| `file` | `string` | `false` | Absolute filepath to the zip/gzip file to be manipulated. Actions: list, read, readBinary, unzip, zip |  |
| `destination` | `string` | `false` | Absolute destination directory where the zip/gzip file will be to. If it doesn't exist it will be created for you. Actions: unzip |  |
| `filter` | `any` | `false` | This can be a regular expression (*.txt) or a BoxLang Closure/Lambda ((path) => path.endsWith(".txt")) that will be used to filter the files. Actions: delete, list, unzip, zip |  |
| `entryPath` | `any` | `false` | Zip entry path or an array of entry paths on which the action is performed. Actions: delete, list, read, readBinary, unzip |  |
| `charset` | `string` | `false` | Valid Java Charset to use when reading the contents of a file inside a zip file. Default is the machine's default charset. Actions: read, readBinary |  |
| `result` | `string` | `false` |  | `bxzip` |
| `overwrite` | `boolean` | `false` | Whether to overwrite the destination file(s) if it already exists when zipping/unzipping. Default is false. Actions: zip, unzip | `false` |
| `prefix` | `string` | `false` | The prefix to add to the files when zipping files, this is the directory name to store files in. Not used by default. Actions: zip |  |
| `recurse` | `boolean` | `false` | Whether to recurse into subdirectories when listing/zipping/unzipping. Default is true. Actions: list, zip, unzip | `true` |
| `flatList` | `boolean` | `false` | If false, the list action will return an array of structs with all kinds of information about the entries. If true, it will return a flat list of strings with the path of the entries. Default is false. Actions: list | `false` |
| `source` | `string` | `false` | The absolute path to the source directory to be zipped. Actions: zip |  |
| `variable` | `string` | `false` | The name of the variable to store the read content in |  |

## Examples

```
<bx:Zip action=[string]
file=[string]
destination=[string]
filter=[any]
entryPath=[any]
charset=[string]
result=[string]
overwrite=[boolean]
prefix=[string]
recurse=[boolean]
flatList=[boolean]
source=[string]
variable=[string] />
```

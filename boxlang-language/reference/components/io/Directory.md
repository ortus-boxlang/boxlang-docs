[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the Component class)
# Component: `Directory`

Allows you to list, create, delete or rename a directory in the server file system.

## Component Signature

```
<bx:Directory action=[string]
directory=[string]
name=[string]
filter=[string]
mode=[string]
sort=[string]
newDirectory=[string]
destination=[string]
recurse=[boolean]
type=[string]
listInfo=[string]
createPath=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `action` | `string` | `true` | The action to perform (list, create, delete, rename) |  |
| `directory` | `string` | `true` | The directory to perform the action on |  |
| `name` | `string` | `false` | Name for output record set. |  |
| `filter` | `string` | `false` | Filter applied to returned names. For example: *.bx You can use a pipe ("|") delimiter to specify multiple filters. For example:<br>                   *.bxm|*.bx Filter pattern matches are case-sensitive on UNIX and Linux. Can also be a UDF/Closure which accepts the<br>                   file/directory name and returns a Boolean value to indicate whether that item should be included in the result or not. | `*` |
| `mode` | `string` | `false` | Applies only to UNIX and Linux. Permissions. Octal values of Unix chmod command. Assigned to owner, group, and other, respectively.<br>                 For example: 777 |  |
| `sort` | `string` | `false` | Query column(s) by which to sort directory listing. Delimited list of columns from query output. |  |
| `newDirectory` | `string` | `false` | The new directory name for the rename action. |  |
| `destination` | `string` | `false` |  |  |
| `recurse` | `boolean` | `false` | Recurse into subdirectories. | `false` |
| `type` | `string` | `true` | Type of directory listing to return (dir, file, all). | `all` |
| `listInfo` | `string` | `true` | Information to return in the listing (name, all). | `query` |
| `createPath` | `boolean` | `false` | Whether to create all paths necessary to create the directory path. | `true` |

## Examples

```
<bx:Directory action=[string]
directory=[string]
name=[string]
filter=[string]
mode=[string]
sort=[string]
newDirectory=[string]
destination=[string]
recurse=[boolean]
type=[string]
listInfo=[string]
createPath=[boolean] />
```

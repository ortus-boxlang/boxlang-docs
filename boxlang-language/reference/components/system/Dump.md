
# Component: `Dump`

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

## Component Signature

```
<bx:Dump var=[any]
label=[string]
top=[numeric]
expand=[boolean]
abort=[any]
output=[string]
format=[string]
showUDFs=[boolean] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `var` | `any` | `false` | The variable to dump, can be any type |  |
| `label` | `string` | `false` | A custom label to display above the dump (Only in HTML output) |  |
| `top` | `numeric` | `false` | The number of levels to display when dumping collections. Great to avoid dumping the entire world! Default is inifinity. (Only in HTML output) |  |
| `expand` | `boolean` | `false` | Whether to expand the dump. Be default, we try to expand as much as possible. (Only in HTML output) |  |
| `abort` | `any` | `false` | Whether to do a hard abort the request after dumping. Default is false | `false` |
| `output` | `string` | `false` | The output format which can be "buffer", "console", or "{absolute file path}". The default is "buffer". |  |
| `format` | `string` | `false` | The format of the output to a <strong>filename</strong>. Can be "html" or "text". The default is according to the output location. |  |
| `showUDFs` | `boolean` | `false` | Show UDFs or not. Default is true. (Only in HTML output) | `true` |

## Examples

### Dump a variable to the browser

Outputs structured debug information for any variable type.

```java
<bx:dump var="#myStruct#">

```

### Dump with a label

```java
<bx:dump var="#users#" label="User List">

```

### Limit dump depth

Prevents dumping deeply nested structures by limiting the number of levels.

```java
<bx:dump var="#complexObject#" top="3">

```

### Dump to console

```java
<bx:dump var="#debugInfo#" output="console" format="text">

```

### Dump to a file

```java
<bx:dump var="#errorData#" output="/tmp/debug.txt" format="text">

```

### Dump and abort

```java
<bx:dump var="#exception#" abort="true">

```

### Hide UDFs in dump output

```java
<bx:dump var="#myComponent#" showUDFs="false">

```

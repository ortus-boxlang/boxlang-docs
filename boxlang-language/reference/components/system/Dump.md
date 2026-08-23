
# Component: `Dump`

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

## Component Signature

```
<bx:Dump var=[any]
label=[string]
depth=[numeric]
maxRows=[numeric]
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
| `depth` | `numeric` | `false` | The recursion depth to display when dumping nested collections. 1-based: -1 (default) is unlimited, 0 shows nothing, 1 shows the top level with no recursion, 2 recurses once, etc. (Only in HTML output) |  |
| `maxRows` | `numeric` | `false` | The maximum number of keys/rows/items to display per level of a collection, array, or query. 1-based: -1 (default) is unlimited, 0 shows nothing, 1 shows a single row, etc. (Only in HTML output) |  |
| `top` | `numeric` | `false` | Deprecated: use maxRows instead. When maxRows is not also passed, top's value is used as maxRows. Kept for backwards compatibility with existing BoxLang code. (Only in HTML output) |  |
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

### Limit recursion depth

Prevents dumping deeply nested structures by limiting how many levels are recursed into.
`depth` is 1-based: `-1` (the default) is unlimited, `0` shows nothing, `1` shows the top
level with no recursion, `2` recurses once, etc.

```java
<bx:dump var="#complexObject#" depth="3">

```

### Limit the number of rows/items shown

Limits how many keys, array elements, or query rows are shown per level, independently of
recursion depth. Same 1-based semantics as `depth`.

```java
<bx:dump var="#bigArray#" maxRows="10">

```

### Deprecated: top

`top` is deprecated in favor of `maxRows` and `depth` above. For backwards compatibility it is
still accepted and, when `maxRows` is not also passed, its value is used as `maxRows`. A
deprecation warning is logged when it's used.

```java
<bx:dump var="#bigArray#" top="10">

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

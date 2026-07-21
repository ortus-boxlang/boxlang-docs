
# Component: `ZipParam`

Adds a param to a zip component.

## Component Signature

```
<bx:ZipParam charset=[string]
content=[any]
entryPath=[string]
filter=[any]
filterDelimiters=[string]
prefix=[string]
source=[string]
recurse=[boolean]
password=[string]
encryptionAlgorithm=[string] />
```

### Attributes


| Atrribute | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `charset` | `string` | `false` | The charset to use for the content of the Zip entry - used only when the content attribute is provided with text content |  |
| `content` | `any` | `false` | The content of the Zip entry - can be binary or text content |  |
| `entryPath` | `string` | `false` | The path of the Zip entry - required if content is specified |  |
| `filter` | `any` | `false` | The filter to apply to the content of the Zip entry - applies for source directories |  |
| `filterDelimiters` | `string` | `false` | The delimiters to use for the filter - not implemented in the current release |  |
| `prefix` | `string` | `false` | The prefix to use for the created zip entries |  |
| `source` | `string` | `false` | The source of the Zip entry - either a file or a directory |  |
| `recurse` | `boolean` | `false` | Whether to recurse into subdirectories when zipping | `true` |
| `password` | `string` | `false` | The password to use for the Zip entry - not implemented in the current release |  |
| `encryptionAlgorithm` | `string` | `false` | The encryption algorithm to use for the Zip entry - not implemented in the current release |  |

## Examples

### Add a file to a ZIP archive

Defines a source file or directory to include in a ZIP operation.

```java
<bx:zip action="zip" file="/tmp/archive.zip" source="/tmp/myfile.txt">

```

### Add a directory recursively

```java
<bx:zip action="zip" file="/tmp/archive.zip" source="/tmp/myfolder" recurse="true">

```

### Add content directly as a ZIP entry

Creates a ZIP entry from in-memory content without a source file.

```java
<bx:zip action="zip" file="/tmp/archive.zip">
    <bx:zipParam content="Hello World" entryPath="greeting.txt">
</bx:zip>

```

### Add content with a specific charset

```java
<bx:zip action="zip" file="/tmp/archive.zip">
    <bx:zipParam content="Bonjour le monde" entryPath="french.txt" charset="UTF-8">
</bx:zip>

```

### Filter files when zipping a directory

```java
<bx:zip action="zip" file="/tmp/archive.zip" source="/tmp/logs">
    <bx:zipParam filter="*.log">
</bx:zip>

```

### Add a prefix to ZIP entry paths

```java
<bx:zip action="zip" file="/tmp/archive.zip" source="/tmp/data">
    <bx:zipParam prefix="backup/2024/">
</bx:zip>

```

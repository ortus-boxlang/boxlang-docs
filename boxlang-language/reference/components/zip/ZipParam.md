
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
| `filterDelimiters` | `string` | `false` | The delimiters to use for the filter - not implemented in the current release | `ortus.boxlang.runtime.validation.NotImplemented@47b6f580` |
| `prefix` | `string` | `false` | The prefix to use for the created zip entries |  |
| `source` | `string` | `false` | The source of the Zip entry - either a file or a directory |  |
| `recurse` | `boolean` | `false` | Whether to recurse into subdirectories when zipping | `true` |
| `password` | `string` | `false` | The password to use for the Zip entry - not implemented in the current release | `ortus.boxlang.runtime.validation.NotImplemented@47b6f580` |
| `encryptionAlgorithm` | `string` | `false` | The encryption algorithm to use for the Zip entry - not implemented in the current release | `ortus.boxlang.runtime.validation.NotImplemented@47b6f580` |

## Examples



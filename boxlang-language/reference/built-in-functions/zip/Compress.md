[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Compress`

Compress the source file or folder to the destination file or folder using
 the specified format:

<p>,
 - zip
 - gzip (It will all files separately to the destination folder)
 ,<p>,
 The ,{@code includeBaseFolder}, argument is used to include the base folder as the root
 of the compressed file. The default is ,{@code true},.
 ,<p>,
 The ,{@code overwrite}, argument is used to overwrite the destination
 file if it already exists, else it will throw an exception. The default is ,{@code false},.

## Method Signature

```
Compress(format=[string], source=[string], destination=[string], includeBaseFolder=[boolean], overwrite=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `true` | The format to use for the compression: zip or gzip. |  |
| `source` | `string` | `true` | The absolute path to the source file or folder to compress. |  |
| `destination` | `string` | `true` | The absolute path with a file name to save as the compressed file. Extension is optional. |  |
| `includeBaseFolder` | `boolean` | `false` | Whether to include the base folder as the root of the compressed file. Default is true. | `true` |
| `overwrite` | `boolean` | `false` | Whether to overwrite the destination file if it already exists. Default is false. | `false` |

## Examples



## Related

  * [Extract](./Extract.md)
  * [IsZipFile](./IsZipFile.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Compress`

Compress the source file or folder to the destination file or folder using
 the specified format:

<p>
 - zip
 - gzip (It will all files separately to the destination folder)
 <p>
 The {@code includeBaseFolder} argument is used to include the base folder as the root
 of the compressed file. The default is {@code true}.
 <p>
 The {@code overwrite} argument is used to overwrite the destination
 file if it already exists, else it will throw an exception. The default is {@code false}.
 <p>
 <h2>Compression Levels</h2>
 The {@code compressionLevel} argument is used to specify the compression level to use for the compression.
 The default is {@code 6}, which is a good balance between speed and compression ratio.
 The valid range is from {@code 0} (no compression) to {@code 9} (maximum compression).

## Method Signature

```
Compress(format=[string], source=[string], destination=[string], includeBaseFolder=[boolean], overwrite=[boolean], prefix=[string], filter=[any], recurse=[boolean], compressionLevel=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `true` | The format to use for the compression: zip or gzip. Default is zip. | `zip` |
| `source` | `string` | `true` | The absolute path to the source file or folder to compress. |  |
| `destination` | `string` | `true` | The absolute path with a file name to save as the compressed file. Extension is optional. |  |
| `includeBaseFolder` | `boolean` | `false` | Whether to include the base folder as the root of the compressed file. Default is true. | `true` |
| `overwrite` | `boolean` | `false` | Whether to overwrite the destination file if it already exists. Default is false. | `false` |
| `prefix` | `string` | `false` | The prefix directory to store the compressed files under. Default is empty. |  |
| `filter` | `any` | `false` | A regular expression to filter the files to compress or a function that receives the file name and returns a boolean. |  |
| `recurse` | `boolean` | `false` | Whether to compress the files recursively. Default is true. | `true` |
| `compressionLevel` | `integer` | `false` | The compression level to use for the compression. Default is 6, which is a good balance between speed and compression ratio. | `6` |

## Examples

### Compress a file

Compress the file "example.txt" to a zip-file.


```java
compress( "zip", "example.txt", "output.zip" );

```


### Compress a directory

Compress the "example-directory" to a zip-file.


```java
compress( "zip", "example-directory", "output.zip" );

```


### Additional Examples


## Related

  * [Extract](./Extract.md)
  * [IsZipFile](./IsZipFile.md)

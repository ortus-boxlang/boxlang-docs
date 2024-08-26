[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Extract`

Extract the source file or folder to the destination folder using the specified format:

<p>,
 - zip
 - gzip
 ,<p>,
 The ,{@code overwrite}, argument is used to overwrite the destination
 file if it already exists, else it will throw an exception. The default is ,{@code false},.
 ,<p>,
 The ,{@code recurse}, argument is used to extract the files recursively. The default is ,{@code true},.
 ,<p>,
 The ,{@code filter}, argument is used to filter the files to extract. It can be:
 ,<p>,
 - A string with a regular expression to match the file names. Example: ".*\\.txt"
 - A Function/Lambda that receives the file name and returns a boolean. Example: (name) => name.endsWith(".txt")
 ,<p>,
 The ,{@code entryPaths}, argument is used to extract only the files that match the given paths. It can be a string
 or an array of strings with the paths to extract. Example: "folder1/file1.txt" or ["folder1/file1.txt", "folder2/file2.txt"]

## Method Signature

```
Extract(format=[string], source=[string], destination=[string], overwrite=[boolean], recurse=[boolean], filter=[any], entryPaths=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `true` | The format to use for the compression: zip or gzip. |  |
| `source` | `string` | `true` | The absolute path to the source file or folder to compress. |  |
| `destination` | `string` | `true` | The absolute path with a file name to save as the compressed file. Extension is optional. |  |
| `overwrite` | `boolean` | `false` | Whether to overwrite the destination file if it already exists. Default is false. | `false` |
| `recurse` | `boolean` | `false` | Whether to extract the files recursively. Default is true. | `true` |
| `filter` | `any` | `false` | A regular expression or a Function/Lambda to filter the files to extract. |  |
| `entryPaths` | `any` | `false` | The paths to extract. It can be a string or an array of strings. |  |

## Examples



## Related

  * [Compress](./Compress.md)
  * [IsZipFile](./IsZipFile.md)

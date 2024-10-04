# Compress

Compress the source file or folder to the destination file or folder using the specified format:

, - zip - gzip (It will all files separately to the destination folder) ,

, The ,{@code includeBaseFolder}, argument is used to include the base folder as the root of the compressed file. The default is ,{@code true},. ,

, The ,{@code overwrite}, argument is used to overwrite the destination file if it already exists, else it will throw an exception. The default is ,{@code false},.

## Method Signature

```
Compress(format=[string], source=[string], destination=[string], includeBaseFolder=[boolean], overwrite=[boolean], prefix=[string], filter=[any], recurse=[boolean])
```

### Arguments

| Argument            | Type      | Required | Description                                                                                                           | Default |
| ------------------- | --------- | -------- | --------------------------------------------------------------------------------------------------------------------- | ------- |
| `format`            | `string`  | `true`   | The format to use for the compression: zip or gzip.                                                                   |         |
| `source`            | `string`  | `true`   | The absolute path to the source file or folder to compress.                                                           |         |
| `destination`       | `string`  | `true`   | The absolute path with a file name to save as the compressed file. Extension is optional.                             |         |
| `includeBaseFolder` | `boolean` | `false`  | Whether to include the base folder as the root of the compressed file. Default is true.                               | `true`  |
| `overwrite`         | `boolean` | `false`  | Whether to overwrite the destination file if it already exists. Default is false.                                     | `false` |
| `prefix`            | `string`  | `false`  | The prefix directory to store the compressed files under. Default is empty.                                           |         |
| `filter`            | `any`     | `false`  | A regular expression to filter the files to compress or a function that receives the file name and returns a boolean. |         |
| `recurse`           | `boolean` | `false`  | Whether to compress the files recursively. Default is true.                                                           | `true`  |

## Examples

## Related

* [Extract](extract.md)
* [IsZipFile](iszipfile.md)

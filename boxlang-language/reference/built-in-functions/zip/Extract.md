[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Extract`

Extract the source file or folder to the destination folder using the specified format:

The `destination` argument is the directory where extracted entries are written. Older code may use `target`; the transpiler maps `target` to `destination` for compatibility.

<p>
 - zip
 - gzip
 - bzip
 - bzip2
 - tar
 - tbz
 - tbz2
 - tgz
 - tar.gz
 <p>
 The {@code overwrite} argument is used to overwrite the destination
 file if it already exists, else it will throw an exception. The default is {@code false}.
 <p>
 The {@code recurse} argument is used to extract the files recursively. The default is {@code true}.
 <p>
 The {@code filter} argument is used to filter the files to extract. It can be:
 <p>
 - A string with a regular expression to match the file names. Example: ".*\\.txt"
 - A Function/Lambda that receives the file name and returns a boolean. Example: (name) => name.endsWith(".txt")
 <p>
 The {@code entryPaths} argument is used to extract only the files that match the given paths. It can be a string
 or an array of strings with the paths to extract. Example: "folder1/file1.txt" or ["folder1/file1.txt", "folder2/file2.txt"]

## Method Signature

```
Extract(format=[string], source=[string], destination=[string], overwrite=[boolean], recurse=[boolean], filter=[any], entryPaths=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `format` | `string` | `true` | The format to use for extraction: zip, gzip, bzip, bzip2, tar, tbz, tbz2, tgz, or tar.gz. |  |
| `source` | `string` | `true` | The absolute path to the archive file or folder to extract. |  |
| `destination` | `string` | `true` | The absolute path to the directory where extracted files are written. |  |
| `overwrite` | `boolean` | `false` | Whether to overwrite the destination file if it already exists. Default is false. | `false` |
| `recurse` | `boolean` | `false` | Whether to extract the files recursively. Default is true. | `true` |
| `filter` | `any` | `false` | A regular expression or a Function/Lambda to filter the files to extract. |  |
| `entryPaths` | `any` | `false` | The paths to extract. It can be a string or an array of strings. |  |

## Examples

### Extract a zip-file

Extract a zip-file and save the data in the "output-directory".


```java
extract(
  source = "test.zip",
  destination = "output-directory",
  format = "zip"
)

```


### Extract a multiple zip-files via a directory

Extract all zip-files, which are stored in the "multiple-directory" and save the data in the "output-directory".


```java
extract(
  source = "multiple-directory",
  destination = "output-directory",
  format = "zip"
)

```


### Additional Examples

Extract a tbz2 archive:

```java
extract(
  source = "/tmp/project.tbz2",
  destination = "/tmp/project-out",
  format = "tbz2"
)
```


```java
extract(
  source = "D:\\test.zip",
  destination = "D:\\zipresult",
  format = "zip"
)

```



## Related

  * [Compress](./Compress.md)
  * [IsZipFile](./IsZipFile.md)

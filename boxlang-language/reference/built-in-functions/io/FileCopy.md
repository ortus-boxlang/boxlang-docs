[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileCopy`

Copies a file from one location to another.

The destionation can be a file or a directory.
 If the destination is a directory, the source file name will be appended to the destination.

## Method Signature

```
FileCopy(source=[string], destination=[string], createPath=[boolean], overwrite=[boolean], accept=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `source` | `string` | `true` | The source file |  |
| `destination` | `string` | `true` | A destionation file or directory, if it's a directory, the suorce file name will be appended |  |
| `createPath` | `boolean` | `false` | [ true ] whether to create any nested paths required to the new file | `true` |
| `overwrite` | `boolean` | `false` | Whether to overwrite the destination file if it exists. Defaults to true. | `true` |
| `accept` | `string` | `false` | A comma separated list of file extensions to accept - which will override runtime security settings |  |

## Examples

### Copy file from here to there




```java
fileCopy( sourceFile, destinationFile );

```


### Additional Examples


```java
fileCopy( "path/to/my/file.md", "new/location/for/file.md" );

```



## Related

  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [DirectoryCopy](./DirectoryCopy.md)
  * [DirectoryCreate](./DirectoryCreate.md)
  * [DirectoryDelete](./DirectoryDelete.md)
  * [DirectoryExists](./DirectoryExists.md)
  * [DirectoryList](./DirectoryList.md)
  * [DirectoryMove](./DirectoryMove.md)
  * [DirectoryRename](./DirectoryRename.md)
  * [ExpandPath](./ExpandPath.md)
  * [FileAppend](./FileAppend.md)
  * [FileClose](./FileClose.md)
  * [FileDelete](./FileDelete.md)
  * [FileExists](./FileExists.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileInfo](./FileInfo.md)
  * [FileIsEOF](./FileIsEOF.md)
  * [FileMove](./FileMove.md)
  * [FileOpen](./FileOpen.md)
  * [FileRead](./FileRead.md)
  * [FileReadBinary](./FileReadBinary.md)
  * [FileReadLine](./FileReadLine.md)
  * [FileSeek](./FileSeek.md)
  * [FileSetAccessMode](./FileSetAccessMode.md)
  * [FileSetAttribute](./FileSetAttribute.md)
  * [FileSetLastModified](./FileSetLastModified.md)
  * [FileSkipBytes](./FileSkipBytes.md)
  * [FileWrite](./FileWrite.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)

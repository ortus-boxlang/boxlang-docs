[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileRead`

Reads the contents of a file and returns it as a string or binary object

## Method Signature

```
FileRead(filepath=[string], charsetOrBufferSize=[string], charset=[string], buffersize=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filepath` | `string` | `true` | The path to the file to read. |  |
| `charsetOrBufferSize` | `string` | `false` | Either the charset to use when reading the file, or the buffer size to use when reading the file. If providing a buffer size, the next argument can be the charset. |  |
| `charset` | `string` | `false` | The explicit charset to use when reading the file. |  |
| `buffersize` | `string` | `false` | The explicit buffer size to use when reading the file. |  |

## Examples

### Read a file into a binary object

Uses expandPath to grab a file in current directory.


```java
binaryContent = fileReadBinary( expandPath( "./file.pdf" ) );

```


### Additional Examples


```java
binaryContent = fileReadBinary( expandPath( "./image.jpg" ) );

```



## Related

  * [FileIsEOF](./FileIsEOF.md)
  * [FileExists](./FileExists.md)
  * [FileInfo](./FileInfo.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [DirectoryExists](./DirectoryExists.md)
  * [FileAppend](./FileAppend.md)
  * [FileReadBinary](./FileReadBinary.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [DirectoryCreate](./DirectoryCreate.md)
  * [DirectoryMove](./DirectoryMove.md)
  * [DirectoryRename](./DirectoryRename.md)
  * [DirectoryCopy](./DirectoryCopy.md)
  * [FileOpen](./FileOpen.md)
  * [FileCopy](./FileCopy.md)
  * [FileClose](./FileClose.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [FileReadLine](./FileReadLine.md)
  * [FileMove](./FileMove.md)
  * [FileSetAccessMode](./FileSetAccessMode.md)
  * [FileSeek](./FileSeek.md)
  * [FileSkipBytes](./FileSkipBytes.md)
  * [ExpandPath](./ExpandPath.md)
  * [FileSetLastModified](./FileSetLastModified.md)
  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [DirectoryDelete](./DirectoryDelete.md)
  * [FileSetAttribute](./FileSetAttribute.md)
  * [FileDelete](./FileDelete.md)
  * [DirectoryList](./DirectoryList.md)
  * [FileWrite](./FileWrite.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [getTempFile](./getTempFile.md)

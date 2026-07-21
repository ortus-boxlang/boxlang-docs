[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileReadBinary`

Reads the contents of a file and returns it as a string or binary object.

<p>
 When called with a <b>file path</b> (string, Path, or File), the entire file is read from disk.
 HTTP URLs are also supported as string paths.
 When called with an <b>open BoxFile object</b> (from {@code fileOpen()}), the remaining content
 is read from the current stream position to EOF. For text mode files, returns a String.
 For binary mode files, returns a byte[]. The caller is responsible for closing the file object afterward.

## Method Signature

```
FileReadBinary(filepath=[any], charsetOrBufferSize=[string], charset=[string], buffersize=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `filepath` | `any` | `true` | A file path (string, Path, File, or HTTP URL) to read entirely, or an open BoxFile object to read remaining content from. |  |
| `charsetOrBufferSize` | `string` | `false` | Either the charset to use when reading the file, or the buffer size. Only applies to path-based reads. |  |
| `charset` | `string` | `false` | The explicit charset to use when reading the file. Only applies to path-based reads. |  |
| `buffersize` | `string` | `false` | The explicit buffer size to use when reading the file. Only applies to path-based reads. |  |

## Examples



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
  * [FileCopy](./FileCopy.md)
  * [FileDelete](./FileDelete.md)
  * [FileExists](./FileExists.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileInfo](./FileInfo.md)
  * [FileIsEOF](./FileIsEOF.md)
  * [FileMove](./FileMove.md)
  * [FileOpen](./FileOpen.md)
  * [FileRead](./FileRead.md)
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
  * [PropertyFile](./PropertyFile.md)

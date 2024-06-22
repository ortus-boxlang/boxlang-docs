[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileWrite`

Writes the contents of a string or binary data to a file

## Method Signature

```
FileWrite(file=[string], data=[any], charset=[string], createPath=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `string` | `true` | The string path of the file - either root relative or absolute |  |
| `data` | `any` | `true` | The string or binary byte array of the file content |  |
| `charset` | `string` | `false` | The charset encoding ( ignored for binary data ) | `utf-8` |
| `createPath` | `boolean` | `false` |  | `false` |

## Examples



## Related

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
  * [FileReadBinary](./FileReadBinary.md)
  * [FileReadLine](./FileReadLine.md)
  * [FileSeek](./FileSeek.md)
  * [FileSetAccessMode](./FileSetAccessMode.md)
  * [FileSetAttribute](./FileSetAttribute.md)
  * [FileSetLastModified](./FileSetLastModified.md)
  * [FileSkipBytes](./FileSkipBytes.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryList`

List the contents of a directory.

## Method Signature
```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[string], sort=[string], type=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The path to the directory to list. |  |
| `recurse` | `boolean` | `true` | Whether to recurse into subdirectories. | `false` |
| `listInfo` | `string` | `false` | The type of information to return. Valid values are "path", "name", and "query". | `path` |
| `filter` | `string` | `false` | A filter to apply to the listing. |  |
| `sort` | `string` | `false` |  | `name` |
| `type` | `string` | `false` | The type of items to list. Valid values are "all", "file", and "dir". | `all` |

## Examples

```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[string], sort=[string], type=[string])
```

## Related
  * [CreateTempDirectory](CreateTempDirectory.md)
  * [CreateTempFile](CreateTempFile.md)
  * [DirectoryCopy](DirectoryCopy.md)
  * [DirectoryCreate](DirectoryCreate.md)
  * [DirectoryDelete](DirectoryDelete.md)
  * [DirectoryExists](DirectoryExists.md)
  * [DirectoryMove](DirectoryMove.md)
  * [DirectoryRename](DirectoryRename.md)
  * [ExpandPath](ExpandPath.md)
  * [FileAppend](FileAppend.md)
  * [FileClose](FileClose.md)
  * [FileCopy](FileCopy.md)
  * [FileDelete](FileDelete.md)
  * [FileExists](FileExists.md)
  * [FileGetMimeType](FileGetMimeType.md)
  * [FileInfo](FileInfo.md)
  * [FileIsEOF](FileIsEOF.md)
  * [FileMove](FileMove.md)
  * [FileOpen](FileOpen.md)
  * [FileRead](FileRead.md)
  * [FileReadBinary](FileReadBinary.md)
  * [FileReadLine](FileReadLine.md)
  * [FileSeek](FileSeek.md)
  * [FileSetAccessMode](FileSetAccessMode.md)
  * [FileSetAttribute](FileSetAttribute.md)
  * [FileSetLastModified](FileSetLastModified.md)
  * [FileSkipBytes](FileSkipBytes.md)
  * [FileWrite](FileWrite.md)
  * [FileWriteLine](FileWriteLine.md)
  * [GetCanonicalPath](GetCanonicalPath.md)
  * [GetDirectoryFromPath](GetDirectoryFromPath.md)
  * [GetFileInfo](GetFileInfo.md)
  * [getTempFile](getTempFile.md)

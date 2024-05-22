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
  * [CreateTempDirectory](boxlang-language/reference/built-in-functions/CreateTempDirectory.md)
  * [CreateTempFile](boxlang-language/reference/built-in-functions/CreateTempFile.md)
  * [DirectoryCopy](boxlang-language/reference/built-in-functions/DirectoryCopy.md)
  * [DirectoryCreate](boxlang-language/reference/built-in-functions/DirectoryCreate.md)
  * [DirectoryDelete](boxlang-language/reference/built-in-functions/DirectoryDelete.md)
  * [DirectoryExists](boxlang-language/reference/built-in-functions/DirectoryExists.md)
  * [DirectoryMove](boxlang-language/reference/built-in-functions/DirectoryMove.md)
  * [DirectoryRename](boxlang-language/reference/built-in-functions/DirectoryRename.md)
  * [ExpandPath](boxlang-language/reference/built-in-functions/ExpandPath.md)
  * [FileAppend](boxlang-language/reference/built-in-functions/FileAppend.md)
  * [FileClose](boxlang-language/reference/built-in-functions/FileClose.md)
  * [FileCopy](boxlang-language/reference/built-in-functions/FileCopy.md)
  * [FileDelete](boxlang-language/reference/built-in-functions/FileDelete.md)
  * [FileExists](boxlang-language/reference/built-in-functions/FileExists.md)
  * [FileGetMimeType](boxlang-language/reference/built-in-functions/FileGetMimeType.md)
  * [FileInfo](boxlang-language/reference/built-in-functions/FileInfo.md)
  * [FileIsEOF](boxlang-language/reference/built-in-functions/FileIsEOF.md)
  * [FileMove](boxlang-language/reference/built-in-functions/FileMove.md)
  * [FileOpen](boxlang-language/reference/built-in-functions/FileOpen.md)
  * [FileRead](boxlang-language/reference/built-in-functions/FileRead.md)
  * [FileReadBinary](boxlang-language/reference/built-in-functions/FileReadBinary.md)
  * [FileReadLine](boxlang-language/reference/built-in-functions/FileReadLine.md)
  * [FileSeek](boxlang-language/reference/built-in-functions/FileSeek.md)
  * [FileSetAccessMode](boxlang-language/reference/built-in-functions/FileSetAccessMode.md)
  * [FileSetAttribute](boxlang-language/reference/built-in-functions/FileSetAttribute.md)
  * [FileSetLastModified](boxlang-language/reference/built-in-functions/FileSetLastModified.md)
  * [FileSkipBytes](boxlang-language/reference/built-in-functions/FileSkipBytes.md)
  * [FileWrite](boxlang-language/reference/built-in-functions/FileWrite.md)
  * [FileWriteLine](boxlang-language/reference/built-in-functions/FileWriteLine.md)
  * [GetCanonicalPath](boxlang-language/reference/built-in-functions/GetCanonicalPath.md)
  * [GetDirectoryFromPath](boxlang-language/reference/built-in-functions/GetDirectoryFromPath.md)
  * [GetFileInfo](boxlang-language/reference/built-in-functions/GetFileInfo.md)
  * [getTempFile](boxlang-language/reference/built-in-functions/getTempFile.md)

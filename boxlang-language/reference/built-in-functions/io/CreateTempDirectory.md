[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateTempDirectory`

Creates a temporary directory in the specified directory with the specified prefix if passed.

## Method Signature
```
CreateTempDirectory(directory=[string], prefix=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `directory` | `string` | `false` | The directory in which to create the temp directory, we default to the system temp directory | `/var/folders/sh/yq09rnbj48764cvf2k4nhcxh0000gn/T/` |
| `prefix` | `string` | `false` | The prefix string to be used in generating the directory's name; may be empty |  |

## Examples

```
CreateTempDirectory(directory=[string], prefix=[string])
```

## Related
  * [CreateTempFile](boxlang-language/reference/built-in-functions/CreateTempFile.md)
  * [DirectoryCopy](boxlang-language/reference/built-in-functions/DirectoryCopy.md)
  * [DirectoryCreate](boxlang-language/reference/built-in-functions/DirectoryCreate.md)
  * [DirectoryDelete](boxlang-language/reference/built-in-functions/DirectoryDelete.md)
  * [DirectoryExists](boxlang-language/reference/built-in-functions/DirectoryExists.md)
  * [DirectoryList](boxlang-language/reference/built-in-functions/DirectoryList.md)
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

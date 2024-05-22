[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryCreate`

Creates a directory

## Method Signature
```
DirectoryCreate(path=[string], createPath=[boolean], ignoreExists=[boolean], mode=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The directory path to create |  |
| `createPath` | `boolean` | `false` | [true] Whether to create all paths necessary to create the directory path | `true` |
| `ignoreExists` | `boolean` | `false` | [false] Whether to ignore if a directory already exists | `false` |
| `mode` | `string` | `false` | When provided will attempt to set the posix permissions on the directory |  |

## Examples

```
DirectoryCreate(path=[string], createPath=[boolean], ignoreExists=[boolean], mode=[string])
```

## Related
  * [CreateTempDirectory](boxlang-language/reference/built-in-functions/CreateTempDirectory.md)
  * [CreateTempFile](boxlang-language/reference/built-in-functions/CreateTempFile.md)
  * [DirectoryCopy](boxlang-language/reference/built-in-functions/DirectoryCopy.md)
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

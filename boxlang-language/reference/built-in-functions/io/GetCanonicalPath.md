[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetCanonicalPath`

Returns the canonical path of a file, resolving all relative path elements and symlinks

## Method Signature

```
GetCanonicalPath(path=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The file or directory path string |  |

## Examples

### getCanonicalPath Example

 Returns the canonical path of the input path.

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSE8tcU7My8%2FLTE7MCUgsyQCLOCUWp4ak5hbkJJakggU1FYDQmgsAiaEUTg%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( getCanonicalPath( getBaseTemplatePath() ) );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLSixOjS9ILMlQsFVITy1xAnJDUnMLchJLUgOAohqa1lzJiXn5eZnJiTkQJc4wLlheIQluAFBpSmlugYYCQgNQSEFfX0E%2FIz83Vb88NalYvzipQj%2BnNDk11VQfaFZRam5%2BSapeclouFwDd4y8X" target="_blank">Run Example</a>

```java
base_path = getBaseTemplatePath();
canonical = getCanonicalPath( base_path );
dump( canonical );
 // /var/task

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
  * [FileWrite](./FileWrite.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)

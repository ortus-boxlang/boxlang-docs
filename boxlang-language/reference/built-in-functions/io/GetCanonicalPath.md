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

  * [FileIsEOF](./FileIsEOF.md)
  * [FileExists](./FileExists.md)
  * [FileInfo](./FileInfo.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [DirectoryExists](./DirectoryExists.md)
  * [FileAppend](./FileAppend.md)
  * [FileRead](./FileRead.md)
  * [FileReadBinary](./FileReadBinary.md)
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

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateTempFile`

Creates a temporary file in the specified directory with the specified prefix and suffix if passed.

## Method Signature

```
CreateTempFile(directory=[string], prefix=[string], suffix=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `directory` | `string` | `false` | The directory in which to create the temp file, we default to the system temp directory | `/var/folders/qr/xsqq4bd544x8qdm9s8ngwtdh0000gn/T/` |
| `prefix` | `string` | `false` | The prefix string to be used in generating the file's name; may be empty |  |
| `suffix` | `string` | `false` | The suffix string to be used in generating the file's name; may be empty, in which case ".tmp" is used |  |

## Examples

### Create temp file in temp dir

Returns path of file created

<a href="https://try.boxlang.io/?code=eJxLTy0JSc0tcMvMSdVQSIdwXDKLUpNL8osqNTR1FJRKUotLQNJKCprWXACZ5g%2FZ" target="_blank">Run Example</a>

```java
getTempFile( getTempDirectory(), "testFile" );

```

Result: /private/var/folders/k6/hm9skhxj2dd_901z2f2mkwt00000gn/T/testFile13427324567646329113.tmp

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FBwTy0JSc0tcMvMSdVQSIdwXDKLUpNL8osqNTR1FJRSUnPzlRQ0FTStuQDQaBBl" target="_blank">Run Example</a>

```java
dump( GetTempFile( getTempDirectory(), "demo" ) );

```



## Related

  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
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
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)
  * [PropertyFile](./PropertyFile.md)

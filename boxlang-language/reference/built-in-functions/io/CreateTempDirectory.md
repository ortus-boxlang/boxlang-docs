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
| `directory` | `string` | `false` | The directory in which to create the temp directory, we default to the system temp directory | `/var/folders/qr/xsqq4bd544x8qdm9s8ngwtdh0000gn/T/` |
| `prefix` | `string` | `false` | The prefix string to be used in generating the directory's name; may be empty |  |

## Examples

### Create a temporary directory

```java
dir = createTempDirectory();
writeOutput( directoryExists( dir ) );

```

Result: true

### With a prefix

```java
dir = createTempDirectory( "myapp-" );
writeOutput( dir.contains( "myapp-" ) );

```

Result: true

## Related

  * [ContractPath](./ContractPath.md)
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
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)
  * [PropertyFile](./PropertyFile.md)

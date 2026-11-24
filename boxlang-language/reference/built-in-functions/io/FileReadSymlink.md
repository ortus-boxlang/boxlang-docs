[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileReadSymlink`

Returns the target a symbolic link points to.

Throws an exception if the path is not a symbolic link.

## Method Signature

```
FileReadSymlink(path=[string], resolve=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The symbolic link to read |  |
| `resolve` | `boolean` | `false` | [false] When false, the target is returned exactly as stored in the link. When true, it is returned as a normalized absolute path. | `false` |

## Examples

### Read where a link points

Returns the target exactly as it is stored in the link. Throws an exception if the path is not a symbolic link.

```java
base = getTempDirectory() & "linkDemo";
directoryCreate( base & "/releases/v2" );
fileCreateSymlink( base & "/current", "releases/v2" );
writeOutput( fileReadSymlink( base & "/current" ) );

```

Result: releases/v2

### Resolve the target to an absolute path

With `resolve=true` a relative target is resolved against the folder that holds the link and the path is normalized.

```java
resolved = fileReadSymlink( path=base & "/current", resolve=true );
writeOutput( resolved == base & "/releases/v2" );

```

Result: true

## Related

  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [DirectoryCopy](./DirectoryCopy.md)
  * [DirectoryCreate](./DirectoryCreate.md)
  * [DirectoryExists](./DirectoryExists.md)
  * [DirectoryList](./DirectoryList.md)
  * [DirectoryMove](./DirectoryMove.md)
  * [DirectoryRename](./DirectoryRename.md)
  * [ExpandPath](./ExpandPath.md)
  * [FileAppend](./FileAppend.md)
  * [FileClose](./FileClose.md)
  * [FileCopy](./FileCopy.md)
  * [FileCreateSymlink](./FileCreateSymlink.md)
  * [FileDelete](./FileDelete.md)
  * [FileExists](./FileExists.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileInfo](./FileInfo.md)
  * [FileIsEOF](./FileIsEOF.md)
  * [FileIsSymlink](./FileIsSymlink.md)
  * [FileMove](./FileMove.md)
  * [FileOpen](./FileOpen.md)
  * [FileRead](./FileRead.md)
  * [FileReadBinary](./FileReadBinary.md)
  * [FileReadLine](./FileReadLine.md)
  * [FileReadSymlink](./FileReadSymlink.md)
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

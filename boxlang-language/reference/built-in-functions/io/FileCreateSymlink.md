[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileCreateSymlink`

Creates a symbolic link at the given path pointing to the given target.

Throws an exception if the link cannot be created, for example when the
 operating system does not allow the current user to create symbolic links.

## Method Signature

```
FileCreateSymlink(link=[string], target=[string], overwrite=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `link` | `string` | `true` | The path of the link to create. Missing parent directories are created. |  |
| `target` | `string` | `true` | The path the link points to. It is stored exactly as given, so a relative target is relative to the folder holding the link. |  |
| `overwrite` | `boolean` | `false` | [false] Whether to replace an existing file or link at the link path. Directories are never replaced. | `false` |

## Examples

### Point a link at a folder

Create `current` as a symbolic link to the `releases/v2` folder.

```java
base = getTempDirectory() & "linkDemo";
directoryCreate( base & "/releases/v2" );
fileCreateSymlink( base & "/current", base & "/releases/v2" );
writeOutput( fileIsSymlink( base & "/current" ) );

```

Result: true

### Use a relative target and replace an existing link

The target is stored exactly as given, so a relative target is relative to the folder that holds the link. Pass `overwrite=true` to replace an existing file or link. Folders are never replaced.

```java
fileCreateSymlink( link=base & "/current", target="releases/v2", overwrite=true );
writeOutput( fileReadSymlink( base & "/current" ) );

```

Result: releases/v2

### The call throws if the path already exists

```java
fileCreateSymlink( base & "/current", "releases/v1" );

```

Result: throws "The path [/tmp/linkDemo/current] already exists and the overwrite argument is set to false."

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

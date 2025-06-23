[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ExpandPath`

Creates an absolute, platform-appropriate path that is equivalent to the value of 'path', appended to the base path.

This function (despite its
 name) can accept an absolute or relative path in the 'path' attribute.

## Method Signature

```
ExpandPath(path=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | Relative or absolute directory reference or filename, to convert to an absolute path. Can include forward or backward slashes. |  |

## Examples

### Expand the current path



<a href="https://try.boxlang.io/?code=eJxLrShIzEsJSCzJ0FBQ0tNXUtC05gIAR2MFhQ%3D%3D" target="_blank">Run Example</a>

```java
expandPath( "./" );

```

Result: /Users/scottsteinbeck/Downloads/BL-1468/

### Expand the parent folder path



<a href="https://try.boxlang.io/?code=eJxLrShIzEsJSCzJ0FBQ0tPTV1LQtOYCAE1LBbM%3D" target="_blank">Run Example</a>

```java
expandPath( "../" );

```

Result: /Users/scottsteinbeck/Downloads/BL-1468/

### Expand the path to a subfolder



<a href="https://try.boxlang.io/?code=eJxLrShIzEsJSCzJ0FBQKgBS%2BiX5%2BsWlSWn5OSmpRUoKmtZcAOUFC9w%3D" target="_blank">Run Example</a>

```java
expandPath( "path/to/subfolder" );

```

Result: /Users/scottsteinbeck/Downloads/BL-1468/path/to/subfolder


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

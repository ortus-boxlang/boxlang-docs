[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryCopy`

Copies a directory from one location to another

## Method Signature

```
DirectoryCopy(source=[string], destination=[string], recurse=[boolean], filter=[any], createPath=[boolean], overwrite=[boolean], followLinks=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `source` | `string` | `true` | The source directory |  |
| `destination` | `string` | `true` | The destination directory |  |
| `recurse` | `boolean` | `false` | whether to recurse in to sub-directories and create paths | `false` |
| `filter` | `any` | `false` | A file or directory filter to pass | `*` |
| `createPath` | `boolean` | `false` | whether to create any nested paths required to the new directory | `true` |
| `overwrite` | `boolean` | `false` | whether to overwrite existing files at the destination | `false` |
| `followLinks` | `boolean` | `false` | [default:false] whether to follow symbolic links. When false, a link inside the source is copied as a link. When true, the<br>                       content the link points to is copied instead. | `false` |

## Examples

### Simple DirectoryCopy Example

Copy directory from one place to another.


```java
directoryCopy( expandPath( "./mySourceDirectory" ), expandPath( "../MyDestinationDirectory" ) );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLySxKTS7JL6pMzi%2Bo1FBQSoHxCxJLMpR00AUUNK25FPT1FfLzUhVQZBRK8hUS8%2FJLMlKLEBIKIBk9PT0uAG2KJCs%3D" target="_blank">Run Example</a>

```java
directorycopy( "directorypath", "directorypath" );
 // one directorypath to another directory path...

```

### Copy a folder that contains symbolic links

By default a symbolic link is copied as a link that points to the same place.

```java
shared = getTempDirectory() & "linkDemoShared";
build = getTempDirectory() & "linkDemoBuild";
dest = getTempDirectory() & "linkDemoCopy";
directoryCreate( shared );
fileWrite( shared & "/keep.txt", "keep" );
directoryCreate( build );
fileCreateSymlink( build & "/lib", shared );

directoryCopy( build, dest, true );
writeOutput( fileIsSymlink( dest & "/lib" ) );

```

Result: true

### Copy what the links point to

Pass `followLinks=true` to copy the content of the linked folders instead of the link.

```java
directoryDelete( dest, true );
directoryCopy( source=build, destination=dest, recurse=true, followLinks=true );
writeOutput( fileIsSymlink( dest & "/lib" ) & " " & fileExists( dest & "/lib/keep.txt" ) );

```

Result: false true

## Related

  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [CreateTempFile](./CreateTempFile.md)
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

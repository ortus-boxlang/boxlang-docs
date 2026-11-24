[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryDelete`

Deletes a directory

## Method Signature

```
DirectoryDelete(path=[string], recursive=[boolean], followLinks=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | the path of the directory to delete |  |
| `recursive` | `boolean` | `true` | [default:false] whether to recursively delete the directory.<br>                     If falls and the directory is not empty, with throw a runtime exception | `false` |
| `followLinks` | `boolean` | `false` | [default:false] whether to follow symbolic links found inside the directory when deleting recursively. When false, links are<br>                       removed as links and the folders they point to are never touched. When true, the contents of those folders are deleted too,<br>                       except for a link that leads back into the directory being deleted or to a folder above it, which is removed as a link.<br>                       A symbolic link given as the path only has the link removed, whatever the value of followLinks. | `false` |

## Examples

### Tag Syntax




```java
<bx:set delDirectory = "someDirPath" >
<bx:set recurse = true >
<bx:set directoryDelete( delDirectory, recurse ) >
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLySxKTS7JL6pMSc1JLUnVUFBygYkEJJZkKCloWnMBAP8NDKU%3D" target="_blank">Run Example</a>

```java
directorydelete( "DirectoryPath" );

```

### Delete a folder that contains symbolic links

A recursive delete never follows symbolic links. A link is removed as a link and the folder it points to is left alone.

```java
shared = getTempDirectory() & "linkDemoShared";
build = getTempDirectory() & "linkDemoBuild";
directoryCreate( shared );
fileWrite( shared & "/keep.txt", "keep" );
directoryCreate( build );
fileWrite( build & "/out.txt", "out" );
fileCreateSymlink( build & "/lib", shared );

directoryDelete( build, true );
writeOutput( directoryExists( build ) & " " & fileExists( shared & "/keep.txt" ) );

```

Result: false true

### Delete a symbolic link given as the path

Only the link is removed, with or without `recursive` and even when `followLinks` is true.

```java
fileCreateSymlink( build, shared );
directoryDelete( build, true );
writeOutput( fileIsSymlink( build ) & " " & fileExists( shared & "/keep.txt" ) );

```

Result: false true

### Follow symbolic links when deleting

Pass `followLinks=true` to delete the contents of the folders that links inside the directory point to as well. Use with care, the targets are emptied. A link that leads back into the folder being deleted, or to a folder above it, is removed as a link.

```java
directoryCreate( build );
fileCreateSymlink( build & "/lib", shared );

directoryDelete( build, true, true );
writeOutput( directoryExists( build ) & " " & fileExists( shared & "/keep.txt" ) );

```

Result: false false

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

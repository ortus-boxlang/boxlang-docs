[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryCopy`

Copies a directory from one location to another

## Method Signature

```
DirectoryCopy(source=[string], destination=[string], recurse=[boolean], filter=[any], createPath=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `source` | `string` | `true` | The source directory |  |
| `destination` | `string` | `true` | The destination directory |  |
| `recurse` | `boolean` | `false` | [ false ] whether to recurse in to sub-directories and create paths | `false` |
| `filter` | `any` | `false` | [ "*" ] a file or directory filter to pass | `*` |
| `createPath` | `boolean` | `false` | [ true ] whether to create any nested paths required to the new directory | `true` |

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

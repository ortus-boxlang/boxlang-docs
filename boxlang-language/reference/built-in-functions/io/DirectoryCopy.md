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
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [DirectoryCreate](./DirectoryCreate.md)
  * [DirectoryMove](./DirectoryMove.md)
  * [DirectoryRename](./DirectoryRename.md)
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

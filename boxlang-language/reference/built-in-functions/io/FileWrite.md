[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileWrite`

Writes the contents of a string or binary data to a file

## Method Signature

```
FileWrite(file=[string], data=[any], charset=[string], createPath=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `string` | `true` | The string path of the file - either root relative or absolute |  |
| `data` | `any` | `true` | The string or binary byte array of the file content |  |
| `charset` | `string` | `false` | The charset encoding ( ignored for binary data ) | `UTF-8` |
| `createPath` | `boolean` | `false` |  | `false` |

## Examples

### Write a Temporary File



<a href="https://try.boxlang.io/?code=eJxLy8xJDS%2FKLEnVUEhPLQlJzS1wA4rAOS6ZRanJJflFlRqaOgpKJVBpJQUQz7dSwSWxJBHIseYCAIc0Fvs%3D" target="_blank">Run Example</a>

```java
fileWrite( getTempFile( getTempDirectory(), "tempFile" ), "My Data" );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLy8xJLS%2FKLEnVUFBKA7ILEksylHQgbOf8vJLUvBKFknyFpFQFsColBU1rLgDn%2FxFz" target="_blank">Run Example</a>

```java
filewrite( "filepath", "fileContent to be write" );

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
  * [CreateTempFile](./CreateTempFile.md)
  * [getTempFile](./getTempFile.md)

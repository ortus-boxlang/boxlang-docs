[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileWrite`

Writes the contents of a string or binary data to a file.

<p>
 When called with a <b>file path</b> (string, Path, or File), the file is created/overwritten on disk.
 When called with an <b>open BoxFile object</b> (from {@code fileOpen()}), the data is written through
 the file's existing stream, respecting the current mode (write or append) and position.
 The caller is responsible for closing the file object afterward.

## Method Signature

```
FileWrite(file=[boxfile], data=[any], charset=[string], createPath=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `boxfile` | `true` | A file path (string, Path, File) to create/overwrite, or an open BoxFile object to write through its stream. |  |
| `data` | `any` | `true` | The string or binary byte array of the file content. |  |
| `charset` | `string` | `false` | The charset encoding (ignored for binary data). Only applies to path-based writes. | `UTF-8` |
| `createPath` | `boolean` | `false` | When true, ensures all directories to the file destination are created. Only applies to path-based writes. | `false` |

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
  * [FileWriteLine](./FileWriteLine.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)
  * [PropertyFile](./PropertyFile.md)

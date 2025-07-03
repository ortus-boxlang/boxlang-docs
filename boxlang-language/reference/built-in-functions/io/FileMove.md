# FileMove

Moves file from source to destination.

The destination can be a file or a directory. If the destination is a directory, the\
file will be moved to that directory with the same name as the source file.

## Method Signature

```
FileMove(source=[string], destination=[string], overwrite=[boolean], accept=[string])
```

### Arguments

| Argument      | Type      | Required | Description                                                                                         | Default |
| ------------- | --------- | -------- | --------------------------------------------------------------------------------------------------- | ------- |
| `source`      | `string`  | `true`   | The source file path.                                                                               |         |
| `destination` | `string`  | `true`   | The destination file path or directory path.                                                        |         |
| `overwrite`   | `boolean` | `true`   | Whether to overwrite the destination file if it exists. Defaults to true.                           | `true`  |
| `accept`      | `string`  | `false`  | A comma separated list of file extensions to accept - which will override runtime security settings |         |

## Examples

### Move file from here to there

```java
fileMove( sourcefile, destinationfile );

```

### Additional Examples

```java
filemove( sourceFilePath, destinationFilePath );

```

## Related

* [ContractPath](ContractPath.md)
* [CreateTempDirectory](CreateTempDirectory.md)
* [CreateTempFile](CreateTempFile.md)
* [DirectoryCopy](DirectoryCopy.md)
* [DirectoryCreate](DirectoryCreate.md)
* [DirectoryDelete](DirectoryDelete.md)
* [DirectoryExists](DirectoryExists.md)
* [DirectoryList](DirectoryList.md)
* [DirectoryMove](DirectoryMove.md)
* [DirectoryRename](DirectoryRename.md)
* [ExpandPath](ExpandPath.md)
* [FileAppend](FileAppend.md)
* [FileClose](FileClose.md)
* [FileCopy](FileCopy.md)
* [FileDelete](FileDelete.md)
* [FileExists](FileExists.md)
* [FileGetMimeType](FileGetMimeType.md)
* [FileInfo](FileInfo.md)
* [FileIsEOF](FileIsEOF.md)
* [FileOpen](FileOpen.md)
* [FileRead](FileRead.md)
* [FileReadBinary](FileReadBinary.md)
* [FileReadLine](FileReadLine.md)
* [FileSeek](FileSeek.md)
* [FileSetAccessMode](FileSetAccessMode.md)
* [FileSetAttribute](FileSetAttribute.md)
* [FileSetLastModified](FileSetLastModified.md)
* [FileSkipBytes](FileSkipBytes.md)
* [FileWrite](FileWrite.md)
* [FileWriteLine](FileWriteLine.md)
* [GetCanonicalPath](GetCanonicalPath.md)
* [GetDirectoryFromPath](GetDirectoryFromPath.md)
* [GetFileInfo](GetFileInfo.md)
* [getTempFile](getTempFile.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryExists`

Determines whether a directory exists

## Method Signature

```
DirectoryExists(path=[string], allowRealPath=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The directory path |  |
| `allowRealPath` | `boolean` | `true` | Whether to allow an absolute path as the path argument | `true` |

## Examples

### Script Syntax

Checking if a directory called 'icons' exists and then creating the directory if it does not exist.

<a href="https://try.boxlang.io/?code=eJzLTNNQUEzJLEpNLskvqnStyCwuKdZQSK0oSMxLCUgsydBQUNJPLC5OLSnWz8xN189Mzs8rVlLQBMNqLk64Tuei1MSSVKBqLIqtuWq5AEzXIoU%3D" target="_blank">Run Example</a>

```java
if( !directoryExists( expandPath( "/assets/img/icons" ) ) ) {
	directoryCreate( "assets/img/icons" );
}

```

Result: The directory 'icons' will be created under the img folder.

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLySxKTS7JL6p0rcgsLinWUFBKgYkEJJZkKCloWnMBAAI%2BDNI%3D" target="_blank">Run Example</a>

```java
directoryExists( "directoryPath" );

```

Result: false


## Related

  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [DirectoryCopy](./DirectoryCopy.md)
  * [DirectoryCreate](./DirectoryCreate.md)
  * [DirectoryDelete](./DirectoryDelete.md)
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

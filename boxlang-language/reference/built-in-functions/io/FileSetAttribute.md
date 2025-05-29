[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileSetAttribute`

Sets a file access attribute

## Method Signature

```
FileSetAttribute(file=[any], attribute=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `any` | `true` | The file path or File instance |  |
| `attribute` | `string` | `true` | The attribute to set true |  |

## Examples

### Create a temporary file and then change read-only mode



<a href="https://try.boxlang.io/?code=eJzLrXTLzElVsFVITy0JSc0tAPE0YByXzKLU5JL8okoNTR0FpZLU4hKQtJKCpjVXeVFmSap%2FaUlBaYmGglJmsQJIIDEpJ9VKQUlBDWQASKlnXlq%2BhkIuxA5NPWdHv%2FAgzxBXkAFpQKHg1BLHkpKizKTSklSYMqBFRamJKf55OZVYLFJ41DaJSAsARH5HRA%3D%3D" target="_blank">Run Example</a>

```java
myFile = getTempFile( getTempDirectory(), "testFile" );
writeOutput( "is writable: " & getFileInfo( myFile ).CANWRITE );
fileSetAttribute( myFile, "readOnly" );
writeOutput( " → " & getFileInfo( myFile ).CANWRITE );

```

Result: is writable: YES → NO

### Additional Examples


```java
filesetattribute( "example.txt", "readonly" );

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
  * [FileDelete](./FileDelete.md)
  * [DirectoryList](./DirectoryList.md)
  * [FileWrite](./FileWrite.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [getTempFile](./getTempFile.md)

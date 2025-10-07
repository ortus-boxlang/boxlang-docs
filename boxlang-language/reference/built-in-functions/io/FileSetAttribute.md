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
  * [FileSetLastModified](./FileSetLastModified.md)
  * [FileSkipBytes](./FileSkipBytes.md)
  * [FileWrite](./FileWrite.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)
  * [PropertyFile](./PropertyFile.md)

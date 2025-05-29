[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileSeek`

Moves the buffer cursor position forward the number of characters specified by the position argument

## Method Signature

```
FileSeek(file=[any], position=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `any` | `true` | The File instance |  |
| `position` | `integer` | `true` | The cursor position to move forward in the file |  |

## Examples

### Script Syntax




```java
<bx:script>
	NewFile = fileOpen( expandPath( "." ) & "	est.txt", "write", "", true );
	fileSeek( NewFile, 5 );
</bx:script>
   
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

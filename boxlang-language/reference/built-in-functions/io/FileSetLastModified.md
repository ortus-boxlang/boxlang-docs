[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileSetLastModified`

Sets the last modified time of a file

## Method Signature

```
FileSetLastModified(file=[any], date=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `any` | `true` | A file path or object |  |
| `date` | `any` | `true` | A date time object or string |  |

## Examples

### Script Syntax




```java
<bx:script>
	fileSetLastModified( "c:	emp	est1.txt", "#now()#" );
	writeOutput( getFileInfo( "c:	emp	est1.txt" ).LASTMODIFIED );
</bx:script>
  
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJyFzEEKwjAQQNG9pxiySiBEcOuqEIWCUkEvMDgTHWiTYqa0xzeeQP7285KMXFlHrDoVkiRMFnibMdMN9W3BhL1y1SdWDrqpAeeBULmjNhoyHg4eclmtg9Zxt35EOS7TbOHFmhovOZV%2FJrhw6e6P6xD7c3%2BKP%2BgLmnEw%2FA%3D%3D" target="_blank">Run Example</a>

```java
filesetlastmodified( expandPath( "./testcase.txt" ), dateAdd( "d", 2, now() ) );
writeDump( getfileinfo( expandPath( "./testcase.txt" ) ).LASTMODIFIED );

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
  * [FileSkipBytes](./FileSkipBytes.md)
  * [FileWrite](./FileWrite.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)

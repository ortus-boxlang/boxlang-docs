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
  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [DirectoryDelete](./DirectoryDelete.md)
  * [FileSetAttribute](./FileSetAttribute.md)
  * [FileDelete](./FileDelete.md)
  * [DirectoryList](./DirectoryList.md)
  * [FileWrite](./FileWrite.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [getTempFile](./getTempFile.md)

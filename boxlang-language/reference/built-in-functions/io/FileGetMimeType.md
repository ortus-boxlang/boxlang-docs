[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileGetMimeType`

Gets the MIME type for the file path/file object you have specified.

## Method Signature

```
FileGetMimeType(file=[any], strict=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `any` | `true` | The file path or file object to get the MIME type for. |  |
| `strict` | `boolean` | `false` | If true, throws an exception if the file does not exist or is empty. If false, returns "application/octet-stream" for non-existent or empty files. | `true` |

## Examples

### Two PDFs and two text files with and without strict mode

Assume that you have a file named test.pdf in temp directory and test.txt in the same folder, and you want to check the MIME type. Here test.txt is a copy of test.pdf with extension renamed to txt.


```java
<bx:script>
	mimeTypes = "";
	mimeTypes = listAppend( mimeTypes, fileGetMimeType( expandPath( "/folder1/test.pdf" ) ) );
	mimeTypes = listAppend( mimeTypes, fileGetMimeType( expandPath( "/folder1/test.pdf" ), false ) );
	mimeTypes = listAppend( mimeTypes, fileGetMimeType( expandPath( "/folder1/test.txt" ) ) );
	mimeTypes = listAppend( mimeTypes, fileGetMimeType( expandPath( "/folder1/test.txt" ), false ) );
	writeOutput( mimeTypes );
</bx:script>

```

Result: application/pdf,application/pdf,text/plain,text/plain

### Additional Examples


```java
file = filegetmimetype( filepath / filename.EXT );
writeDump( file );

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
  * [PropertyFile](./PropertyFile.md)

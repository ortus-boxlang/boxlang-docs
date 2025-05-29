[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileGetMimeType`

Gets the MIME type for the file path/file object you have specified.

## Method Signature

```
FileGetMimeType(file=[string], strict=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `string` | `true` | The file path or file object to get the MIME type for. |  |
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

  * [FileIsEOF](./FileIsEOF.md)
  * [FileExists](./FileExists.md)
  * [FileInfo](./FileInfo.md)
  * [GetFileInfo](./GetFileInfo.md)
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
  * [FileWrite](./FileWrite.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [getTempFile](./getTempFile.md)

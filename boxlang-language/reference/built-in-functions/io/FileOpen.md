[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileOpen`

Opens a file for reading or writing and returns a file object for future operations

## Method Signature

```
FileOpen(file=[string], mode=[string], charset=[string], seekable=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `string` | `true` | The file to open. |  |
| `mode` | `string` | `false` | The mode to open the file in. Defaults to "read". | `read` |
| `charset` | `string` | `false` | The character set to use when reading or writing the file. Defaults to "utf-8". | `utf-8` |
| `seekable` | `boolean` | `false` | Whether the file should be opened as seekable. Defaults to false. |  |

## Examples

### Opens a file, reads a line then closes it.




```java
// Open File
var fileObject = fileOpen( "/path/to/file.txt" );
// Perform Actions
try {
	// Read Line
	writeOutput( fileReadLine( fileObject ) );
}
// Error Handling
 catch (any ex) {
	// Report Exception
	writeDump( ex );
}finally {
	// Always Close
	// Close File
	fileClose( fileObject );
}

```


### Additional Examples


```java
myFile = fileOpen( "filepath/filename.ext" );
writeDump( myfile );

```



```java
// how to access the underlying resource provider info
f = "ram://demo.txt";
fileWrite( f, "demo" );
dump( f.getResource().getResourceProvider().getScheme() );
 // ram ( i.e. the resource provider type)

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

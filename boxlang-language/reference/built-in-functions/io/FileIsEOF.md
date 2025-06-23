[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `FileIsEOF`

Determines whether the end of the file has been reached while reading it.

## Method Signature

```
FileIsEOF(file=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `file` | `any` | `true` | The currently open file object |  |

## Examples

### Simple usage syntax

Call fileIsEOF on a file object and save the result to a variable.


```java
fileObj = fileOpen(expandPath('./file.txt');
isEndOfFile = fileIsEOF(fileObj);
```


### Using fileIsEOF to loop over all lines of a text file

Simplified example of using fileIsEOF to determine when all lines have been read from a file. Error handling omitted for clarity.


```java
// Error handling omitted for clarity.
// open a file for reading
fileObj = fileOpen( expandPath( "./file.txt" ), "read" );
// read each line until we read the end of the file.
// fileIsEOF(fileObj) == false until we've read in the last line.
while (!fileIsEOF( fileObj )) {
	lineContent = fileReadLine( fileObj );
	// do something with content of each line

}
// end of file reached, close the file handle
fileClose( fileObj );

```


### Additional Examples


```java
filePath = "/path/to/file.txt";
openFile = fileopen( filePath, "read" );
lines = [];
// IMPORTANT: must close file, use try/catch/finally to do so
try {
	// fileIsEOF(openFile) == false until we've read in the last line.
	while (!fileIsEoF( openFile )) {
		arrayAppend( lines, fileReadLine( openFile ) );
	}
} catch (any e) {
	rethrow;
}finally {
	fileClose( openFile );
}

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

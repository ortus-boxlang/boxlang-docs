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
  * [FileSetAttribute](./FileSetAttribute.md)
  * [FileDelete](./FileDelete.md)
  * [DirectoryList](./DirectoryList.md)
  * [FileWrite](./FileWrite.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [getTempFile](./getTempFile.md)

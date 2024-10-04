# FileReadBinary

Reads the contents of a file and returns it as a string or binary object

## Method Signature

```
FileReadBinary(filepath=[string], charsetOrBufferSize=[string], charset=[string], buffersize=[string])
```

### Arguments

| Argument              | Type     | Required | Description                                                                                                                                                         | Default |
| --------------------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `filepath`            | `string` | `true`   | The path to the file to read.                                                                                                                                       |         |
| `charsetOrBufferSize` | `string` | `false`  | Either the charset to use when reading the file, or the buffer size to use when reading the file. If providing a buffer size, the next argument can be the charset. |         |
| `charset`             | `string` | `false`  | The explicit charset to use when reading the file.                                                                                                                  |         |
| `buffersize`          | `string` | `false`  | The explicit buffer size to use when reading the file.                                                                                                              |         |

## Examples

## Related

* [ContractPath](contractpath.md)
* [CreateTempDirectory](createtempdirectory.md)
* [CreateTempFile](createtempfile.md)
* [DirectoryCopy](directorycopy.md)
* [DirectoryCreate](directorycreate.md)
* [DirectoryDelete](directorydelete.md)
* [DirectoryExists](directoryexists.md)
* [DirectoryList](directorylist.md)
* [DirectoryMove](directorymove.md)
* [DirectoryRename](directoryrename.md)
* [ExpandPath](expandpath.md)
* [FileAppend](fileappend.md)
* [FileClose](fileclose.md)
* [FileCopy](filecopy.md)
* [FileDelete](filedelete.md)
* [FileExists](fileexists.md)
* [FileGetMimeType](filegetmimetype.md)
* [FileInfo](fileinfo.md)
* [FileIsEOF](fileiseof.md)
* [FileMove](filemove.md)
* [FileOpen](fileopen.md)
* [FileRead](fileread.md)
* [FileReadLine](filereadline.md)
* [FileSeek](fileseek.md)
* [FileSetAccessMode](filesetaccessmode.md)
* [FileSetAttribute](filesetattribute.md)
* [FileSetLastModified](filesetlastmodified.md)
* [FileSkipBytes](fileskipbytes.md)
* [FileWrite](filewrite.md)
* [FileWriteLine](filewriteline.md)
* [GetCanonicalPath](getcanonicalpath.md)
* [GetDirectoryFromPath](getdirectoryfrompath.md)
* [GetFileInfo](getfileinfo.md)
* [getTempFile](gettempfile.md)

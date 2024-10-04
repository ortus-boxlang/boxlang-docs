# FileGetMimeType

Gets the MIME type for the file path/file object you have specified.

## Method Signature

```
FileGetMimeType(file=[string], strict=[boolean])
```

### Arguments

| Argument | Type      | Required | Description                                                                                                                                        | Default |
| -------- | --------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `file`   | `string`  | `true`   | The file path or file object to get the MIME type for.                                                                                             |         |
| `strict` | `boolean` | `false`  | If true, throws an exception if the file does not exist or is empty. If false, returns "application/octet-stream" for non-existent or empty files. | `true`  |

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
* [FileInfo](fileinfo.md)
* [FileIsEOF](fileiseof.md)
* [FileMove](filemove.md)
* [FileOpen](fileopen.md)
* [FileRead](fileread.md)
* [FileReadBinary](filereadbinary.md)
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

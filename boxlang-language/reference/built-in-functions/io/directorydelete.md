# DirectoryDelete

Deletes a directory

## Method Signature

```
DirectoryDelete(path=[string], recursive=[boolean])
```

### Arguments

| Argument    | Type      | Required | Description                                                                                                                                    | Default |
| ----------- | --------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `path`      | `string`  | `true`   | the path of the directory to delete                                                                                                            |         |
| `recursive` | `boolean` | `true`   | <p>[default:false] whether to recursively delete the directory.<br>If falls and the directory is not empty, with throw a runtime exception</p> | `false` |

## Examples

## Related

* [ContractPath](contractpath.md)
* [CreateTempDirectory](createtempdirectory.md)
* [CreateTempFile](createtempfile.md)
* [DirectoryCopy](directorycopy.md)
* [DirectoryCreate](directorycreate.md)
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

# FileAppend

Appends new contents to a file starting at the last character in the file

## Method Signature

```
FileAppend(file=[any], data=[any], charset=[string])
```

### Arguments

| Argument   | Type     | Required   | Description                                               | Default   |
| ---------- | -------- | ---------- | --------------------------------------------------------- | --------- |
| `file`     | `any`    | `true`     | The file object or string file path                       |           |
| `data`     | `any`    | `true`     | The data to append                                        |           |
| `charset`  | `string` | `false`    | \[utf-8] the default charset to open the file for writing | utf-8     |
| ---------- | ------   | ---------- | -------------                                             | --------- |

## Examples

```
FileAppend(file=[any], data=[any], charset=[string])
```

## Related

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

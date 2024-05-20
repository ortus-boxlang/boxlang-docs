# FileWrite

Writes the contents of a string or binary data to a file

## Method Signature

```
FileWrite(file=[string], data=[any], charset=[string], createPath=[boolean])
```

### Arguments

| Argument     | Type      | Required   | Description                                                    | Default   |
| ------------ | --------- | ---------- | -------------------------------------------------------------- | --------- |
| `file`       | `string`  | `true`     | The string path of the file - either root relative or absolute |           |
| `data`       | `any`     | `true`     | The string or binary byte array of the file content            |           |
| `charset`    | `string`  | `false`    | The charset encoding ( ignored for binary data )               | utf-8     |
| `createPath` | `boolean` | `false`    |                                                                | false     |
| ----------   | ------    | ---------- | -------------                                                  | --------- |

## Examples

```
FileWrite(file=[string], data=[any], charset=[string], createPath=[boolean])
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
* [FileWriteLine](filewriteline.md)
* [GetCanonicalPath](getcanonicalpath.md)
* [GetDirectoryFromPath](getdirectoryfrompath.md)
* [GetFileInfo](getfileinfo.md)
* [getTempFile](gettempfile.md)

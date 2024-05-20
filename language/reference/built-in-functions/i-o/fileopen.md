# FileOpen

Describe what the invocation of your bif function does

## Method Signature

```
FileOpen(file=[string], mode=[string], charset=[string], seekable=[boolean])
```

### Arguments

| Argument   | Type      | Required   | Description   | Default   |
| ---------- | --------- | ---------- | ------------- | --------- |
| `file`     | `string`  | `true`     |               |           |
| `mode`     | `string`  | `false`    |               | read      |
| `charset`  | `string`  | `false`    |               | utf-8     |
| `seekable` | `boolean` | `false`    |               |           |
| ---------- | ------    | ---------- | ------------- | --------- |

## Examples

```
FileOpen(file=[string], mode=[string], charset=[string], seekable=[boolean])
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

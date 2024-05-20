# DirectoryMove

Moves a directory from one location to another

## Method Signature

```
DirectoryMove(oldPath=[string], newPath=[string], createPath=[boolean])
```

### Arguments

| Argument     | Type      | Required   | Description                                                   | Default   |
| ------------ | --------- | ---------- | ------------------------------------------------------------- | --------- |
| `oldPath`    | `string`  | `true`     | The previous directory path                                   |           |
| `newPath`    | `string`  | `true`     | The new directory path                                        |           |
| `createPath` | `boolean` | `false`    | \[true] Whether to create all necessary paths to the new path | true      |
| ----------   | ------    | ---------- | -------------                                                 | --------- |

## Examples

```
DirectoryMove(oldPath=[string], newPath=[string], createPath=[boolean])
```

## Related

* [CreateTempDirectory](createtempdirectory.md)
* [CreateTempFile](createtempfile.md)
* [DirectoryCopy](directorycopy.md)
* [DirectoryCreate](directorycreate.md)
* [DirectoryDelete](directorydelete.md)
* [DirectoryExists](directoryexists.md)
* [DirectoryList](directorylist.md)
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

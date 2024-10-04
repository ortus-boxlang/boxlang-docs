# DirectoryCopy

Copies a directory from one location to another

## Method Signature

```
DirectoryCopy(source=[string], destination=[string], recurse=[boolean], filter=[string], createPath=[boolean])
```

### Arguments

| Argument      | Type      | Required | Description                                                                | Default |
| ------------- | --------- | -------- | -------------------------------------------------------------------------- | ------- |
| `source`      | `string`  | `true`   | The source directory                                                       |         |
| `destination` | `string`  | `true`   | The destination directory                                                  |         |
| `recurse`     | `boolean` | `false`  | \[ false ] whether to recurse in to sub-directories and create paths       | `false` |
| `filter`      | `string`  | `false`  | \[ "\*" ] a file or directory filter to pass                               | `*`     |
| `createPath`  | `boolean` | `false`  | \[ true ] whether to create any nested paths required to the new directory | `true`  |

## Examples

## Related

* [ContractPath](contractpath.md)
* [CreateTempDirectory](createtempdirectory.md)
* [CreateTempFile](createtempfile.md)
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
* [FileWrite](filewrite.md)
* [FileWriteLine](filewriteline.md)
* [GetCanonicalPath](getcanonicalpath.md)
* [GetDirectoryFromPath](getdirectoryfrompath.md)
* [GetFileInfo](getfileinfo.md)
* [getTempFile](gettempfile.md)

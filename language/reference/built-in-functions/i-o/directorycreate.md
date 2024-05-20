# DirectoryCreate

Creates a directory

## Method Signature

```
DirectoryCreate(path=[string], createPath=[boolean], ignoreExists=[boolean], mode=[string])
```

### Arguments

| Argument       | Type      | Required   | Description                                                                | Default   |
| -------------- | --------- | ---------- | -------------------------------------------------------------------------- | --------- |
| `path`         | `string`  | `true`     | The directory path to create                                               |           |
| `createPath`   | `boolean` | `false`    | \[true] Whether to create all paths necessary to create the directory path | true      |
| `ignoreExists` | `boolean` | `false`    | \[false] Whether to ignore if a directory already exists                   | false     |
| `mode`         | `string`  | `false`    | When provided will attempt to set the posix permissions on the directory   |           |
| ----------     | ------    | ---------- | -------------                                                              | --------- |

## Examples

```
DirectoryCreate(path=[string], createPath=[boolean], ignoreExists=[boolean], mode=[string])
```

## Related

* [CreateTempDirectory](createtempdirectory.md)
* [CreateTempFile](createtempfile.md)
* [DirectoryCopy](directorycopy.md)
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

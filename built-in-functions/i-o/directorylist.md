# DirectoryList

Describe what the invocation of your bif function does

## Method Signature

```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[string], sort=[string], type=[string])
```

### Arguments

| Argument   | Type      | Required   | Description   | Default   |
| ---------- | --------- | ---------- | ------------- | --------- |
| `path`     | `string`  | `true`     |               |           |
| `recurse`  | `boolean` | `true`     |               | false     |
| `listInfo` | `string`  | `false`    |               | path      |
| `filter`   | `string`  | `false`    |               |           |
| `sort`     | `string`  | `false`    |               | name      |
| `type`     | `string`  | `false`    |               | all       |
| ---------- | ------    | ---------- | ------------- | --------- |

## Examples

```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[string], sort=[string], type=[string])
```

## Related

* [CreateTempDirectory](createtempdirectory.md)
* [CreateTempFile](createtempfile.md)
* [DirectoryCopy](directorycopy.md)
* [DirectoryCreate](directorycreate.md)
* [DirectoryDelete](directorydelete.md)
* [DirectoryExists](directoryexists.md)
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

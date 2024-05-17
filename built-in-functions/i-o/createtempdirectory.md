# CreateTempDirectory

Creates a temporary directory in the specified directory with the specified prefix if passed.

## Method Signature

```
CreateTempDirectory(directory=[string], prefix=[string])
```

### Arguments

| Argument    | Type     | Required   | Description                                                                                  | Default                                           |
| ----------- | -------- | ---------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `directory` | `string` | `false`    | The directory in which to create the temp directory, we default to the system temp directory | /var/folders/sh/yq09rnbj48764cvf2k4nhcxh0000gn/T/ |
| `prefix`    | `string` | `false`    | The prefix string to be used in generating the directory's name; may be empty                |                                                   |
| ----------  | ------   | ---------- | -------------                                                                                | ---------                                         |

## Examples

```
CreateTempDirectory(directory=[string], prefix=[string])
```

## Related

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
* [FileWrite](filewrite.md)
* [FileWriteLine](filewriteline.md)
* [GetCanonicalPath](getcanonicalpath.md)
* [GetDirectoryFromPath](getdirectoryfrompath.md)
* [GetFileInfo](getfileinfo.md)
* [getTempFile](gettempfile.md)

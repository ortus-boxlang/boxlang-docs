# CreateTempFile

Creates a temporary file in the specified directory with the specified prefix and suffix if passed.

## Method Signature

```
CreateTempFile(directory=[string], prefix=[string], suffix=[string])
```

### Arguments

| Argument    | Type     | Required   | Description                                                                                            | Default                                           |
| ----------- | -------- | ---------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------- |
| `directory` | `string` | `false`    | The directory in which to create the temp file, we default to the system temp directory                | /var/folders/sh/yq09rnbj48764cvf2k4nhcxh0000gn/T/ |
| `prefix`    | `string` | `false`    | The prefix string to be used in generating the file's name; may be empty                               |                                                   |
| `suffix`    | `string` | `false`    | The suffix string to be used in generating the file's name; may be empty, in which case ".tmp" is used |                                                   |
| ----------  | ------   | ---------- | -------------                                                                                          | ---------                                         |

## Examples

```
CreateTempFile(directory=[string], prefix=[string], suffix=[string])
```

## Related

* [CreateTempDirectory](createtempdirectory.md)
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

# DirectoryList

List the contents of a directory.

Returns either an array, or a query depending on the ,{@code listInfo}, argument. ,

, The ,{@code listInfo}, argument can be one of the following: ,

* , ,
* ,{@code name}, - Returns an array of the names of the items in the directory.,
* , ,
* ,{@code path}, - Returns an array of the absolute paths of the items in the directory.,
* , ,
*   ,{@code query}, - Returns a query of the items in the directory containing the following fields: ,

    * , ,
    * ,{@code attributes}, - The attributes of the item (R, W, X, H).,
    * , ,
    * ,{@code dateLastModified}, - The date the item was last modified.,
    * , ,
    * ,{@code directory}, - The directory containing the item.,
    * , ,
    * ,{@code mode}, - The mode of the item.,
    * , ,
    * ,{@code name}, - The name of the item.,
    * , ,
    * ,{@code size}, - The size of the item in bytes.,
    * , ,
    * ,{@code type}, - The type of the item (either "Dir" or "File").,
    * , ,

    , ,
* , ,

, ,

, The ,{@code filter}, argument can be the following: ,

* , ,
*   , A closure/lambda that takes a single argument (the path of the item) and returns a boolean. True to return it, false otherwise.

    ,

    ```
    ,
    DirectoryList( path: "/path/to/dir", filter: path -> path.endsWith(".txt") )
    ,
    ```

    ,

    ,
* , ,
* , A string that is a glob pattern: E.g. "_.txt" to only return files with the .txt extension. Or you can use the ,{@code |}, pipe to separate multiple patterns: E.g. "_.txt|\*.csv" to return files with either the .txt or .csv extension. ,
* , ,

## Method Signature

```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[any], sort=[string], type=[string])
```

### Arguments

| Argument   | Type      | Required | Description                                                                                                                                                                                      | Default |
| ---------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| `path`     | `string`  | `true`   | The absolute path to the directory to list.                                                                                                                                                      |         |
| `recurse`  | `boolean` | `true`   | Whether to recurse into subdirectories or not. The default is false.                                                                                                                             | `false` |
| `listInfo` | `string`  | `false`  | The type of information to return. Valid values are "name", "path", and "query". The default is "path".                                                                                          | `path`  |
| `filter`   | `any`     | `false`  | A filter to apply to the listing. This can be a function that takes a single argument (the path of the item) and returns a boolean or a string that is a glob pattern. The default is no filter. |         |
| `sort`     | `string`  | `false`  | The sort order of the listing. Valid values are "name", "size", "date", and "type". The default is "name".You can also use `asc` or `desc` to specify the sort order. E.g. `sort: "name desc"`.  | `name`  |
| `type`     | `string`  | `false`  | The type of items to list. Valid values are "all", "file", and "dir". Default is "all".                                                                                                          | `all`   |

## Examples

## Related

* [ContractPath](contractpath.md)
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

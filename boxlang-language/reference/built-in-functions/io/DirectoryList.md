[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryList`

List the contents of a directory.

Returns either an array, or a query depending on the 
{@code listInfo}
 argument.
 
<p>

 The 
{@code listInfo}
 argument can be one of the following:
 
<ul>

 
<li>
{@code name}
 - Returns an array of the names of the items in the directory.
</li>

 
<li>
{@code path}
 - Returns an array of the absolute paths of the items in the directory.
</li>

 
<li>
{@code query}
 - Returns a query of the items in the directory containing the following fields:
 
<ul>

 
<li>
{@code attributes}
 - The attributes of the item (R, W, X, H).
</li>

 
<li>
{@code dateLastModified}
 - The date the item was last modified.
</li>

 
<li>
{@code directory}
 - The directory containing the item.
</li>

 
<li>
{@code mode}
 - The mode of the item.
</li>

 
<li>
{@code name}
 - The name of the item.
</li>

 
<li>
{@code size}
 - The size of the item in bytes.
</li>

 
<li>
{@code type}
 - The type of the item (either "Dir" or "File").
</li>

 
</ul>

 
</li>

 
</ul>

 
<p>

 The 
{@code filter}
 argument can be the following:
 
<ul>

 
<li>

 A closure/lambda that takes a single argument (the path of the item) and returns a boolean. True to return it, false otherwise.

 
<pre>

 DirectoryList( path: "/path/to/dir", filter: path -> path.endsWith(".txt") )
 
</pre>


 
</li>

 
<li>

 A string that is a glob pattern: E.g. "*.txt" to only return files with the .txt extension. Or you can use the 
{@code |}
 pipe to separate multiple patterns: E.g. "*.txt|*.csv" to return files with either the .txt or .csv extension.
 
</li>

 
</ul>

## Method Signature

```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[any], sort=[string], type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `path` | `string` | `true` | The absolute path to the directory to list. |  |
| `recurse` | `boolean` | `true` | Whether to recurse into subdirectories or not. The default is false. | `false` |
| `listInfo` | `string` | `false` | The type of information to return. Valid values are "name", "path", and "query". The default is "path". | `path` |
| `filter` | `any` | `false` | A filter to apply to the listing. This can be a function that takes a single argument (the path of the item) and returns a boolean or a string that is a glob pattern. The default is no filter. |  |
| `sort` | `string` | `false` | The sort order of the listing. Valid values are "name", "size", "date", and "type". The default is "name".You can also use <code>asc</code> or <code>desc</code> to specify the sort order. E.g. <code>sort: "name desc"</code>. | `name` |
| `type` | `string` | `false` | The type of items to list. Valid values are "all", "file", and "dir". Default is "all". | `all` |

## Examples



## Related

  * [ContractPath](./ContractPath.md)
  * [CreateTempDirectory](./CreateTempDirectory.md)
  * [CreateTempFile](./CreateTempFile.md)
  * [DirectoryCopy](./DirectoryCopy.md)
  * [DirectoryCreate](./DirectoryCreate.md)
  * [DirectoryDelete](./DirectoryDelete.md)
  * [DirectoryExists](./DirectoryExists.md)
  * [DirectoryMove](./DirectoryMove.md)
  * [DirectoryRename](./DirectoryRename.md)
  * [ExpandPath](./ExpandPath.md)
  * [FileAppend](./FileAppend.md)
  * [FileClose](./FileClose.md)
  * [FileCopy](./FileCopy.md)
  * [FileDelete](./FileDelete.md)
  * [FileExists](./FileExists.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileInfo](./FileInfo.md)
  * [FileIsEOF](./FileIsEOF.md)
  * [FileMove](./FileMove.md)
  * [FileOpen](./FileOpen.md)
  * [FileRead](./FileRead.md)
  * [FileReadBinary](./FileReadBinary.md)
  * [FileReadLine](./FileReadLine.md)
  * [FileSeek](./FileSeek.md)
  * [FileSetAccessMode](./FileSetAccessMode.md)
  * [FileSetAttribute](./FileSetAttribute.md)
  * [FileSetLastModified](./FileSetLastModified.md)
  * [FileSkipBytes](./FileSkipBytes.md)
  * [FileWrite](./FileWrite.md)
  * [FileWriteLine](./FileWriteLine.md)
  * [GetCanonicalPath](./GetCanonicalPath.md)
  * [GetDirectoryFromPath](./GetDirectoryFromPath.md)
  * [GetFileInfo](./GetFileInfo.md)
  * [getTempFile](./getTempFile.md)

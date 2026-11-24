[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DirectoryList`

List the contents of a directory.

Returns either an array, or a query depending on the {@code listInfo} argument.
 <p>
 The {@code listInfo} argument can be one of the following:
 <ul>
 <li>{@code name} - Returns an array of the names of the items in the directory.</li>
 <li>{@code path} - Returns an array of the absolute paths of the items in the directory.</li>
 <li>{@code query} - Returns a query of the items in the directory containing the following fields:
 <ul>
 <li>{@code attributes} - The attributes of the item (R, W, X, H).</li>
 <li>{@code dateLastModified} - The date the item was last modified.</li>
 <li>{@code directory} - The directory containing the item.</li>
 <li>{@code isLink} - True if the item is a symbolic link.</li>
 <li>{@code linkTarget} - The target of the symbolic link, or an empty string if the item is not a link.</li>
 <li>{@code mode} - The mode of the item.</li>
 <li>{@code name} - The name of the item.</li>
 <li>{@code size} - The size of the item in bytes.</li>
 <li>{@code type} - The type of the item (either "Dir" or "File").</li>
 </ul>
 </li>
 </ul>
 <p>
 The {@code filter} argument can be the following:
 <ul>
 <li>
 A closure/lambda that takes a single argument (the path of the item) and returns a boolean. True to return it, false otherwise.

 <pre>
 DirectoryList( path: "/path/to/dir", filter: path -> path.endsWith(".txt") )
 </pre>

 </li>
 <li>
 A string that is a glob pattern: E.g. "*.txt" to only return files with the .txt extension. Or you can use the {@code |} pipe to separate multiple patterns: E.g. "*.txt|*.csv" to return files with either the .txt or .csv extension.
 </li>
 </ul>

## Method Signature

```
DirectoryList(path=[string], recurse=[boolean], listInfo=[string], filter=[any], sort=[string], type=[string], followLinks=[boolean])
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
| `followLinks` | `boolean` | `false` | Whether to descend into symbolic links to directories when recursing. The default is false. A symbolic link given as the path is always resolved. | `false` |

## Examples

### An array of files in this directory



<a href="https://try.boxlang.io/?code=eJxLLCpKrPRP88lPTsxxy8xJLVawVUjJLEpNLskvqvTJLC7RUEitKEjMSwlILMnQUFDS01dS0NRRSEvMKU7VUVDKS8xNBQpYcwEAo5oXPg%3D%3D" target="_blank">Run Example</a>

```java
arrayOfLocalFiles = directoryList( expandPath( "./" ), false, "name" );

```

Result: [.DS_Store, .ortus, Application.bx, MyDestinationDirectory, Page.bx, assets, bifs, components, compressed_test.txt.gz, example.bxm, example.bxm, filepath, images, index.bxm, myNewFileName.txt, new, new_directory, server.json, setup_db.sql, some, test.txt, testcase.txt]

### A query of files in this directory sorted by date last modified



<a href="https://try.boxlang.io/?code=eJwrLE0tqvRPc8vMSS1WsFVIySxKTS7JL6r0ySwu0VBIrShIzEsJSCzJ0FBQ0tNXUtDUUUhLzClO1VFQKgTpVAIyQNglsSTVJ7G4xDc%2FJTMtMzVFwcU12Bmo3JoLAELdHpE%3D" target="_blank">Run Example</a>

```java
queryOfFiles = directoryList( expandPath( "./" ), false, "query", "", "DateLastModified DESC" );

```

### An array of files in the temp directory

Including sub-directories and as an array containing full paths

<a href="https://try.boxlang.io/?code=eJxLLCpKrPRPC0nNLXDLzEktVrBVSMksSk0uyS%2Bq9MksLtFQUNLTV9JRKCkqTVXQtOYCAKoOD88%3D" target="_blank">Run Example</a>

```java
arrayOfTempFiles = directoryList( "./", true );

```


### Filter files with closure

Pass a closure instead of a string as `filter` param

<a href="https://try.boxlang.io/?code=eJwljUsKg0AQRNfxFI0rA8NcIBiQRFf5QG7Qji1O0Bnp7gQl5O4ZyaaKgno8ZMb13jd%2BVGLqUpNACZ1nchp5vXjRAnKbG%2BhxFDKQB5wozQKqsMKMOsAeyiN8sh2TvjjAxjQ%2BdLd4QqFEV%2FM8eofqY7DtYji2UcXqokaI38T2KTGYHt%2FepUcKYwdF50jEPOrqfK3t1CXlX3bIvlv8AAO8Pew%3D" target="_blank">Run Example</a>

```java
arrayOfFilteredFiles = directoryList( ".", false, "name", ( Any path ) => {
	return ListFindNoCase( "Application.bx,robots.txt,server.json,favicon.ico,.htaccess,README.md", path );
} );

```

Result: []

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLySxKTS7JL6r0ySwu0VBQ0i9LLNJPSSxJVNJRSEvMKU7VUVAqSCzJAHI1FBzzKhVAHAVNBVs7hWouzqLUktKiPIXEovTS3NS8kmK9AMcQD72MxOLg0rS0zAqgeXo5%2BelKCprWXLUgAgDHRiJT" target="_blank">Run Example</a>

```java
directoryList( "/var/data", false, "path", ( Any path ) => {
	return arguments.PATH.hasSuffix( ".log" );
} );

```

Result: []

### Symbolic links in a recursive listing

A recursive listing does not descend into symbolic links by default. Pass `followLinks=true` to list what the links point to. A link given as the `path` itself is always resolved.

```java
base = getTempDirectory() & "linkDemo";
directoryCreate( base & "/releases/v2" );
fileWrite( base & "/releases/v2/app.txt", "app" );
fileCreateSymlink( base & "/current", base & "/releases/v2" );

names = directoryList( path=base, recurse=true, listInfo="name" );
writeOutput( names.len() & " " & names.toList() );

```

Result: 4 current,releases,v2,app.txt

```java
names = directoryList( path=base, recurse=true, listInfo="name", followLinks=true );
writeOutput( names.len() & " " & names.toList() );

```

Result: 5 current,app.txt,releases,v2,app.txt

### Find the links with the query columns

The query returned by `listInfo="query"` has the `isLink` and `linkTarget` columns. `linkTarget` is an empty string for items that are not links.

```java
q = directoryList( base, false, "query" );
for ( row in q ) {
	writeOutput( row.name & " isLink=" & row.isLink & " target=" & row.linkTarget.listLast( "/" ) & "; " );
}

```

Result: current isLink=true target=v2; releases isLink=false target=;

### Filter to only the links

`type` keeps its values of `all`, `file` and `dir`. To list only links, use a `filter` closure with `fileIsSymlink()`.

```java
links = directoryList( path=base, listInfo="name", filter=( path ) => fileIsSymlink( path ) );
writeOutput( links.toList() );

```

Result: current

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
  * [FileCreateSymlink](./FileCreateSymlink.md)
  * [FileDelete](./FileDelete.md)
  * [FileExists](./FileExists.md)
  * [FileGetMimeType](./FileGetMimeType.md)
  * [FileInfo](./FileInfo.md)
  * [FileIsEOF](./FileIsEOF.md)
  * [FileIsSymlink](./FileIsSymlink.md)
  * [FileMove](./FileMove.md)
  * [FileOpen](./FileOpen.md)
  * [FileRead](./FileRead.md)
  * [FileReadBinary](./FileReadBinary.md)
  * [FileReadLine](./FileReadLine.md)
  * [FileReadSymlink](./FileReadSymlink.md)
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
  * [PropertyFile](./PropertyFile.md)

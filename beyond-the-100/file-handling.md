# File Handling

BoxLang allows you to manipulate, read, upload, and more files via its built-in methods, which are great and easy to use. It can even help you manipulate zip/jar archives! We won't go into every single detail of file handling, but below, you can find the majority of functions to handle file handling.

{% hint style="success" %}
You can find the file system functions here: [https://cfdocs.org/filesystem-functions](https://cfdocs.org/filesystem-functions).
{% endhint %}

TODO: REVIEW LINKS BELOW AND UPDATE

* `DirectoryCopy` Copies the contents of a directory to a destination directory.
* `DirectoryCreate` Creates a new directory for the specified path
* `DirectoryDelete` Deletes directory for a given path
* `DirectoryExists` Determines whether a directory exists.
* `DirectoryList` Lists the directory and returns the list of files under it as an array or query
* `DirectoryRename` Renames given directory
* `ExpandPath` Creates an absolute, platform-appropriate path that is equivalent to the value of relative\_path, appended to the base path. This function (despite its name) can accept an absolute or relative path in the relative\_path attribute
* `FileAppend` appends the entire content to the specified file.
* `FileClose` Closes an open file.
* `FileCopy` Copies the specified on-disk or in-memory source file to the specified destination file.
* `FileDelete` Deletes the specified file on the server.
* `FileExists` Determines whether a file exists
* `FileGetMimeType` Returns the mime type of the given file
* `FileInfo` returns detailed info about the given file.
* `FileIsEOF` Determines whether Lucee has reached the end of the file while reading it.
* `FileMove` Moves file from source to destination
* `FileOpen` Opens a file to read, write, or append.
* `FileRead` Reads an on-disk or in-memory text file or a file object created with the FileOpen function.
* `FileReadLine` Reads a line from a file.
* `FileSeek` Shifts the file pointer to the given position. The file must be opened with the seekable option
* `FileSetAccessMode` This function sets the attributes of an on-disk file on UNIX or Linux. It does not work with in-memory files.
* `FileSetAttribute` For the given path, set the file attributes.
* `FileSetLastModified` For the given file, set the last modification date
* `FileSkipBytes` Shifts the file pointer by the given number of bytes.
* `FileTouch` Touches the given file and creates it if it does not already exist.
* `FileUpload` Uploads a file to a directory on the server.
* `FileUploadAll` Uploads files to a directory on the server.
* `FileWrite` If you specify a file path, it writes the entire content to the specified file. If you specify a file object, it writes text or binary data to the file object.
* `FileWriteLine` Opens up the file (or uses the existing file object) and appends the given line of text
* `GetFileInfo` Retrieves file information.
* `GetFreeSpace` Returns the number of unallocated bytes in the partition named by this abstract path name.
* `GetTempDirectory` Returns the full path to the currently assigned temporary directory
* `GetTempFile` Creates a temporary file in a directory whose name starts with (at most) the first three characters of the prefix.
* `ImageWrite` Writes an image to the specified filename or destination.

```java
// A few examples
content = fileRead( expandPath( "/config/myfile.txt" ) );
if( fileExists( "filepath.txt" ) ){

}
fileDelete( "filepath.txt" )
fileWrite( getTempFile( getTempDirectory(), "tempFile"), "My Data" );

directoryList( "/my/path" )
directoryExists( "/my/path" )

<form method="post" enctype="multipart/form-data">
  <input type="file" name="fileInput">
  <button type="submit">Upload</button>
</form>

<cfscript>
  if( structKeyExists( form, "fileInput" )) {
    try {
      uploadedFile = fileUpload( getTempDirectory(), "fileInput", "image/jpeg,image/pjpeg", "MakeUnique" );
      // check the file extension of the uploaded file; mime types can be spoofed
      if (not listFindNoCase("jpg,jpeg", cffile.serverFileExt)) {
      throw("The uploaded file is not of type JPG.");
      }
      // do stuff with uploadedFile...
    } catch ( e ) {
      writeOutput( "This upload form only accepts JPEG files." );
    }
    catch (any e) {
      writeOutput( "An error occurred while uploading your file: #e.message#" );
    }
  }
</cfscript>

```

## Dealing With Large Files

If you want to read or manipulate large files, we recommend leveraging our [cbStreams](https://forgebox.io/view/cbstreams) library or native Java file streaming. Below, you can find some sample usage of reading large files with cbStreams, which implements the Java Streams API.

```java
stream = streamBuilder.new().ofFile( absolutePath );
try{
    //work on the stream of lines of files and close it in the finally block
} finally{
    stream.close();
}

//You can even process file lines concurrently
stream = streamBuilder.new()
    .parallel()
    .ofFile( absolutePath );
```

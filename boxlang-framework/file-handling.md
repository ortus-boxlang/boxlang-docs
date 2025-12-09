---
description: Comprehensive file and directory operations using BoxLang's NIO-powered file system API
icon: cabinet-filing
---

# File Handling

BoxLang provides a powerful and intuitive API for file and directory operations, built on Java's modern NIO (New I/O) packages for optimal performance and reliability. Whether you need to read configuration files, process large datasets, manage directory structures, or handle file uploads, BoxLang offers both **function-based** (BIFs) and **component-based** approaches to suit your coding style.

{% hint style="info" %}
**Dual Approach**: BoxLang offers two ways to work with files:

- **Functional Approach** - Using global functions: `fileRead()`, `directoryList()`
- **Declarative Approach** - Using components in script or template:
  - Script: `bx:file action="read";`
  - Template: `<bx:file action="read">`

Both approaches provide the same functionality - choose based on your preference!
{% endhint %}

## 🚀 Core Features

- **NIO-Powered** - Built on Java's `java.nio.file` for modern, high-performance I/O
- **Closure/Lambda Support** - Filter and transform with functional programming
- **Stream Processing** - Handle large files efficiently with streams
- **Cross-Platform** - Consistent behavior across Windows, Linux, and macOS
- **Path Expansion** - Automatic resolution of relative and absolute paths
- **Charset Support** - Full Unicode and encoding support

## 📋 Table of Contents

- [Core Features](#core-features)
- [File Operations](#file-operations)
- [Directory Operations](#directory-operations)
- [Dealing With Large Files](#dealing-with-large-files)
- [Best Practices](#best-practices)
- [Function Reference](#function-reference)
- [Common Use Cases](#common-use-cases)

## 📁 File Operations

BoxLang provides comprehensive file manipulation capabilities through global functions (BIFs) and the `<bx:file>` component.

{% hint style="info" %}
**Reference Documentation**:

- [File Functions Reference](../boxlang-language/reference/built-in-functions/io/)
- [File Component Reference](../boxlang-language/reference/components/io/File.md)

{% endhint %}

### Reading Files

Read entire file contents into memory:

```js
// Simple read
content = fileRead( "/path/to/config.txt" )

// With specific charset
content = fileRead( "/path/to/data.txt", "UTF-8" )

// Read binary data
binaryData = fileReadBinary( "/path/to/image.jpg" )

// Using component (script)
bx:file action="read" file="/path/to/file.txt" variable="fileContent";
```

```xml
<!-- Using component (template) -->
<bx:file action="read" file="/path/to/file.txt" variable="fileContent">
```

**Reference**: [`fileRead()`](../boxlang-language/reference/built-in-functions/io/FileRead.md)

### Writing Files

Write content to files with automatic path creation:

```js
// Simple write
fileWrite( "/path/to/output.txt", "Hello BoxLang!" )

// Write with charset
fileWrite( "/path/to/output.txt", "Hello BoxLang!", "UTF-8" )

// Write with path creation
fileWrite( "/deep/nested/path/file.txt", "data", "UTF-8", true )

// Write binary
fileWrite( "/path/to/image.jpg", binaryData )

// Using component (script)
bx:file
    action="write"
    file="/path/to/file.txt"
    output="Hello BoxLang!";
```

```xml
<!-- Using component (template) -->
<bx:file
    action="write"
    file="/path/to/file.txt"
    output="Hello BoxLang!">
```

**Reference**: [`fileWrite()`](../boxlang-language/reference/built-in-functions/io/FileWrite.md)

### Appending to Files

Add content to existing files:

```js
// Append string content
fileAppend( "/path/to/log.txt", "New log entry" )

// Using open file handle
file = fileOpen( "/path/to/log.txt", "append" )
fileAppend( file, "Entry 1" )
fileAppend( file, "Entry 2" )
fileClose( file )

// Using component (script)
bx:file
    action="append"
    file="/path/to/log.txt"
    output="Additional content";
```

```xml
<!-- Using component (template) -->
<bx:file
    action="append"
    file="/path/to/log.txt"
    output="Additional content">
```

**Reference**: [`fileAppend()`](../boxlang-language/reference/built-in-functions/io/FileAppend.md)

### File Operations

Common file management operations:

```js
// Check if file exists
if( fileExists( "/path/to/file.txt" ) ){
    // File operations
}

// Copy file
fileCopy( "/source/file.txt", "/destination/file.txt" )

// Move/Rename file
fileMove( "/old/location.txt", "/new/location.txt" )

// Delete file
fileDelete( "/path/to/file.txt" )

// Get file info
info = fileInfo( "/path/to/file.txt" )
// Returns: { name, path, size, type, dateLastModified, attributes, mode }

// Get MIME type
mimeType = fileGetMimeType( "/path/to/document.pdf" )

// Set file attributes (Unix/Linux)
fileSetAccessMode( "/path/to/script.sh", "755" )

// Set last modified time
fileSetLastModified( "/path/to/file.txt", now() )
```

**Reference**: [`fileExists()`](../boxlang-language/reference/built-in-functions/io/FileExists.md), [`fileCopy()`](../boxlang-language/reference/built-in-functions/io/FileCopy.md), [`fileMove()`](../boxlang-language/reference/built-in-functions/io/FileMove.md), [`fileDelete()`](../boxlang-language/reference/built-in-functions/io/FileDelete.md), [`fileInfo()`](../boxlang-language/reference/built-in-functions/io/FileInfo.md)

### Working with File Handles

For fine-grained control, use file handles:

```js
// Open file for reading
file = fileOpen( "/path/to/data.txt", "read" )

// Read line by line
while( !fileIsEOF( file ) ){
    line = fileReadLine( file )
    // Process line
}
fileClose( file )

// Open file for writing
file = fileOpen( "/path/to/output.txt", "write", "UTF-8" )
fileWriteLine( file, "First line" )
fileWriteLine( file, "Second line" )
fileClose( file )

// Seekable file operations
file = fileOpen( "/path/to/data.bin", "read", "UTF-8", true )
fileSeek( file, 100 ) // Jump to position 100
data = fileRead( file )
fileClose( file )
```

**Reference**: [`fileOpen()`](../boxlang-language/reference/built-in-functions/io/FileOpen.md), [`fileClose()`](../boxlang-language/reference/built-in-functions/io/FileClose.md), [`fileReadLine()`](../boxlang-language/reference/built-in-functions/io/FileReadLine.md), [`fileWriteLine()`](../boxlang-language/reference/built-in-functions/io/FileWriteLine.md), [`fileIsEOF()`](../boxlang-language/reference/built-in-functions/io/FileIsEOF.md), [`fileSeek()`](../boxlang-language/reference/built-in-functions/io/FileSeek.md)

### File Upload Handling

Handle HTTP file uploads securely in web runtimes.

{% hint style="warning" %}
**Web Runtime Only**: File upload functions (`fileUpload()`, `fileUploadAll()`) are only available in web runtimes (Servlet, MiniServer). They are not available in CLI or other runtime contexts.
{% endhint %}

```html
<form method="post" enctype="multipart/form-data">
    <input type="file" name="uploadedFile">
    <button type="submit">Upload</button>
</form>
```

```js
if( structKeyExists( form, "uploadedFile" ) ){
    try {
        // Upload with MIME type validation
        result = fileUpload(
            getTempDirectory(),
            "uploadedFile",
            "image/jpeg,image/png",
            "makeUnique"
        )

        // Verify file extension (MIME types can be spoofed)
        if( !listFindNoCase( "jpg,jpeg,png", result.serverFileExt ) ){
            throw( "Invalid file type" )
        }

        // Process uploaded file
        writeOutput( "Uploaded: #result.serverFile#" )

    } catch( any e ){
        writeOutput( "Upload failed: #e.message#" )
    }
}

// Upload multiple files
results = fileUploadAll( getTempDirectory(), "image/*" )
results.each( function( uploadResult ){
    // Process each uploaded file
} )
```

**Reference**: [`fileUpload()`](../boxlang-language/reference/built-in-functions/io/FileUpload.md), [`fileUploadAll()`](../boxlang-language/reference/built-in-functions/io/FileUploadAll.md)

### Temporary Files

Create and manage temporary files:

```js
// Get system temp directory
tempDir = getTempDirectory()

// Create temporary file
tempFile = createTempFile( getTempDirectory(), "myapp" )

// Use temp file
fileWrite( tempFile, "temporary data" )

// Cleanup happens automatically or manually
fileDelete( tempFile )
```

**Reference**: [`getTempDirectory()`](../boxlang-language/reference/built-in-functions/io/GetTempDirectory.md), [`createTempFile()`](../boxlang-language/reference/built-in-functions/io/CreateTempFile.md), [`createTempDirectory()`](../boxlang-language/reference/built-in-functions/io/CreateTempDirectory.md)

## 📂 Directory Operations

Manage directory structures with powerful listing, filtering, and manipulation capabilities.

{% hint style="info" %}
**Reference Documentation**:

- [Directory Functions Reference](../boxlang-language/reference/built-in-functions/io/)
- [Directory Component Reference](../boxlang-language/reference/components/io/Directory.md)

{% endhint %}

### Basic Directory Management

```js
// Check if directory exists
if( directoryExists( "/path/to/dir" ) ){
    // Directory operations
}

// Create directory
directoryCreate( "/path/to/new/directory" )

// Create nested directories
directoryCreate( "/deep/nested/path", true ) // createPath=true

// Copy directory
directoryCopy( "/source/dir", "/destination/dir" )

// Copy recursively
directoryCopy( "/source/dir", "/destination/dir", true )

// Move/Rename directory
directoryMove( "/old/path", "/new/path" )

// Delete directory
directoryDelete( "/path/to/dir" )

// Delete recursively
directoryDelete( "/path/to/dir", true )

// Using component (script)
bx:directory action="create" directory="/path/to/new/dir";
bx:directory action="delete" directory="/path/to/dir" recurse="true";
```

```xml
<!-- Using component (template) -->
<bx:directory action="create" directory="/path/to/new/dir">
<bx:directory action="delete" directory="/path/to/dir" recurse="true">
```

**Reference**: [`directoryExists()`](../boxlang-language/reference/built-in-functions/io/DirectoryExists.md), [`directoryCreate()`](../boxlang-language/reference/built-in-functions/io/DirectoryCreate.md), [`directoryCopy()`](../boxlang-language/reference/built-in-functions/io/DirectoryCopy.md), [`directoryMove()`](../boxlang-language/reference/built-in-functions/io/DirectoryMove.md), [`directoryDelete()`](../boxlang-language/reference/built-in-functions/io/DirectoryDelete.md)

### Listing Directory Contents

BoxLang provides flexible directory listing with multiple return formats:

```js
// Simple list - returns array of absolute paths
files = directoryList( "/path/to/dir" )

// List names only
names = directoryList(
    path = "/path/to/dir",
    listInfo = "name"
)

// List as query with full details
query = directoryList(
    path = "/path/to/dir",
    listInfo = "query"
)
// Query columns: name, size, type, dateLastModified, attributes, mode, directory

// Recursive listing
allFiles = directoryList(
    path = "/path/to/dir",
    recurse = true
)

// Filter by type
filesOnly = directoryList(
    path = "/path/to/dir",
    type = "file"
)

dirsOnly = directoryList(
    path = "/path/to/dir",
    type = "dir"
)

// Sort results
sorted = directoryList(
    path = "/path/to/dir",
    sort = "name asc"
)

// Available sort columns: name, size, date, type
// Sort directions: asc, desc
```

**Reference**: [`directoryList()`](../boxlang-language/reference/built-in-functions/io/DirectoryList.md)

### Filtering with Closures/Lambdas

Use functional programming for powerful filtering:

```js
// Filter with lambda - only .txt files
textFiles = directoryList(
    path = "/documents",
    filter = ( path ) => path.endsWith( ".txt" )
)

// Filter with closure - files modified today
todayFiles = directoryList(
    path = "/uploads",
    listInfo = "query",
    filter = ( path ) => {
        info = fileInfo( path )
        return info.dateLastModified.dateCompare( now(), "d" ) == 0
    }
)

// Filter by size - files larger than 1MB
largeFiles = directoryList(
    path = "/data",
    listInfo = "query",
    filter = ( path ) => {
        info = fileInfo( path )
        return info.size > 1048576
    }
)

// Complex filtering - specific file patterns
configFiles = directoryList(
    path = "/config",
    recurse = true,
    filter = ( path ) => {
        fileName = getFileFromPath( path )
        return fileName.startsWith( "app-" ) && fileName.endsWith( ".json" )
    }
)
```

### Glob Pattern Filtering

Use glob patterns for simple filtering:

```js
// Single pattern
txtFiles = directoryList(
    path = "/documents",
    filter = "*.txt"
)

// Multiple patterns with pipe separator
mediaFiles = directoryList(
    path = "/media",
    filter = "*.jpg|*.png|*.gif"
)

// Pattern matching
configFiles = directoryList(
    path = "/config",
    filter = "app-*.json"
)
```

### Advanced Directory Queries

```js
// Get detailed directory information
query = directoryList(
    path = "/projects",
    recurse = true,
    listInfo = "query",
    type = "file",
    sort = "size desc"
)

// Process query results
query.each( function( row ){
    println( "File: #row.name# - Size: #row.size# bytes" )
} )

// Filter query results
largeFiles = query.filter( function( row ){
    return row.size > 1000000 // Files > 1MB
} )

// Sum total size
totalSize = query.reduce( function( sum, row ){
    return sum + row.size
}, 0 )
```

### Path Utilities

Work with file system paths:

```js
// Expand relative paths to absolute
absolutePath = expandPath( "../config/settings.json" )

// Get canonical path (resolves symbolic links)
canonicalPath = getCanonicalPath( "/path/with/symlinks" )

// Contract absolute path to relative
relativePath = contractPath( "/full/path/to/file.txt" )

// Extract directory from full path
directory = getDirectoryFromPath( "/path/to/file.txt" )
// Returns: /path/to/

// Check free space on partition
freeBytes = getFreeSpace( "/data/partition" )
```

**Reference**: [`expandPath()`](../boxlang-language/reference/built-in-functions/io/ExpandPath.md), [`getCanonicalPath()`](../boxlang-language/reference/built-in-functions/io/GetCanonicalPath.md), [`contractPath()`](../boxlang-language/reference/built-in-functions/io/ContractPath.md), [`getDirectoryFromPath()`](../boxlang-language/reference/built-in-functions/io/GetDirectoryFromPath.md)

## 🌊 Dealing With Large Files

When working with large files, loading entire contents into memory can cause performance issues. BoxLang leverages Java NIO streams for efficient processing of large files. Through BoxLang's 100% Java interoperability, you can directly use Java's powerful Stream API for advanced file processing.

{% hint style="info" %}
**Java Interoperability**: BoxLang provides seamless integration with Java classes. Simply import the Java classes you need with `import java:fully.qualified.ClassName` and use them directly in your BoxLang code.
{% endhint %}

### Stream-Based File Reading

Process files line-by-line without loading everything into memory:

```js
// Open file for line-by-line reading
file = fileOpen( "/path/to/large-file.log", "read" )

try {
    while( !fileIsEOF( file ) ){
        line = fileReadLine( file )

        // Process each line
        if( line.contains( "ERROR" ) ){
            // Handle error line
            writeLog( line )
        }
    }
} finally {
    fileClose( file )
}
```

### Using Java Streams for Advanced Processing

BoxLang's Java interoperability allows you to use Java NIO Streams directly for powerful file processing:

```js
// Import Java classes
import java:java.nio.file.Files;
import java:java.nio.file.Paths;
import java:java.util.stream.Collectors;

// Process large file with Java Streams
path = Paths.get( "/path/to/large-data.csv" )
stream = Files.lines( path )

try {
    // Filter and transform lines using Java Streams
    results = stream
        .filter( ( line ) => line.contains( "active" ) )
        .map( ( line ) => listToArray( line ) )
        .collect( Collectors.toList() )

} finally {
    stream.close()
}
```

### Parallel File Processing

Process large files using multiple threads with parallel streams:

```js
import java:java.nio.file.Files;
import java:java.nio.file.Paths;

// Parallel stream processing
path = Paths.get( "/path/to/huge-file.log" )
stream = Files.lines( path ).parallel()

try {
    // Process lines in parallel
    errorCount = stream
        .filter( ( line ) => line.contains( "ERROR" ) )
        .count()

    println( "Found #errorCount# errors" )

} finally {
    stream.close()
}
```

### Chunked Reading

Read files in chunks for controlled memory usage:

```js
// Read file in chunks
file = fileOpen( "/path/to/binary-data.bin", "read" )
chunkSize = 8192 // 8KB chunks

try {
    while( !fileIsEOF( file ) ){
        chunk = fileRead( file, chunkSize )
        // Process chunk
        processChunk( chunk )
    }
} finally {
    fileClose( file )
}
```

### Processing Large CSV Files

Efficient CSV processing without loading entire file:

```js
file = fileOpen( "/path/to/large-dataset.csv", "read" )
lineNumber = 0

try {
    // Skip header
    header = fileReadLine( file )

    // Process data rows
    while( !fileIsEOF( file ) ){
        lineNumber++
        line = fileReadLine( file )

        // Parse CSV line
        data = listToArray( line )

        // Process record
        processRecord( data )

        // Progress indicator every 1000 rows
        if( lineNumber % 1000 == 0 ){
            println( "Processed #lineNumber# rows" )
        }
    }
} finally {
    fileClose( file )
}
```

**Alternative using Java Streams**:

```js
import java:java.nio.file.Files;
import java:java.nio.file.Paths;

path = Paths.get( "/path/to/large-dataset.csv" )
stream = Files.lines( path ).skip( 1 ) // Skip header

try {
    stream.forEach( ( line ) => {
        data = listToArray( line )
        processRecord( data )
    } )
} finally {
    stream.close()
}
```

### Streaming Log File Analysis

Analyze large log files efficiently using Java Streams:

```js
import java:java.nio.file.Files;
import java:java.nio.file.Paths;
import java:java.util.stream.Collectors;
import java:java.util.function.Function;

// Analyze log patterns without loading entire file
path = Paths.get( "/var/log/application.log" )
stream = Files.lines( path )

try {
    // Group errors by type
    errorCounts = stream
        .filter( ( line ) => line.contains( "[ERROR]" ) )
        .map( ( line ) => {
            // Extract error type
            matches = line.reMatch( "(?<=\[ERROR\]\s)[^:]*" )
            return matches.len() > 0 ? matches[ 1 ] : "Unknown"
        } )
        .collect(
            Collectors.groupingBy(
                Function.identity(),
                Collectors.counting()
            )
        )

    // Display results
    errorCounts.forEach( ( type, count ) => {
        println( "#type#: #count# occurrences" )
    } )

} finally {
    stream.close()
}
### Memory-Efficient File Copying

Copy large files with controlled buffer size:

```js
// Copy large file with custom buffer
source = fileOpen( "/source/large-file.dat", "read" )
destination = fileOpen( "/destination/large-file.dat", "write" )

try {
    bufferSize = 65536 // 64KB buffer

    while( !fileIsEOF( source ) ){
        chunk = fileRead( source, bufferSize )
        fileWrite( destination, chunk )
    }

} finally {
    fileClose( source )
    fileClose( destination )
}
```

{% hint style="success" %}
**Performance Tip**: For files larger than 100MB, always use stream-based processing or chunked reading to avoid memory issues. BoxLang's Java interoperability gives you direct access to Java NIO Streams for powerful functional operations while maintaining low memory footprint.
{% endhint %}

## 🔐 Best Practices

### Security Considerations

```js
// Validate file paths to prevent directory traversal
function sanitizePath( userPath ){
    // Remove potentially dangerous patterns
    safePath = userPath
        .replace( "..", "" )
        .replace( "~", "" )

    // Ensure path is within allowed directory
    basePath = expandPath( "/uploads" )
    fullPath = expandPath( safePath )

    if( !fullPath.startsWith( basePath ) ){
        throw( "Invalid file path" )
    }

    return fullPath
}

// Validate uploaded files
if( structKeyExists( form, "upload" ) ){
    result = fileUpload( getTempDirectory(), "upload" )

    // Check file extension
    allowedExtensions = "jpg,png,gif,pdf"
    if( !listFindNoCase( allowedExtensions, result.serverFileExt ) ){
        fileDelete( result.serverDirectory & result.serverFile )
        throw( "File type not allowed" )
    }

    // Check file size
    maxSize = 5 * 1024 * 1024 // 5MB
    if( result.fileSize > maxSize ){
        fileDelete( result.serverDirectory & result.serverFile )
        throw( "File too large" )
    }
}
```

### Error Handling

```js
// Robust file operations with error handling
try {
    if( !fileExists( configPath ) ){
        throw(
            type = "FileNotFound",
            message = "Configuration file not found: #configPath#"
        )
    }

    content = fileRead( configPath )
    config = deserializeJSON( content )

} catch( "FileNotFound" e ){
    // Create default config
    config = getDefaultConfig()
    fileWrite( configPath, serializeJSON( config ) )

} catch( any e ){
    // Log error and use fallback
    writeLog(
        type = "error",
        text = "Config load failed: #e.message#"
    )
    config = getDefaultConfig()
}
```

### Resource Management

```js
// Always close file handles
file = fileOpen( "/path/to/file.txt", "write" )
try {
    fileWrite( file, "data" )
} finally {
    // Ensures file is closed even if error occurs
    fileClose( file )
}

// Use try-finally for cleanup
tempFile = createTempFile( getTempDirectory(), "process" )
try {
    // Process with temp file
    fileWrite( tempFile, processData() )
    result = analyzeFile( tempFile )
} finally {
    // Always cleanup temp files
    if( fileExists( tempFile ) ){
        fileDelete( tempFile )
    }
}
```

### Cross-Platform Paths

```js
// Use forward slashes - BoxLang handles conversion
goodPath = "/path/to/file.txt"  // ✓ Works everywhere
badPath = "\path\to\file.txt"   // ✗ Windows-specific

// Let BoxLang expand paths
relativePath = "../config/app.json"
absolutePath = expandPath( relativePath )

// Use path functions for manipulation
directory = getDirectoryFromPath( absolutePath )
fileName = getFileFromPath( absolutePath )
```

## 📚 Function Reference

### File Functions

| Function | Purpose |
|----------|---------|
| `fileRead()` | Read entire file contents |
| `fileReadBinary()` | Read file as binary data |
| `fileWrite()` | Write content to file |
| `fileAppend()` | Append content to file |
| `fileOpen()` | Open file handle |
| `fileClose()` | Close file handle |
| `fileReadLine()` | Read single line |
| `fileWriteLine()` | Write single line |
| `fileCopy()` | Copy file |
| `fileMove()` | Move/rename file |
| `fileDelete()` | Delete file |
| `fileExists()` | Check file existence |
| `fileInfo()` | Get file metadata |
| `fileIsEOF()` | Check end of file |
| `fileSeek()` | Set file pointer position |
| `fileGetMimeType()` | Get file MIME type |
| `fileSetAccessMode()` | Set Unix file permissions |
| `fileSetAttribute()` | Set file attributes |
| `fileSetLastModified()` | Set modification time |
| `fileUpload()` | Handle file upload |
| `fileUploadAll()` | Handle multiple uploads |
| `createTempFile()` | Create temporary file |

### Directory Functions

| Function | Purpose |
|----------|---------|
| `directoryList()` | List directory contents |
| `directoryCreate()` | Create directory |
| `directoryDelete()` | Delete directory |
| `directoryCopy()` | Copy directory |
| `directoryMove()` | Move/rename directory |
| `directoryExists()` | Check directory existence |

### Path Functions

| Function | Purpose |
|----------|---------|
| `expandPath()` | Convert relative to absolute path |
| `contractPath()` | Convert absolute to relative path |
| `getCanonicalPath()` | Resolve symbolic links |
| `getDirectoryFromPath()` | Extract directory from path |
| `getTempDirectory()` | Get system temp directory |
| `createTempDirectory()` | Create temporary directory |
| `getFreeSpace()` | Get partition free space |

{% hint style="info" %}
**Full Reference**: Complete documentation for all file and directory functions is available at:
[BoxLang I/O Functions Reference](https://boxlang.ortusbooks.com/boxlang-language/reference/built-in-functions/io)
{% endhint %}

## 🎯 Common Use Cases

### Reading Configuration Files

```js
// Load JSON config
function loadConfig( configPath ){
    if( !fileExists( configPath ) ){
        return {}
    }

    content = fileRead( configPath )
    return deserializeJSON( content )
}

config = loadConfig( expandPath( "./config/app.json" ) )
```

### Writing Log Files

```js
// Append to daily log file
function writeLog( message ){
    logDir = expandPath( "./logs" )

    if( !directoryExists( logDir ) ){
        directoryCreate( logDir )
    }

    logFile = logDir & "/" & dateFormat( now(), "yyyy-mm-dd" ) & ".log"
    timestamp = dateTimeFormat( now(), "yyyy-mm-dd HH:nn:ss" )
    logEntry = "[#timestamp#] #message#" & chr( 10 )

    fileAppend( logFile, logEntry )
}

writeLog( "Application started" )
```

### Batch File Processing

```js
// Process all JSON files in directory
files = directoryList(
    path = "/data/input",
    filter = "*.json"
)

results = []

files.each( function( filePath ){
    try {
        data = deserializeJSON( fileRead( filePath ) )
        processed = processData( data )
        results.append( processed )
    } catch( any e ){
        writeLog( "Error processing #filePath#: #e.message#" )
    }
} )
```

### Creating Directory Archives

```js
// Collect files for archiving
filesToArchive = directoryList(
    path = "/documents",
    recurse = true,
    filter = ( path ) => {
        info = fileInfo( path )
        // Files older than 30 days
        return info.dateLastModified.dateAdd( "d", 30 ) < now()
    }
)

// Process files
filesToArchive.each( function( file ){
    // Move to archive
    archivePath = "/archive" & file.replace( "/documents", "" )
    directory = getDirectoryFromPath( archivePath )

    if( !directoryExists( directory ) ){
        directoryCreate( directory, true )
    }

    fileMove( file, archivePath )
} )

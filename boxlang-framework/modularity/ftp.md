---
description: >-
  The FTP module allows you perform various operations against an FTP or SFTP
  server.
icon: globe
---

# ⚡︎ BoxLang FTP Module

> 📁 A comprehensive FTP client module for BoxLang that brings seamless file transfer capabilities to your applications!

This module provides powerful FTP client functionality to the [BoxLang](https://boxlang.io) language, making it easy to connect to FTP servers, transfer files, and manage remote directories with minimal code.

## ✨ Features

- 🌐 **FTP/FTPS Support**: Connect to standard FTP and secure FTP servers
- 📁 **Complete File Operations**: Upload, download, rename, and delete files
- 📂 **Directory Management**: Create, remove, list, and navigate directories
- 🔐 **Secure Connections**: Support for passive and active modes
- 🎯 **Connection Pooling**: Named connections tracked globally via FTPService
- 🔄 **Proxy Support**: Connect through proxy servers with custom ports
- 📊 **Flexible Results**: Query or array return types for directory listings
- ⚡ **Event-Driven**: Interception points for logging, monitoring, and custom logic
- 🛠️ **Production Ready**: Built by Ortus Solutions with enterprise-grade quality
- 🔧 **Zero Configuration**: Sensible defaults get you started quickly

## 📦 Installation

### Requirements

- **BoxLang**: 1.0.0+
- **Java**: JDK 21+

### Install via CommandBox

```bash
box install bx-ftp
```

The module will automatically register and be available as `bx:ftp` or `<bx:ftp>` in your BoxLang script and template applications.

### From Source

```bash
# Clone the repository
git clone https://github.com/ortus-boxlang/bx-ftp.git
cd bx-ftp

# Build the module
./gradlew build

# The built module will be in build/distributions/
```

## 🚀 Quick Start

Here's how to connect to an FTP server and upload a file in just a few lines:

```java
// Connect to FTP server
bx:ftp
    action="open"
    connection="myFTP"
    server="ftp.example.com"
    username="myuser"
    password="mypass";

// Upload a file
bx:ftp
    action="putfile"
    connection="myFTP"
    localFile="/path/to/local/file.txt"
    remoteFile="/remote/file.txt";

// Close connection
bx:ftp action="close" connection="myFTP";
```

That's it! 🎉 You now have a fully functional FTP client.

## 💡 Usage Examples

### Basic Examples

#### 📁 Connect and List Files

```java
// Open connection
bx:ftp
    action="open"
    connection="myConn"
    server="ftp.example.com"
    username="user"
    password="pass";

// List directory contents
bx:ftp
    action="listdir"
    connection="myConn"
    directory="/"
    name="files";

// Display results
writeDump(files);

// Close connection
bx:ftp action="close" connection="myConn";
```

#### 📤 Upload a File

```java
bx:ftp action="open" connection="uploader" server="ftp.example.com" username="user" password="pass";

bx:ftp
    action="putfile"
    connection="uploader"
    localFile="/Users/documents/report.pdf"
    remoteFile="/uploads/monthly-report.pdf"
    result="uploadResult";

if (uploadResult.succeeded) {
    writeOutput("File uploaded successfully!");
} else {
    writeOutput("Upload failed: #uploadResult.statusText#");
}

bx:ftp action="close" connection="uploader";
```

#### 📥 Download a File

```java
bx:ftp action="open" connection="downloader" server="ftp.example.com" username="user" password="pass";

bx:ftp
    action="getfile"
    connection="downloader"
    remoteFile="/reports/sales-2025.csv"
    localFile="/Users/downloads/sales-2025.csv"
    failIfExists="false"
    result="downloadResult";

writeOutput("Download complete: #downloadResult.succeeded#");

bx:ftp action="close" connection="downloader";
```

### Advanced Examples

#### 🔐 Secure Connection with Passive Mode

```java
try {
    // Open secure connection
    bx:ftp
        action="open"
        connection="secureFTP"
        server="secure.ftp.example.com"
        port="990"
        username="admin"
        password="secretpass"
        secure="true"
        passive="true"
        timeout="60"
        result="ftpResult";

    if (ftpResult.succeeded) {
        writeOutput("Connected to secure FTP server");

        // Perform operations...

    } else {
        throw("Connection failed: #ftpResult.statusText#");
    }
} catch (any e) {
    writeOutput("FTP Error: #e.message#");
} finally {
    bx:ftp action="close" connection="secureFTP";
}
```

#### 🌐 Connect Through Proxy Server

```java
// Connect via proxy with custom port
bx:ftp
    action="open"
    connection="proxyConn"
    server="ftp.example.com"
    username="user"
    password="pass"
    proxyServer="proxy.company.com:8080";

// Connect via proxy with default port (1080)
bx:ftp
    action="open"
    connection="proxyConn"
    server="ftp.example.com"
    username="user"
    password="pass"
    proxyServer="proxy.company.com";
```

#### 📂 Directory Management

```java
bx:ftp action="open" connection="dirManager" server="ftp.example.com" username="user" password="pass";

// Create a new directory
bx:ftp
    action="createdir"
    connection="dirManager"
    new="/uploads/2025"
    result="createResult";

// Check if directory exists
bx:ftp
    action="existsdir"
    connection="dirManager"
    directory="/uploads/2025"
    result="existsResult";

writeOutput("Directory exists: #existsResult.returnValue#");

// Change to directory
bx:ftp
    action="changedir"
    connection="dirManager"
    directory="/uploads/2025";

// Get current directory
bx:ftp
    action="getcurrentdir"
    connection="dirManager"
    result="cwdResult";

writeOutput("Current directory: #cwdResult.returnValue#");

bx:ftp action="close" connection="dirManager";
```

#### 📊 List Directory as Array

```java
bx:ftp action="open" connection="lister" server="ftp.example.com" username="user" password="pass";

// Get directory listing as array of structs
bx:ftp
    action="listdir"
    connection="lister"
    directory="/uploads"
    name="fileList"
    returnType="array";

// Process each file
for (file in fileList) {
    writeOutput("File: #file.name# - Size: #file.size# bytes - Type: #file.type#<br>");

    if (file.isDirectory) {
        writeOutput("  → This is a directory<br>");
    } else {
        writeOutput("  → Last modified: #file.lastModified#<br>");
    }
}

bx:ftp action="close" connection="lister";
```

#### 🔄 Bulk File Transfer

```java
bx:ftp action="open" connection="bulk" server="ftp.example.com" username="user" password="pass";

files = ["report1.pdf", "report2.pdf", "report3.pdf"];
successCount = 0;
failCount = 0;

for (fileName in files) {
    bx:ftp
        action="putfile"
        connection="bulk"
        localFile="/local/reports/#fileName#"
        remoteFile="/remote/reports/#fileName#"
        result="uploadResult";

    if (uploadResult.succeeded) {
        successCount++;
        writeOutput("✓ Uploaded: #fileName#<br>");
    } else {
        failCount++;
        writeOutput("✗ Failed: #fileName# - #uploadResult.statusText#<br>");
    }
}

writeOutput("<br>Summary: #successCount# successful, #failCount# failed");

bx:ftp action="close" connection="bulk";
```

#### 🏷️ Rename Files and Directories

```java
bx:ftp action="open" connection="renamer" server="ftp.example.com" username="user" password="pass";

// Rename a file
bx:ftp
    action="renamefile"
    connection="renamer"
    existing="/uploads/temp.txt"
    new="/uploads/final-report.txt"
    result="renameResult";

if (renameResult.returnValue) {
    writeOutput("File renamed successfully");
}

// Rename a directory
bx:ftp
    action="renamedir"
    connection="renamer"
    existing="/old-folder"
    new="/new-folder"
    result="dirRenameResult";

bx:ftp action="close" connection="renamer";
```

## 📚 Available Actions

All actions can use a `result` attribute to store the result of the action in a variable. If not provided, the result will be stored in a variable called `bxftp` (or `cftp` if you are in CFML compat mode).

### 🔌 Connection Actions

#### `open` - Connect to FTP Server

Opens a connection to an FTP server and tracks it in the FTPService.

**Attributes:**

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `connection` | string | ✅ Yes | - | Name of the connection to track |
| `server` | string | ✅ Yes | - | Server IP or hostname |
| `port` | numeric | No | 21 | FTP port number |
| `username` | string | ✅ Yes | - | Authentication username |
| `password` | string | ✅ Yes | - | Authentication password |
| `timeout` | numeric | No | 30 | Connection timeout in seconds |
| `secure` | boolean | No | false | Use secure FTP (FTPS) |
| `passive` | boolean | No | true | Use passive mode |
| `proxyServer` | string | No | - | Proxy server (hostname:port) |

**Examples:**

```java
// Basic connection
bx:ftp
    action="open"
    connection="myConn"
    server="ftp.example.com"
    username="user"
    password="pass";

// Secure connection with custom port
bx:ftp
    action="open"
    connection="secureConn"
    server="secure.ftp.example.com"
    port="990"
    username="admin"
    password="pass"
    secure="true"
    timeout="60";

// Connection via proxy
bx:ftp
    action="open"
    connection="proxyConn"
    server="ftp.example.com"
    username="user"
    password="pass"
    proxyServer="proxy.company.com:8080";
```

#### `close` - Close FTP Connection

Closes an open FTP connection and removes it from the FTPService.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Name of the connection to close |

**Example:**

```java
bx:ftp action="close" connection="myConn";
```

### 📂 Directory Actions

#### `changedir` - Change Working Directory

Changes the current working directory on the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `directory` | string | ✅ Yes | Directory path to change to |

**Example:**

```java
bx:ftp action="changedir" connection="myConn" directory="/uploads/2025";
```

#### `createdir` - Create Directory

Creates a new directory on the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `new` | string | ✅ Yes | Path of directory to create |

**Example:**

```java
bx:ftp action="createdir" connection="myConn" new="/uploads/reports" result="createResult";

if (createResult.returnValue) {
    writeOutput("Directory created successfully");
}
```

#### `existsdir` - Check Directory Existence

Checks if a directory exists on the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `directory` | string | ✅ Yes | Directory path to check |

**Example:**

```java
bx:ftp action="existsdir" connection="myConn" directory="/uploads" result="existsResult";

if (existsResult.returnValue) {
    writeOutput("Directory exists");
} else {
    writeOutput("Directory not found");
}
```

#### `getcurrentdir` - Get Working Directory

Retrieves the current working directory path.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |

**Example:**

```java
bx:ftp action="getcurrentdir" connection="myConn" result="cwdResult";
writeOutput("Current directory: #cwdResult.returnValue#");
```

#### `listdir` - List Directory Contents

Lists files and directories in the specified directory.

**Attributes:**

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `connection` | string | ✅ Yes | - | Connection name |
| `directory` | string | ✅ Yes | - | Directory to list |
| `name` | string | ✅ Yes | - | Variable name to store results |
| `returnType` | string | No | "query" | Return format: "query" or "array" |

**Query Columns:**

- `name` - File/directory name
- `isDirectory` - Boolean indicating if item is a directory
- `lastModified` - Last modification timestamp
- `size` - File size in bytes (aliased as `length` for CFML compatibility)
- `mode` - File permissions mode
- `path` - File path without drive designation
- `url` - Complete URL for the item
- `type` - Type: "file", "directory", "symbolic link", or "unknown"
- `raw` - Raw FTP listing representation
- `attributes` - File attributes
- `isReadable` - Boolean for read permission
- `isWritable` - Boolean for write permission
- `isExecutable` - Boolean for execute permission

**Examples:**

```java
// List as query (default)
bx:ftp action="listdir" connection="myConn" directory="/" name="files";

// List as array of structs
bx:ftp action="listdir" connection="myConn" directory="/" name="files" returnType="array";

// Process results
for (file in files) {
    writeOutput("#file.name# - #file.size# bytes<br>");
}
```

#### `removedir` - Remove Directory

Removes a directory from the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `directory` | string | ✅ Yes | Directory path to remove |

**Example:**

```java
bx:ftp action="removedir" connection="myConn" directory="/temp/old-data" result="removeResult";

if (removeResult.returnValue) {
    writeOutput("Directory removed successfully");
}
```

#### `renamedir` - Rename Directory

Renames a directory on the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `existing` | string | ✅ Yes | Current directory path |
| `new` | string | ✅ Yes | New directory path |

**Example:**

```java
bx:ftp
    action="renamedir"
    connection="myConn"
    existing="/old-name"
    new="/new-name"
    result="renameResult";
```

### 📄 File Actions

#### `existsfile` - Check File Existence

Checks if a file exists on the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `remoteFile` | string | ✅ Yes | Remote file path to check |

**Example:**

```java
bx:ftp action="existsfile" connection="myConn" remoteFile="/data/report.pdf" result="existsResult";

if (existsResult.returnValue) {
    writeOutput("File exists");
}
```

#### `getfile` - Download File

Downloads a file from the FTP server to the local filesystem.

**Attributes:**

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `connection` | string | ✅ Yes | - | Connection name |
| `remoteFile` | string | ✅ Yes | - | Remote file path to download |
| `localFile` | string | ✅ Yes | - | Local file path to save to |
| `failIfExists` | boolean | No | true | Fail if local file already exists |

**Example:**

```java
// Download with overwrite protection
bx:ftp
    action="getfile"
    connection="myConn"
    remoteFile="/reports/sales.csv"
    localFile="/Users/downloads/sales.csv";

// Download and overwrite if exists
bx:ftp
    action="getfile"
    connection="myConn"
    remoteFile="/reports/sales.csv"
    localFile="/Users/downloads/sales.csv"
    failIfExists="false"
    result="downloadResult";

if (downloadResult.succeeded) {
    writeOutput("Download complete");
}
```

#### `putfile` - Upload File

Uploads a file from the local filesystem to the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `localFile` | string | ✅ Yes | Local file path to upload |
| `remoteFile` | string | ✅ Yes | Remote file path destination |

**Example:**

```java
bx:ftp
    action="putfile"
    connection="myConn"
    localFile="/Users/documents/report.pdf"
    remoteFile="/uploads/report.pdf"
    result="uploadResult";

if (uploadResult.succeeded) {
    writeOutput("Upload successful: #uploadResult.statusText#");
}
```

#### `removefile` (or `remove`) - Delete File

Deletes a file from the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `remoteFile` | string | ✅ Yes | Remote file path to delete |

**Example:**

```java
bx:ftp action="removefile" connection="myConn" remoteFile="/temp/old-file.txt" result="removeResult";

if (removeResult.returnValue) {
    writeOutput("File deleted successfully");
}
```

#### `renamefile` - Rename File

Renames a file on the FTP server.

**Attributes:**

| Attribute | Type | Required | Description |
|-----------|------|----------|-------------|
| `connection` | string | ✅ Yes | Connection name |
| `existing` | string | ✅ Yes | Current file path |
| `new` | string | ✅ Yes | New file path |

**Example:**

```java
bx:ftp
    action="renamefile"
    connection="myConn"
    existing="/uploads/temp.txt"
    new="/uploads/final-report.txt"
    result="renameResult";

if (renameResult.returnValue) {
    writeOutput("File renamed successfully");
}
```

## 📊 Result Object

All FTP actions return a result object with the following structure:

```java
{
    statusCode : 200,              // Numeric FTP status code
    statusText : "Success",        // Human-readable status message
    errorCode : 0,                 // Error code (if any)
    errorText : "",                // Error message (if any)
    returnValue : true,            // Action-specific return value
    succeeded : true               // Boolean indicating success/failure
}
```

### Common Status Codes

| Code | Meaning | Description |
|------|---------|-------------|
| 200 | Success | Command successful |
| 221 | Goodbye | Service closing control connection |
| 226 | Transfer complete | Closing data connection, file transfer successful |
| 230 | Login successful | User logged in |
| 250 | Success | Requested file action okay, completed |
| 550 | Failed | File unavailable or permission denied |
| 552 | Exceeded | Storage allocation exceeded |
| 553 | Not allowed | File name not allowed |

### Using Result Variables

```java
// Store result in custom variable
bx:ftp action="putfile" connection="myConn" localFile="test.txt" remoteFile="/test.txt" result="uploadResult";

if (uploadResult.succeeded) {
    writeOutput("Success! Status: #uploadResult.statusCode#");
} else {
    writeOutput("Failed: #uploadResult.errorText#");
}

// Default result variable (bxftp)
bx:ftp action="putfile" connection="myConn" localFile="test.txt" remoteFile="/test.txt";

if (bxftp.succeeded) {
    writeOutput("Upload successful");
}
```

## 🎯 Interception Points

The FTP module announces several interception points that allow you to hook into the FTP operation lifecycle for logging, monitoring, metrics, or custom logic.

### `beforeFTPCall`

Announced before any FTP action is executed.

**Interceptor Data:**

```java
{
    connection : FTPConnection,    // The FTP connection object
    action : "putfile",           // The action being performed
    result : FTPResult,           // The result object (empty at this point)
    attributes : {                // All attributes passed to the component
        connection : "myConn",
        localFile : "/path/to/file.txt",
        remoteFile : "/remote/file.txt"
        // ... other attributes
    }
}
```

**Use Cases:**

- Pre-flight validation
- Logging all FTP operations
- Performance monitoring (start timer)
- Security auditing

**Example:**

```java
class {
    function beforeFTPCall( event, interceptData ) {
        var logger = getLogger();
        logger.info(
            "FTP Action Starting: #interceptData.action# on connection #interceptData.attributes.connection#"
        );

        // Store start time for performance tracking
        interceptData.startTime = now();
    }
}
```

### `afterFTPCall`

Announced after an FTP action completes successfully.

**Interceptor Data:**

```java
{
    connection : FTPConnection,    // The FTP connection object
    action : "putfile",           // The action that was performed
    result : FTPResult,           // The populated result object
    attributes : {                // All attributes passed to the component
        connection : "myConn",
        localFile : "/path/to/file.txt",
        remoteFile : "/remote/file.txt"
    }
}
```

**Use Cases:**

- Success logging
- Performance metrics (calculate duration)
- Notifications or alerts
- Analytics and reporting

**Example:**

```java
class {
    function afterFTPCall( event, interceptData ) {
        var logger = getLogger();
        var result = interceptData.result;

        logger.info(
            "FTP Action Completed: #interceptData.action# - Status: #result.statusCode# - Success: #result.succeeded#"
        );

        // Track successful transfers
        if ( result.succeeded && interceptData.action == "putfile" ) {
            metrics.recordUpload( interceptData.attributes.remoteFile );
        }
    }
}
```

### `onFTPConnectionOpen`

Announced when a new FTP connection is opened.

**Interceptor Data:**

```java
{
    connection : FTPConnection,    // The newly opened connection
    attributes : {                // Connection attributes
        server : "ftp.example.com",
        username : "user",
        port : 21,
        passive : true
        // ... other connection attributes
    }
}
```

**Use Cases:**

- Connection logging
- Connection pooling metrics
- Security monitoring
- Access auditing

**Example:**

```java
class {
    function onFTPConnectionOpen( event, interceptData ) {
        var logger = getLogger();
        var attrs = interceptData.attributes;

        logger.info(
            "FTP Connection Opened: #attrs.server#:#attrs.port# as #attrs.username# (Passive: #attrs.passive#)"
        );

        // Track active connections
        connectionMonitor.recordConnection(
            server = attrs.server,
            user = attrs.username,
            timestamp = now()
        );
    }
}
```

### `onFTPConnectionClose`

Announced when an FTP connection is closed.

**Interceptor Data:**

```java
{
    connection : FTPConnection    // The connection being closed
}
```

**Use Cases:**

- Connection cleanup logging
- Session duration tracking
- Connection pool management
- Resource monitoring

**Example:**

```java
component {
    function onFTPConnectionClose( event, interceptData ) {
        var logger = getLogger();
        var conn = interceptData.connection;

        logger.info(
            "FTP Connection Closed: #conn.getName()# - Status: #conn.getStatus()#"
        );

        // Track connection closures
        connectionMonitor.recordClosure(
            connection = conn.getName(),
            timestamp = now()
        );
    }
}
```

### `onFTPError`

Announced when an FTP operation encounters an error.

**Interceptor Data:**

```java
{
    connection : FTPConnection,    // The FTP connection object
    action : "putfile",           // The action that failed
    error : IOException,          // The exception object
    attributes : {                // All attributes passed to the component
        connection : "myConn",
        localFile : "/path/to/file.txt",
        remoteFile : "/remote/file.txt"
    }
}
```

**Use Cases:**

- Error logging and alerting
- Retry logic
- Fallback mechanisms
- Error analytics

**Example:**

```java
component {
    function onFTPError( event, interceptData ) {
        var logger = getLogger();
        var error = interceptData.error;

        logger.error(
            "FTP Action Failed: #interceptData.action# - Error: #error.getMessage()#",
            error
        );

        // Send alert for critical errors
        if ( interceptData.action == "putfile" ) {
            alertService.send(
                message = "FTP upload failed: #error.getMessage()#",
                severity = "high",
                details = interceptData
            );
        }
    }
}
```

## 🔗 Connection Management

The FTP module uses the **FTPService** to manage **named** connections globally across your application.

### Connection Lifecycle

1. **Open**: Connection is created and tracked by name
2. **Use**: Multiple actions can use the same connection
3. **Close**: Connection is removed from tracking

### Reusing Connections

```java
// Open once
bx:ftp action="open" connection="myConn" server="ftp.example.com" username="user" password="pass";

// Use multiple times
bx:ftp action="putfile" connection="myConn" localFile="file1.txt" remoteFile="/file1.txt";
bx:ftp action="putfile" connection="myConn" localFile="file2.txt" remoteFile="/file2.txt";
bx:ftp action="listdir" connection="myConn" directory="/" name="files";

// Close when done
bx:ftp action="close" connection="myConn";
```

### Connection Best Practices

- ✅ **Always close connections** when done to free resources
- ✅ **Use descriptive names** for connections to avoid conflicts
- ✅ **Reuse connections** for multiple operations to improve performance
- ✅ **Use try/finally** to ensure connections are closed even on errors
- ❌ **Don't leave connections open** indefinitely

### Accessing Connection Information

After opening a connection, it's stored in a variable with the connection name:

```java
bx:ftp action="open" connection="info" server="ftp.example.com" username="user" password="pass";

writeDump( info );
// Outputs connection details: server, port, username, status, etc.
```

## ❌ Error Handling

### Common Connection Issues

**Connection Refused Errors:**

- Verify FTP server is running and accessible
- Check firewall settings for FTP ports (21 for control, 20 for data)
- For passive mode, ensure passive port range is accessible
- Verify credentials are correct

**Passive vs Active Mode:**

- **Passive Mode** (default): Client initiates both control and data connections
- **Active Mode**: Server initiates data connection back to client
- Use passive mode for connections through firewalls/NAT

### Error Handling Patterns

#### Try/Catch/Finally

```java
try {
    bx:ftp action="open" connection="safeConn" server="ftp.example.com" username="user" password="pass";

    bx:ftp action="putfile" connection="safeConn" localFile="file.txt" remoteFile="/file.txt" result="uploadResult";

    if (!uploadResult.succeeded) {
        throw("Upload failed: #uploadResult.statusText#");
    }

} catch (any e) {
    writeOutput("FTP Error: #e.message#<br>");
    // Log error, send alert, etc.
} finally {
    // Always close connection
    bx:ftp action="close" connection="safeConn";
}
```

#### Status Code Checking

```java
bx:ftp action="putfile" connection="conn" localFile="test.txt" remoteFile="/test.txt" result="ftpResult";

switch (ftpResult.statusCode) {
    case 226:
        writeOutput("Transfer successful");
        break;
    case 550:
        writeOutput("File not found or permission denied");
        break;
    case 552:
        writeOutput("Storage allocation exceeded");
        break;
    case 553:
        writeOutput("File name not allowed");
        break;
    default:
        writeOutput("Operation failed: #ftpResult.statusText#");
}
```

## ❓ Troubleshooting

### Connection Refused Errors

**Problem:** FTP operations fail with "Connection refused" errors.

**Solutions:**

- ✅ Verify FTP server is running: `nc -v hostname port`
- ✅ Check firewall allows FTP ports (21, 20, and passive range)
- ✅ Ensure passive mode is configured on server (for passive=true)
- ✅ Verify credentials are correct
- ✅ Test connection with FTP client (FileZilla, etc.)

### Passive Mode Failures

**Problem:** Connection succeeds but file transfers fail.

**Solutions:**

- ✅ Ensure FTP server has passive mode enabled
- ✅ Check passive port range is open in firewall
- ✅ Verify server announces correct IP for passive connections
- ✅ Try active mode instead: `passive="false"`

### File Upload Failures

**Problem:** Files fail to upload with permission errors.

**Solutions:**

- ✅ Verify user has write permissions on remote directory
- ✅ Check disk space on FTP server
- ✅ Ensure remote directory exists
- ✅ Try uploading to a different directory

### Connection Timeout

**Problem:** Connection attempts timeout.

**Solutions:**

- ✅ Increase timeout: `timeout="60"`
- ✅ Check network connectivity to FTP server
- ✅ Verify server is not blocking your IP
- ✅ Test if server is behind a firewall or proxy

### Proxy Connection Issues

**Problem:** Cannot connect through proxy server.

**Solutions:**

- ✅ Verify proxy server address and port: `proxyServer="proxy.company.com:8080"`
- ✅ Check proxy supports FTP protocol
- ✅ Ensure proxy authentication (if required) is configured
- ✅ Test proxy with other FTP clients

## 🛠️ Development & Testing

### Local Development Setup

This module includes Docker configuration for local FTP server testing:

```bash
# Start FTP test server
docker-compose up -d --build

# Run tests
./gradlew test

# Stop FTP server
docker-compose down
```

### Test Server Configuration

- **Host**: localhost
- **Control Port**: 2221
- **Data Port**: 2220
- **Passive Ports**: 10000-10010
- **Username**: test_user
- **Password**: testpass

### Building from Source

```bash
# Clone repository
git clone https://github.com/ortus-boxlang/bx-ftp.git
cd bx-ftp

# Download BoxLang dependency
./gradlew downloadBoxLang

# Build module
./gradlew build

# Run tests (requires Docker FTP server)
docker-compose up -d
./gradlew test

# Create distribution
./gradlew zipModuleStructure
```

### Module Architecture

- **FTPService**: Global singleton service managing all FTP connections
- **FTP Component**: BoxLang component (`@BoxComponent`) providing FTP operations
- **FTPConnection**: Represents an active FTP connection with state management
- **FTPResult**: Encapsulates operation results with status codes and messages
- **Dependencies**: Apache Commons Net 3.11.1 for FTP protocol implementation

### Testing with Docker

The included Docker setup provides a consistent FTP testing environment:

```bash
# Start FTP server with specific configuration
docker-compose up -d --build

# View logs
docker-compose logs -f

# Stop and remove containers
docker-compose down

# Force recreate (after vsftpd.conf changes)
docker-compose up -d --build --force-recreate
```

**Important**: The `vsftpd.conf` file includes critical passive mode configuration:

```conf
pasv_enable=YES
pasv_min_port=10000
pasv_max_port=10010
pasv_address=127.0.0.1
```

## 🔄 CFML Compatibility

This module will require the `bx-cfml-compat` module if you want it to work like Adobe ColdFusion/Lucee in your CFML applications.

### Differences from CFML

- **Result Variable**: BoxLang uses `bxftp` by default, CFML compat mode uses `cftp`
- **Component Name**: Use `bx:ftp` in BoxLang, `cftp` with compat module
- **Features**: BoxLang FTP includes modern features like event interception

### Migration from CFML

All CFML `<cfftp>` should work with no changes when using `bx-cfml-compat`. However, for native BoxLang usage, update tags as follows:

```java
// CFML
<cfftp action="open" connection="myConn" server="ftp.example.com" username="user" password="pass">

// BoxLang (with bx-cfml-compat)
<cftp action="open" connection="myConn" server="ftp.example.com" username="user" password="pass">

// BoxLang (native)
<bx:ftp action="open" connection="myConn" server="ftp.example.com" username="user" password="pass">
```

## 🤝 Contributing

We ❤️ contributions! This project is open source and welcomes your help to make it even better.

### 🐛 Found a Bug?

If you discover a bug, please:

1. **Check existing issues** at [GitHub Issues](https://github.com/ortus-boxlang/bx-ftp/issues)
2. **Create a new issue** with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - BoxLang version and environment details
   - Sample code that demonstrates the issue

### 💡 Have an Enhancement Idea?

We'd love to hear your ideas! Please:

1. Open a [Feature Request](https://github.com/ortus-boxlang/bx-ftp/issues/new)
2. Describe the feature and its use case
3. Explain how it would benefit users

### 📚 Improve Documentation

Documentation improvements are always welcome:

- Fix typos or unclear explanations
- Add more examples
- Improve code comments
- Create tutorials or guides

### 💰 Financial Support

You can support BoxLang and all Ortus Solutions open source projects:

- 🌟 [Become a Patron](https://www.patreon.com/ortussolutions)
- 💵 [One-time PayPal Donation](https://www.paypal.com/paypalme/ortussolutions)

Patrons get exclusive benefits like:

- Priority support
- Early access to new features
- FORGEBOX Pro account
- CFCasts account

### 📞 Support Channels

Need help? Don't create an issue—use our support channels:

- 💬 [Ortus Community Discourse](https://community.ortussolutions.com)
- 📱 [Box Team Slack](http://boxteam.ortussolutions.com/)
- 🏢 [Professional Support](https://www.ortussolutions.com/services/support)

### 🏆 Contributors

Thank you to all our amazing contributors! ❤️

<a href="https://github.com/ortus-boxlang/bx-ftp/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ortus-boxlang/bx-ftp" alt="Contributors"/>
</a>

Made with [contributors-img](https://contrib.rocks)

## 🔐 Security Vulnerabilities

If you discover a security vulnerability:

1. **DO NOT** create a public issue
2. Email [security@ortussolutions.com](mailto:security@ortussolutions.com?subject=security)
3. Report in `#security` channel on [Box Team Slack](http://boxteam.ortussolutions.com/)

All vulnerabilities will be promptly addressed.

## 📄 License

This project is licensed under the **Apache License 2.0**.

```
Copyright 2025 Ortus Solutions, Corp

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

See [LICENSE](LICENSE) file for full details.

## 💼 Support & Resources

### 📖 Documentation

- **Module Docs**: You're reading them! 📚
- **BoxLang Docs**: [https://boxlang.ortusbooks.com/](https://boxlang.ortusbooks.com/)
- **Apache Commons Net**: [https://commons.apache.org/proper/commons-net/](https://commons.apache.org/proper/commons-net/)

### 🌐 Links

- **BoxLang Website**: [https://boxlang.io](https://boxlang.io)
- **Ortus Solutions**: [https://www.ortussolutions.com](https://www.ortussolutions.com)
- **GitHub Repository**: [https://github.com/ortus-boxlang/bx-ftp](https://github.com/ortus-boxlang/bx-ftp)
- **Issue Tracker**: [https://github.com/ortus-boxlang/bx-ftp/issues](https://github.com/ortus-boxlang/bx-ftp/issues)
- **ForgeBox**: [https://forgebox.io/view/bx-ftp](https://forgebox.io/view/bx-ftp)

### 🎓 Learning Resources

- **BoxLang Training**: [https://www.ortussolutions.com/services/training](https://www.ortussolutions.com/services/training)
- **CFCasts**: [https://www.cfcasts.com](https://www.cfcasts.com)
- **Blog**: [https://www.ortussolutions.com/blog](https://www.ortussolutions.com/blog)

## THE DAILY BREAD

> "I am the way, and the truth, and the life; no one comes to the Father, but by me (JESUS)" Jn 14:1-12

---

<blockquote>
	Copyright Since 2025 by Ortus Solutions, Corp
	<br>
	<a href="https://www.boxlang.io">www.boxlang.io</a> |
	<a href="https://www.ortussolutions.com">www.ortussolutions.com</a>
</blockquote>

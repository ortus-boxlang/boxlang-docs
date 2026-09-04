---
description: Execute OS processes, read environment variables, inspect files, and interact with the underlying system from BoxLang.
icon: terminal
---

# OS Integration

BoxLang provides two layers of OS interaction. The **built-in layer** covers process execution, environment variables, system properties, file metadata, timing, and console output — all available with no dependencies. The **extended layer** adds deep hardware and OS introspection via the optional `bx-oshi` module, and direct Java interop unlocks the full power of `ProcessBuilder` for advanced process pipelines.

---

## 🖥️ The `server` Scope — OS Quick Reference

The `server` scope is automatically populated at runtime with read-only OS and runtime metadata. The keys below are **unmodifiable** once the scope is initialized.

### `server.os`

Operating system details sourced from Java system properties and the network stack.

| Key | Example | Description |
|-----|---------|-------------|
| `name` | `"Mac OS X"` | OS name |
| `version` | `"14.5"` | OS version |
| `arch` | `"aarch64"` | CPU architecture |
| `archModel` | `"aarch64"` | Same as arch |
| `hostname` | `"myserver.local"` | Local hostname |
| `ipAddress` | `"192.168.1.10"` | Local IP address |
| `macAddress` | `"a1:b2:c3:d4:e5:f6"` | Primary MAC address |

```js
writeOutput( "Running on: #server.os.name# #server.os.version# (#server.os.arch#)" )
writeOutput( "Host: #server.os.hostname# / #server.os.ipAddress#" )
```

### `server.separator`

Path and line separator characters for the current OS — useful for portable file path construction.

| Key | Unix | Windows | Description |
|-----|------|---------|-------------|
| `file` | `/` | `\` | File path separator |
| `path` | `:` | `;` | Path list separator (like `$PATH`) |
| `line` | `\n` | `\r\n` | Line ending character(s) |

```js
// Cross-platform path joining
fullPath = "/var/data" & server.separator.file & "myfile.txt"

// Write a cross-platform text file
content = "Line 1" & server.separator.line & "Line 2"
```

### `server.java`

JVM runtime information.

| Key | Description |
|-----|-------------|
| `version` | Java version string |
| `vendor` | JVM vendor name |
| `archModel` | CPU architecture |
| `executionPath` | Working directory at JVM startup |
| `freeMemory` | Current free JVM heap (bytes) |
| `totalMemory` | Total JVM heap allocated (bytes) |
| `maxMemory` | Maximum JVM heap allowed (bytes) |
| `defaultLocale` | Default locale display name |
| `availableLocales` | Sorted list of all available locales |
| `pid` | Current process ID |

```js
// Memory usage as MB
usedMB = ( server.java.totalMemory - server.java.freeMemory ) / 1024 / 1024
writeOutput( "JVM using #numberFormat( usedMB, '0.00' )# MB — PID: #server.java.pid#" )
```

### `server.cli`

CLI invocation details. `args` and `parsed` are only populated when running in CLI mode; they are empty string/struct in web/lambda contexts.

| Key | Description |
|-----|-------------|
| `executionPath` | Directory from which BoxLang was invoked |
| `command` | Full command line string (`sun.java.command`) |
| `args` | Array of raw CLI arguments (CLI mode only) |
| `parsed` | Struct of parsed flags and values (CLI mode only) |

```js
// Defensive CLI argument access
if ( server.boxlang.cliMode ) {
    args = server.cli.parsed
    verbose = args.keyExists( "verbose" ) && args.verbose
}
```

### `server.system`

All Java system properties and OS environment variables. **Disabled by default** for security — enable in `boxlang.json`:

```json
{
  "security": {
    "populateServerSystemScope": true
  }
}
```

When enabled:

```js
// All OS environment variables
javaHome = server.system.environment[ "JAVA_HOME" ]

// All Java system properties
userHome = server.system.properties[ "user.home" ]
tmpDir   = server.system.properties[ "java.io.tmpdir" ]
```

{% hint style="warning" %}
`server.system.environment` and `server.system.properties` expose **all** environment variables and Java system properties to your code. Only enable `populateServerSystemScope` when you need bulk access. For targeted lookups, use `getSystemSetting()` instead.
{% endhint %}

### `server.boxlang`

BoxLang runtime metadata.

| Key | Description |
|-----|-------------|
| `version` | BoxLang version string |
| `buildDate` | Build date |
| `codename` | Release codename |
| `boxlangId` | Runtime instance hash |
| `compiler` | Compiler mode (`asm`, `java`, etc.) |
| `cliMode` | `true` when running as CLI |
| `debugMode` | `true` when debug mode is active |
| `jarMode` | `true` when running from a JAR |
| `runtimeHome` | Path to the BoxLang home directory |
| `modules` | Struct of loaded modules |

---

## ⚙️ Process Execution

### `systemExecute()` BIF

Execute any system process and capture its output.

```js
result = systemExecute( name="git", arguments="--version" )
writeOutput( result.output )   // git version 2.44.0
writeOutput( result.exitCode ) // 0
```

**Arguments:**

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `name` | string | ✅ | — | Binary name or full path |
| `arguments` | string \| array | ❌ | `null` | Arguments — string is auto-tokenized (quotes preserved); array is used directly |
| `timeout` | long | ❌ | unlimited | Max seconds to wait |
| `terminateOnTimeout` | boolean | ❌ | `false` | Kill process when timeout is reached |
| `directory` | string | ❌ | `null` | Working directory for the process |
| `output` | string | ❌ | `null` | File path to redirect stdout to |
| `error` | string | ❌ | `null` | File path to redirect stderr to |
| `inheritEnvironment` | boolean | ❌ | `true` | Inherit parent process environment |
| `environment` | struct | ❌ | `{}` | Additional/override environment variables (merged after inherit decision) |

**Return struct:**

| Key | Type | Description |
|-----|------|-------------|
| `output` | string | Captured stdout (`null` if redirected to file) |
| `error` | string | Captured stderr (`null` if redirected to file) |
| `exitCode` | integer | Process exit code |
| `pid` | long | Process ID |
| `timeout` | boolean | Whether timeout was reached |
| `terminated` | boolean | Whether process was force-killed |

**Examples:**

```js
// Array arguments — no shell tokenization, safest approach
result = systemExecute(
    name      = "git",
    arguments = [ "log", "--oneline", "-10" ],
    directory = "/var/apps/myproject"
)
if ( result.exitCode != 0 ) {
    throw( message="git failed: #result.error#" )
}

// Timeout with graceful termination
result = systemExecute(
    name              = "ffmpeg",
    arguments         = [ "-i", "input.mp4", "-t", "60", "output.mp4" ],
    timeout           = 120,
    terminateOnTimeout = true
)

// Isolated environment — start fresh with only what you provide
result = systemExecute(
    name               = "node",
    arguments          = [ "build.js" ],
    inheritEnvironment = false,
    environment        = {
        NODE_ENV : "production",
        PATH     : "/usr/local/bin:/usr/bin"
    }
)

// Redirect large output to file
systemExecute(
    name   = "pg_dump",
    arguments = [ "-Fc", "mydb" ],
    output = "/backups/mydb.dump",
    error  = "/logs/pgdump.err"
)
```

{% hint style="info" %}
For string arguments, BoxLang tokenizes using a regex that preserves quoted strings, so `arguments="--format 'Hello World'"` correctly passes two tokens. For guaranteed correctness, use an array.
{% endhint %}

### `bx:execute` Component

The component version of `systemExecute()`. Results are distributed into separate named variables rather than returned as a struct.

```js
// Script syntax
bx:execute name="git" arguments="--version" variable="gitVersion" exitCode="code";
writeOutput( "Git: #gitVersion# (exit: #code#)" )
```

```xml
<!-- Template syntax -->
<bx:execute
    name         = "git"
    arguments    = "--version"
    variable     = "gitVersion"
    errorVariable = "gitError"
    exitCode     = "code"
/>
<bx:output>Git: #gitVersion#</bx:output>
```

**Attributes:**

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `name` | string | ✅ | — | Binary name or full path |
| `arguments` | string \| array | ❌ | — | Process arguments |
| `variable` | string | ❌ | — | Variable to receive stdout |
| `errorVariable` | string | ❌ | — | Variable to receive stderr |
| `exitCode` | string | ❌ | — | Variable to receive exit code |
| `outputFile` | string | ❌ | — | File path to redirect stdout to |
| `errorFile` | string | ❌ | — | File path to redirect stderr to |
| `timeout` | long | ❌ | unlimited | Max seconds to wait |
| `terminateOnTimeout` | boolean | ❌ | `false` | Kill process on timeout |
| `directory` | string | ❌ | — | Working directory |
| `inheritEnvironment` | boolean | ❌ | `true` | Inherit parent environment |
| `environment` | struct | ❌ | `{}` | Additional environment variables |

{% hint style="info" %}
Note that the component uses `outputFile`/`errorFile` (not `output`/`error` like the BIF).
{% endhint %}

### Cross-Platform Shell Invocation

When you need shell features like pipes, redirects, or glob expansion:

```js
// Unix / macOS
result = systemExecute(
    name      = "bash",
    arguments = [ "-c", "ls -la /tmp | grep '\.log$' | wc -l" ]
)

// Windows
result = systemExecute(
    name      = "cmd",
    arguments = [ "/s", "/c", "dir C:\\Logs\\*.log /b" ]
)

// Cross-platform helper
isWindows = server.os.name.findNoCase( "windows" ) > 0
shell     = isWindows ? "cmd" : "bash"
flag      = isWindows ? "/c" : "-c"
result    = systemExecute( name=shell, arguments=[ flag, "echo hello" ] )
```

---

## 🌍 Environment Variables & System Properties

### `getSystemSetting( key [, defaultValue] )`

Retrieve a Java system property or OS environment variable by name.

```js
// Read an environment variable
dbHost = getSystemSetting( "DB_HOST" )

// With a default value (no exception if missing)
dbPort = getSystemSetting( "DB_PORT", 5432 )

// Read a Java system property (checked before env vars)
userHome = getSystemSetting( "user.home" )
tmpDir   = getSystemSetting( "java.io.tmpdir" )

// Safe existence check pattern
apiKey = getSystemSetting( "API_KEY", "" )
if ( !len( apiKey ) ) {
    throw( message="API_KEY environment variable is required" )
}
```

**Lookup order:**

1. Registered system setting providers (by namespace)
2. Java system properties (`System.getProperties()`)
3. OS environment variables (`System.getenv()`)
4. `defaultValue` — or throws `BoxRuntimeException` if none provided

**Notes:**
- Key names are **case-sensitive**
- Namespace support via `.` separator (e.g., custom provider registered under `myapp`)

{% hint style="success" %}
Use `getSystemSetting()` for targeted lookups. It is more secure than enabling `server.system` scope population, since it does not expose all environment variables to templates.
{% endhint %}

### `.env` File Auto-Loading (CLI)

When running in CLI mode, BoxLang automatically loads environment variables from `.env` files before your script executes. Two files are loaded in order — user-level first, then project-level:

| File | Description |
|------|-------------|
| `~/.box.env` | User-level defaults — loaded on every CLI invocation (since BoxLang 1.13.0) |
| `.env` | Project-level file in the current working directory — values override user-level |

All values are available immediately via `getSystemSetting()`:

```js
// Reads from ~/.box.env, .env, Java system properties, or OS environment — in that priority
dbHost = getSystemSetting( "DB_HOST", "localhost" )
apiKey = getSystemSetting( "OPENAI_API_KEY" )
```

{% hint style="info" %}
The MiniServer has its own `.env` loading from the webroot — see the [MiniServer documentation](../getting-started/running-boxlang/miniserver.md) for details. For CLI `.env` behavior, see [CLI Scripting](../getting-started/running-boxlang/cli-scripting.md).
{% endhint %}

---

## 📺 Console Output

| BIF | Signature | Description |
|-----|-----------|-------------|
| `print()` | `print( message )` | Write to stdout without a newline |
| `println()` | `println( message )` | Write to stdout with a trailing newline |
| `systemOutput()` | `systemOutput( obj, addNewLine, doErrorStream )` | Full control — stdout or stderr |

```js
print( "Processing... " )
println( "done!" )

// Write to stderr
systemOutput( "Warning: cache miss for key #cacheKey#", true, true )

// Useful in CLI scripts
items.each( ( item ) => {
    println( "Processing: #item.name#" )
    systemOutput( "Skipping #item.name#", true, true )   // stderr for diagnostic output
})
```

---

## ⏱️ Timing & Performance

### `getTickCount( [unit] )`

Returns a high-resolution system timer value. Default unit is `"milli"`.

| Unit | Returns |
|------|---------|
| `"milli"` (default) | `System.currentTimeMillis()` — wall-clock milliseconds |
| `"nano"` | `System.nanoTime()` — monotonic nanoseconds |
| `"second"` | Current time in seconds |

```js
start  = getTickCount()
// ... do work ...
elapsed = getTickCount() - start
writeOutput( "Completed in #elapsed# ms" )

// High-precision benchmark
startNano = getTickCount( "nano" )
// ... tight loop ...
elapsedNs = getTickCount( "nano" ) - startNano
writeOutput( "Took #elapsedNs / 1_000_000# ms (#elapsedNs# ns)" )
```

### `sleep( duration )`

Pauses the current thread for `duration` **milliseconds**. Throws `BoxRuntimeException` if the thread is interrupted.

```js
// Poll with backoff
attempts = 0
while ( !resourceReady() && ++attempts <= 5 ) {
    sleep( 500 * attempts )   // 500ms, 1s, 1.5s, 2s, 2.5s
}
```

---

## ℹ️ System & Runtime Information

### `getBoxVersionInfo()`

Returns a struct with BoxLang runtime version details.

| Key | Description |
|-----|-------------|
| `version` | Version string (e.g., `"1.13.0"`) |
| `buildDate` | Build date |
| `codename` | Release codename |
| `boxlangId` | Runtime instance identifier |

```js
info = getBoxVersionInfo()
writeOutput( "BoxLang #info.version# (#info.codename#) built on #info.buildDate#" )

// Guard for version-specific features
semver = getSemver( info.version )
if ( semver.major >= 1 && semver.minor >= 13 ) {
    // Use 1.13.0+ features
}
```

---

## 📄 File & Disk Information

### `fileInfo( file )` / `getFileInfo( file )`

Both BIFs inspect a file or directory path. `getFileInfo()` is the verbose alias with additional OS-level attributes.

**`fileInfo()` returns:**

| Key | Type | Description |
|-----|------|-------------|
| `name` | string | Filename only |
| `path` | string | Absolute path |
| `size` | long | Size in bytes (`0` for directories) |
| `type` | string | `"file"` or `"directory"` |
| `lastModified` | string | Formatted last-modified datetime |
| `attributes` | string | Empty string (compatibility key) |
| `mode` | string | Octal POSIX permissions (e.g., `"644"`) — empty on Windows |
| `read` | boolean | Is the path readable |
| `write` | boolean | Is the path writable |
| `execute` | boolean | Is the path executable |
| `checksum` | string | MD5 checksum of file content (empty for directories) |

**`getFileInfo()` returns** (different key set):

| Key | Type | Description |
|-----|------|-------------|
| `name`, `path`, `size`, `type`, `lastModified` | — | Same as above |
| `parent` | string | Parent directory absolute path |
| `isHidden` | boolean | Hidden file/directory |
| `canRead` / `canWrite` / `canExecute` | boolean | Permission flags |
| `isArchive` / `isSystem` | boolean | Windows DOS attributes only |
| `isAttributesSupported` | boolean | `true` on Windows |
| `isModeSupported` | boolean | `true` on POSIX systems |
| `isCaseSensitive` | boolean | Heuristic: is the FS case-sensitive |

```js
// Quick file check
info = fileInfo( "/var/data/import.csv" )
writeOutput( "Size: #info.size# bytes, writable: #info.write#, MD5: #info.checksum#" )

// POSIX permissions
if ( server.os.name != "Windows" && info.mode != "644" ) {
    writeOutput( "Warning: unexpected permissions #info.mode# on #info.path#" )
}

// Verbose info
details = getFileInfo( "/etc/hosts" )
writeOutput( "Hidden: #details.isHidden#, Case-sensitive FS: #details.isCaseSensitive#" )
```

For file size details on disk partitions, use the `bx-oshi` module's `getFreeSpace()` / `getTotalSpace()` convenience BIFs.

---

## 📁 Temp Files & Directories

```js
// System temp directory
tmp = getTempDirectory()   // e.g., "/var/folders/.../T/"

// Create a named temp file (suffix defaults to ".tmp" if empty)
report = createTempFile( getTempDirectory(), "report-", ".csv" )
fileWrite( report, csvData )

// Create a temp working directory
workDir = createTempDirectory( getTempDirectory(), "build-" )
```

---

## 🔬 Deep OS Introspection — `bx-oshi`

The [bx-oshi module](../boxlang-framework/modularity/hardware-and-system-info.md) wraps the [OSHI library](https://github.com/oshi/oshi) to expose hardware and OS metrics with no native library requirements.

```bash
# BoxLang CLI quick install
install-bx-module bx-oshi

# CommandBox / web server
box install bx-oshi
```

### Convenience BIFs

| BIF | Description |
|-----|-------------|
| `getCpuUsage( [interval] )` | CPU utilization percentage |
| `getFreeSpace( path )` | Free disk space for the given path (bytes) |
| `getTotalSpace( path )` | Total disk capacity for the given path (bytes) |
| `getSystemFreeMemory()` | Free OS physical memory (bytes) |
| `getSystemTotalMemory()` | Total OS physical memory (bytes) |
| `getJVMFreeMemory()` | Free JVM heap (bytes) |
| `getJVMTotalMemory()` | Total JVM heap allocated (bytes) |

```js
// Health check snippet
cpu   = getCpuUsage( 500 )   // sample over 500ms
freeMB = getSystemFreeMemory() / 1024 / 1024
diskGB = getFreeSpace( "/var" ) / 1024 / 1024 / 1024

writeOutput( "CPU: #numberFormat( cpu * 100, '0.0' )#%" )
writeOutput( "Free RAM: #numberFormat( freeMB, '0' )# MB" )
writeOutput( "Free disk: #numberFormat( diskGB, '0.0' )# GB" )
```

### Full Hardware & OS Access

For deeper data — CPU topology, network interfaces, disk I/O, sensors, batteries — use the core BIFs:

```js
si = getSystemInfo()
os = getOperatingSystem()
hw = getHardware()

// OS details
writeOutput( "OS: #os.getFamily()# #os.getVersionInfo().getVersion()#" )
writeOutput( "Uptime: #os.getSystemUptime()# seconds" )

// Running processes
processes = os.getProcesses()
for ( p in processes ) {
    writeOutput( "#p.getProcessID()# #p.getName()# — #p.getResidentSetSize() / 1024# KB" )
}

// Physical memory
memory = hw.getMemory()
writeOutput( "Total RAM: #memory.getTotal() / 1024 / 1024 / 1024# GB" )

// CPU
cpu = hw.getProcessor()
writeOutput( "CPU: #cpu.getProcessorIdentifier().getName()#" )
writeOutput( "Physical cores: #cpu.getPhysicalProcessorCount()#" )
writeOutput( "Logical cores: #cpu.getLogicalProcessorCount()#" )
```

{% content-ref url="../boxlang-framework/modularity/hardware-and-system-info.md" %}
[hardware-and-system-info.md](../boxlang-framework/modularity/hardware-and-system-info.md)
{% endcontent-ref %}

---

## 🔧 Advanced: Java `ProcessBuilder` Interop

`systemExecute()` covers most use cases. When you need streaming output, process pipelines, or interactive I/O, use Java's `ProcessBuilder` directly via BoxLang's Java interop.

### Streaming Process Output

```js
pb = createObject( "java", "java.lang.ProcessBuilder" )
    .init( [ "tail", "-f", "/var/log/app.log" ] )

pb.redirectErrorStream( true )   // merge stderr into stdout

process = pb.start()
reader  = createObject( "java", "java.io.BufferedReader" )
    .init( createObject( "java", "java.io.InputStreamReader" )
    .init( process.getInputStream() ) )

// Read first 50 lines then stop
count = 0
line  = reader.readLine()
while ( !isNull( line ) && ++count <= 50 ) {
    println( line )
    line = reader.readLine()
}

process.destroyForcibly()
reader.close()
```

### Custom Working Directory & Environment

```js
pb = createObject( "java", "java.lang.ProcessBuilder" )
    .init( [ "npm", "run", "build" ] )

// Set working directory
pb.directory(
    createObject( "java", "java.io.File" ).init( "/var/apps/frontend" )
)

// Modify environment in place
env = pb.environment()
env.put( "NODE_ENV", "production" )
env.put( "CI", "true" )
env.remove( "npm_config_cache" )

process = pb.start()
exitCode = process.waitFor()
writeOutput( "Build exited: #exitCode#" )
```

### Inherit Parent I/O (Interactive)

```js
// The child process shares the parent's stdin/stdout/stderr directly
// Useful for interactive CLI tools or when you want live output without buffering
pb = createObject( "java", "java.lang.ProcessBuilder" )
    .init( [ "bash", "-i" ] )
pb.inheritIO()
process = pb.start()
process.waitFor()
```

### Process Pipeline (Java 9+)

Chain processes so stdout of one feeds stdin of the next:

```js
ProcessBuilder = createObject( "java", "java.lang.ProcessBuilder" )

pb1 = ProcessBuilder.init( [ "cat", "/var/log/app.log" ] )
pb2 = ProcessBuilder.init( [ "grep", "ERROR" ] )
pb3 = ProcessBuilder.init( [ "wc", "-l" ] )

processes = ProcessBuilder.startPipeline( [ pb1, pb2, pb3 ] )
last      = processes[ processes.size() ]

reader = createObject( "java", "java.io.BufferedReader" )
    .init( createObject( "java", "java.io.InputStreamReader" )
    .init( last.getInputStream() ) )

count = reader.readLine()
println( "Error count: #count#" )
```

{% hint style="info" %}
Prefer `systemExecute()` for straightforward commands — it handles stream draining, timeout, and exit code in a single call. Use `ProcessBuilder` only when you need streaming I/O, pipelines, or interactive processes.
{% endhint %}

---

## 🔐 Security Considerations

{% hint style="danger" %}
**Command Injection** — Never build command strings by concatenating user-supplied input. Always use array arguments so each token is passed directly to the OS without shell interpretation.

```js
// ❌ UNSAFE — user input can inject shell commands
result = systemExecute( name="bash", arguments="-c ls #userInput#" )

// ✅ SAFE — array args bypass the shell entirely
result = systemExecute( name="ls", arguments=[ userInput ] )
```
{% endhint %}

Additional guidelines:

- **Validate paths** before passing them to `directory`, `output`, or `error` arguments — prevent path traversal attacks.
- **Use `inheritEnvironment=false`** when spawning processes that should not have access to your application's secrets (API keys, DB passwords in env vars).
- **Disable `populateServerSystemScope`** unless you specifically need bulk access to all env vars; use `getSystemSetting()` for individual lookups instead.
- **Restrict output file paths** — ensure processes cannot write to sensitive locations by validating the `output`/`outputFile` arguments.
- **Set timeouts** for all externally invoked processes to prevent resource exhaustion.

---

## 🔗 Related Documentation

{% content-ref url="../getting-started/running-boxlang/cli-scripting.md" %}
[cli-scripting.md](../getting-started/running-boxlang/cli-scripting.md)
{% endcontent-ref %}

{% content-ref url="file-handling/README.md" %}
[README.md](file-handling/README.md)
{% endcontent-ref %}

{% content-ref url="file-handling/property-files.md" %}
[property-files.md](file-handling/property-files.md)
{% endcontent-ref %}

{% content-ref url="../boxlang-language/variable-scopes.md" %}
[variable-scopes.md](../boxlang-language/variable-scopes.md)
{% endcontent-ref %}

{% content-ref url="../boxlang-framework/modularity/hardware-and-system-info.md" %}
[hardware-and-system-info.md](../boxlang-framework/modularity/hardware-and-system-info.md)
{% endcontent-ref %}

{% content-ref url="../boxlang-language/reference/built-in-functions/zip/README.md" %}
[zip/README.md](../boxlang-language/reference/built-in-functions/zip/README.md)
{% endcontent-ref %}

{% content-ref url="java-integration.md" %}
[java-integration.md](java-integration.md)
{% endcontent-ref %}

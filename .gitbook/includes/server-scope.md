---
title: Server Scope
---

# Server Scope

BoxLang has the concept of [variables scopes](../../boxlang-language/variable-scopes.md) that are backed by Java maps we lovingly call structs.  They are fast, case-insensitive, fluent, and functional.  BoxLang creates a `server`scope you can access from any executing file and lives for the application's lifespan.  This scope contains many useful variables, but it can also be used to store any simple/complex variables that you see fit that will persist until the application is shut down or exists.

```java
// Create a variable in the server scope
server.appCreated = now()

// Use a variable in the scope
var inCLIMode = server.boxlang.cliMode
```

The `server` scope is composed of the following internal structures of information:

<table><thead><tr><th width="206">Key</th><th>Hint</th></tr></thead><tbody><tr><td><code>boxlang</code></td><td>A structure containing the runtime information about the language and execution mode.</td></tr><tr><td><code>os</code></td><td>Information about the running operating system</td></tr><tr><td><code>separator</code></td><td>Information about the separators used in the operating system</td></tr><tr><td><code>cli</code></td><td>A collection of variables pertaining to the CLI execution (if any) of the application</td></tr><tr><td><code>java</code></td><td>Information about the running JRE/JDK</td></tr><tr><td><code>system</code></td><td>It contains all the Java properties and System environment variables used to execute the application.</td></tr></tbody></table>

Let's investigate each struct of data because they contain much information about CLI-based scripting and apps.

## boxlang

The following variables are in this structure.

<table><thead><tr><th width="205">Variable</th><th width="100"><select><option value="M25oLpjbfLeo" label="String" color="blue"></option><option value="FKu4P8Bcnsat" label="Number" color="blue"></option><option value="3aeCl3Vi6Hn0" label="Boolean" color="blue"></option><option value="aGop9y9MZCRu" label="Timestamp" color="blue"></option><option value="aC32fOXQJVht" label="Path" color="blue"></option></select></th><th>Hint</th></tr></thead><tbody><tr><td><code>buildDate</code></td><td><span data-option="aGop9y9MZCRu">Timestamp</span></td><td>The build date of BoxLang</td></tr><tr><td><code>boxLangID</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The unique identifier of the current installation</td></tr><tr><td><code>codename</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The codename of the version of BoxLang</td></tr><tr><td><code>cliMode</code></td><td><span data-option="3aeCl3Vi6Hn0">Boolean</span></td><td>True if we are in CLI running mode, else false.</td></tr><tr><td><code>webMode</code></td><td><span data-option="3aeCl3Vi6Hn0">Boolean</span></td><td>True if running in web (servlet/MiniServer) mode. <strong>New in 1.14.0</strong></td></tr><tr><td><code>debugMode</code></td><td><span data-option="3aeCl3Vi6Hn0">Boolean</span></td><td>True if we are in debug mode or not.</td></tr><tr><td><code>jarMode</code></td><td><span data-option="3aeCl3Vi6Hn0">Boolean</span></td><td>True if we are running the language from a JAR or an exploded source.</td></tr><tr><td><code>runtimeHome</code></td><td><span data-option="aC32fOXQJVht">Path</span></td><td>The absolute path to the runtime's home directory</td></tr><tr><td><code>version</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The semantic version of the language</td></tr></tbody></table>

## OS

The following variables are in this structure.

<table><thead><tr><th width="210">Variable</th><th width="100"><select><option value="M25oLpjbfLeo" label="String" color="blue"></option><option value="FKu4P8Bcnsat" label="Number" color="blue"></option><option value="3aeCl3Vi6Hn0" label="Boolean" color="blue"></option><option value="aGop9y9MZCRu" label="Timestamp" color="blue"></option><option value="aC32fOXQJVht" label="Path" color="blue"></option></select></th><th>Hint</th></tr></thead><tbody><tr><td><code>arch</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>OS Architecture</td></tr><tr><td><code>archModel</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>OS Architecture model</td></tr><tr><td><code>hostname</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The machine's hostname</td></tr><tr><td><code>ipAddress</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The machine's IP Address</td></tr><tr><td><code>macAddress</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The machine's mac address</td></tr><tr><td><code>name</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>Operating system name</td></tr><tr><td><code>version</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>Operating system version</td></tr></tbody></table>

## separator

The following variables are in this structure.

<table><thead><tr><th width="220">Variable</th><th width="100"><select><option value="M25oLpjbfLeo" label="String" color="blue"></option><option value="FKu4P8Bcnsat" label="Number" color="blue"></option><option value="3aeCl3Vi6Hn0" label="Boolean" color="blue"></option><option value="aGop9y9MZCRu" label="Timestamp" color="blue"></option><option value="aC32fOXQJVht" label="Path" color="blue"></option></select></th><th>Hint</th></tr></thead><tbody><tr><td><code>path</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>Path character separator</td></tr><tr><td><code>file</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>File path character separator</td></tr><tr><td><code>line</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>Line character separator</td></tr></tbody></table>

## CLI

The following variables are in this structure.

<table><thead><tr><th width="216">Variable</th><th width="100"><select><option value="M25oLpjbfLeo" label="String" color="blue"></option><option value="FKu4P8Bcnsat" label="Number" color="blue"></option><option value="3aeCl3Vi6Hn0" label="Boolean" color="blue"></option><option value="aGop9y9MZCRu" label="Timestamp" color="blue"></option><option value="aC32fOXQJVht" label="Path" color="blue"></option><option value="NsqJAGMFv1VJ" label="Struct" color="blue"></option></select></th><th>Hint</th></tr></thead><tbody><tr><td><code>executionPath</code></td><td><span data-option="aC32fOXQJVht">Path</span></td><td>The absolute path from which the execution of the CLI application started.  Maps to the Java <code>user.dir</code>property</td></tr><tr><td><code>command</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The full commandline used to execute</td></tr><tr><td><code>args</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>The original command line arguments used in the execution</td></tr><tr><td><code>parsed</code></td><td><span data-option="NsqJAGMFv1VJ">Struct</span></td><td>A structure containing the parsed command line arguments: <code>positionals</code>and <code>options</code></td></tr></tbody></table>

## Java

The following variables are in this structure.

<table><thead><tr><th width="216">Variable</th><th width="100"><select><option value="M25oLpjbfLeo" label="String" color="blue"></option><option value="FKu4P8Bcnsat" label="Number" color="blue"></option><option value="3aeCl3Vi6Hn0" label="Boolean" color="blue"></option><option value="aGop9y9MZCRu" label="Timestamp" color="blue"></option><option value="aC32fOXQJVht" label="Path" color="blue"></option><option value="NsqJAGMFv1VJ" label="Struct" color="blue"></option></select></th><th>Hint</th></tr></thead><tbody><tr><td><code>executionPath</code></td><td><span data-option="aC32fOXQJVht">Path</span></td><td>The absolute path from which the execution of the CLI application started.  Maps to the Java <code>user.dir</code>property</td></tr><tr><td><code>freeMemory</code></td><td><span data-option="FKu4P8Bcnsat">Number</span></td><td>Free JVM memory</td></tr><tr><td><code>maxMemory</code></td><td><span data-option="FKu4P8Bcnsat">Number</span></td><td>Max JVM memory</td></tr><tr><td><code>totalMemory</code></td><td><span data-option="FKu4P8Bcnsat">Number</span></td><td>Total JVM memory</td></tr><tr><td><code>vendor</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>JDK Vendor</td></tr><tr><td><code>version</code></td><td><span data-option="M25oLpjbfLeo">String</span></td><td>JDK Version</td></tr></tbody></table>

## System

The following variables are in this structure.

<table><thead><tr><th width="216">Variable</th><th width="100"><select><option value="M25oLpjbfLeo" label="String" color="blue"></option><option value="FKu4P8Bcnsat" label="Number" color="blue"></option><option value="3aeCl3Vi6Hn0" label="Boolean" color="blue"></option><option value="aGop9y9MZCRu" label="Timestamp" color="blue"></option><option value="aC32fOXQJVht" label="Path" color="blue"></option><option value="NsqJAGMFv1VJ" label="Struct" color="blue"></option></select></th><th>Hint</th></tr></thead><tbody><tr><td><code>environment</code></td><td><span data-option="NsqJAGMFv1VJ">Struct</span></td><td>A struct of ALL the environment vairables found when creating the runtime.</td></tr><tr><td><code>properties</code></td><td><span data-option="NsqJAGMFv1VJ">Struct</span></td><td>All the Java properties</td></tr></tbody></table>

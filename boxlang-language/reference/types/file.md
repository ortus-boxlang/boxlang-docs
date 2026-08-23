[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `File`



## File Methods

<details>
<summary><code>info()</code></summary>

Returns a struct of file information.

Different values are returned for FileInfo and GetFileInfo
</details>
<details>
<summary><code>writeLine(data=[string])</code></summary>

Writes a line of data to a file

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `data` | `string` | `true` | `null` |

</details>
<details>
<summary><code>readLine()</code></summary>

Returns the next line from the file object stream
</details>
<details>
<summary><code>setAccessMode(mode=[string])</code></summary>

Sets the Posix permissions on a file

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mode` | `string` | `true` | `null` |

</details>
<details>
<summary><code>seek(position=[integer])</code></summary>

Moves the buffer cursor position forward the number of characters specified by the position argument

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>skipBytes(position=[integer])</code></summary>

Moves the buffer cursor position forward the number of characters specified by the position argument

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>setLastModified(date=[any])</code></summary>

Sets the last modified time of a file

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date` | `any` | `true` | `null` |

</details>
<details>
<summary><code>setAttribute(attribute=[string])</code></summary>

Sets a file access attribute

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `attribute` | `string` | `true` | `null` |

</details>
<details>
<summary><code>bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

<p>,
 The available ,<code>,output,</code>, locations are:
 - ,<strong>,buffer,</strong>,: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser.
 - ,<strong>,console,</strong>,: The output is printed to the System console.
 - ,<strong>,Absolute File Path,</strong>, The output is written to a file with the specified absolute file path.
 ,</p>,
 
 The output `format` can be either HTML or plain text.
 
 The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `label` | `string` | `false` | `null` |
| `depth` | `numeric` | `false` | `null` |
| `maxRows` | `numeric` | `false` | `null` |
| `top` | `numeric` | `false` | `null` |
| `expand` | `boolean` | `false` | `true` |
| `abort` | `boolean` | `false` | `false` |
| `output` | `string` | `false` | `null` |
| `format` | `string` | `false` | `null` |
| `showUDFs` | `boolean` | `false` | `true` |

</details>


## Examples

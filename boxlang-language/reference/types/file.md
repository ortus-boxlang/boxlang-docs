[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `File`



## File Methods

<dl>
<dt><code>close()</code></dt><dd>Closes either the read or write stream</dd>
<dt><code>getLastModifedTime()</code></dt><dd>Retrieves the last modified time of a file</dd>
<dt><code>info()</code></dt><dd>Returns a struct of file information.

Different values are returned for FileInfo and GetFileInfo</dd>
<dt><code>readLine()</code></dt><dd>Returns the next line from the file object stream</dd>
<dt><code>seek(position=[integer])</code></dt><dd>Moves the buffer cursor position forward the number of characters specified by the position argument

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |

</dd>
<dt><code>setAccessMode(mode=[string])</code></dt><dd>Sets the Posix permissions on a file

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mode` | `string` | `true` | `` |

</dd>
<dt><code>setAttribute(attribute=[string])</code></dt><dd>Sets a file access attribute

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `attribute` | `string` | `true` | `` |

</dd>
<dt><code>setLastModified(date=[any])</code></dt><dd>Sets the last modified time of a file

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date` | `any` | `true` | `` |

</dd>
<dt><code>skipBytes(position=[integer])</code></dt><dd>Moves the buffer cursor position forward the number of characters specified by the position argument

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |

</dd>
<dt><code>writeLine(data=[string])</code></dt><dd>Writes a line of data to a file

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `data` | `string` | `true` | `` |

</dd>

</dl>

## Examples

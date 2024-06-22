[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `File`



## File Methods

<details>
<summary><code>close()</code></summary>
Closes either the read or write stream
</details>
<details>
<summary><code>getLastModifedTime()</code></summary>
Retrieves the last modified time of a file
</details>
<details>
<summary><code>info()</code></summary>
Returns a struct of file information.

Different values are returned for FileInfo and GetFileInfo
</details>
<details>
<summary><code>readLine()</code></summary>
Returns the next line from the file object stream
</details>
<details>
<summary><code>seek(position=[integer])</code></summary>
Moves the buffer cursor position forward the number of characters specified by the position argument

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |


</details>
<details>
<summary><code>setAccessMode(mode=[string])</code></summary>
Sets the Posix permissions on a file

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `mode` | `string` | `true` | `` |


</details>
<details>
<summary><code>setAttribute(attribute=[string])</code></summary>
Sets a file access attribute

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `attribute` | `string` | `true` | `` |


</details>
<details>
<summary><code>setLastModified(date=[any])</code></summary>
Sets the last modified time of a file

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `date` | `any` | `true` | `` |


</details>
<details>
<summary><code>skipBytes(position=[integer])</code></summary>
Moves the buffer cursor position forward the number of characters specified by the position argument

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `position` | `integer` | `true` | `` |


</details>
<details>
<summary><code>writeLine(data=[string])</code></summary>
Writes a line of data to a file

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `data` | `string` | `true` | `` |


</details>


## Examples

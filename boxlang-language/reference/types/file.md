[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `File`



## File Methods

<details>
<summary><code>close()</code></summary>
<p>Closes either the read or write stream
</p></details>
<details>
<summary><code>getLastModifedTime()</code></summary>
<p>Retrieves the last modified time of a file
</p></details>
<details>
<summary><code>info()</code></summary>
<p>Returns a struct of file information.

Different values are returned for FileInfo and GetFileInfo
</p></details>
<details>
<summary><code>readLine()</code></summary>
<p>Returns the next line from the file object stream
</p></details>
<details>
<summary><code>seek(position=[integer])</code></summary>
<p>Moves the buffer cursor position forward the number of characters specified by the position argument

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`position`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>setAccessMode(mode=[string])</code></summary>
<p>Sets the Posix permissions on a file

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`mode`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>setAttribute(attribute=[string])</code></summary>
<p>Sets a file access attribute

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`attribute`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>setLastModified(date=[any])</code></summary>
<p>Sets the last modified time of a file

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`date`</td>
<td>`any`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>skipBytes(position=[integer])</code></summary>
<p>Moves the buffer cursor position forward the number of characters specified by the position argument

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`position`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>writeLine(data=[string])</code></summary>
<p>Writes a line of data to a file

 Arguments:
<table>
<thead>
<tr>
<th>Argument</th>
<th>Type</th>
<th>Required</th>
<th>Default</th>
</tr>
</thead>
<tbody>

<tr>
<td>`data`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>


## Examples

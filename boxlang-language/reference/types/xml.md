[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Xml`

This type represents an XML Object in BoxLang

## Xml Methods

<details>
<summary><code>childPos(childname=[string], n=[integer])</code></summary>
<p>Gets the position of a child element within an XML document object.

The position, in an XmlChildren array, of the Nth child that has the specified name.

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
<td>`childname`</td>
<td>`string`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`n`</td>
<td>`integer`</td>
<td>`true`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>getNodeType()</code></summary>
<p>Get XML values according to given xPath query
</p></details>
<details>
<summary><code>search(xpath=[String], params=[Struct])</code></summary>
<p>Get XML values according to given xPath query

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
<td>`xpath`</td>
<td>`String`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`params`</td>
<td>`Struct`</td>
<td>`false`</td>
<td>`{}`</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>toString(encoding=[string])</code></summary>
<p>Converts a value to a string.

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
<td>`encoding`</td>
<td>`string`</td>
<td>`false`</td>
<td>``</td>
</tr></tbody>
</table>

</p></details>
<details>
<summary><code>transform(XSL=[String], parameters=[Struct])</code></summary>
<p>Get XML values according to given xPath query

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
<td>`XSL`</td>
<td>`String`</td>
<td>`true`</td>
<td>``</td>
</tr>

<tr>
<td>`parameters`</td>
<td>`Struct`</td>
<td>`false`</td>
<td>`{}`</td>
</tr></tbody>
</table>

</p></details>


## Examples

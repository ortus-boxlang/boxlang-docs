[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Xml`

This type represents an XML Object in BoxLang

## Xml Methods

<dl>
<dt><code>childPos(childname=[string], n=[integer])</code></dt><dd>Gets the position of a child element within an XML document object.

The position, in an XmlChildren array, of the Nth child that has the specified name.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `childname` | `string` | `true` | `` |
| `n` | `integer` | `true` | `` |

</dd>
<dt><code>getNodeType()</code></dt><dd>Get XML values according to given xPath query</dd>
<dt><code>search(xpath=[String], params=[Struct])</code></dt><dd>Get XML values according to given xPath query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `xpath` | `String` | `true` | `` |
| `params` | `Struct` | `false` | `{}` |

</dd>
<dt><code>toString(encoding=[string])</code></dt><dd>Converts a value to a string.

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `encoding` | `string` | `false` | `` |

</dd>
<dt><code>transform(XSL=[String], parameters=[Struct])</code></dt><dd>Get XML values according to given xPath query

 Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `XSL` | `String` | `true` | `` |
| `parameters` | `Struct` | `false` | `{}` |

</dd>

</dl>

## Examples

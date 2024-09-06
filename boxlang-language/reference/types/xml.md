[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Xml`

This type represents an XML Object in BoxLang

## Xml Methods

<details>
<summary><code>childPos(childname=[string], n=[integer])</code></summary>

Gets the position of a child element within an XML document object.

The position, in an XmlChildren array, of the Nth child that has the specified name.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `childname` | `string` | `true` | `null` |
| `n` | `integer` | `true` | `null` |

</details>
<details>
<summary><code>getNodeType()</code></summary>

Get XML values according to given xPath query
</details>
<details>
<summary><code>search(xpath=[String], params=[Struct])</code></summary>

Get XML values according to given xPath query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `xpath` | `String` | `true` | `null` |
| `params` | `Struct` | `false` | `{}` |

</details>
<details>
<summary><code>transform(XSL=[String], parameters=[Struct])</code></summary>

Get XML values according to given xPath query

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `XSL` | `String` | `true` | `null` |
| `parameters` | `Struct` | `false` | `{}` |

</details>


## Examples

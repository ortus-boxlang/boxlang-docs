[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Xml`

This type represents an XML Object in BoxLang

## Xml Methods

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
<summary><code>clone()</code></summary>

Clone this XML object
</details>
<details>
<summary><code>getNodeType()</code></summary>

Get XML values according to given xPath query
</details>
<details>
<summary><code>keyExists(key=[any])</code></summary>

Tests whether a key exists in a struct and returns a boolean value

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `key` | `any` | `true` | `null` |

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

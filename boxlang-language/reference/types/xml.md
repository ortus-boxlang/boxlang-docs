
# Type: `Xml`

This type represents an XML Object in BoxLang

## Xml Methods

<details>
<summary><code>bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])</code></summary>

Outputs the contents of a variable (simple or complex) of any type for debugging purposes to a specific output location.

<p>
 The available <code>output</code> locations are:
 - <strong>buffer</strong>: The output is written to the buffer, which is the default location. If running on a web server, the output is written to the browser.
 - <strong>console</strong>: The output is printed to the System console.
 - <strong>Absolute File Path</strong> The output is written to a file with the specified absolute file path.
 </p>
 
 The output `format` can be either HTML or plain text.
 
 The default format is HTML if the output location is the buffer or a web server or a file, otherwise it is plain text for the console.

### Method Signature

```
bxDump(label=[string], depth=[numeric], maxRows=[numeric], top=[numeric], expand=[boolean], abort=[boolean], output=[string], format=[string], showUDFs=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `label` | `string` | `false` | A custom label to display above the dump (Only in HTML output) |  |
| `depth` | `numeric` | `false` | The recursion depth to display when dumping nested collections. 1-based: -1 (default) is unlimited, 0 shows nothing,<br>                 1 shows the top level with no recursion, 2 recurses once, etc. (Only in HTML output) |  |
| `maxRows` | `numeric` | `false` | The maximum number of keys/rows/items to display per level of a collection, array, or query. 1-based: -1 (default)<br>                   is unlimited, 0 shows nothing, 1 shows a single row, etc. (Only in HTML output) |  |
| `top` | `numeric` | `false` | Deprecated: use maxRows instead. When maxRows is not also passed, top's value is used as maxRows.<br>               Kept for backwards compatibility with existing BoxLang code. (Only in HTML output) |  |
| `expand` | `boolean` | `false` | Whether to expand the dump. Be default, we try to expand as much as possible. (Only in HTML output) | `true` |
| `abort` | `boolean` | `false` | Whether to do a hard abort the request after dumping. Default is false | `false` |
| `output` | `string` | `false` | The output format which can be "buffer", "console", or "{absolute file path}". The default is "buffer". |  |
| `format` | `string` | `false` | The format of the output to a <strong>filename</strong>. Can be "html" or "text". The default is according to the output location. |  |
| `showUDFs` | `boolean` | `false` | Show UDFs or not. Default is true. (Only in HTML output) | `true` |
</details>
<details>
<summary><code>childPos(childname=[string], n=[integer])</code></summary>

Gets the position of a child element within an XML document object.

The position, in an XmlChildren array, of the Nth child that has the specified name.

### Method Signature

```
childPos(childname=[string], n=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `childname` | `string` | `true` | The name of the child element. |  |
| `n` | `integer` | `true` | The position of the child element. 1-based. |  |
</details>
<details>
<summary><code>clone()</code></summary>

Clone this XML object

### Method Signature

```
clone()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>getNodeType()</code></summary>

Get XML values according to given xPath query

### Method Signature

```
getNodeType()
```

### Arguments

This function does not accept any arguments
</details>
<details>
<summary><code>keyExists(key=[any])</code></summary>

Tests whether a key exists in a struct and returns a boolean value

### Method Signature

```
keyExists(key=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `key` | `any` | `true` | The key within the struct to test for existence |  |
</details>
<details>
<summary><code>search(xpath=[String], params=[Struct])</code></summary>

Get XML values according to given xPath query

### Method Signature

```
search(xpath=[String], params=[Struct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `xpath` | `String` | `true` | The xpath query to search for |  |
| `params` | `Struct` | `false` | The parameters to pass to the xpath query | `{}` |
</details>
<details>
<summary><code>transform(XSL=[String], parameters=[Struct], XMLSettings=[struct])</code></summary>

Get XML values according to given xPath query

### Method Signature

```
transform(XSL=[String], parameters=[Struct], XMLSettings=[struct])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `XSL` | `String` | `true` | The XSL to use for the transformation |  |
| `parameters` | `Struct` | `false` | The parameters to pass to the xsl transformation | `{}` |
| `XMLSettings` | `struct` | `false` |  |  |
</details>




## Examples



[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Stream`



## Stream Methods

<details>
<summary><code>toBXList(delimiter=[string])</code></summary>

Collect a Java stream into a BoxLang delimited list.

Each item in the stream will cast
 to a string and then be joined with the delimiter.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `delimiter` | `string` | `false` | `,` |

</details>
<details>
<summary><code>toBXArray()</code></summary>

Collect a Java stream into a BoxLang Array
</details>
<details>
<summary><code>toBXQuery(query=[query])</code></summary>

Collect a Java stream into a BoxLang Query.

Provde an empty query to populate.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `query` | `query` | `true` | `null` |

</details>
<details>
<summary><code>toBXStruct(type=[string])</code></summary>

Collect a Java stream into a BoxLang Struct.

Must be a stream of Map.Entry instances.

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `type` | `string` | `false` | `default` |

</details>


## Examples

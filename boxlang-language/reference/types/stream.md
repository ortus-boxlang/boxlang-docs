# stream

## Stream Methods

<details>

<summary><code>toBXList(delimiter=[string])</code></summary>

Collect a Java stream into a BoxLang delimited list.

Each item in the stream will cast to a string and then be joined with the delimiter.

Arguments:

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

</details>

<details>

<summary><code>toBXStruct(type=[string])</code></summary>

Collect a Java stream into a BoxLang Struct.

Must be a stream of Map.Entry instances.

Arguments:

</details>

## Examples

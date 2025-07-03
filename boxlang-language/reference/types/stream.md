# stream

## Stream Methods

<details>

<summary><code>toBXList(delimiter=[string])</code></summary>

Collect a Java stream into a BoxLang delimited list.

Each item in the stream will cast\
to a string and then be joined with the delimiter.

Arguments:

| Argument    | Type     | Required | Default |
| ----------- | -------- | -------- | ------- |
| `delimiter` | `string` | `false`  | `,`     |

</details>

<details>

<summary><code>toBXArray()</code></summary>

Collect a Java stream into a BoxLang Array

</details>

<details>

<summary><code>toBXQuery(query=[query])</code></summary>

Collect a Java stream into a BoxLang Query.

Provide a template query to match the columns and types of the stream.\
Once the stream collects, it will return a Query object that can be used in BoxLang.

,

### ,Usage,

,

,

```
,
// Create a query template
templateQuery = queryNew( "id,name,age" );
// Create a stream from an array of structs
stream = [ {id:1, name:"John", age:30}, {id:2, name:"Jane", age:25} ].toStream();
// Convert the stream to a query
result = stream.toBXQuery( templateQuery );
,
```

Arguments:

| Argument | Type    | Required | Default |
| -------- | ------- | -------- | ------- |
| `query`  | `query` | `true`   | `null`  |

</details>

<details>

<summary><code>toBXStruct(type=[string])</code></summary>

Collect a Java stream into a BoxLang Struct.

Must be a stream of Map.Entry instances.

Arguments:

| Argument | Type     | Required | Default   |
| -------- | -------- | -------- | --------- |
| `type`   | `string` | `false`  | `default` |

</details>

## Examples

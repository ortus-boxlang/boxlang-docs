
# Type: `Class`

In BoxLang, the `class` type is represented by the native Java class `ortus.boxlang.runtime.runnables.IClassRunnable`. The member functions below are provided by the BoxLang runtime and can be called directly on the value, in addition to the methods of the underlying Java class.

## Class Methods

<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>Query Format Options</h2>
 The <code>queryFormat</code> argument determines how queries are serialized:
 <ul>
 <li><code>row</code> or <code>false</code>: Serializes the query as a top-level struct with two keys:
 <code>columns</code> (an array of column names) and <code>data</code> (an array of arrays representing
 each row's data).</li>
 <li><code>column</code> or <code>true</code>: Serializes the query as a top-level struct with three keys:
 <code>rowCount</code> (the number of rows), <code>columns</code> (an array of column names), and
 <code>data</code> (a struct where each key is a column name and the value is an array of values for that column).</li>
 <li><code>struct</code>: Serializes the query as an array of structs, where each struct represents a row of data.</li>
 </ul>

 <h2>Usage</h2>

 <pre>
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 </pre>

### Method Signature

```
toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `queryFormat` | `string` | `false` | If the variable is a query, specifies whether to serialize the query by rows or by columns. Valid values are:<br>                       <code>row</code> same as <code>false</code>, <code>column</code> same as <code>true</code>, or <code>struct</code>. Defaults to <code>row</code>. |  |
| `useSecureJSONPrefix` | `string` | `false` | If true, the JSON string is prefixed with a secure JSON prefix. (Not implemented yet) | `false` |
| `useCustomSerializer` | `boolean` | `false` | If true, the JSON string is serialized using a custom serializer. (Not implemented yet) |  |
| `pretty` | `boolean` | `false` | If true, the JSON string is formatted with indentation and line breaks for readability. Defaults to false. | `false` |
</details>




## Examples



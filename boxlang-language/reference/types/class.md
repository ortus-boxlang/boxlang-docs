[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the type class, itself)

# Type: `Class`



## Class Methods

<details>
<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

<h2>,Query Format Options,</h2>,
 The ,<code>,queryFormat,</code>, argument determines how queries are serialized:
 ,<ul>,
 ,<li>,<code>,row,</code>, or ,<code>,false,</code>,: Serializes the query as a top-level struct with two keys:
 ,<code>,columns,</code>, (an array of column names) and ,<code>,data,</code>, (an array of arrays representing
 each row's data).,</li>,
 ,<li>,<code>,column,</code>, or ,<code>,true,</code>,: Serializes the query as a top-level struct with three keys:
 ,<code>,rowCount,</code>, (the number of rows), ,<code>,columns,</code>, (an array of column names), and
 ,<code>,data,</code>, (a struct where each key is a column name and the value is an array of values for that column).,</li>,
 ,<li>,<code>,struct,</code>,: Serializes the query as an array of structs, where each struct represents a row of data.,</li>,
 ,</ul>,

 ,<h2>,Usage,</h2>,
 
 ,<pre>,
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 ,</pre>

Arguments:

| Argument | Type | Required | Default |
|----------|------|----------|---------|
| `queryFormat` | `string` | `false` | `row` |
| `useSecureJSONPrefix` | `string` | `false` | `false` |
| `useCustomSerializer` | `boolean` | `false` | `null` |
| `pretty` | `boolean` | `false` | `false` |

</details>


## Examples

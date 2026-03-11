# class

## Class Methods

<details>

<summary><code>toJSON(queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])</code></summary>

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

### ,Query Format Options,

, The ,`,queryFormat,`, argument determines how queries are serialized: ,

* , ,
* ,`,row,`, or ,`,false,`,: Serializes the query as a top-level struct with two keys: ,`,columns,`, (an array of column names) and ,`,data,`, (an array of arrays representing each row's data).,
* , ,
* ,`,column,`, or ,`,true,`,: Serializes the query as a top-level struct with three keys: ,`,rowCount,`, (the number of rows), ,`,columns,`, (an array of column names), and ,`,data,`, (a struct where each key is a column name and the value is an array of values for that column).,
* , ,
* ,`,struct,`,: Serializes the query as an array of structs, where each struct represents a row of data.,
* , ,

,

,

### ,Usage,

,

,

```
,
// Convert a query to JSON
myQuery = ...;
json = jsonSerialize( myQuery, queryFormat="row" );
// Convert a list to JSON
myList = "foo,bar,baz";
jsonList = jsonSerialize( myList );
,
```

Arguments:

| Argument              | Type      | Required | Default |
| --------------------- | --------- | -------- | ------- |
| `queryFormat`         | `string`  | `false`  | `row`   |
| `useSecureJSONPrefix` | `string`  | `false`  | `false` |
| `useCustomSerializer` | `boolean` | `false`  | `null`  |
| `pretty`              | `boolean` | `false`  | `false` |

</details>

## Examples

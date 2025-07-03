# JSONSerialize

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string according to the specified options.

## Query Format Options

The `queryFormat` argument determines how queries are serialized:

* `row` or `false`: Serializes the query as a top-level struct with two keys:`columns` (an array of column names) and `data` (an array of arrays representing\
  each row's data).
* `column` or `true`: Serializes the query as a top-level struct with three keys:`rowCount` (the number of rows), `columns` (an array of column names), and`data` (a struct where each key is a column name and the value is an array of values for that column).
* `struct`: Serializes the query as an array of structs, where each struct represents a row of data.

## Usage

```
 // Convert a query to JSON
 myQuery = ...;
 json = jsonSerialize( myQuery, queryFormat="row" );
 // Convert a list to JSON
 myList = "foo,bar,baz";
 jsonList = jsonSerialize( myList );
 
```

## Method Signature

```
JSONSerialize(data=[any], queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean], pretty=[boolean])
```

### Arguments

| Argument              | Type      | Required | Description                                                                                                                                                                                                                                                               | Default |
| --------------------- | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `data`                | `any`     | `true`   | The variable to convert to a JSON string.                                                                                                                                                                                                                                 |         |
| `queryFormat`         | `string`  | `false`  | <p>If the variable is a query, specifies whether to serialize the query by rows or by columns. Valid values are:<br><code>row</code> same as <code>false</code>, <code>column</code> same as <code>true</code>, or <code>struct</code>. Defaults to <code>row</code>.</p> | `row`   |
| `useSecureJSONPrefix` | `string`  | `false`  | If true, the JSON string is prefixed with a secure JSON prefix. (Not implemented yet)                                                                                                                                                                                     | `false` |
| `useCustomSerializer` | `boolean` | `false`  | If true, the JSON string is serialized using a custom serializer. (Not implemented yet)                                                                                                                                                                                   |         |
| `pretty`              | `boolean` | `false`  | If true, the JSON string is formatted with indentation and line breaks for readability. Defaults to false.                                                                                                                                                                | `false` |

## Examples

## Related

* [DataNavigate](DataNavigate.md)
* [JSONDeserialize](JSONDeserialize.md)
* [JSONPrettify](JSONPrettify.md)
* [LSParseNumber](LSParseNumber.md)
* [ParseNumber](ParseNumber.md)
* [ToBase64](ToBase64.md)
* [ToBinary](ToBinary.md)
* [ToModifiable](ToModifiable.md)
* [ToNumeric](ToNumeric.md)
* [ToScript](ToScript.md)
* [ToString](ToString.md)
* [ToUnmodifiable](ToUnmodifiable.md)

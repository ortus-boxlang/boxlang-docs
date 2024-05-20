# JSONSerialize

Converts a ColdFusion variable into a JSON (JavaScript Object Notation) string.

## Method Signature

```
JSONSerialize(var=[any], queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])
```

### Arguments

| Argument              | Type      | Required   | Description                                                                                 | Default   |
| --------------------- | --------- | ---------- | ------------------------------------------------------------------------------------------- | --------- |
| `var`                 | `any`     | `true`     | The variable to convert to a JSON string.                                                   |           |
| `queryFormat`         | `string`  | `false`    | If the variable is a query, specifies whether to serialize the query by rows or by columns. | row       |
| `useSecureJSONPrefix` | `boolean` | `false`    | If true, the JSON string is prefixed with a secure JSON prefix.                             | false     |
| `useCustomSerializer` | `boolean` | `false`    | If true, the JSON string is serialized using a custom serializer. (Not used)                |           |
| ----------            | ------    | ---------- | -------------                                                                               | --------- |

## Examples

```
JSONSerialize(var=[any], queryFormat=[string], useSecureJSONPrefix=[boolean], useCustomSerializer=[boolean])
```

## Related

* [DataNavigate](datanavigate.md)
* [JSONDeserialize](jsondeserialize.md)
* [ParseNumber](parsenumber.md)
* [serializeJSON](serializejson.md)
* [ToBase64](tobase64.md)
* [ToBinary](tobinary.md)
* [ToNumeric](tonumeric.md)
* [ToScript](toscript.md)
* [ToString](tostring.md)

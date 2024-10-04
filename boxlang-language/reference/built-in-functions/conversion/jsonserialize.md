# JSONSerialize

Converts a BoxLang variable into a JSON (JavaScript Object Notation) string.

## Method Signature

```
JSONSerialize(var=[any], queryFormat=[string], useSecureJSONPrefix=[string], useCustomSerializer=[boolean])
```

### Arguments

| Argument              | Type      | Required | Description                                                                                 | Default |
| --------------------- | --------- | -------- | ------------------------------------------------------------------------------------------- | ------- |
| `var`                 | `any`     | `true`   | The variable to convert to a JSON string.                                                   |         |
| `queryFormat`         | `string`  | `false`  | If the variable is a query, specifies whether to serialize the query by rows or by columns. | `row`   |
| `useSecureJSONPrefix` | `string`  | `false`  | If true, the JSON string is prefixed with a secure JSON prefix.                             | `false` |
| `useCustomSerializer` | `boolean` | `false`  | If true, the JSON string is serialized using a custom serializer. (Not used)                |         |

## Examples

## Related

* [DataNavigate](datanavigate.md)
* [JSONDeserialize](jsondeserialize.md)
* [JSONPrettify](jsonprettify.md)
* [LSParseNumber](lsparsenumber.md)
* [ParseNumber](parsenumber.md)
* [ToBase64](tobase64.md)
* [ToBinary](tobinary.md)
* [ToImmutable](toimmutable.md)
* [ToMutable](tomutable.md)
* [ToNumeric](tonumeric.md)
* [ToScript](toscript.md)
* [ToString](tostring.md)

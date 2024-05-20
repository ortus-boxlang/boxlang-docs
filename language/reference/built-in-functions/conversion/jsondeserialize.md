# JSONDeserialize

Converts a JSON (JavaScript Object Notation) string data representation into data, such as a structure or array.

## Method Signature

```
JSONDeserialize(json=[string], strictMapping=[boolean], useCustomSerializer=[string])
```

### Arguments

| Argument              | Type      | Required   | Description                                                                                                  | Default   |
| --------------------- | --------- | ---------- | ------------------------------------------------------------------------------------------------------------ | --------- |
| `json`                | `string`  | `true`     | The JSON string to convert to data.                                                                          |           |
| `strictMapping`       | `boolean` | `false`    | A Boolean value that specifies whether to convert the JSON strictly. If true, everything becomes structures. | true      |
| `useCustomSerializer` | `string`  | `false`    | A string that specifies the name of a custom serializer to use. (Not used)                                   |           |
| ----------            | ------    | ---------- | -------------                                                                                                | --------- |

## Examples

```
JSONDeserialize(json=[string], strictMapping=[boolean], useCustomSerializer=[string])
```

## Related

* [DataNavigate](datanavigate.md)
* [JSONSerialize](jsonserialize.md)
* [ParseNumber](parsenumber.md)
* [serializeJSON](serializejson.md)
* [ToBase64](tobase64.md)
* [ToBinary](tobinary.md)
* [ToNumeric](tonumeric.md)
* [ToScript](toscript.md)
* [ToString](tostring.md)

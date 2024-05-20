# ToBase64

Calculates the Base64 representation of a string or binary object.

## Method Signature

```
ToBase64(string_or_object=[any], encoding=[string])
```

### Arguments

| Argument           | Type     | Required   | Description                                                                  | Default   |
| ------------------ | -------- | ---------- | ---------------------------------------------------------------------------- | --------- |
| `string_or_object` | `any`    | `true`     | A string or a binary object.                                                 |           |
| `encoding`         | `string` | `false`    | The character encoding (character set) of the string, used with binary data. | UTF-8     |
| ----------         | ------   | ---------- | -------------                                                                | --------- |

## Examples

```
ToBase64(string_or_object=[any], encoding=[string])
```

## Related

* [DataNavigate](datanavigate.md)
* [JSONDeserialize](jsondeserialize.md)
* [JSONSerialize](jsonserialize.md)
* [ParseNumber](parsenumber.md)
* [serializeJSON](serializejson.md)
* [ToBinary](tobinary.md)
* [ToNumeric](tonumeric.md)
* [ToScript](toscript.md)
* [ToString](tostring.md)

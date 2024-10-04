# ToBase64

Calculates the Base64 representation of a string or binary object.

The Base64 format uses printable characters, allowing binary data to be sent in forms and e-mail, and stored in a database or file.

## Method Signature

```
ToBase64(string_or_object=[any], encoding=[string])
```

### Arguments

| Argument           | Type     | Required | Description                                                                  | Default |
| ------------------ | -------- | -------- | ---------------------------------------------------------------------------- | ------- |
| `string_or_object` | `any`    | `true`   | A string or a binary object.                                                 |         |
| `encoding`         | `string` | `false`  | The character encoding (character set) of the string, used with binary data. | `UTF-8` |

## Examples

## Related

* [DataNavigate](datanavigate.md)
* [JSONDeserialize](jsondeserialize.md)
* [JSONPrettify](jsonprettify.md)
* [JSONSerialize](jsonserialize.md)
* [LSParseNumber](lsparsenumber.md)
* [ParseNumber](parsenumber.md)
* [ToBinary](tobinary.md)
* [ToImmutable](ToImmutable.md)
* [ToMutable](ToMutable.md)
* [ToNumeric](tonumeric.md)
* [ToScript](toscript.md)
* [ToString](tostring.md)

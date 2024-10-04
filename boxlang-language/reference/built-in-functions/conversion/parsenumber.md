# ParseNumber

Converts a string to a number in the specified numeral system

## Method Signature

```
ParseNumber(number=[string], locale=[string], radix=[string])
```

### Arguments

| Argument | Type     | Required | Description                                                                                                                            | Default |
| -------- | -------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `number` | `string` | `true`   | The string to convert to a number.                                                                                                     |         |
| `locale` | `string` | `false`  | The locale to use when parsing the number. If not provided, the system or application-configured locale is used.                       |         |
| `radix`  | `string` | `false`  | The numeral system to use for conversion (e.g., "bin", "oct", "dec", "hex"). If not provided, the number is parsed as locale-sensitive |         |

## Examples

## Related

* [DataNavigate](datanavigate.md)
* [JSONDeserialize](jsondeserialize.md)
* [JSONPrettify](jsonprettify.md)
* [JSONSerialize](jsonserialize.md)
* [LSParseNumber](lsparsenumber.md)
* [ToBase64](tobase64.md)
* [ToBinary](tobinary.md)
* [ToImmutable](ToImmutable.md)
* [ToMutable](ToMutable.md)
* [ToNumeric](tonumeric.md)
* [ToScript](toscript.md)
* [ToString](tostring.md)

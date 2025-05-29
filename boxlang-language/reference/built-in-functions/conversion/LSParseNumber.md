[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSParseNumber`

Converts a string to a number in the specified numeral system

## Method Signature

```
LSParseNumber(number=[string], locale=[string], radix=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `string` | `true` | The string to convert to a number. |  |
| `locale` | `string` | `false` | The locale to use when parsing the number. If not provided, the system or application-configured locale is used. |  |
| `radix` | `string` | `false` | The numeral system to use for conversion (e.g., "bin", "oct", "dec", "hex"). If not provided, the number is parsed as locale-sensitive |  |

## Examples



## Related

  * [ToNumeric](./ToNumeric.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [ToScript](./ToScript.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)
  * [ToBase64](./ToBase64.md)
  * [DataNavigate](./DataNavigate.md)
  * [ParseNumber](./ParseNumber.md)
  * [ToBinary](./ToBinary.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToString](./ToString.md)
  * [JSONSerialize](./JSONSerialize.md)

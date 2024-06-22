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

  * [DataNavigate](./DataNavigate.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [ParseNumber](./ParseNumber.md)
  * [ToBase64](./ToBase64.md)
  * [ToBinary](./ToBinary.md)
  * [ToImmutable](./ToImmutable.md)
  * [ToMutable](./ToMutable.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)

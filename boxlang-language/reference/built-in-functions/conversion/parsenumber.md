[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ParseNumber`

Converts a string to a number in the specified numeral system

## Method Signature
```
ParseNumber(number=[string], radix=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `string` | `true` | The string to convert to a number. |  |
| `radix` | `string` | `false` | The numeral system to use for conversion (e.g., "bin", "oct", "dec", "hex"). |  |

## Examples

```
ParseNumber(number=[string], radix=[string])
```

## Related
  * [DataNavigate](DataNavigate.md)
  * [JSONDeserialize](JSONDeserialize.md)
  * [JSONSerialize](JSONSerialize.md)
  * [serializeJSON](serializeJSON.md)
  * [ToBase64](ToBase64.md)
  * [ToBinary](ToBinary.md)
  * [ToNumeric](ToNumeric.md)
  * [ToScript](ToScript.md)
  * [ToString](ToString.md)

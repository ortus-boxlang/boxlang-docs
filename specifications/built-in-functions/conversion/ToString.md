[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToString`

Converts a value to a string.

## Method Signature
```
ToString(value=[any], encoding=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | Value to convert to a string; can be a simple value such as an integer, a binary object, or an XML document object. | |
| `encoding` | `string` | `false` | The character encoding (character set) of the string, used with binary data. | |
|----------|------|----------|-------------|---------|



## Examples

```
ToString(value=[any], encoding=[string])
```

## Related
  * [DataNavigate](DataNavigate.md)
  * [JSONDeserialize](JSONDeserialize.md)
  * [JSONSerialize](JSONSerialize.md)
  * [ParseNumber](ParseNumber.md)
  * [serializeJSON](serializeJSON.md)
  * [ToBase64](ToBase64.md)
  * [ToBinary](ToBinary.md)
  * [ToNumeric](ToNumeric.md)
  * [ToScript](ToScript.md)

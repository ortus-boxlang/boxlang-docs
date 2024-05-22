[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToBase64`

Calculates the Base64 representation of a string or binary object.

## Method Signature
```
ToBase64(string_or_object=[any], encoding=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string_or_object` | `any` | `true` | A string or a binary object. |  |
| `encoding` | `string` | `false` | The character encoding (character set) of the string, used with binary data. | `UTF-8` |

## Examples

```
ToBase64(string_or_object=[any], encoding=[string])
```

## Related
  * [DataNavigate](./DataNavigate.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [ParseNumber](./ParseNumber.md)
  * [serializeJSON](./serializeJSON.md)
  * [ToBinary](./ToBinary.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)

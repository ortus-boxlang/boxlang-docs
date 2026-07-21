[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToBinary`

Calculates the binary representation of Base64-encoded data.

## Method Signature

```
ToBinary(base64_or_object=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `base64_or_object` | `any` | `true` | A string containing base64-encoded data. |  |

## Examples

### Decode a Base64 string to binary

```java
encoded = toBase64( "Hello, World!" );
result = toBinary( encoded );
writeOutput( isBinary( result ) );

```

Result: true

## Related

  * [DataNavigate](./DataNavigate.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ParseNumber](./ParseNumber.md)
  * [ToBase64](./ToBase64.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)

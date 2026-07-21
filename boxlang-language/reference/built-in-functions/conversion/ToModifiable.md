[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToModifiable`

Convert an array, struct, query or set to its Modifiable counterpart.

## Method Signature

```
ToModifiable(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The array, struct, query or set to convert. |  |

## Examples

### Convert to a modifiable copy

```java
data = { name: "test" };
frozen = toUnmodifiable( data );
modifiable = toModifiable( frozen );
modifiable.name = "changed";
writeOutput( modifiable.name );

```

Result: changed

## Related

  * [DataNavigate](./DataNavigate.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ParseNumber](./ParseNumber.md)
  * [ToBase64](./ToBase64.md)
  * [ToBinary](./ToBinary.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)

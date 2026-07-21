[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToUnmodifiable`

Convert an array, struct, query or set to its Unmodifiable counterpart.

## Method Signature

```
ToUnmodifiable(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The array, struct, query or set to convert. |  |

## Examples

### Convert to an unmodifiable (immutable) copy

```java
data = { name: "test" };
frozen = toUnmodifiable( data );
writeOutput( isObject( frozen ) );

```

Result: true

### Mutating an unmodifiable struct throws an error

```java
data = [ 1, 2, 3 ];
frozen = data.toUnmodifiable();
try {
    frozen.append( 4 );
    writeOutput( "error" );
} catch ( any e ) {
    writeOutput( "caught" );
}

```

Result: caught

## Related

  * [DataNavigate](./DataNavigate.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ParseNumber](./ParseNumber.md)
  * [ToBase64](./ToBase64.md)
  * [ToBinary](./ToBinary.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)

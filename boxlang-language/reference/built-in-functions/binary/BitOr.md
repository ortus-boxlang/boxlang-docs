[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitOr`

Performs a bitwise logical OR operation.

## Method Signature

```
BitOr(number1=[long], number2=[long])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number1` | `long` | `true` | Numeric value for bitwise OR. |  |
| `number2` | `long` | `true` | Numeric value for bitwise OR. |  |

## Examples

### Calculate bitwise logical OR

Uses the bitOr function to perform the logical OR operation on each pair of the corresponding bits

<a href="https://try.boxlang.io/?code=eJxLyizxL9JQMNVRMFbQtOYCACLPA4s%3D" target="_blank">Run Example</a>

```java
bitOr( 5, 3 );

```

Result: 7

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSMos8S%2FSUDDRUTA0slDQVNC05ipHlleySSqyU8IQhmozNNBRMIDoAgCeFxlj" target="_blank">Run Example</a>

```java
writeOutput( bitOr( 4, 128 ) );
writeOutput( "<br>" );
writeOutput( bitOr( 10, 0 ) );

```



## Related

  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitNot](./BitNot.md)
  * [BitSh](./BitSh.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

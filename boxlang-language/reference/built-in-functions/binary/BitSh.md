[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitSh`

Performs a bitwise shift-left or shift-right, no-rotation operation.

## Method Signature

```
BitSh(number=[integer], count=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `integer` | `true` | Numeric value to shift. |  |
| `count` | `integer` | `true` | Number of bits to shift (Integer in the range 0-31, inclusive). |  |

## Examples

### Shift right by 1 bit

Uses the function bitShrn to perform a bitwise shift-right operation (no-rotation)

<a href="https://try.boxlang.io/?code=eJxLyiwJzijK01Aw1VEwVNC05gIAMI8EYw%3D%3D" target="_blank">Run Example</a>

```java
bitShrn( 5, 1 );

```

Result: 2

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSMosCfYI8tNQMDSy0FEwVdBU0LTmAgDORwm6" target="_blank">Run Example</a>

```java
writeOutput( bitSHRN( 128, 5 ) );

```



## Related

  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitNot](./BitNot.md)
  * [BitOr](./BitOr.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

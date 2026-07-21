[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitMaskSet`

Performs a bitwise mask set operation.

## Method Signature

```
BitMaskSet(number=[long], mask=[long], start=[integer], length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `long` | `true` | 64-bit signed integer value for the bitwise mask set. |  |
| `mask` | `long` | `true` | 64-bit signed integer value for the mask. |  |
| `start` | `integer` | `true` | Start bit for the set mask (Integer in the range 0-31, inclusive). |  |
| `length` | `integer` | `true` | Length of bits in the set mask (Integer in the range 0-31, inclusive). |  |

## Examples

### Bitwise Mask Set

Performs masking operation on each of the corresponding bits

<a href="https://try.boxlang.io/?code=eJxLyizxTSzODk4t0VAw01Ew1FEwAJIKmtZcAGsZBno%3D" target="_blank">Run Example</a>

```java
bitMaskSet( 6, 1, 0, 1 );

```

Result: 7

### Using non zero start parameter

Bit shift the mask 2 places

<a href="https://try.boxlang.io/?code=eJxLyizxTSzODk4t0VAwNNBRMNRRMAKSCprWXABx9Aan" target="_blank">Run Example</a>

```java
bitMaskSet( 10, 1, 2, 1 );

```

Result: 14

### Using non zero mask start and length parameters



<a href="https://try.boxlang.io/?code=eJxLyizxTSzODk4t0VAwNNBRMNJRMASSCprWXABx%2FAao" target="_blank">Run Example</a>

```java
bitMaskSet( 10, 2, 1, 2 );

```

Result: 12

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSMos8U0szg5OBbKNTE11IAQIKWgqaFpzlSMrVrJJKrJTwhDGMMMQiA10FEwgRgAAn0IgKQ%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( bitMaskSet( 255, 255, 5, 5 ) );
writeOutput( "<br>" );
writeOutput( bitMaskSet( 255, 15, 0, 4 ) );

```



## Related

  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitNot](./BitNot.md)
  * [BitOr](./BitOr.md)
  * [BitSh](./BitSh.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

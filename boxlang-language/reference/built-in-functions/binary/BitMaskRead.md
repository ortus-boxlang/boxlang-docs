[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitMaskRead`

Performs a bitwise mask read operation.

## Method Signature

```
BitMaskRead(number=[integer], start=[integer], length=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `integer` | `true` | 32-bit signed integer from which to read the mask. |  |
| `start` | `integer` | `true` | Start bit for the read mask (Integer in the range 0-31, inclusive). |  |
| `length` | `integer` | `true` | Length of bits in the read mask (Integer in the range 0-31, inclusive). |  |

## Examples

### Bitwise Mask Read

Uses the bitMaskRead function to read each of the corresponding bits specified in the mask

<a href="https://try.boxlang.io/?code=eJxLyizxTSzODkpNTNFQMNZRMNBRMFTQtOYCAGABBko%3D" target="_blank">Run Example</a>

```java
bitMaskRead( 3, 0, 1 );

```

Result: 1

### Using non zero start parameter

Bit shift the mask 2 places

<a href="https://try.boxlang.io/?code=eJxLyizxTSzODkpNTNFQMDTQUTDSUTBU0LTmAgBmzAZ6" target="_blank">Run Example</a>

```java
bitMaskRead( 10, 2, 1 );

```

Result: 0

### Using non zero read mask start and length parameters



<a href="https://try.boxlang.io/?code=eJxLyizxTSzODkpNTNFQMDTQUTDUUTBW0LTmAgBmzgZ7" target="_blank">Run Example</a>

```java
bitMaskRead( 10, 1, 3 );

```

Result: 5

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSMos8U0szg5KTUzRUDAyNdVRACEFTQVNa65yZIVKNklFdkoYwpj6DXQUTCD6AeqjHy8%3D" target="_blank">Run Example</a>

```java
writeOutput( bitMaskRead( 255, 5, 5 ) );
writeOutput( "<br>" );
writeOutput( bitMaskRead( 255, 0, 4 ) );

```



## Related

  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitNot](./BitNot.md)
  * [BitOr](./BitOr.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

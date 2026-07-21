[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitNot`

Performs a bitwise logical NOT operation.

## Method Signature

```
BitNot(number=[long])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `long` | `true` | Numeric value for bitwise NOT. |  |

## Examples

### Calculate bitwise logical NOT

Uses the bitNot function to perform the logical NOT operation of a signed 32-bit integer (two's complement)

<a href="https://try.boxlang.io/?code=eJxLyizxyy%2FRUDBQ0LTmAgAdxQN3" target="_blank">Run Example</a>

```java
bitNot( 0 );

```

Result: -1

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSMos8csH0gYKmgqa1lzlyHJKNklFdkoYwjAtRqamEE0ATLQZFw%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( bitNot( 0 ) );
writeOutput( "<br>" );
writeOutput( bitNot( 255 ) );

```



## Related

  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitOr](./BitOr.md)
  * [BitSh](./BitSh.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

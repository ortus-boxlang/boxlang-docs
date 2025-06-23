[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitXor`

Performs a bitwise logical XOR operation.

## Method Signature

```
BitXor(number1=[integer], number2=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number1` | `integer` | `true` | Numeric value for bitwise XOR. |  |
| `number2` | `integer` | `true` | Numeric value for bitwise XOR. |  |

## Examples

### Calculate bitwise logical XOR

Uses the bitXor function to perform the logical XOR operation on each pair of the corresponding bits

<a href="https://try.boxlang.io/?code=eJxLyiyJyC%2FSUDDVUTBW0LTmAgAqBwQD" target="_blank">Run Example</a>

```java
bitXor( 5, 3 );

```

Result: 6

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQSMosicgv0lAwNLLQUTBV0FTQtOYCAMcpCbg%3D" target="_blank">Run Example</a>

```java
writeOutput( bitXor( 128, 5 ) );

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

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitAnd`

Performs a bitwise logical AND operation.

## Method Signature

```
BitAnd(number1=[integer], number2=[integer])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number1` | `integer` | `true` | Numeric value for bitwise AND. |  |
| `number2` | `integer` | `true` | Numeric value for bitwise AND. |  |

## Examples

### Calculate bitwise logical AND

Uses the bitAnd function to perform the logical AND operation on each pair of the corresponding bits, by multiplying them

<a href="https://try.boxlang.io/?code=eJxLyixxzEvRUDDVUTBW0LTmAgAoNgPd" target="_blank">Run Example</a>

```java
bitAnd( 5, 3 );

```

Result: 1

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLzCsoLQlLzClNNVSwVTC15sqECxgBBYxMgULlRZklqf6lJUAJDYWkzBLHvBQNBYQ6Qx0FZE2aCppoWpRskorslEDCmfhtMyDLLgCxcz%2FZ" target="_blank">Run Example</a>

```java
inputValue1 = 5;
inputValue2 = 255;
writeOutput( bitAnd( inputValue1, inputValue2 ) );
writeOutput( "<br>" );
inputValue1 = 5;
inputValue2 = 0;
writeOutput( bitAnd( inputValue1, inputValue2 ) );

```



## Related

  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitNot](./BitNot.md)
  * [BitOr](./BitOr.md)
  * [BitSh](./BitSh.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

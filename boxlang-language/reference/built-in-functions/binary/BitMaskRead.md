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

```
BitMaskRead(number=[integer], start=[integer], length=[integer])
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

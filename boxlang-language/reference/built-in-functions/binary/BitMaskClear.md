[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitMaskClear`

Performs a bitwise mask clear operation.

## Method Signature
```
BitMaskClear(number=[integer], start=[integer], length=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `integer` | `true` | 32-bit signed integer on which the mask clear operation is performed. |  |
| `start` | `integer` | `true` | Start bit for the clear mask (Integer in the range 0-31, inclusive). |  |
| `length` | `integer` | `true` | Length of bits in the clear mask (Integer in the range 0-31, inclusive). |  |

## Examples

```
BitMaskClear(number=[integer], start=[integer], length=[integer])
```

## Related
  * [BinaryDecode](./BinaryDecode.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitNot](./BitNot.md)
  * [BitOr](./BitOr.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)
  * [BitXor](./BitXor.md)

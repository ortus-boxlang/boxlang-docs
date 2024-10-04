# BitMaskSet

Performs a bitwise mask set operation.

## Method Signature

```
BitMaskSet(number=[integer], mask=[integer], start=[integer], length=[integer])
```

### Arguments

| Argument | Type      | Required | Description                                                            | Default |
| -------- | --------- | -------- | ---------------------------------------------------------------------- | ------- |
| `number` | `integer` | `true`   | Numeric value for the bitwise mask set.                                |         |
| `mask`   | `integer` | `true`   | Numeric value for the mask.                                            |         |
| `start`  | `integer` | `true`   | Start bit for the set mask (Integer in the range 0-31, inclusive).     |         |
| `length` | `integer` | `true`   | Length of bits in the set mask (Integer in the range 0-31, inclusive). |         |

## Examples

## Related

* [BinaryDecode](binarydecode.md)
* [BinaryEncode](binaryencode.md)
* [BitAnd](bitand.md)
* [BitMaskClear](bitmaskclear.md)
* [BitMaskRead](bitmaskread.md)
* [BitNot](bitnot.md)
* [BitOr](bitor.md)
* [bitShln](bitshln.md)
* [bitShrn](bitshrn.md)
* [BitXor](bitxor.md)

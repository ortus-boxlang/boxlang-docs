# BitMaskRead

Performs a bitwise mask read operation.

## Method Signature

```
BitMaskRead(number=[integer], start=[integer], length=[integer])
```

### Arguments

| Argument | Type      | Required | Description                                                             | Default |
| -------- | --------- | -------- | ----------------------------------------------------------------------- | ------- |
| `number` | `integer` | `true`   | 32-bit signed integer from which to read the mask.                      |         |
| `start`  | `integer` | `true`   | Start bit for the read mask (Integer in the range 0-31, inclusive).     |         |
| `length` | `integer` | `true`   | Length of bits in the read mask (Integer in the range 0-31, inclusive). |         |

## Examples

## Related

* [BinaryDecode](binarydecode.md)
* [BinaryEncode](binaryencode.md)
* [BitAnd](bitand.md)
* [BitMaskClear](bitmaskclear.md)
* [BitMaskSet](bitmaskset.md)
* [BitNot](bitnot.md)
* [BitOr](bitor.md)
* [bitShln](bitshln.md)
* [bitShrn](bitshrn.md)
* [BitXor](bitxor.md)

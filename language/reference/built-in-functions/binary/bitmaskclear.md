# BitMaskClear

Performs a bitwise mask clear operation.

## Method Signature

```
BitMaskClear(number=[integer], start=[integer], length=[integer])
```

### Arguments

| Argument   | Type      | Required   | Description                                                              | Default   |
| ---------- | --------- | ---------- | ------------------------------------------------------------------------ | --------- |
| `number`   | `integer` | `true`     | 32-bit signed integer on which the mask clear operation is performed.    |           |
| `start`    | `integer` | `true`     | Start bit for the clear mask (Integer in the range 0-31, inclusive).     |           |
| `length`   | `integer` | `true`     | Length of bits in the clear mask (Integer in the range 0-31, inclusive). |           |
| ---------- | ------    | ---------- | -------------                                                            | --------- |

## Examples

```
BitMaskClear(number=[integer], start=[integer], length=[integer])
```

## Related

* [BinaryDecode](binarydecode.md)
* [BinaryEncode](binaryencode.md)
* [BitAnd](bitand.md)
* [BitMaskRead](bitmaskread.md)
* [BitMaskSet](bitmaskset.md)
* [BitNot](bitnot.md)
* [BitOr](bitor.md)
* [bitShln](bitshln.md)
* [bitShrn](bitshrn.md)
* [BitXor](bitxor.md)

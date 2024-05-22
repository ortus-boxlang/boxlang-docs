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
  * [BinaryDecode](boxlang-language/reference/built-in-functions/BinaryDecode.md)
  * [BinaryEncode](boxlang-language/reference/built-in-functions/BinaryEncode.md)
  * [BitAnd](boxlang-language/reference/built-in-functions/BitAnd.md)
  * [BitMaskRead](boxlang-language/reference/built-in-functions/BitMaskRead.md)
  * [BitMaskSet](boxlang-language/reference/built-in-functions/BitMaskSet.md)
  * [BitNot](boxlang-language/reference/built-in-functions/BitNot.md)
  * [BitOr](boxlang-language/reference/built-in-functions/BitOr.md)
  * [bitShln](boxlang-language/reference/built-in-functions/bitShln.md)
  * [bitShrn](boxlang-language/reference/built-in-functions/bitShrn.md)
  * [BitXor](boxlang-language/reference/built-in-functions/BitXor.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BitMaskSet`

Performs a bitwise mask set operation.

## Method Signature
```
BitMaskSet(number=[integer], mask=[integer], start=[integer], length=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `integer` | `true` | Numeric value for the bitwise mask set. |  |
| `mask` | `integer` | `true` | Numeric value for the mask. |  |
| `start` | `integer` | `true` | Start bit for the set mask (Integer in the range 0-31, inclusive). |  |
| `length` | `integer` | `true` | Length of bits in the set mask (Integer in the range 0-31, inclusive). |  |

## Examples

```
BitMaskSet(number=[integer], mask=[integer], start=[integer], length=[integer])
```

## Related
  * [BinaryDecode](boxlang-language/reference/built-in-functions/BinaryDecode.md)
  * [BinaryEncode](boxlang-language/reference/built-in-functions/BinaryEncode.md)
  * [BitAnd](boxlang-language/reference/built-in-functions/BitAnd.md)
  * [BitMaskClear](boxlang-language/reference/built-in-functions/BitMaskClear.md)
  * [BitMaskRead](boxlang-language/reference/built-in-functions/BitMaskRead.md)
  * [BitNot](boxlang-language/reference/built-in-functions/BitNot.md)
  * [BitOr](boxlang-language/reference/built-in-functions/BitOr.md)
  * [bitShln](boxlang-language/reference/built-in-functions/bitShln.md)
  * [bitShrn](boxlang-language/reference/built-in-functions/bitShrn.md)
  * [BitXor](boxlang-language/reference/built-in-functions/BitXor.md)

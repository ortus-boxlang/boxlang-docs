[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `bitShrn`

Performs a bitwise shift-left or shift-right, no-rotation operation.

## Method Signature
```
bitShrn(number=[integer], count=[integer])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `integer` | `true` | Numeric value to shift. | |
| `count` | `integer` | `true` | Number of bits to shift (Integer in the range 0-31, inclusive). | |
|----------|------|----------|-------------|---------|



## Examples

```
bitShrn(number=[integer], count=[integer])
```

## Related
  * [BinaryDecode](BinaryDecode.md)
  * [BinaryEncode](BinaryEncode.md)
  * [BitAnd](BitAnd.md)
  * [BitMaskClear](BitMaskClear.md)
  * [BitMaskRead](BitMaskRead.md)
  * [BitMaskSet](BitMaskSet.md)
  * [BitNot](BitNot.md)
  * [BitOr](BitOr.md)
  * [bitShln](bitShln.md)
  * [BitXor](BitXor.md)

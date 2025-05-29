[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `BinaryDecode`

Encodes binary data to a string with the specified algorithm

## Method Signature

```
BinaryDecode(string=[string], encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | The string to decode that has binary encoded data |  |
| `encoding` | `string` | `true` | The encoding type to use for decoding the binary data. Valid values are: Hex, UU, Base64, Base64Url |  |

## Examples

### Decode a string using hex back into binary encoding of the string

use binaryDecode to decode with hex

<a href="https://try.boxlang.io/?code=eJxLysxLLKp0SU3OT0nVUFByMzNyUtJRUMpIrVBS0LTmAgCgUAip" target="_blank">Run Example</a>

```java
binaryDecode( "F62B", "hex" );

```

Result: [B@1a0d6c79

### Decode a string using UNIX UUencode (UU) back into binary encoding of the string

use binaryDecode to decode with UNIX UUencode (UU)

<a href="https://try.boxlang.io/?code=eJxLysxLLKp0SU3OT0nVUFBSswk3DLIyi3RX0lFQCg1VUtC05gIAxowJag%3D%3D" target="_blank">Run Example</a>

```java
binaryDecode( "&<W1R:6YG", "UU" );

```

Result: [B@20fe6ce1

### Decode a string using base64 back into binary encoding of the string

use binaryDecode to decode with base64

<a href="https://try.boxlang.io/?code=eJxLysxLLKp0SU3OT0nVUFAKNQ6qTAw3zVPSUVBKSixONTNRUtC05gIA9ccLJw%3D%3D" target="_blank">Run Example</a>

```java
binaryDecode( "U3RyaW5n", "base64" );

```

Result: [B@2a0e22fa

### Create a byte array with 16 bytes

Each byte in the array is set to 0

<a href="https://try.boxlang.io/?code=eJxLLCpKrPRJzdNQSMrMSyyqdElNzk9J1VBQMiAAlHQUlDJSK5QUNBU0rbkA1%2FwRiA%3D%3D" target="_blank">Run Example</a>

```java
arrayLen( binaryDecode( "00000000000000000000000000000000", "hex" ) );

```

Result: 16

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLSixOjTczUbBVCMl3ArLNTDQUlDwVEnMVEhWKS4oy89L1lBQ0rbmSMvMSiyrjUxJLEiFqwXwNhSSofqCS1Lzk%2FJTUlHiIUqAqiBpXsDBQJcIEHQWljNQKsLkppbkFGlCVLqkQlagGwRWDlAMAIkc3%2Fg%3D%3D" target="_blank">Run Example</a>

```java
base_64 = ToBase64( "I am a string." );
binary_data = ToBinary( base_64 );
encoded_binary = BinaryEncode( binary_data, "hex" );
dump( BinaryDecode( encoded_binary, "hex" ) );

```



## Related

  * [BitNot](./BitNot.md)
  * [BitXor](./BitXor.md)
  * [BitOr](./BitOr.md)
  * [BitAnd](./BitAnd.md)
  * [BitMaskRead](./BitMaskRead.md)
  * [BitMaskSet](./BitMaskSet.md)
  * [BitMaskClear](./BitMaskClear.md)
  * [BinaryEncode](./BinaryEncode.md)
  * [bitShln](./bitShln.md)
  * [bitShrn](./bitShrn.md)

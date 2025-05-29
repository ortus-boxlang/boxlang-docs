[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ToBase64`

Calculates the Base64 representation of a string or binary object.

The Base64 format uses printable characters, allowing binary data to be sent in
 forms and e-mail, and stored in a database or file.

## Method Signature

```
ToBase64(string_or_object=[any], encoding=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string_or_object` | `any` | `true` | A string or a binary object. |  |
| `encoding` | `string` | `false` | The character encoding (character set) of the string, used with binary data. | `UTF-8` |

## Examples

### String Example

Converts a String to a Base64-String.

<a href="https://try.boxlang.io/?code=eJwLyXdKLE41M9FQUApJLS5RCC4pysxLV1LQtOYCAHaPB%2Fo%3D" target="_blank">Run Example</a>

```java
ToBase64( "Test String" );

```

Result: VGVzdCBTdHJpbmc=

### Binary Object Example

Converts an Image Binary to a Base64-String.


```java
ToBase64( ToBinary( ImageRead( "example.jpg" ) ) );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FAIyXdKLE41M9FQUIIxlRQ0FTStuRT09RXC3C2dIyP8cvyyAm25AFw%2BDSQ%3D" target="_blank">Run Example</a>

```java
dump( ToBase64( "ToBase64" ) );
 // VG9CYXNlNjQ=

```



## Related

  * [ToNumeric](./ToNumeric.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [ToScript](./ToScript.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)
  * [DataNavigate](./DataNavigate.md)
  * [ParseNumber](./ParseNumber.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ToBinary](./ToBinary.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToString](./ToString.md)
  * [JSONSerialize](./JSONSerialize.md)

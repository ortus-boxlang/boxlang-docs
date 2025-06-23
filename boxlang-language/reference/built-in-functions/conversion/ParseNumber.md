[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ParseNumber`

Converts a string to a number in the specified numeral system

## Method Signature

```
ParseNumber(number=[string], locale=[string], radix=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `number` | `string` | `true` | The string to convert to a number. |  |
| `locale` | `string` | `false` | The locale to use when parsing the number. If not provided, the system or application-configured locale is used. |  |
| `radix` | `string` | `false` | The numeral system to use for conversion (e.g., "bin", "oct", "dec", "hex"). If not provided, the number is parsed as locale-sensitive |  |

## Examples

### Convert decimal number to binary



<a href="https://try.boxlang.io/?code=eJwrSCwqTvUrzU1KLdJQMDQwNNBRUErKzFNS0LTmAgCF7Afm" target="_blank">Run Example</a>

```java
parseNumber( 1010, "bin" );

```

Result: 10

### Convert decimal number to hex



<a href="https://try.boxlang.io/?code=eJwrSCwqTvUrzU1KLdJQMDQwNNBRUMpIrVBS0LTmAgCGPAfy" target="_blank">Run Example</a>

```java
parseNumber( 1010, "hex" );

```

Result: 4112

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLK81NSi1SsFVQMjQwMFCy5kpNzsjXUAhILCpO9QPLaSjkgWkdBaWU1GQlBU0FTWsFfX0FkHq8qpMy8xCqLfAqzU8uQSg1NTTCqzgjtQKimAuk2sTA0owLAG2kODM%3D" target="_blank">Run Example</a>

```java
number = "1000";
echo( ParseNumber( number, "dec" ) ); // 1000
echo( ParseNumber( number, "bin" ) ); // 8
echo( ParseNumber( number, "oct" ) ); // 512
echo( ParseNumber( number, "hex" ) );
 // 4096

```



## Related

  * [DataNavigate](./DataNavigate.md)
  * [JSONDeserialize](./JSONDeserialize.md)
  * [JSONPrettify](./JSONPrettify.md)
  * [JSONSerialize](./JSONSerialize.md)
  * [LSParseNumber](./LSParseNumber.md)
  * [ToBase64](./ToBase64.md)
  * [ToBinary](./ToBinary.md)
  * [ToModifiable](./ToModifiable.md)
  * [ToNumeric](./ToNumeric.md)
  * [ToScript](./ToScript.md)
  * [ToString](./ToString.md)
  * [ToUnmodifiable](./ToUnmodifiable.md)

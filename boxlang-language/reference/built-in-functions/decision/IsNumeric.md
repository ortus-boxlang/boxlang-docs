[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsNumeric`

Tests whether a value is numeric

## Method Signature

```
IsNumeric(string=[any], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `any` | `true` |  |  |
| `locale` | `string` | `false` | Optional locale string, otherwise the context locale default is used when parsing string values |  |

## Examples

### Simple Lsisnumeric Example

Check whether the string is number or not in locale

<a href="https://try.boxlang.io/?code=eJzLKfYs9ivNTS3KTNZQUApJzVNS0LTmAgBZgQaw" target="_blank">Run Example</a>

```java
lsIsNumeric( "Ten" );

```

Result: false

### Simple Lsisnumeric Example

Check whether the string is number or not in locale

<a href="https://try.boxlang.io/?code=eJzLKfYs9ivNTS3KTNZQUDIxM7dQUtC05gIAXLgGYg%3D%3D" target="_blank">Run Example</a>

```java
lsIsNumeric( "4678" );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSc0vLSkoLdFQyCn2LPYrzU0tykzWUFAyNDJWUtBUUFNQskkqsgMyrbnKcatOyyxLJUG5sZ6RIQnKDQwMjUhSrmcANh6%2FMkM9YyNDHQMDNJMV9PUV0hJzilOJ0qujoJSeWpSbmIfuPpAxJUWlqVwAR9doVw%3D%3D" target="_blank">Run Example</a>

```java
writeoutput( lsIsNumeric( "123" ) & "<br>" );
writeoutput( lsIsNumeric( "five" ) & "<br>" );
writeoutput( lsIsNumeric( "3.21" ) & "<br>" );
writeoutput( lsIsNumeric( "0012" ) & "<br>" );
writeoutput( lsIsNumeric( "00.01" ) );
writeoutput( lsIsNumeric( "1.321,00" ) & "<br>" ); // false
writeoutput( lsIsNumeric( "1.321,00", "german" ) & "<br>" );
 // true

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsBinary](./IsBinary.md)
  * [IsDate](./IsDate.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsDefined](./IsDefined.md)
  * [IsEmpty](./IsEmpty.md)
  * [structIsEmpty](./structIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsObject](./IsObject.md)
  * [IsDateObject](./IsDateObject.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsValid](./IsValid.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsLeapYear](./IsLeapYear.md)
  * [IsQuery](./IsQuery.md)
  * [IsArray](./IsArray.md)
  * [IsJSON](./IsJSON.md)
  * [IsXML](./IsXML.md)
  * [IsIPv6](./IsIPv6.md)
  * [IsNull](./IsNull.md)
  * [IsClosure](./IsClosure.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStruct](./IsStruct.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsFileObject](./IsFileObject.md)

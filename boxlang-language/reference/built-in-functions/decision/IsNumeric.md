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
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsBoxSet](./IsBoxSet.md)
  * [IsClosure](./IsClosure.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsDate](./IsDate.md)
  * [IsDateObject](./IsDateObject.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsDefined](./IsDefined.md)
  * [IsEmpty](./IsEmpty.md)
  * [IsFileObject](./IsFileObject.md)
  * [IsIPv6](./IsIPv6.md)
  * [IsJSON](./IsJSON.md)
  * [IsLeapYear](./IsLeapYear.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsNull](./IsNull.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsObject](./IsObject.md)
  * [IsQuery](./IsQuery.md)
  * [IsRange](./IsRange.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStringBuilder](./IsStringBuilder.md)
  * [IsStruct](./IsStruct.md)
  * [IsValid](./IsValid.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)

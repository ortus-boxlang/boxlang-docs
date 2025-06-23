[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsSimpleValue`

Determine whether the given value is a string, boolean, numeric, or date value.

## Method Signature

```
IsSimpleValue(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `false` | Value to test for simple-ness. |  |

## Examples

### A number is a simple value



<a href="https://try.boxlang.io/?code=eJzLLA7OzC3ISQ1LzClN1VAwMVLQtOYCAFTKBoA%3D" target="_blank">Run Example</a>

```java
isSimpleValue( 42 );

```

Result: true

### A string is a simple value as well



<a href="https://try.boxlang.io/?code=eJzLLA7OzC3ISQ1LzClN1VBQ8kjNyclXKM8vyklRUtC05gIAwFQKmg%3D%3D" target="_blank">Run Example</a>

```java
isSimpleValue( "Hello world" );

```

Result: true

### A structure is a complex value

So it can't a be simple value

<a href="https://try.boxlang.io/?code=eJzLLA7OzC3ISQ1LzClN1VAoLikqTS7xSy3X0FTQtOYCALCMCjo%3D" target="_blank">Run Example</a>

```java
isSimpleValue( structNew() );

```

Result: false

### An array is a complex value



<a href="https://try.boxlang.io/?code=eJzLLA7OzC3ISQ1LzClN1VBILCpKrPRLLddQMFTQVNC05gIAwT8KJQ%3D%3D" target="_blank">Run Example</a>

```java
isSimpleValue( arrayNew( 1 ) );

```

Result: false

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQyCwOzswtyEkNS8wpTdVQUCouKcrMS1dS0FRQU1CySSqyAzKtucrxaDE0MjYxNSNBQ3pqSUhmbmpVfl6qhiYJ%2BvLyy0lSn5VYlpicWAyUUErOSCxS0lFQcgR5jAQbS3NyIExSdEXHkqC4upYExYWlqUWVfqnlQB%2BVpBaXQDwD1AMAZpWTJw%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( isSimpleValue( "string" ) & "<br>" );
writeOutput( isSimpleValue( 123456 ) & "<br>" );
writeOutput( isSimpleValue( getTimezone() ) & "<br>" );
writeOutput( isSimpleValue( now() ) & "<br>" );
writeOutput( isSimpleValue( javacast( "char", "A" ) ) & "<br>" );
writeOutput( isSimpleValue( nullValue() ) & "<br>" );
writeOutput( isSimpleValue( [] ) & "<br>" );
writeOutput( isSimpleValue( {} ) & "<br>" );
writeOutput( isSimpleValue( queryNew( "test" ) ) );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
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
  * [IsNumeric](./IsNumeric.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsObject](./IsObject.md)
  * [IsQuery](./IsQuery.md)
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

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsQuery`

Determine whether the given value is a BoxLang Query object.

## Method Signature

```
IsQuery(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | Value to test for query-ness. |  |

## Examples

### Create and populate a query and output the 'name' column as a list if it is a valid query



<a href="https://try.boxlang.io/?code=eJzLS8xNLVawVSgsTS2q9Est11BQygMKKekoKJUlFiVnJBYpKWhac4GlHVNSgvKBKvLAemCiwaklzqk5OVBhHYR%2BoEQG2Zq9UvPAejPTNBQyiwNBauF6gbCai7O8KLMk1b%2B0pKC0RAPifOf8nNLcPJfEkkQ08xQ09UryfTKLSzQ0QWbWcgEAS4NOYQ%3D%3D" target="_blank">Run Example</a>

```java
names = queryNew( "name", "varchar" );
queryAddRow( names );
querySetCell( names, "name", "Seth" );
queryAddRow( names );
querySetCell( names, "name", "Jen" );
if( isQuery( names ) ) {
	writeOutput( queryColumnData( names, "name" ).toList() );
}

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJx9zTELwjAQBeA9v%2BKRKV0szqV7XQQddA72CoVro3cXxH%2BviQ6dnI53D75npHaJgh5%2BIOaEaxIefefaFmeyLKtiiqyEqJgNs2JNhohHJnnt3JiXe8BBTyUG2I9r0HSuhPr%2F6PUe6Rngb4n3vvSbCZO8Wfinf8HqvwHHPj0b" target="_blank">Run Example</a>

```java
testVar = "Hello World";
// Returns false as it is not a query.
dump( IsQuery( testVar ) );
testQuery = QueryNew( "col1" );
// Returns true as it is a query.
dump( IsQuery( testQuery ) );

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
  * [IsNumeric](./IsNumeric.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsObject](./IsObject.md)
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

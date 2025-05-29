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
  * [IsArray](./IsArray.md)
  * [IsJSON](./IsJSON.md)
  * [IsXML](./IsXML.md)
  * [IsIPv6](./IsIPv6.md)
  * [IsNull](./IsNull.md)
  * [IsClosure](./IsClosure.md)
  * [IsNumeric](./IsNumeric.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStruct](./IsStruct.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsFileObject](./IsFileObject.md)

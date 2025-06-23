[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsJSON`

Evaluates whether a string is in valid JSON (JavaScript Object Notation) data interchange format.

## Method Signature

```
IsJSON(var=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `var` | `any` | `true` | The value to test for JSON |  |

## Examples

### isJSON Example

Returns true when the argument is a valid JSON value.

<a href="https://try.boxlang.io/?code=eJzLLPYK9vfTUFCKNtQx0jGOVVLQtOYCAD3kBNc%3D" target="_blank">Run Example</a>

```java
isJSON( "[1,2,3]" );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJydj7FqwzAQhmf7KQ5NDmionBYKxUOTThlSirsFD6f0aASy3ZytGvfpKzkppK49NCAh8Yvv%2B08dm5aeXPmRgEVNNhOPzNgLCZ%2FImWk2TV0lIHZKpnJZCFjA4iHu%2FkC5qd4tQeVKTexR62ikULNoyx6eZETjGqPS5e3dfPEFDZ1pD9AQG7Tmizb583YkDFH%2B8372D%2Bpp%2BaquLWF1pb1lD82610zoI79fTfl%2F%2BW88gfRG3UtQl%2BvUHdqP3EMGR0fcb6nz%2F0ZEqbX2FcJ37A%2FIQ1m4%2BGwXR35FAoUMhxZxVMhztj9lbyGLi%2BmvvYSi0fhhhGGWb41ZwUw%3D" target="_blank">Run Example</a>

```java
writeDump( label="Array", var=isJson( "[1,2,3]" ) );
writeDump( label="Single number value", var=isJson( 1 ) );
writeDump( label="String value", var=isJson( "susi12345" ) );
writeDump( label="String value with serializeJSON", var=isJson( JSONSerialize( "susi" ) ) );
writeDump( label="Boolean value with serializeJSON", var=isJson( JSONSerialize( true ) ) );
writeDump( label="CreateDateTime with serializeJSON", var=isJson( JSONSerialize( CreateDateTime( 2018, 1, 1, 1, 1, 1 ) ) ) );
qry = queryNew( "aaa,bbb", "varchar, varchar", [
	[
		"a",
		"b"
	],
	[
		"c",
		"d"
	]
] );
writeDump( label="Query", var=isJson( qry ) );

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
  * [IsLeapYear](./IsLeapYear.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsNull](./IsNull.md)
  * [IsNumeric](./IsNumeric.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsObject](./IsObject.md)
  * [IsQuery](./IsQuery.md)
  * [IsSimpleValue](./IsSimpleValue.md)
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

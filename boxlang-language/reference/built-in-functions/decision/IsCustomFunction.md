[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsCustomFunction`

Determine whether a given object is a custom function.

## Method Signature

```
IsCustomFunction(object=[any], type=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `object` | `any` | `true` | The value to test for closure-ness. |  |
| `type` | `string` | `false` | Check for a specific type of custom function - `UDF`, `Lambda`, or `Closure`. |  |

## Examples

### isCustomFunction Example

Here we've example to check the given variable is user defined function or not.

<a href="https://try.boxlang.io/?code=eJzjSivNSy7JzM9TyK0EMTU0Faq5OItSS0qL8hQMrblqucqLMktSXUpzCzQUMoudS4tL8nPdoHo0oJoUNBU0rbkA0i0ZNg%3D%3D" target="_blank">Run Example</a>

```java

function myfunc() {
	return 1;
}
writeDump( isCustomFunction( myfunc ) );

```

Result: YES

### isCustomFunction Example

Here we've example to check the given variable is user defined function or not.

<a href="https://try.boxlang.io/?code=eJzLrUwrzUtWsFVQMlKy5iovyixJdSnNLdBQyCx2Li0uyc91A0qXZObnaSjkQpRqKmhacwEABtYSIg%3D%3D" target="_blank">Run Example</a>

```java
myfunc = "2";
writeDump( isCustomFunction( myfunc ) );

```

Result: NO

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUMgsdi4tLsnPdSvNSy7JzM%2FTUChKTcwJdXFT0FTQtOYqx6eyoqICoqoktbgEKKxgC9NszRUB5BgS0A%2FTRtimCIgarjSoCMweDU2Fai7OotSS0qI8kHW1SEqArtNQcMyrVCjLz0xRACms5QIAOE1SOA%3D%3D" target="_blank">Run Example</a>

```java
writeDump( isCustomFunction( realUDF ) );
writeDump( isCustomFunction( xxx ) );
testFun = realUDF;
X = 1;
writeDump( isCustomFunction( testFun ) );
writeDump( isCustomFunction( X ) );

function realUDF() {
	return 1;
}

function xxx( Any void ) {
}

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

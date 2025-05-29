[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsStruct`

Determine whether a value is a struct

## Method Signature

```
IsStruct(variable=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `variable` | `any` | `true` | The value to test for structi-ness. |  |

## Examples

### isStruct Example

Returns true if variable is a Boxlang structure or is a Java object that implements the java.lang.Map interface. 

<a href="https://try.boxlang.io/?code=eJzLLA4uKSpNLtFQKAbTfqnlGpoKmtZcAHq5CFg%3D" target="_blank">Run Example</a>

```java
isStruct( structNew() );

```

Result: true

### isStruct Example for False

Returns false is the object in the variable parameter is a user-defined function UDF).  In the example below exponent is a function created by the user

<a href="https://try.boxlang.io/?code=eJzLLA4uKSpNLtFQSCwqSqz0Sy3XUDBU0FTQtOYCAIeoCEM%3D" target="_blank">Run Example</a>

```java
isStruct( arrayNew( 1 ) );

```

Result: false

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrLilSsFUoLikqTS7xSy3X0LTmKi%2FKLEn1Ly0pKC3RUMgsDgbLaYDUKGgqAOUB1fIRGQ%3D%3D" target="_blank">Run Example</a>

```java
str = structNew();
writeOutput( isStruct( str ) );

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
  * [IsNumeric](./IsNumeric.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsFileObject](./IsFileObject.md)

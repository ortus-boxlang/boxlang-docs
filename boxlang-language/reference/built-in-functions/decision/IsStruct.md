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
  * [IsQuery](./IsQuery.md)
  * [IsRange](./IsRange.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStringBuilder](./IsStringBuilder.md)
  * [IsValid](./IsValid.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsBinary`

Determines whether a value is stored as binary data.

## Method Signature

```
IsBinary(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | The value to test |  |

## Examples

### Checks if toBase64() function returns binary data 

toBase64() returns base64 encoded data which is not binary

<a href="https://try.boxlang.io/?code=eJzLLHbKzEssqtRQKMl3SixONTPRUDBU0FTQtOYCAH7oB6I%3D" target="_blank">Run Example</a>

```java
isBinary( toBase64( 1 ) );

```

Result: false

### Checks if toBinary() function returns binary data 

toBinary() expects base64 encoded data and returns binary data

<a href="https://try.boxlang.io/?code=eJzLLHbKzEssqtRQKMlHYiUWp5qZaCgYKmiCoDUXAAs6C3s%3D" target="_blank">Run Example</a>

```java
isBinary( toBinary( toBase64( 1 ) ) );

```

Result: true

### Additional Examples

<a href="https://try.boxlang.io/?code=eJx1j88KwjAMh%2B8%2BRehpA5ENxIvsYNnFyy76ApkEKfSPpK1lb2%2B7gRftKYHk%2B%2FJLYhVojObVgMaZ9CCkc5rQwht1JLHPlQflpbLISwOBI0EL7XmXfsgpGmL1qJB913c18hZY2WcFFPPaiBp8YcalwmKZTZTy%2BYL%2FF2zLFcPdfV93Ej2djjnRFdAAgl9jH8SmLvIPTkxslQ%3D%3D" target="_blank">Run Example</a>

```java
writeDump( label="Boolean value", var=isBinary( true ) );
writeDump( label="Numeric value", var=isBinary( 1010 ) );
writeDump( label="String value", var=isBinary( "binary" ) );
writeDump( label="Array value", var=isBinary( arrayNew( 1 ) ) );
writeDump( label="Binary value", var=isBinary( ToBinary( toBase64( "I am a string." ) ) ) );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
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
  * [IsStruct](./IsStruct.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsFileObject](./IsFileObject.md)

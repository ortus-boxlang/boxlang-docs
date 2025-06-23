[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsIPv6`

Determine whether the given hostname supports IPv6.

## Method Signature

```
IsIPv6(hostname=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `hostname` | `string` | `false` |  |  |

## Examples

### isIPV6 Example



<a href="https://try.boxlang.io/?code=eJzLLPYMCDPTUFAyNDLXMwBCQyUFTWsuAEPKBNE%3D" target="_blank">Run Example</a>

```java
isIPV6( "127.0.0.1" );

```

Result: false

### Additional Examples

<a href="https://try.boxlang.io/?code=eJzLLFCwVVByc7UwsHJ2MTCwMjAAEc4urlaGRqbmEK6RoaGrlbmRpbOSNVd5UWZJqn9pSUFpiYZCZrFnQJkZkC5Q0FTQtOYCANXQE3Y%3D" target="_blank">Run Example</a>

```java
ip = "FE80:CD00:0000:0CDE:1257:0000:211E:729C";
writeOutput( isIPv6( ip ) );

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
  * [IsJSON](./IsJSON.md)
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

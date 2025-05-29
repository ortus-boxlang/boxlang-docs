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

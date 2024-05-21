[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsSimpleValue`

Determine whether the given value is a string, numeric, or date.Arrays, structs, queries, closures, classes and components, and other complex
 structures will return false.

## Method Signature
```
IsSimpleValue(value=[any])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `false` | Value to test for simple-ness. |  |

## Examples

```
IsSimpleValue(value=[any])
```

## Related
  * [ArrayIsEmpty](ArrayIsEmpty.md)
  * [IsArray](IsArray.md)
  * [IsBinary](IsBinary.md)
  * [IsBoolean](IsBoolean.md)
  * [IsClosure](IsClosure.md)
  * [IsCustomFunction](IsCustomFunction.md)
  * [IsDate](IsDate.md)
  * [IsDateObject](IsDateObject.md)
  * [IsDebugMode](IsDebugMode.md)
  * [IsDefined](IsDefined.md)
  * [IsEmpty](IsEmpty.md)
  * [IsFileObject](IsFileObject.md)
  * [IsIPv6](IsIPv6.md)
  * [IsJSON](IsJSON.md)
  * [IsLeapYear](IsLeapYear.md)
  * [IsLocalHost](IsLocalHost.md)
  * [IsNull](IsNull.md)
  * [IsNumeric](IsNumeric.md)
  * [IsObject](IsObject.md)
  * [IsQuery](IsQuery.md)
  * [IsStruct](IsStruct.md)
  * [IsValid](IsValid.md)
  * [IsXML](IsXML.md)
  * [IsXmlAttribute](IsXmlAttribute.md)
  * [IsXMLDoc](IsXMLDoc.md)
  * [IsXMLElem](IsXMLElem.md)
  * [IsXMLNode](IsXMLNode.md)
  * [IsXMLRoot](IsXMLRoot.md)
  * [structIsEmpty](structIsEmpty.md)

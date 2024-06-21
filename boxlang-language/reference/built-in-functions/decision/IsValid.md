[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsValid`

Determine whether the given value is a string, numeric, or date.Arrays, structs, queries, closures, classes and components, and other complex
 structures will return false.

<p>,
 Note we expressly do not support the `eurodate` type, since date formats vary across EU countries. For this, prefer the `LSIsDate( date, locale )`
 method instead.

## Method Signature

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The type to validate the value against |  |
| `value` | `any` | `true` | Value to test for validaty on a given type |  |
| `min` | `any` | `false` | The minimum value for the range type or a pattern to validate the value against |  |
| `max` | `any` | `false` | The maximum value for the range type |  |
| `pattern` | `any` | `false` | The pattern to validate the value against |  |

## Examples

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
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
  * [IsJSON](./IsJSON.md)
  * [IsLeapYear](./IsLeapYear.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsNull](./IsNull.md)
  * [IsNumeric](./IsNumeric.md)
  * [IsObject](./IsObject.md)
  * [IsQuery](./IsQuery.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStruct](./IsStruct.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)

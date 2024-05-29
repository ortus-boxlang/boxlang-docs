[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsDateObject`

Determine whether a given value or variable reference is a date or dateTime object.

Note that date strings, such as `2021-01-01` and timespans returned from `createTimespan()` are NOT date objects. The former are strings and the
 latter are numeric values.

## Method Signature

```
IsDateObject(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | Value to test for date object-ness |  |

## Examples

```
IsDateObject(value=[any])
```

## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsClosure](./IsClosure.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsDate](./IsDate.md)
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
  * [IsValid](./IsValid.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [structIsEmpty](./structIsEmpty.md)

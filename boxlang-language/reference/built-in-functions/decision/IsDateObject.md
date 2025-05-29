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

### Check if date is a date OBJECT, not just a date string




```java
<bx:script>
	date = IsDateObject( now() );
	writeOutput( "Can string be converted to a date/time value : " & date );
</bx:script>

```

Result: Can string be converted to a date/time value : YES


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

# IsValid

Validates the incoming `value` against the given `type`.

If the type is a range, the value is validated against the range. If the type is a pattern, the value is validated against the pattern. If the type is a date, the value is validated against the date format. If the type is a locale date, the value is validated against the locale date format. If the type is a regular expression, the value is validated against the regular expression.

**Note we expressly do not support the \`eurodate\` type, since date formats vary across EU countries. For this, prefer the \`LSIsDate( date, locale )\` method instead.**

## Valid Types

* array
* binary
* boolean
* component
* creditcard
* date
* email
* float
* function
* guid
* integer
* numeric
* query
* range
* regex
* regular\_expression
* social\_security\_number
* ssn
* string
* struct
* telephone
* time
* time
* url
* usdate
* uuid
* variablename
* xml
* zipcode

## Method Signature

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

### Arguments

| Argument  | Type     | Required | Description                                                                               | Default |
| --------- | -------- | -------- | ----------------------------------------------------------------------------------------- | ------- |
| `type`    | `string` | `true`   | The type to validate the value against                                                    |         |
| `value`   | `any`    | `true`   | Value to test for validaty on a given type                                                |         |
| `min`     | `any`    | `false`  | <p>The minimum value for the range type or a pattern to validate<br>the value against</p> |         |
| `max`     | `any`    | `false`  | The maximum value for the range type                                                      |         |
| `pattern` | `any`    | `false`  | The pattern to validate the value against                                                 |         |

## Examples

## Related

* [ArrayIsEmpty](ArrayIsEmpty.md)
* [Attempt](Attempt.md)
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
* [IsNumericDate](IsNumericDate.md)
* [IsObject](IsObject.md)
* [IsQuery](IsQuery.md)
* [IsSimpleValue](IsSimpleValue.md)
* [IsStruct](IsStruct.md)
* [IsXML](IsXML.md)
* [IsXmlAttribute](IsXmlAttribute.md)
* [IsXMLDoc](IsXMLDoc.md)
* [IsXMLElem](IsXMLElem.md)
* [IsXMLNode](IsXMLNode.md)
* [IsXMLRoot](IsXMLRoot.md)
* [LSIsNumeric](LSIsNumeric.md)
* [structIsEmpty](structIsEmpty.md)

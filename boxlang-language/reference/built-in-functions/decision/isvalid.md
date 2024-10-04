# IsValid

Determine whether the given value is a string, numeric, or date.Arrays, structs, queries, closures, classes and components, and other complex structures will return false.

, Note we expressly do not support the \`eurodate\` type, since date formats vary across EU countries. For this, prefer the \`LSIsDate( date, locale )\` method instead.

## Method Signature

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

### Arguments

| Argument  | Type     | Required | Description                                                                     | Default |
| --------- | -------- | -------- | ------------------------------------------------------------------------------- | ------- |
| `type`    | `string` | `true`   | The type to validate the value against                                          |         |
| `value`   | `any`    | `true`   | Value to test for validaty on a given type                                      |         |
| `min`     | `any`    | `false`  | The minimum value for the range type or a pattern to validate the value against |         |
| `max`     | `any`    | `false`  | The maximum value for the range type                                            |         |
| `pattern` | `any`    | `false`  | The pattern to validate the value against                                       |         |

## Examples

## Related

* [ArrayIsEmpty](arrayisempty.md)
* [Attempt](attempt.md)
* [IsArray](isarray.md)
* [IsBinary](isbinary.md)
* [IsBoolean](isboolean.md)
* [IsClosure](isclosure.md)
* [IsCustomFunction](iscustomfunction.md)
* [IsDate](isdate.md)
* [IsDateObject](isdateobject.md)
* [IsDebugMode](isdebugmode.md)
* [IsDefined](isdefined.md)
* [IsEmpty](isempty.md)
* [IsFileObject](isfileobject.md)
* [IsIPv6](isipv6.md)
* [IsJSON](isjson.md)
* [IsLeapYear](isleapyear.md)
* [IsLocalHost](islocalhost.md)
* [IsNull](isnull.md)
* [IsNumeric](isnumeric.md)
* [IsNumericDate](isnumericdate.md)
* [IsObject](isobject.md)
* [IsQuery](isquery.md)
* [IsSimpleValue](issimplevalue.md)
* [IsStruct](isstruct.md)
* [IsXML](isxml.md)
* [IsXmlAttribute](isxmlattribute.md)
* [IsXMLDoc](isxmldoc.md)
* [IsXMLElem](isxmlelem.md)
* [IsXMLNode](isxmlnode.md)
* [IsXMLRoot](isxmlroot.md)
* [LSIsNumeric](lsisnumeric.md)
* [structIsEmpty](structisempty.md)

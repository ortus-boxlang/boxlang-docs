# IsValid

Determine whether the given value is a string, numeric, or date.Arrays, structs, queries, closures, classes and components, and other complex structures will return false.

## Method Signature

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

### Arguments

| Argument   | Type     | Required   | Description                                | Default   |
| ---------- | -------- | ---------- | ------------------------------------------ | --------- |
| `type`     | `string` | `true`     |                                            |           |
| `value`    | `any`    | `true`     | Value to test for validaty on a given type |           |
| `min`      | `any`    | `false`    |                                            |           |
| `max`      | `any`    | `false`    |                                            |           |
| `pattern`  | `any`    | `false`    |                                            |           |
| ---------- | ------   | ---------- | -------------                              | --------- |

## Examples

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

## Related

* [ArrayIsEmpty](arrayisempty.md)
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
* [structIsEmpty](structisempty.md)

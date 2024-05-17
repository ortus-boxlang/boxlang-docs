# IsDefined

Determine whether a given variable reference exists.

## Method Signature

```
IsDefined(variable=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                                                              | Default |
| ---------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------ | ------- |
| `variable` | `string` | `true`   | The variable reference to test for existence. For security reasons, only dot-notation is supported. Struct/array bracket |         |

```
                notation
                is not supported, nor is function invocation, etc. | |
```

\|----------|------|----------|-------------|---------|

## Examples

```
IsDefined(variable=[string])
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
* [IsValid](isvalid.md)
* [IsXML](isxml.md)
* [IsXmlAttribute](isxmlattribute.md)
* [IsXMLDoc](isxmldoc.md)
* [IsXMLElem](isxmlelem.md)
* [IsXMLNode](isxmlnode.md)
* [IsXMLRoot](isxmlroot.md)
* [structIsEmpty](structisempty.md)

# IsDefined

Determine whether a given variable reference exists.

, For example: ,

* , ,
* ,`,isDefined( "luis" ),`, will test for the existence of an ,`,lmajano,`, variable in any accessible scope.,
* , ,
* ,`,isDefined( "variables.foo" ),`, will test for the existence of a ,`,foo,`, variable in the ,`,variables,`, scope.,
* , ,
* ,`,isDefined( "brad.age" ),`, will test for the existence of an ,`,age,`, key in the ,`,brad,`, struct, in any accessible scope,
* , ,

, ,

## Method Signature

```
IsDefined(variable=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                                                                                                                                       | Default |
| ---------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `variable` | `string` | `true`   | <p>The variable reference to test for existence. For security reasons, only dot-notation is supported. Struct/array bracket<br>notation<br>is not supported, nor is function invocation, etc.</p> |         |

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
* [IsValid](isvalid.md)
* [IsXML](isxml.md)
* [IsXmlAttribute](isxmlattribute.md)
* [IsXMLDoc](isxmldoc.md)
* [IsXMLElem](isxmlelem.md)
* [IsXMLNode](isxmlnode.md)
* [IsXMLRoot](isxmlroot.md)
* [LSIsNumeric](lsisnumeric.md)
* [structIsEmpty](structisempty.md)

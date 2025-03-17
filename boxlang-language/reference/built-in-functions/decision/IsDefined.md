# IsDefined

Determine whether a given variable reference exists.

For example:

* `isDefined( "luis" )` will test for the existence of an `lmajano` variable in any accessible scope.
* `isDefined( "variables.foo" )` will test for the existence of a `foo` variable in the `variables` scope.
* `isDefined( "brad.age" )` will test for the existence of an `age` key in the `brad` struct, in any accessible scope

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
* [IsValid](IsValid.md)
* [IsXML](IsXML.md)
* [IsXmlAttribute](IsXmlAttribute.md)
* [IsXMLDoc](IsXMLDoc.md)
* [IsXMLElem](IsXMLElem.md)
* [IsXMLNode](IsXMLNode.md)
* [IsXMLRoot](IsXMLRoot.md)
* [LSIsNumeric](LSIsNumeric.md)
* [structIsEmpty](structIsEmpty.md)

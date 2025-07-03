# IsDefined

Determine whether a given variable reference exists.

For example:

* `isDefined( "luis" )` will test for the existence of an `lmajano` variable in any accessible scope.
* `isDefined( "variables.foo" )` will test for the existence of a `foo` variable in the `variables` scope.
* `isDefined( "brad.age" )` will test for the existence of an `age` key in the `brad` struct, in any accessible\
  scope

## Method Signature

```
IsDefined(variable=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                                                                                                                                       | Default |
| ---------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `variable` | `string` | `true`   | <p>The variable reference to test for existence. For security reasons, only dot-notation is supported. Struct/array bracket<br>notation<br>is not supported, nor is function invocation, etc.</p> |         |

## Examples

### Using IsDefined

Checking for the existence of a `form` variable.

```java
<bx:if isDefined( "form.submit" ) >...</bx:if>
```

### Scope Evaluation Order and Unscoped Variables

Beware of scope evaluation order when checking for an unscoped variable name.

[Run Example](https://try.boxlang.io/?code=eJwrLcrRc%2FP3V7BVUCoFMtPy85WsudLyi3JhomA2RLi8KLMkNb%2B0pKC0RENBybNYQR0orq6QkpqWmZeaYq%2BgpKCmkFnsAuFqgLTmKyloKmii6cSiBKRXA6QdyAeSSppKClYKSkogrQC9mS57)

```java
url.FOO = "url.foo";
form.FOO = "form.foo";
writeoutput( "Is 'foo' defined? " & isDefined( "foo" ) );
writeoutput( isDefined( "foo" ) ? " (" & foo & ")" : "" );

```

Result: Is 'foo' defined? YES (url.foo)

### Dot-notation Variable Names

Potentially unexpected behavior when checking for a dot-notation variable containing a scope name.

[Run Example](https://try.boxlang.io/?code=eJyNjrsOgjAYhXee4uQMUBYfQFQS48LgpE6GQQSSJmBNL%2FH1TWGplRjH%2F9z%2Bb1D323AFe6XHlXHNKC1RYwsOk5MFRlazSKb7dNkfq7NPhb0ieWlpO%2BXs01kBVgYfdbRdLx9dWxIppDnMl4ie58ijoR%2FREoTwcyFWCubEGuTXFDeN3i3IHjWmRIz5H%2BEC3CxFXG8CzHSZ)

```java
local[ "form.submit" ] = "local['form.submit']";
form.SUBMIT = "form.submit";
writeoutput( "Is 'form.submit' defined?" & isDefined( "form.submit" ) );
writeoutput( isDefined( "form.submit" ) ? " (" & form.SUBMIT & ")" : "" );
writeoutput( "<br>" );
writeoutput( "Is 'submit' defined? " & isDefined( "submit" ) );
writeoutput( isDefined( "submit" ) ? " (" & submit & ")" : "" );

```

Result: Is 'form.submit' defined? YES (local\['form.submit']) Is 'submit' defined? YES(form.submit)

### Additional Examples

[Run Example](https://try.boxlang.io/?code=eJxVjbEOgkAQRGv3KzZXYcN9ALEwQmeLPXKDbiJ35m5PTAj%2FLtgYM81M8jLPWs5J%2FI0l1RjEw%2FEkeuc%2BeCcqwXPSTjHCK8lQ%2FLCCzRDiWEYkqOH9mpl21vIpOLAGvoKbN%2FqscEQLJY184HmptlZejue2WbdRJDUVTVEUdR6f%2F4YNfXWPjK%2BgIl7%2FNWbQB8M5Ojo%3D)

```java
// using isDefined with condition statement
if( isDefined( "form.reset" ) ) {
	// Code to be Executed

}
str = {};
str.VALUE = "test";
writeDump( isDefined( "str.value" ) );
 // true

```

## Related

* [ArrayIsEmpty](ArrayIsEmpty.md)
* [arrayIsEmpty](arrayIsEmpty.md)
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

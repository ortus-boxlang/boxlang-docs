[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsDefined`

Determine whether a given variable reference exists.

<p>
 For example:
 <ul>
 <li><code>isDefined( "luis" )</code> will test for the existence of an <code>lmajano</code> variable in any accessible scope.</li>
 <li><code>isDefined( "variables.foo" )</code> will test for the existence of a <code>foo</code> variable in the <code>variables</code> scope.</li>
 <li><code>isDefined( "brad.age" )</code> will test for the existence of an <code>age</code> key in the <code>brad</code> struct, in any accessible
 scope</li>
 </ul>
 </p>

## Method Signature

```
IsDefined(variable=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `variable` | `string` | `true` | The variable reference to test for existence. For security reasons, only dot-notation is supported. Struct/array bracket<br>                    notation<br>                    is not supported, nor is function invocation, etc. |  |

## Examples

### Using IsDefined

Checking for the existence of a `form` variable.


```java
<bx:if isDefined( "form.submit" ) >...</bx:if>
```


### Scope Evaluation Order and Unscoped Variables

Beware of scope evaluation order when checking for an unscoped variable name.

<a href="https://try.boxlang.io/?code=eJwrLcrRc%2FP3V7BVUCoFMtPy85WsudLyi3JhomA2RLi8KLMkNb%2B0pKC0RENBybNYQR0orq6QkpqWmZeaYq%2BgpKCmkFnsAuFqgLTmKyloKmii6cSiBKRXA6QdyAeSSppKClYKSkogrQC9mS57" target="_blank">Run Example</a>

```java
url.FOO = "url.foo";
form.FOO = "form.foo";
writeoutput( "Is 'foo' defined? " & isDefined( "foo" ) );
writeoutput( isDefined( "foo" ) ? " (" & foo & ")" : "" );

```

Result: Is 'foo' defined? YES (url.foo)

### Dot-notation Variable Names

Potentially unexpected behavior when checking for a dot-notation variable containing a scope name.

<a href="https://try.boxlang.io/?code=eJyNjrsOgjAYhXee4uQMUBYfQFQS48LgpE6GQQSSJmBNL%2FH1TWGplRjH%2F9z%2Bb1D323AFe6XHlXHNKC1RYwsOk5MFRlazSKb7dNkfq7NPhb0ieWlpO%2BXs01kBVgYfdbRdLx9dWxIppDnMl4ie58ijoR%2FREoTwcyFWCubEGuTXFDeN3i3IHjWmRIz5H%2BEC3CxFXG8CzHSZ" target="_blank">Run Example</a>

```java
local[ "form.submit" ] = "local['form.submit']";
form.SUBMIT = "form.submit";
writeoutput( "Is 'form.submit' defined?" & isDefined( "form.submit" ) );
writeoutput( isDefined( "form.submit" ) ? " (" & form.SUBMIT & ")" : "" );
writeoutput( "<br>" );
writeoutput( "Is 'submit' defined? " & isDefined( "submit" ) );
writeoutput( isDefined( "submit" ) ? " (" & submit & ")" : "" );

```

Result: Is 'form.submit' defined? YES (local['form.submit']) Is 'submit' defined? YES(form.submit)

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxVjbEOgkAQRGv3KzZXYcN9ALEwQmeLPXKDbiJ35m5PTAj%2FLtgYM81M8jLPWs5J%2FI0l1RjEw%2FEkeuc%2BeCcqwXPSTjHCK8lQ%2FLCCzRDiWEYkqOH9mpl21vIpOLAGvoKbN%2FqscEQLJY184HmptlZejue2WbdRJDUVTVEUdR6f%2F4YNfXWPjK%2BgIl7%2FNWbQB8M5Ojo%3D" target="_blank">Run Example</a>

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

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsBinary](./IsBinary.md)
  * [IsDate](./IsDate.md)
  * [IsNumericDate](./IsNumericDate.md)
  * [IsEmpty](./IsEmpty.md)
  * [structIsEmpty](./structIsEmpty.md)
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsObject](./IsObject.md)
  * [IsDateObject](./IsDateObject.md)
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

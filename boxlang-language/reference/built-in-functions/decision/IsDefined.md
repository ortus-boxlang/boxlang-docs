[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsDefined`

Determine whether a given variable reference exists.

<p>,
 For example:
 ,<ul>,
 ,<li>,<code>,isDefined( "luis" ),</code>, will test for the existence of an ,<code>,lmajano,</code>, variable in any accessible scope.,</li>,
 ,<li>,<code>,isDefined( "variables.foo" ),</code>, will test for the existence of a ,<code>,foo,</code>, variable in the ,<code>,variables,</code>, scope.,</li>,
 ,<li>,<code>,isDefined( "brad.age" ),</code>, will test for the existence of an ,<code>,age,</code>, key in the ,<code>,brad,</code>, struct, in any accessible
 scope,</li>,
 ,</ul>,
 ,</p>

## Method Signature

```
IsDefined(variable=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `variable` | `string` | `true` | The variable reference to test for existence. For security reasons, only dot-notation is supported. Struct/array bracket<br>                    notation<br>                    is not supported, nor is function invocation, etc. |  |

## Examples



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsClosure](./IsClosure.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsDate](./IsDate.md)
  * [IsDateObject](./IsDateObject.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsEmpty](./IsEmpty.md)
  * [IsFileObject](./IsFileObject.md)
  * [IsIPv6](./IsIPv6.md)
  * [IsJSON](./IsJSON.md)
  * [IsLeapYear](./IsLeapYear.md)
  * [IsLocalHost](./IsLocalHost.md)
  * [IsNull](./IsNull.md)
  * [IsNumeric](./IsNumeric.md)
  * [IsNumericDate](./IsNumericDate.md)
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
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)

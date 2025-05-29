[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsXMLDoc`

Determines whether the function parameter is an Extended Markup language (XML) document object.

## Method Signature

```
IsXMLDoc(value=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `value` | `any` | `true` | Value to test |  |

## Examples

### Checks if a given XML is valid




```java
<bx:xml variable="example">
	<boxlangengines>
		<engine>
			<name>Adobe ColdFusion</name>
		</engine>
		<engine>
			<name>Boxlang</name>
		</engine>
		<engine>
			<name>Railo</name>
		</engine>
		<engine>
			<name>Open BlueDragon</name>
		</engine>
	</boxlangengines>
</bx:xml>
<bx:script>
	writeOutput( isXMLDoc( example ) );
</bx:script>

```

Result: YES

### Additional Examples


```java
<bx:xml variable="xmlobject">
	<office>
		<employee>
			<emp_name>boxlang_dev</emp_name>
			<emp_no>121</emp_no>
		</employee>
	</office>
	</bx:xml>
<bx:dump var="#isxmldoc( xmlobject )#"/>
```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
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

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
  * [arrayIsEmpty](./arrayIsEmpty.md)
  * [Attempt](./Attempt.md)
  * [IsArray](./IsArray.md)
  * [IsBinary](./IsBinary.md)
  * [IsBoolean](./IsBoolean.md)
  * [IsBoxSet](./IsBoxSet.md)
  * [IsClosure](./IsClosure.md)
  * [IsCustomFunction](./IsCustomFunction.md)
  * [IsDate](./IsDate.md)
  * [IsDateObject](./IsDateObject.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsDefined](./IsDefined.md)
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
  * [IsRange](./IsRange.md)
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStringBuilder](./IsStringBuilder.md)
  * [IsStruct](./IsStruct.md)
  * [IsValid](./IsValid.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)

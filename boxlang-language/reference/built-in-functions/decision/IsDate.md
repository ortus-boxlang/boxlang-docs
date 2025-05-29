[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsDate`

Determine whether a given value is a date object or a date string.

## Method Signature

```
IsDate(date=[any], locale=[string], timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | Value to test for date-ness |  |
| `locale` | `string` | `false` | Optional ISO locale string to use for parsing the date/time string. |  |
| `timezone` | `string` | `false` | Optional timezone to use for parsing the date/time string. |  |

## Examples

### Simple example

To determine whether a string can be converted to a date/time value.


```java
<bx:set Date = isNumericDate( now() ) >
<bx:output>#Date#</bx:output>
```

Result: Yes

### Simple example

To determine whether a string can be converted to a date/time value.


```java
<bx:set result = isNumericDate( "Monday" ) >
<bx:output>#result#</bx:output>
```

Result: No

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUMhJTErNsVUKzsxLz0lVyCvNTS3KTFYoS8wpTVXSAdJFtpnFfhBRl8SSVA0FQwVNBU1rrnIMIzzzSlLTU4vw6jWAAVyG%2BOWXa2hi15wHksKlD6QEn81KBob6IGSihMsE38y80mK8RugawgFOU4JLioAhideY1LTilDSoAQBonH0R" target="_blank">Run Example</a>

```java
writeDump( label="Single numeric value", var=isNumericDate( 1 ) );
writeDump( label="Integer value", var=isNumericDate( 1000000000 ) );
writeDump( label="Now()", var=isNumericDate( now() ) );
writeDump( label="Date value", var=isNumericDate( "01/01/04" ) );
writeDump( label="Minus value", var=isNumericDate( "-1111111111" ) );
writeDump( label="String value", var=isNumericDate( "efsdf" ) );

```



## Related

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsBinary](./IsBinary.md)
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

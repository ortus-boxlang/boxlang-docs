# IsValid

Validates the incoming `value` against the given`type`.

If the type is a range, the value is\
validated against the range. If the type is a pattern, the value is validated\
against the pattern. If the type is a\
date, the value is validated against the date format. If the type is a locale\
date, the value is validated against the\
locale date format. If the type is a regular expression, the value is\
validated against the regular expression.

**Note we expressly do not support the \`eurodate\` type, since date formats vary**\
**across EU countries. For this, prefer the \`LSIsDate( date, locale )\`**\
**method instead.**

## Valid Types

* array
* binary
* boolean
* component
* creditcard
* date
* email
* float
* function
* guid
* hex
* integer
* numeric
* query
* range
* regex
* regular\_expression
* social\_security\_number
* ssn
* string
* struct
* telephone
* time
* time
* url
* usdate
* uuid
* variablename
* xml
* zipcode

## Method Signature

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

### Arguments

| Argument  | Type     | Required | Description                                                                               | Default |
| --------- | -------- | -------- | ----------------------------------------------------------------------------------------- | ------- |
| `type`    | `string` | `true`   | The type to validate the value against                                                    |         |
| `value`   | `any`    | `true`   | Value to test for validaty on a given type                                                |         |
| `min`     | `any`    | `false`  | <p>The minimum value for the range type or a pattern to validate<br>the value against</p> |         |
| `max`     | `any`    | `false`  | The maximum value for the range type                                                      |         |
| `pattern` | `any`    | `false`  | The pattern to validate the value against                                                 |         |

## Examples

### Check to see if a 235 is an integer

Use the isValid function with integer as the type.

[Run Example](https://try.boxlang.io/?code=eJzLLA5LzMlM0VBQyswrSU1PLVLSUTAyNlXQtOYCAH0oB7s%3D)

```java
isValid( "integer", 235 );

```

Result: true

### Validate an Email Address

Use the isValid function with email as the type.

[Run Example](https://try.boxlang.io/?code=eJzLLA5LzMlM0VBQSs1NzMxR0lFQKi1OLXJIrUjMLchJ1UvOz1VS0LTmAgAT6QzX)

```java
isValid( "email", "user@example.com" );

```

Result: true

### Additional Examples

```java
<bx:set anArray = [] >
<bx:set boolean = true >
<bx:set email = "test@test.com" >
<bx:set guid = createGUID() >
<bx:set integer = 15 >
<bx:set string = "Hello World" >
<bx:set http_url = "http://www.test.com" >
<bx:set uuid = createUUID() >

<bx:output>
	Array: #isValid( "array", anArray )#<br>
	Boolean: #isValid( "boolean", boolean )#<br>
	Email: #isValid( "email", email )#<br>
	GUID: #isValid( "guid", guid )#<br>
	Integer: #isValid( "integer", integer )#<br>
	String: #isValid( "string", string )#<br>
	URL: #isValid( "url", http_url )#<br>
	UUID: #isValid( "uuid", uuid )#
</bx:output>
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
* [IsDefined](IsDefined.md)
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
* [IsXML](IsXML.md)
* [IsXmlAttribute](IsXmlAttribute.md)
* [IsXMLDoc](IsXMLDoc.md)
* [IsXMLElem](IsXMLElem.md)
* [IsXMLNode](IsXMLNode.md)
* [IsXMLRoot](IsXMLRoot.md)
* [LSIsNumeric](LSIsNumeric.md)
* [structIsEmpty](structIsEmpty.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsValid`

Validates the incoming <code>value</code> against the given
 <code>type</code>.

If the type is a range, the value is
 validated against the range. If the type is a pattern, the value is validated
 against the pattern. If the type is a
 date, the value is validated against the date format. If the type is a locale
 date, the value is validated against the
 locale date format. If the type is a regular expression, the value is
 validated against the regular expression.
 <p>
 <strong>
 Note we expressly do not support the `eurodate` type, since date formats vary
 across EU countries. For this, prefer the `LSIsDate( date, locale )`
 method instead.
 </strong>
 <p>
 <h2>Valid Types</h2>
 <ul>
 <li>array</li>
 <li>binary</li>
 <li>boolean</li>
 <li>component</li>
 <li>creditcard</li>
 <li>date</li>
 <li>email</li>
 <li>float</li>
 <li>function</li>
 <li>guid</li>
 <li>hex</li>
 <li>integer</li>
 <li>numeric</li>
 <li>query</li>
 <li>range</li>
 <li>regex</li>
 <li>regular_expression</li>
 <li>social_security_number</li>
 <li>ssn</li>
 <li>string</li>
 <li>struct</li>
 <li>telephone</li>
 <li>time</li>
 <li>time</li>
 <li>url</li>
 <li>usdate</li>
 <li>uuid</li>
 <li>variablename</li>
 <li>xml</li>
 <li>zipcode</li>
 </ul>

## Method Signature

```
IsValid(type=[string], value=[any], min=[any], max=[any], pattern=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `type` | `string` | `true` | The type to validate the value against |  |
| `value` | `any` | `true` | Value to test for validaty on a given type |  |
| `min` | `any` | `false` | The minimum value for the range type or a pattern to validate<br>               the value against |  |
| `max` | `any` | `false` | The maximum value for the range type |  |
| `pattern` | `any` | `false` | The pattern to validate the value against |  |

## Examples

### Check to see if a 235 is an integer

Use the isValid function with integer as the type.

<a href="https://try.boxlang.io/?code=eJzLLA5LzMlM0VBQyswrSU1PLVLSUTAyNlXQtOYCAH0oB7s%3D" target="_blank">Run Example</a>

```java
isValid( "integer", 235 );

```

Result: true

### Validate an Email Address

Use the isValid function with email as the type.

<a href="https://try.boxlang.io/?code=eJzLLA5LzMlM0VBQSs1NzMxR0lFQKi1OLXJIrUjMLchJ1UvOz1VS0LTmAgAT6QzX" target="_blank">Run Example</a>

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

  * [ArrayIsEmpty](./ArrayIsEmpty.md)
  * [IsXMLDoc](./IsXMLDoc.md)
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

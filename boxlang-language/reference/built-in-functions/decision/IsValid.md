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
  * [IsSimpleValue](./IsSimpleValue.md)
  * [IsStruct](./IsStruct.md)
  * [IsXML](./IsXML.md)
  * [IsXmlAttribute](./IsXmlAttribute.md)
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)
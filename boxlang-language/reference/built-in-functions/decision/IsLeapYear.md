[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `IsLeapYear`

Determine whether a given integer value represents a leap year.

## Method Signature

```
IsLeapYear(year=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `year` | `numeric` | `true` | Number representing the year to test. |  |

## Examples

### Is the current date in a leap year?



<a href="https://try.boxlang.io/?code=eJxLSSxJVbBVyMsv19C05sos9klNLIhMTSwCiiE4GgqVYDIFpFhTAaiwvCizJNW%2FtKSgtEQDSSFICgBT2BqY" target="_blank">Run Example</a>

```java
date = now();
isLeapYear = isLeapYear( year( date ) );
writeOutput( isLeapYear );

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUMhJTErNsVUyMjC0UNJRKEsssvUs9klNLIhMTSzSUAAJK2gqaFpzlWPRYmSAVYuRAS4thljUG0IUAwDp1ytf" target="_blank">Run Example</a>

```java
writeDump( label="2018", var=IsLeapYear( 2018 ) );
writeDump( label="2020", var=IsLeapYear( 2020 ) );
writeDump( label="1", var=IsLeapYear( 1 ) );

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
  * [IsXMLDoc](./IsXMLDoc.md)
  * [IsXMLElem](./IsXMLElem.md)
  * [IsXMLNode](./IsXMLNode.md)
  * [IsXMLRoot](./IsXMLRoot.md)
  * [LSIsNumeric](./LSIsNumeric.md)
  * [structIsEmpty](./structIsEmpty.md)

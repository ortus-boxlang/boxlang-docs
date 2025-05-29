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
  * [IsValid](./IsValid.md)
  * [IsDebugMode](./IsDebugMode.md)
  * [IsBoolean](./IsBoolean.md)
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

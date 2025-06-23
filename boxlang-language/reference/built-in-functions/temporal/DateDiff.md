[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DateDiff`

Returns the numeric difference in the requested date part between two dates

## Method Signature

```
DateDiff(datepart=[string], date1=[any], date2=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `datepart` | `string` | `true` |  |  |
| `date1` | `any` | `true` | The reference date object |  |
| `date2` | `any` | `true` | The date which to compare against date1 |  |

## Examples

### dateDiff Example

Find the difference between two dates.

<a href="https://try.boxlang.io/?code=eJxLSSxJdclMS9NQUEpR0lFQMjIwNNY1MNQ1NEXmGZkqKWhacwEA%2FP0JhQ%3D%3D" target="_blank">Run Example</a>

```java
dateDiff( "d", "2013-01-15", "2013-01-25" );

```

Result: 10

### How old are they?

Calculates a persons age based on a variable birthDate which contains a date. Uses the now function to get current date.

<a href="https://try.boxlang.io/?code=eJxLyiwqyXBJLElVsFVILkoFMkAcDQVDS3MjHQVTHQUjAwVNa67EdJCCFJB0ZlqahoJSJRAo6SgkwbTrKOTll2togtSWF2WWpOaXlhSUlmgogDQCxQBb5x9R" target="_blank">Run Example</a>

```java
birthDate = createDate( 1972, 5, 20 );
age = dateDiff( "yyyy", birthDate, now() );
writeoutput( age );

```


### dateDiff member function


<a href="https://try.boxlang.io/?code=eJw9jEsKg0AQRPeeonA1wiTiOrgICa6EnEHSLQ6EnjDTjdf3g7oqePWqlLO%2BB2W0kDi76lFQGMeD0BpPIoeSSo%2FGQ0979eYUlD%2Bmf1N3FfdtffjXUbXpqGvoFDISqyXJaBAFvX2ZPQYh3Hbwij%2FqLIcoxQLZ7DCY" target="_blank">Run Example</a>

```java
testDate = now();
diffDate = dateAdd( "d", 1, testDate );
writeOutput( testDate.diff( "d", diffDate ) );
```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLTc7I11BwSSxJdclMS9NQUEpR0lFQMjIwNNM1MNM1MkfhWSgpaCqoKSjZJBXZAZnWCvr6CoZcqaQYYY7FCAPSjDDDYoQuFmdkoJqhYGBgBUbowoZQYaL8RqyhBjgNxeJbDEMNSTUUm%2F%2FLUwi61RxPAHCBzDUy4gIAgmpzzQ%3D%3D" target="_blank">Run Example</a>

```java
echo( DateDiff( "d", "2016-06-27", "2016-06-28" ) & "<br>" ); // 1
echo( DateDiff( "d", "2016-06-27", "2016-06-27" ) & "<br>" ); // 0
echo( DateDiff( "d", "2016-06-27", "2016-06-26" ) & "<br>" ); // -1
echo( DateDiff( "h", "2016-06-27 00:00:00", "2016-06-27 01:00:00" ) & "<br>" ); // 1
echo( DateDiff( "h", "2016-06-27 00:00:00", "2016-06-27 00:00:00" ) & "<br>" ); // 0
echo( DateDiff( "h", "2016-06-27 01:00:00", "2016-06-27 00:00:00" ) & "<br>" ); // -1
echo( DateDiff( "wd", "2016-06-27 00:00:00", "2016-07-27 01:00:00" ) & "<br>" );
 // 22

```



## Related

  * [ClearTimezone](./ClearTimezone.md)
  * [CreateDate](./CreateDate.md)
  * [CreateDateTime](./CreateDateTime.md)
  * [CreateODBCDate](./CreateODBCDate.md)
  * [CreateODBCDateTime](./CreateODBCDateTime.md)
  * [CreateODBCTime](./CreateODBCTime.md)
  * [CreateTime](./CreateTime.md)
  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [DateAdd](./DateAdd.md)
  * [DateCompare](./DateCompare.md)
  * [DateConvert](./DateConvert.md)
  * [DateFormat](./DateFormat.md)
  * [DatePart](./DatePart.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [Day](./Day.md)
  * [DayOfWeek](./DayOfWeek.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
  * [DayOfYear](./DayOfYear.md)
  * [DaysInMonth](./DaysInMonth.md)
  * [DaysInYear](./DaysInYear.md)
  * [FirstDayOfMonth](./FirstDayOfMonth.md)
  * [GetNumericDate](./GetNumericDate.md)
  * [GetTime](./GetTime.md)
  * [GetTimezone](./GetTimezone.md)
  * [GetTimezoneInfo](./GetTimezoneInfo.md)
  * [Hour](./Hour.md)
  * [Millisecond](./Millisecond.md)
  * [Minute](./Minute.md)
  * [Month](./Month.md)
  * [MonthAsString](./MonthAsString.md)
  * [MonthShortAsString](./MonthShortAsString.md)
  * [Nanosecond](./Nanosecond.md)
  * [Now](./Now.md)
  * [Offset](./Offset.md)
  * [ParseDateTime](./ParseDateTime.md)
  * [Quarter](./Quarter.md)
  * [Second](./Second.md)
  * [SetTimezone](./SetTimezone.md)
  * [TimeFormat](./TimeFormat.md)
  * [Week](./Week.md)
  * [Year](./Year.md)

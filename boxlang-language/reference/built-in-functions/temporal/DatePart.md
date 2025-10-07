[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DatePart`

Extracts a part from a datetime value as a numeric.

## Method Signature

```
DatePart(datepart=[string], date=[any], timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `datepart` | `string` | `true` | The part of the date to extract. |  |
| `date` | `any` | `true` | The date to extract the part from. |  |
| `timezone` | `string` | `false` | An optional, explicit timezone to apply to the date. |  |

## Examples

### All dateparts

This example shows information available from datePart


```java
<bx:set todayDate = now() >
<h3>datePart Example</h3>
<p>Today's date is <bx:output>#todayDate#</bx:output>.
<p>Using datePart, we extract an integer representing the dateparts from that value <bx:output>
<ul>
<li>year: #datePart( "yyyy", todayDate )#</li>
<li>quarter: #datePart( "q", todayDate )#</li>
<li>month: #datePart( "m", todayDate )#</li>
<li>day of year: #datePart( "y", todayDate )#</li>
<li>day: #datePart( "d", todayDate )#</li>
<li>weekday: #datePart( "w", todayDate )#</li>
<li>week: #datePart( "ww", todayDate )#</li>
<li>hour: #datePart( "h", todayDate )#</li>
<li>minute: #datePart( "n", todayDate )#</li>
<li>second: #datePart( "s", todayDate )#</li>
</ul>
</bx:output>
```


### Additional Examples


```java
writeOutput( "Date for the current date is" & datePart( "d", now() ) );
d1 = CreateDate( 2016, 11, 10 ); // user defined date with member function
writeOutput( "<br>Month of the given date is " & d1.Part( "m", "Asia/Calcutta" ) );

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
  * [DateDiff](./DateDiff.md)
  * [DateFormat](./DateFormat.md)
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
  * [TimeUnits](./TimeUnits.md)
  * [Week](./Week.md)
  * [Year](./Year.md)

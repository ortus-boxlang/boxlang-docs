[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `SetTimezone`

Sets the timezone of the current request context

## Method Signature

```
SetTimezone(timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `true` | The string representation or three character alias of the timezone |  |

## Examples

### Set the current Timezone to CET



<a href="https://try.boxlang.io/?code=eJwrTi0JycxNrcrPS9VQUHJ2DVFS0LTmKi%2FKLEnNLy0pKC3RUEhHKPHMS8vX0NQL8fR1jfL3cwUpBQDe0hVB" target="_blank">Run Example</a>

```java
setTimezone( "CET" );
writeoutput( getTimezoneInfo().TIMEZONE );

```

Result: CET

### Additional Examples


```java
<bx:dump var="#getTimeZone()#">
	<bx:set settimezone( "ART" ) >
	<bx:dump var="#getTimeZone()#">
```



## Related

  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [DateCompare](./DateCompare.md)
  * [Now](./Now.md)
  * [DateDiff](./DateDiff.md)
  * [CreateTime](./CreateTime.md)
  * [ClearTimezone](./ClearTimezone.md)
  * [DateAdd](./DateAdd.md)
  * [Year](./Year.md)
  * [Quarter](./Quarter.md)
  * [Month](./Month.md)
  * [MonthAsString](./MonthAsString.md)
  * [MonthShortAsString](./MonthShortAsString.md)
  * [Day](./Day.md)
  * [DayOfWeek](./DayOfWeek.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
  * [DaysInMonth](./DaysInMonth.md)
  * [DaysInYear](./DaysInYear.md)
  * [DayOfYear](./DayOfYear.md)
  * [FirstDayOfMonth](./FirstDayOfMonth.md)
  * [Week](./Week.md)
  * [Hour](./Hour.md)
  * [Minute](./Minute.md)
  * [Second](./Second.md)
  * [Millisecond](./Millisecond.md)
  * [Nanosecond](./Nanosecond.md)
  * [Offset](./Offset.md)
  * [GetTimezone](./GetTimezone.md)
  * [GetNumericDate](./GetNumericDate.md)
  * [GetTime](./GetTime.md)
  * [CreateDateTime](./CreateDateTime.md)
  * [CreateDate](./CreateDate.md)
  * [GetTimezoneInfo](./GetTimezoneInfo.md)
  * [CreateODBCDateTime](./CreateODBCDateTime.md)
  * [CreateODBCDate](./CreateODBCDate.md)
  * [CreateODBCTime](./CreateODBCTime.md)
  * [DateConvert](./DateConvert.md)
  * [DatePart](./DatePart.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)
  * [ParseDateTime](./ParseDateTime.md)

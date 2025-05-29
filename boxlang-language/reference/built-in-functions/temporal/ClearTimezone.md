[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `ClearTimezone`

Clears the current timezone in the request

## Method Signature

```
ClearTimezone()
```

### Arguments

This function does not accept any arguments

## Examples

### Clear the timezone

Set the timezone and then clear it.

<a href="https://try.boxlang.io/?code=eJwrTi0JycxNjcrPS9VQUHJ2DVFS0LTmKi%2FKLEn1Ly0pKC3RUEiHKKkCKvHMS8vX0NQL8fR1jfL3c1VQU1B61DZJAawnOSc1sQhuFgmGAJUCAM45LCA%3D" target="_blank">Run Example</a>

```java
setTimeZone( "CET" );
writeOutput( getTimezoneInfo().TIMEZONE & "→ " );
clearTimeZone();
writeOutput( getTimezoneInfo().TIMEZONE );

```

Result: CET→ Etc/UTC


## Related

  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [SetTimezone](./SetTimezone.md)
  * [DateCompare](./DateCompare.md)
  * [Now](./Now.md)
  * [DateDiff](./DateDiff.md)
  * [CreateTime](./CreateTime.md)
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

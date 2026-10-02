[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Nanosecond`

Returns the nanosecond of adate object.  If a string is provided as the argument, an attempt will be made to parse it as a date. If parsing fails, an error will be thrown.

## Method Signature

```
Nanosecond(date=[any], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `false` | The date object or date string to be evaluated. |  |
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |

## Examples



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
  * [DatePart](./DatePart.md)
  * [dateSetDay](./dateSetDay.md)
  * [dateSetHour](./dateSetHour.md)
  * [dateSetMinute](./dateSetMinute.md)
  * [dateSetMonth](./dateSetMonth.md)
  * [dateSetSecond](./dateSetSecond.md)
  * [dateSetYear](./dateSetYear.md)
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

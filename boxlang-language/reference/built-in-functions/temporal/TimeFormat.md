[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TimeFormat`

Formats a datetime, date or time

## Method Signature

```
TimeFormat(date=[any], mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | The date string or object |  |
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html) class.<br>                If a common mask is used, the following are supported:<br>                * short: equivalent to "M/d/y h:mm tt"<br>                * medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                * long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                * full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                * ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                * epoch: Total seconds of a given date (Example:1567517664)<br>                * epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |

## Examples



## Related

  * [ClearTimezone](./ClearTimezone.md)
  * [CreateDate](./CreateDate.md)
  * [CreateDateTime](./CreateDateTime.md)
  * [CreateODBCDate](./CreateODBCDate.md)
  * [CreateODBCDateTime](./CreateODBCDateTime.md)
  * [CreateODBCTime](./CreateODBCTime.md)
  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [DateAdd](./DateAdd.md)
  * [DateCompare](./DateCompare.md)
  * [DateConvert](./DateConvert.md)
  * [DateDiff](./DateDiff.md)
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
  * [Week](./Week.md)
  * [Year](./Year.md)

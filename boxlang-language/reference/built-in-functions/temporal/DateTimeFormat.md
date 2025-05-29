[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DateTimeFormat`

Formats a datetime, date or time

## Method Signature

```
DateTimeFormat(date=[any], mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | The date string or object |  |
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html) class.<br>                If a common mask is used, the following are supported:<br>                - short: equivalent to "M/d/y h:mm tt"<br>                - medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                - long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                - full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                - ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                - epoch: Total seconds of a given date (Example:1567517664)<br>                - epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |

## Examples

### Omitting the Mask

Should default mask to `hh:mm tt`

<a href="https://try.boxlang.io/?code=eJwrycxNdcsvyk0s0VBILkpNLEl1AeIQoKiGgpGBobmOgoWOgrGhjoKhqY6CERAbGipoKmhacwEADccPEg%3D%3D" target="_blank">Run Example</a>

```java
timeFormat( createDateTime( 2017, 8, 31, 15, 25, 11 ) );

```

Result: 03:25 pm

### Additional Examples


## Related

  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [SetTimezone](./SetTimezone.md)
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
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)
  * [ParseDateTime](./ParseDateTime.md)

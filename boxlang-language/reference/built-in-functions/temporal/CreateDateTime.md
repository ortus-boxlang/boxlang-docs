[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateDateTime`

Creates a date-time object.

Note that the core implementation of this BIF differs from ACF/Lucee in handling of a year value without a century. BoxLang respects that pre-first century years are valid and and will treat `createDate( 20 )` as 20 AD.
 The behavior modification to emulate ACF/Lucee would require the installation of the `bx-compat` module.

## Method Signature

```
CreateDateTime(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `year` | `integer` | `false` | The year of the date-time object. | `0` |
| `month` | `integer` | `false` | The month of the date-time object. | `1` |
| `day` | `integer` | `false` | The day of the date-time object. | `1` |
| `hour` | `integer` | `false` | The hour of the date-time object. | `0` |
| `minute` | `integer` | `false` | The minute of the date-time object. | `0` |
| `second` | `integer` | `false` | The second of the date-time object. | `0` |
| `millisecond` | `integer` | `false` |  | `0` |
| `timezone` | `string` | `false` |  |  |

## Examples



## Related

  * [ClearTimezone](./ClearTimezone.md)
  * [CreateDate](./CreateDate.md)
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
  * [LSDateFormat](./LSDateFormat.md)
  * [LSDateTimeFormat](./LSDateTimeFormat.md)
  * [LSDayOfWeek](./LSDayOfWeek.md)
  * [LSIsDate](./LSIsDate.md)
  * [LSParseDateTime](./LSParseDateTime.md)
  * [LSTimeFormat](./LSTimeFormat.md)
  * [LSWeek](./LSWeek.md)
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

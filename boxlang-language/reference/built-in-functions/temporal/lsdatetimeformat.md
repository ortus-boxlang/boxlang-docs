[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSDateTimeFormat`

Formats a date in a locale-specific format

## Method Signature
```
LSDateTimeFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | The date string or object |  |
| `mask` | `string` | `false` | Optional format mask, or common mask |  |
| `locale` | `string` | `false` | Optional locale designation of the output ( e.g. es-SA ) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |

## Examples

```
LSDateTimeFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```

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
  * [LSDateFormat](./LSDateFormat.md)
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
  * [WeekOfYear](./WeekOfYear.md)
  * [Year](./Year.md)

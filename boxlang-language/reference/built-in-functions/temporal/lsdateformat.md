[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSDateFormat`

Formats a date in a locale-specific format

## Method Signature
```
LSDateFormat(date=[any], mask=[string], locale=[string], timezone=[string])
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
LSDateFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```

## Related
  * [ClearTimezone](boxlang-language/reference/built-in-functions/ClearTimezone.md)
  * [CreateDate](boxlang-language/reference/built-in-functions/CreateDate.md)
  * [CreateDateTime](boxlang-language/reference/built-in-functions/CreateDateTime.md)
  * [CreateODBCDate](boxlang-language/reference/built-in-functions/CreateODBCDate.md)
  * [CreateODBCDateTime](boxlang-language/reference/built-in-functions/CreateODBCDateTime.md)
  * [CreateODBCTime](boxlang-language/reference/built-in-functions/CreateODBCTime.md)
  * [CreateTimeSpan](boxlang-language/reference/built-in-functions/CreateTimeSpan.md)
  * [DateAdd](boxlang-language/reference/built-in-functions/DateAdd.md)
  * [DateCompare](boxlang-language/reference/built-in-functions/DateCompare.md)
  * [DateConvert](boxlang-language/reference/built-in-functions/DateConvert.md)
  * [DateDiff](boxlang-language/reference/built-in-functions/DateDiff.md)
  * [DateFormat](boxlang-language/reference/built-in-functions/DateFormat.md)
  * [DatePart](boxlang-language/reference/built-in-functions/DatePart.md)
  * [DateTimeFormat](boxlang-language/reference/built-in-functions/DateTimeFormat.md)
  * [Day](boxlang-language/reference/built-in-functions/Day.md)
  * [DayOfWeek](boxlang-language/reference/built-in-functions/DayOfWeek.md)
  * [DayOfWeekAsString](boxlang-language/reference/built-in-functions/DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](boxlang-language/reference/built-in-functions/DayOfWeekShortAsString.md)
  * [DayOfYear](boxlang-language/reference/built-in-functions/DayOfYear.md)
  * [DaysInMonth](boxlang-language/reference/built-in-functions/DaysInMonth.md)
  * [DaysInYear](boxlang-language/reference/built-in-functions/DaysInYear.md)
  * [FirstDayOfMonth](boxlang-language/reference/built-in-functions/FirstDayOfMonth.md)
  * [GetNumericDate](boxlang-language/reference/built-in-functions/GetNumericDate.md)
  * [GetTime](boxlang-language/reference/built-in-functions/GetTime.md)
  * [GetTimezone](boxlang-language/reference/built-in-functions/GetTimezone.md)
  * [GetTimezoneInfo](boxlang-language/reference/built-in-functions/GetTimezoneInfo.md)
  * [Hour](boxlang-language/reference/built-in-functions/Hour.md)
  * [LSDateTimeFormat](boxlang-language/reference/built-in-functions/LSDateTimeFormat.md)
  * [LSDayOfWeek](boxlang-language/reference/built-in-functions/LSDayOfWeek.md)
  * [LSIsDate](boxlang-language/reference/built-in-functions/LSIsDate.md)
  * [LSParseDateTime](boxlang-language/reference/built-in-functions/LSParseDateTime.md)
  * [LSTimeFormat](boxlang-language/reference/built-in-functions/LSTimeFormat.md)
  * [LSWeek](boxlang-language/reference/built-in-functions/LSWeek.md)
  * [Millisecond](boxlang-language/reference/built-in-functions/Millisecond.md)
  * [Minute](boxlang-language/reference/built-in-functions/Minute.md)
  * [Month](boxlang-language/reference/built-in-functions/Month.md)
  * [MonthAsString](boxlang-language/reference/built-in-functions/MonthAsString.md)
  * [MonthShortAsString](boxlang-language/reference/built-in-functions/MonthShortAsString.md)
  * [Nanosecond](boxlang-language/reference/built-in-functions/Nanosecond.md)
  * [Now](boxlang-language/reference/built-in-functions/Now.md)
  * [Offset](boxlang-language/reference/built-in-functions/Offset.md)
  * [ParseDateTime](boxlang-language/reference/built-in-functions/ParseDateTime.md)
  * [Quarter](boxlang-language/reference/built-in-functions/Quarter.md)
  * [Second](boxlang-language/reference/built-in-functions/Second.md)
  * [SetTimezone](boxlang-language/reference/built-in-functions/SetTimezone.md)
  * [TimeFormat](boxlang-language/reference/built-in-functions/TimeFormat.md)
  * [WeekOfYear](boxlang-language/reference/built-in-functions/WeekOfYear.md)
  * [Year](boxlang-language/reference/built-in-functions/Year.md)

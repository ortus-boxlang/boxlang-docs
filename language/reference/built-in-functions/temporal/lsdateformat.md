# LSDateFormat

Formats a date in a locale-specific format

## Method Signature

```
LSDateFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```

### Arguments

| Argument   | Type     | Required   | Description                                                                           | Default   |
| ---------- | -------- | ---------- | ------------------------------------------------------------------------------------- | --------- |
| `date`     | `any`    | `true`     | The date string or object                                                             |           |
| `mask`     | `string` | `false`    | Optional format mask, or common mask                                                  |           |
| `locale`   | `string` | `false`    | Optional locale designation of the output ( e.g. es-SA )                              |           |
| `timezone` | `string` | `false`    | Optional specific timezone to apply to the date ( if not present in the date string ) |           |
| ---------- | ------   | ---------- | -------------                                                                         | --------- |

## Examples

```
LSDateFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```

## Related

* [ClearTimezone](cleartimezone.md)
* [CreateDate](createdate.md)
* [CreateDateTime](createdatetime.md)
* [CreateODBCDate](createodbcdate.md)
* [CreateODBCDateTime](createodbcdatetime.md)
* [CreateODBCTime](createodbctime.md)
* [CreateTimeSpan](createtimespan.md)
* [DateAdd](dateadd.md)
* [DateCompare](datecompare.md)
* [DateConvert](dateconvert.md)
* [DateDiff](datediff.md)
* [DateFormat](dateformat.md)
* [DatePart](datepart.md)
* [DateTimeFormat](datetimeformat.md)
* [Day](day.md)
* [DayOfWeek](dayofweek.md)
* [DayOfWeekAsString](dayofweekasstring.md)
* [DayOfWeekShortAsString](dayofweekshortasstring.md)
* [DayOfYear](dayofyear.md)
* [DaysInMonth](daysinmonth.md)
* [DaysInYear](daysinyear.md)
* [FirstDayOfMonth](firstdayofmonth.md)
* [GetNumericDate](getnumericdate.md)
* [GetTime](gettime.md)
* [GetTimezone](gettimezone.md)
* [GetTimezoneInfo](gettimezoneinfo.md)
* [Hour](hour.md)
* [LSDateTimeFormat](lsdatetimeformat.md)
* [LSDayOfWeek](lsdayofweek.md)
* [LSIsDate](lsisdate.md)
* [LSParseDateTime](lsparsedatetime.md)
* [LSTimeFormat](lstimeformat.md)
* [LSWeek](lsweek.md)
* [Millisecond](millisecond.md)
* [Minute](minute.md)
* [Month](month.md)
* [MonthAsString](monthasstring.md)
* [MonthShortAsString](monthshortasstring.md)
* [Nanosecond](nanosecond.md)
* [Now](now.md)
* [Offset](offset.md)
* [ParseDateTime](parsedatetime.md)
* [Quarter](quarter.md)
* [Second](second.md)
* [SetTimezone](settimezone.md)
* [TimeFormat](timeformat.md)
* [WeekOfYear](weekofyear.md)
* [Year](year.md)

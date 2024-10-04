# DateConvert

Converts local time to Coordinated Universal Time (UTC), or UTC to local time.

The function uses the daylight savings settings in the executing computer to compute daylight savings time, if required.

## Method Signature

```
DateConvert(conversionType=[string], date=[any])
```

### Arguments

| Argument         | Type     | Required | Description                                                        | Default |
| ---------------- | -------- | -------- | ------------------------------------------------------------------ | ------- |
| `conversionType` | `string` | `true`   | The conversion type. Valid values are "utc2Local" and "local2Utc". |         |
| `date`           | `any`    | `true`   | The date to convert.                                               |         |

## Examples

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
* [Week](week.md)
* [Year](year.md)

# CreateDateTime

Describe what the invocation of your bif function does

## Method Signature

```
CreateDateTime(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
```

### Arguments

| Argument      | Type      | Required   | Description   | Default   |
| ------------- | --------- | ---------- | ------------- | --------- |
| `year`        | `integer` | `false`    |               | 0         |
| `month`       | `integer` | `false`    |               | 1         |
| `day`         | `integer` | `false`    |               | 1         |
| `hour`        | `integer` | `false`    |               | 0         |
| `minute`      | `integer` | `false`    |               | 0         |
| `second`      | `integer` | `false`    |               | 0         |
| `millisecond` | `integer` | `false`    |               | 0         |
| `timezone`    | `string`  | `false`    |               |           |
| ----------    | ------    | ---------- | ------------- | --------- |

## Examples

```
CreateDateTime(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
```

## Related

* [ClearTimezone](cleartimezone.md)
* [CreateDate](createdate.md)
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
* [LSDateFormat](lsdateformat.md)
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

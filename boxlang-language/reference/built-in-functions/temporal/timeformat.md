# TimeFormat

Formats a datetime, date or time

## Method Signature

```
TimeFormat(date=[any], mask=[string], timezone=[string], locale=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Default |
| ---------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `date`     | `any`    | `true`   | The date string or object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |         |
| `mask`     | `string` | `false`  | <p>Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br><a href="https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html">java.time.format.DateTimeFormatter</a> class.<br>If a common mask is used, the following are supported:<br>* short: equivalent to "M/d/y h:mm tt"<br>* medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>* long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>* full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>* ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>* epoch: Total seconds of a given date (Example:1567517664)<br>* epochms: Total milliseconds of a given date (Example:1567517664000)</p> |         |
| `timezone` | `string` | `false`  | Optional specific timezone to apply to the date ( if not present in the date string )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |         |
| `locale`   | `string` | `false`  | Optional ISO locale string which will be used to localize the resulting date/time string                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |         |

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
* [Week](week.md)
* [Year](year.md)

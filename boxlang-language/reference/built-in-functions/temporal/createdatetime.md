# CreateDateTime

Creates a date-time object.

Note that the core implementation of this BIF differs from ACF/Lucee in handling of a year value without a century. BoxLang respects that pre-first century years are valid and and will treat `createDate( 20 )` as 20 AD. The behavior modification to emulate ACF/Lucee would require the installation of the `bx-compat-cfml` module.

## Method Signature

```
CreateDateTime(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
```

### Arguments

| Argument      | Type      | Required | Description                         | Default |
| ------------- | --------- | -------- | ----------------------------------- | ------- |
| `year`        | `integer` | `false`  | The year of the date-time object.   | `0`     |
| `month`       | `integer` | `false`  | The month of the date-time object.  | `1`     |
| `day`         | `integer` | `false`  | The day of the date-time object.    | `1`     |
| `hour`        | `integer` | `false`  | The hour of the date-time object.   | `0`     |
| `minute`      | `integer` | `false`  | The minute of the date-time object. | `0`     |
| `second`      | `integer` | `false`  | The second of the date-time object. | `0`     |
| `millisecond` | `integer` | `false`  |                                     | `0`     |
| `timezone`    | `string`  | `false`  |                                     |         |

## Examples

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

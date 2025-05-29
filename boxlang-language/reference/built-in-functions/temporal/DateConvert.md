[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DateConvert`

Converts local time to Coordinated Universal Time (UTC), or UTC to local time.

The function uses the daylight savings settings in the executing computer to compute daylight savings time, if required.

## Method Signature

```
DateConvert(conversionType=[string], date=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `conversionType` | `string` | `true` | The conversion type. Valid values are "utc2Local" and "local2Utc". |  |
| `date` | `any` | `true` | The date to convert. |  |

## Examples

### Converting Local to UTC



<a href="https://try.boxlang.io/?code=eJwrLUmOT0ksSS3JzE1VsFUAMZ3z88pSi0o0FJRy8pMTc4xCS5KVdBTy8ss1NBU0rbkAzC8QaQ%3D%3D" target="_blank">Run Example</a>

```java
utc_datetime = dateConvert( "local2Utc", now() );

```

Result: {ts '2025-05-27 05:12:10'}

### Converting UTC to Local

This example makes sense only if your server time is UTC. now() uses your server settings when creating a datetime object.

<a href="https://try.boxlang.io/?code=eJzLyU9OzIlPSSxJLcnMTVWwVQAxnfPzylKLSjQUlEpLko18QEqUdBTy8ss1NBU0rbkA8ocRKA%3D%3D" target="_blank">Run Example</a>

```java
local_datetime = dateConvert( "utc2Local", now() );

```

Result: {ts '2025-05-26 22:12:10'}

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSXUpzS3QUHBJLEl1zs8rSy0q0VBQ8slPTswxKi1JVtJRUKouKVZQNzIwMNM1MNQ1MlMwMLIyMAAi9VolBU0FTWuuclzGAA0wAhsFNCYvv1xDE6IeAIX5Itg%3D" target="_blank">Run Example</a>

```java
writeDump( DateConvert( "Local2utc", "{ts '2006-01-26 02:00:00'}" ) );
writeDump( DateConvert( "utc2Local", now() ) );

```



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
  * [DatePart](./DatePart.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)
  * [ParseDateTime](./ParseDateTime.md)

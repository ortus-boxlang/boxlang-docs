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

  * [ClearTimezone](./ClearTimezone.md)
  * [CreateDate](./CreateDate.md)
  * [CreateDateTime](./CreateDateTime.md)
  * [CreateODBCDate](./CreateODBCDate.md)
  * [CreateODBCDateTime](./CreateODBCDateTime.md)
  * [CreateODBCTime](./CreateODBCTime.md)
  * [CreateTime](./CreateTime.md)
  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [DateAdd](./DateAdd.md)
  * [DateCompare](./DateCompare.md)
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
  * [TimeUnits](./TimeUnits.md)
  * [Week](./Week.md)
  * [Year](./Year.md)

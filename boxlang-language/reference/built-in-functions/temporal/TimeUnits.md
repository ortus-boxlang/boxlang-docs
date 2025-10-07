[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `TimeUnits`

Provides the BIF and member functions for all time unit request with no arguments

## Method Signature

```
TimeUnits(date=[any], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `false` | The date object to be evaluated. If not provided the current date and time is used |  |
| `timezone` | `string` | `false` | An optional timezone which to convert the date object to |  |
| `locale` | `string` | `false` | An optional ISO locale string which will return the specified time unit with a locale-specific result ( e.g. month name, or starting day of week as Monday vs Sunda ) |  |

## Examples

### Year of a datetime object



<a href="https://try.boxlang.io/?code=eJxLKVGwVUguSk0sSU0B4pLM3FQNBSMDQzMdBUMwMtVRMDbQUTAyVdC05qoEKq5MTSzSUEgpAfHLizJLUvNLSwpKSzQUKkEiAIaoFhM%3D" target="_blank">Run Example</a>

```java
dt = createdatetime( 2016, 1, 1, 5, 30, 25 );
y = year( dt );
writeoutput( y );

```

Result: 2016

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrycgsjkxNLFKwVagEUhoKefnlGpoKmtZcKaW5BRoKJTB5oAgARtsNyA%3D%3D" target="_blank">Run Example</a>

```java
thisYear = year( now() );
dump( thisYear );

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

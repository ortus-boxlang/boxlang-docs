[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateTimeSpan`

Creates a timespan {@link java.time.Duration}

## Method Signature

```
CreateTimeSpan(days=[numeric], hours=[numeric], minutes=[numeric], seconds=[numeric], milliseconds=[numeric])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `days` | `numeric` | `true` | The number of days in the timespan |  |
| `hours` | `numeric` | `true` | The number of hours in the timespan |  |
| `minutes` | `numeric` | `true` | The number of minutes in the timespan |  |
| `seconds` | `numeric` | `true` | The number of seconds in the timespan |  |
| `milliseconds` | `numeric` | `false` | The number of milliseconds in the timespan | `0` |

## Examples

### Use of createTimespan in a bx:query

The createTimespan function is useful in the cachedwithin attribute of bx:query.


```java
<bx:query name="GetParks" datasource="cfdocexamples" cachedWithin="#createTimespan( 0, 6, 0, 0 )#"> 
 SELECT PARKNAME, REGION, STATE 
 FROM Parks 
 ORDER by ParkName, State 
 </bx:query>
```


### The createTimespan function returns a numeric value

Passing 6 hours, or a quarter of a day returns a double representing 1/4

<a href="https://try.boxlang.io/?code=eJxLLkpNLEkNycxNLS5IzNNQMNBRMNMBkQYKmtZcAJu1CDY%3D" target="_blank">Run Example</a>

```java
createTimespan( 0, 6, 0, 0 );

```

Result: PT6H

### Adding a date and a timestamp

Instead of using dateAdd you could add a timestamp to a date object


```java
dateFormat( createDate( 2017, 1, 1 ) + createTimespan( 2, 0, 0, 0 ) );

```

Result: 03-Jan-17

### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FBILkpNLEkNycxNDS5IzNNQMNABIWMQpaCpoGnNpaCvD%2BTq5mbmlZakKpQAFRYDFXIBAD0DEdU%3D" target="_blank">Run Example</a>

```java
dump( createTimeSpan( 0, 0, 30, 0 ) );
 // 30-minute timespan

```



## Related

  * [ClearTimezone](./ClearTimezone.md)
  * [CreateDate](./CreateDate.md)
  * [CreateDateTime](./CreateDateTime.md)
  * [CreateODBCDate](./CreateODBCDate.md)
  * [CreateODBCDateTime](./CreateODBCDateTime.md)
  * [CreateODBCTime](./CreateODBCTime.md)
  * [CreateTime](./CreateTime.md)
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

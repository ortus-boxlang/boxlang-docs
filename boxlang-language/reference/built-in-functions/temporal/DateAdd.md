[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DateAdd`

Modifies a date object by date part and integer time unit

## Method Signature

```
DateAdd(datepart=[string], number=[number], date=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `datepart` | `string` | `true` | The date part to modify |  |
| `number` | `number` | `true` | The number of units to modify by |  |
| `date` | `any` | `true` | The date object to modify |  |

## Examples

### Add Days to a Date

Add 30 days to August 3rd, 2014.

<a href="https://try.boxlang.io/?code=eJxLSSxJdUxJ0VBQSlHSUTA20FFQstA31jcyMDRRUtC05gIAhqsG9Q%3D%3D" target="_blank">Run Example</a>

```java
dateAdd( "d", 30, "8/3/2014" );

```

Result: {ts '2014-04-07 00:00:00'}

### Subtract Days from a Date

Subtract 30 days from August 3rd, 2014.

<a href="https://try.boxlang.io/?code=eJxLSSxJdUxJ0VBQSlHSUdA1NtBRULLQN9Y3MjA0UVLQtOYCAI3mByI%3D" target="_blank">Run Example</a>

```java
dateAdd( "d", -30, "8/3/2014" );

```

Result: {ts '2014-02-06 00:00:00'}

### Add Weeks to a Date

Here we're adding 8 weeks to the date August 3rd, 2014.

<a href="https://try.boxlang.io/?code=eJxLSSxJdUxJ0VBQKi9X0lGw0FFQstA31jcyMDRRUtC05gIAjpQHVA%3D%3D" target="_blank">Run Example</a>

```java
dateAdd( "ww", 8, "8/3/2014" );

```

Result: {ts '2014-05-03 00:00:00'}

### Add Days to a Date (Member Function)

Here we're adding 1 day to the current date/time.

<a href="https://try.boxlang.io/?code=eJxLLkpNLEl1AWINBSMDIyMdBUMDIFbQ1EtMSdFQUEpRAvOsuQDtZQnG" target="_blank">Run Example</a>

```java
createDate( 2022, 10, 1 ).add( "d", 1 );

```

Result: {ts '2022-10-02 00:00:00'}

### Additional Examples

<a href="https://try.boxlang.io/?code=eJyV0LsKwzAMBdA9XyEyuRDIY8jSqZ%2FiWgIbbLn4QcjfV%2B1aqGNpEVzuGTTPUCzBk3w8wEQkcGwSBeKSYV0gOO9dJhMZs0SgTanaA%2BpCA9bwUt%2Fzgahg9OMklQk4HuoGsvdh%2FsfvC1yUs8h7nxwc10JNmTvlDWysqclaYbfr6irVs2Xi5709ZohcbEsNvepJOrXQU%2BbHfQOok8Hu" target="_blank">Run Example</a>

```java
// the below code increments 10 milliseconds in actual date
dump( dateAdd( "l", 10, now() ) );
// the below code increments 60 seconds in actual date
dump( dateAdd( "s", 60, now() ) );
// the below code increments 60 minutes in actual date
dump( dateAdd( "n", 60, now() ) );
// the below code increments 2 hours in actual date
dump( dateAdd( "h", 2, now() ) );
// the below code increments 1 day in actual date
dump( dateAdd( "d", 1, now() ) );
// the below code increments 1 month in actual date
dump( dateAdd( "m", 1, now() ) );
// the below code increments 1 year in actual date
dump( dateAdd( "yyyy", 1, now() ) );

```



## Related

  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [SetTimezone](./SetTimezone.md)
  * [DateCompare](./DateCompare.md)
  * [Now](./Now.md)
  * [DateDiff](./DateDiff.md)
  * [CreateTime](./CreateTime.md)
  * [ClearTimezone](./ClearTimezone.md)
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
  * [DateConvert](./DateConvert.md)
  * [DatePart](./DatePart.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)
  * [ParseDateTime](./ParseDateTime.md)

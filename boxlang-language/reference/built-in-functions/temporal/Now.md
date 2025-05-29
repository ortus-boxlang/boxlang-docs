[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `Now`

Returns the current DateTimeObject representing the current zoned instance

## Method Signature

```
Now(timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | A timezone to use for the DateTime object, defaults to the system default |  |

## Examples

### Using now() in Script

Let's display the current server datetime using script.

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQUArJSFVILi0qSs0rUUhJLElVSMxLUSjJzE1VyCy2UlBSUFPIyy%2FX0FTQtOYCAE2uElw%3D" target="_blank">Run Example</a>

```java
writeOutput( "The current date and time is: " & now() );

```

Result: The current date and time is: {ts '2014-03-19 15:27:42'}

### Using now() in Tagged BL

Let's display the current server datetime using tagged BL.


```java
<p>The current date and time is: <bx:output>#now()#</bx:output></p>
```

Result: The current date and time is: {ts '2014-03-19 15:27:42'}

### Additional Examples

<a href="https://try.boxlang.io/?code=eJwrL8osSfUvLSkoLdFQUEouLSpKzStRcEksSS3JzE1VyCxWUFJQU8jLL9fQVNC05gIAm9EPTg%3D%3D" target="_blank">Run Example</a>

```java
writeOutput( "current Datetime is " & now() );

```



## Related

  * [CreateTimeSpan](./CreateTimeSpan.md)
  * [SetTimezone](./SetTimezone.md)
  * [DateCompare](./DateCompare.md)
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
  * [DateConvert](./DateConvert.md)
  * [DatePart](./DatePart.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)
  * [ParseDateTime](./ParseDateTime.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetTimezoneInfo`

Retrieves a struct of information about the timezone

## Method Signature

```
GetTimezoneInfo(timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `timezone` | `string` | `false` | optional, a specific timezone to retrieve information on |  |
| `locale` | `string` | `false` | optional, a specific locale for language output of the timezone name fields |  |

## Examples

### Output timezone information

This example shows the use of GetTimeZoneInfo


```java
<bx:output>
The local date and time are #now()#.
</bx:output>
<bx:set info = GetTimeZoneInfo() >
<bx:output>
<p>Total offset in seconds is #info.UTCTOTALOFFSET#.</p>
<p>Offset in hours is #info.UTCHOUROFFSET#.</p>
<p>Offset in minutes minus the offset in hours is #info.UTCMINUTEOFFSET#.</p>
<p>Is Daylight Savings Time in effect? #info.ISDSTON#.</p>
</bx:output>
```


### Get Hawaii timezone information in German

Shows the use of getTimeZoneInfo for a known / specific timezone with German locale. 


```java
<bx:script>
	var tz = getTimeZoneInfo( "US/Hawaii", "de-DE" );
</bx:script>

```


### Additional Examples

<a href="https://try.boxlang.io/?code=eJxLKc0t0FBwTy0JycxNjcrPS%2FXMS8vX0FTQtOYCAIYsCLU%3D" target="_blank">Run Example</a>

```java
dump( GetTimeZoneInfo() );

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
  * [CreateODBCDateTime](./CreateODBCDateTime.md)
  * [CreateODBCDate](./CreateODBCDate.md)
  * [CreateODBCTime](./CreateODBCTime.md)
  * [DateConvert](./DateConvert.md)
  * [DatePart](./DatePart.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)
  * [ParseDateTime](./ParseDateTime.md)

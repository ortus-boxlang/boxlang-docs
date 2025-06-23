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

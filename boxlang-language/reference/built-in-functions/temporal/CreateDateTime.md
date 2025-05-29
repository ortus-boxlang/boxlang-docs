[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `CreateDateTime`

Creates a date-time object.

Note that the core implementation of this BIF differs from ACF/Lucee in handling of a year value without a century. BoxLang respects that pre-first century years are valid and and will treat `createDate( 20 )` as 20 AD.
 The behavior modification to emulate ACF/Lucee would require the installation of the `bx-compat` module.

## Method Signature

```
CreateDateTime(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `year` | `integer` | `false` | The year of the date-time object. | `0` |
| `month` | `integer` | `false` | The month of the date-time object. | `1` |
| `day` | `integer` | `false` | The day of the date-time object. | `1` |
| `hour` | `integer` | `false` | The hour of the date-time object. | `0` |
| `minute` | `integer` | `false` | The minute of the date-time object. | `0` |
| `second` | `integer` | `false` | The second of the date-time object. | `0` |
| `millisecond` | `integer` | `false` |  | `0` |
| `timezone` | `string` | `false` |  |  |

## Examples

### Tag Syntax




```java
<bx:set yourDate = createDateTime( "2015", "12", "09", "6", "20", "34" ) >
<bx:dump var="#yourDate#"/>     
```


### Additional Examples


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

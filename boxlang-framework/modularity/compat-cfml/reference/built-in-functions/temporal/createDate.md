[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `createDate`

Overload to creatDateTime behavior to account for ACF/Lucee specific manipulations ( e.g.

converting non-century years to current century )

## Method Signature

```
createDate(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
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



## Related

  * [LSWeek](./LSWeek.md)
  * [LSDayOfWeek](./LSDayOfWeek.md)
  * [LSIsDate](./LSIsDate.md)
  * [DateCompare](./DateCompare.md)
  * [GetHTTPTimestring](./GetHTTPTimestring.md)
  * [LSDateTimeFormat](./LSDateTimeFormat.md)
  * [LSDateFormat](./LSDateFormat.md)
  * [LSTimeFormat](./LSTimeFormat.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
  * [MonthAsString](./MonthAsString.md)
  * [MonthShortAsString](./MonthShortAsString.md)
  * [ToLegacyDate](./ToLegacyDate.md)
  * [LSParseDateTime](./LSParseDateTime.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)

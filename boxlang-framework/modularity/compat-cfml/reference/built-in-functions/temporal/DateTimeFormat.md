[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `DateTimeFormat`

Formats a datetime, date or time

## Method Signature

```
DateTimeFormat(date=[any], mask=[string], timezone=[string], locale=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | The date string or object |  |
| `mask` | `string` | `false` | Optional format mask, or common mask. If an explicit mask is used, it should use the mask characters specified in the<br>                [java.time.format.DateTimeFormatter](https://docs.oracle.com/en%2Fjava%2Fjavase%2F21%2Fdocs%2Fapi%2F%2F/java.base/java/time/format/DateTimeFormatter.html)<br>                class. In compatibility mode the legacy CFML mask characters are also supported.<br>                If a common mask is used, the following are supported:<br>                - short: equivalent to "M/d/y h:mm tt"<br>                - medium: equivalent to "MMM d, yyyy h:mm:ss tt"<br>                - long: medium followed by three-letter time zone; i.e. "MMMM d, yyyy h:mm:ss tt zzz"<br>                - full: equivalent to "dddd, MMMM d, yyyy H:mm:ss tt zz"<br>                - ISO8601/ISO: equivalent to "yyyy-MM-dd'T'HH:mm:ssXXX"<br>                - epoch: Total seconds of a given date (Example:1567517664)<br>                - epochms: Total milliseconds of a given date (Example:1567517664000) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |
| `locale` | `string` | `false` | Optional ISO locale string which will be used to localize the resulting date/time string |  |

## Examples



## Related

  * [createDate](./createDate.md)
  * [DateCompare](./DateCompare.md)
  * [DateFormat](./DateFormat.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
  * [GetHTTPTimestring](./GetHTTPTimestring.md)
  * [LSDateFormat](./LSDateFormat.md)
  * [LSDateTimeFormat](./LSDateTimeFormat.md)
  * [LSDayOfWeek](./LSDayOfWeek.md)
  * [LSIsDate](./LSIsDate.md)
  * [LSParseDateTime](./LSParseDateTime.md)
  * [LSTimeFormat](./LSTimeFormat.md)
  * [LSWeek](./LSWeek.md)
  * [MonthAsString](./MonthAsString.md)
  * [MonthShortAsString](./MonthShortAsString.md)
  * [ParseDateTime](./ParseDateTime.md)
  * [TimeFormat](./TimeFormat.md)
  * [ToLegacyDate](./ToLegacyDate.md)

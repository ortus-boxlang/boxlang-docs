[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSTimeFormat`

Formats a date in a locale-specific format

## Method Signature

```
LSTimeFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | The date string or object |  |
| `mask` | `string` | `false` | Optional format mask, or common mask |  |
| `locale` | `string` | `false` | Optional locale designation of the output ( e.g. es-SA ) |  |
| `timezone` | `string` | `false` | Optional specific timezone to apply to the date ( if not present in the date string ) |  |

## Examples



## Related

  * [createDate](./createDate.md)
  * [DateCompare](./DateCompare.md)
  * [DateFormat](./DateFormat.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
  * [GetHTTPTimestring](./GetHTTPTimestring.md)
  * [LSDateFormat](./LSDateFormat.md)
  * [LSDateTimeFormat](./LSDateTimeFormat.md)
  * [LSDayOfWeek](./LSDayOfWeek.md)
  * [LSIsDate](./LSIsDate.md)
  * [LSParseDateTime](./LSParseDateTime.md)
  * [LSWeek](./LSWeek.md)
  * [MonthAsString](./MonthAsString.md)
  * [MonthShortAsString](./MonthShortAsString.md)
  * [ParseDateTime](./ParseDateTime.md)
  * [TimeFormat](./TimeFormat.md)
  * [ToLegacyDate](./ToLegacyDate.md)

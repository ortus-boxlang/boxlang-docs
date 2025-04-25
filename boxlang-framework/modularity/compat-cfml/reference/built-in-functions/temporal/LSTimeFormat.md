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

  * [LSWeek](./LSWeek.md)
  * [LSDayOfWeek](./LSDayOfWeek.md)
  * [LSIsDate](./LSIsDate.md)
  * [DateCompare](./DateCompare.md)
  * [GetHTTPTimestring](./GetHTTPTimestring.md)
  * [LSDateTimeFormat](./LSDateTimeFormat.md)
  * [LSDateFormat](./LSDateFormat.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
  * [MonthAsString](./MonthAsString.md)
  * [MonthShortAsString](./MonthShortAsString.md)
  * [ToLegacyDate](./ToLegacyDate.md)
  * [createDate](./createDate.md)
  * [LSParseDateTime](./LSParseDateTime.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DateFormat](./DateFormat.md)
  * [TimeFormat](./TimeFormat.md)

# LSDateTimeFormat

Formats a date in a locale-specific format

## Method Signature

```
LSDateTimeFormat(date=[any], mask=[string], locale=[string], timezone=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                           | Default |
| ---------- | -------- | -------- | ------------------------------------------------------------------------------------- | ------- |
| `date`     | `any`    | `true`   | The date string or object                                                             |         |
| `mask`     | `string` | `false`  | Optional format mask, or common mask                                                  |         |
| `locale`   | `string` | `false`  | Optional locale designation of the output ( e.g. es-SA )                              |         |
| `timezone` | `string` | `false`  | Optional specific timezone to apply to the date ( if not present in the date string ) |         |

## Examples

## Related

* [createDate](createDate.md)
* [DateCompare](DateCompare.md)
* [DateFormat](DateFormat.md)
* [DateTimeFormat](DateTimeFormat.md)
* [DayOfWeekAsString](DayOfWeekAsString.md)
* [DayOfWeekShortAsString](DayOfWeekShortAsString.md)
* [GetHTTPTimestring](/broken/pages/12EdXbOXMzAtSTemXnbo)
* [LSDateFormat](LSDateFormat.md)
* [LSDayOfWeek](LSDayOfWeek.md)
* [LSIsDate](LSIsDate.md)
* [LSParseDateTime](LSParseDateTime.md)
* [LSTimeFormat](LSTimeFormat.md)
* [LSWeek](LSWeek.md)
* [MonthAsString](MonthAsString.md)
* [MonthShortAsString](MonthShortAsString.md)
* [ParseDateTime](ParseDateTime.md)
* [TimeFormat](TimeFormat.md)
* [ToLegacyDate](ToLegacyDate.md)

# ParseDateTime

Parses a locale-specific datetime string or object

## Method Signature

```
ParseDateTime(date=[any], format=[string], timezone=[string], locale=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                                                                  | Default |
| ---------- | -------- | -------- | ------------------------------------------------------------------------------------------------------------ | ------- |
| `date`     | `any`    | `true`   | the date, datetime string or an object                                                                       |         |
| `format`   | `string` | `false`  | the format mask to use in parsing                                                                            |         |
| `timezone` | `string` | `false`  | the timezone to apply to the parsed datetime                                                                 |         |
| `locale`   | `string` | `false`  | optional ISO locale string ( e.g. en-US, en\_US, es-SA, es\_ES, ru-RU, etc ) used to parse localized formats |         |

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
* [LSDateTimeFormat](LSDateTimeFormat.md)
* [LSDayOfWeek](LSDayOfWeek.md)
* [LSIsDate](LSIsDate.md)
* [LSParseDateTime](LSParseDateTime.md)
* [LSTimeFormat](LSTimeFormat.md)
* [LSWeek](LSWeek.md)
* [MonthAsString](MonthAsString.md)
* [MonthShortAsString](MonthShortAsString.md)
* [TimeFormat](TimeFormat.md)
* [ToLegacyDate](ToLegacyDate.md)

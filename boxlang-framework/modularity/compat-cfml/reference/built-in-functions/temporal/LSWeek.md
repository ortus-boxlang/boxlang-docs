# LSWeek

Provides the Localized BIF and member functions for time units ( e.g.

different locales have different start days to the week )

## Method Signature

```
LSWeek(date=[any], locale=[string], timezone=[string])
```

### Arguments

| Argument   | Type     | Required | Description                                                    | Default |
| ---------- | -------- | -------- | -------------------------------------------------------------- | ------- |
| `date`     | `any`    | `true`   | The DateTime object or datetime string representation          |         |
| `locale`   | `string` | `false`  | The locale string to be parsed and applied to the final result |         |
| `timezone` | `string` | `false`  | The timezone with which to cast the result                     |         |

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
* [MonthAsString](MonthAsString.md)
* [MonthShortAsString](MonthShortAsString.md)
* [ParseDateTime](ParseDateTime.md)
* [TimeFormat](TimeFormat.md)
* [ToLegacyDate](ToLegacyDate.md)

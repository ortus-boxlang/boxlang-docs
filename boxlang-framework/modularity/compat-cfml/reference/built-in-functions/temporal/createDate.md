# createDate

Overload to creatDateTime behavior to account for ACF/Lucee specific manipulations ( e.g.

converting non-century years to current century )

## Method Signature

```
createDate(year=[integer], month=[integer], day=[integer], hour=[integer], minute=[integer], second=[integer], millisecond=[integer], timezone=[string])
```

### Arguments

| Argument      | Type      | Required | Description                         | Default |
| ------------- | --------- | -------- | ----------------------------------- | ------- |
| `year`        | `integer` | `false`  | The year of the date-time object.   | `0`     |
| `month`       | `integer` | `false`  | The month of the date-time object.  | `1`     |
| `day`         | `integer` | `false`  | The day of the date-time object.    | `1`     |
| `hour`        | `integer` | `false`  | The hour of the date-time object.   | `0`     |
| `minute`      | `integer` | `false`  | The minute of the date-time object. | `0`     |
| `second`      | `integer` | `false`  | The second of the date-time object. | `0`     |
| `millisecond` | `integer` | `false`  |                                     | `0`     |
| `timezone`    | `string`  | `false`  |                                     |         |

## Examples

## Related

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
* [ParseDateTime](ParseDateTime.md)
* [TimeFormat](TimeFormat.md)
* [ToLegacyDate](ToLegacyDate.md)

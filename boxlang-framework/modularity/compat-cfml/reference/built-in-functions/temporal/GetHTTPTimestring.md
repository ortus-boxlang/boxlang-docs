# GetHTTPTimestring

Returns the legacy HTTP TimeString as specified for the now-obsolete RFC 1123/RCF 822.

This method should be used for legacy compatibility with older CFML engines and is not recommended for new code.\
The updated specification, [RFC 2822](https://www.rfc-editor.org/rfc/rfc2822) should be used for new implemenations.

## Method Signature

```
GetHTTPTimestring(date=[any])
```

### Arguments

| Argument | Type  | Required | Description              | Default |
| -------- | ----- | -------- | ------------------------ | ------- |
| `date`   | `any` | `true`   | The date value to format |         |

## Examples

## Related

* [LSWeek](LSWeek.md)
* [LSDayOfWeek](LSDayOfWeek.md)
* [LSIsDate](LSIsDate.md)
* [DateCompare](DateCompare.md)
* [LSDateTimeFormat](LSDateTimeFormat.md)
* [LSDateFormat](LSDateFormat.md)
* [LSTimeFormat](LSTimeFormat.md)
* [DayOfWeekAsString](DayOfWeekAsString.md)
* [DayOfWeekShortAsString](DayOfWeekShortAsString.md)
* [MonthAsString](MonthAsString.md)
* [MonthShortAsString](MonthShortAsString.md)
* [ToLegacyDate](ToLegacyDate.md)
* [createDate](createDate.md)
* [LSParseDateTime](LSParseDateTime.md)
* [DateTimeFormat](DateTimeFormat.md)
* [DateFormat](DateFormat.md)
* [TimeFormat](TimeFormat.md)

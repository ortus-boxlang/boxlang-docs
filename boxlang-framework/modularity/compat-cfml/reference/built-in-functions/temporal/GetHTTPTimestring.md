[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetHTTPTimestring`

Returns the legacy HTTP TimeString as specified for the now-obsolete RFC 1123/RCF 822.

This method should be used for legacy compatibility with older CFML engines and is not recommended for new code.
 The updated specification, [RFC 2822](https://www.rfc-editor.org/rfc/rfc2822) should be used for new implemenations.

## Method Signature

```
GetHTTPTimestring(date=[any])
```

### Arguments


| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `date` | `any` | `true` | The date value to format |  |

## Examples



## Related

  * [createDate](./createDate.md)
  * [DateCompare](./DateCompare.md)
  * [DateFormat](./DateFormat.md)
  * [DateTimeFormat](./DateTimeFormat.md)
  * [DayOfWeekAsString](./DayOfWeekAsString.md)
  * [DayOfWeekShortAsString](./DayOfWeekShortAsString.md)
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

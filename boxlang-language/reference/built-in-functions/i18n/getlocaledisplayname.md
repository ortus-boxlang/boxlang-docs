[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetLocaleDisplayName`

Returns the ,{@link java.util.Locale}, display name with an optional display language/locale

## Method Signature
```
GetLocaleDisplayName(locale=[string], dspLocale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `locale` | `string` | `false` | Optional locale to target - either a common format ( "German" ), or an ISO Directive |  |
| `dspLocale` | `string` | `false` | Optional display language locale |  |

## Examples

```
GetLocaleDisplayName(locale=[string], dspLocale=[string])
```

## Related
  * [GetLocale](boxlang-language/reference/built-in-functions/GetLocale.md)
  * [GetLocaleInfo](boxlang-language/reference/built-in-functions/GetLocaleInfo.md)
  * [LSCurrencyFormat](boxlang-language/reference/built-in-functions/LSCurrencyFormat.md)
  * [LSIsCurrency](boxlang-language/reference/built-in-functions/LSIsCurrency.md)
  * [LSIsNumeric](boxlang-language/reference/built-in-functions/LSIsNumeric.md)
  * [LSNumberFormat](boxlang-language/reference/built-in-functions/LSNumberFormat.md)
  * [LSParseCurrency](boxlang-language/reference/built-in-functions/LSParseCurrency.md)
  * [LSParseNumber](boxlang-language/reference/built-in-functions/LSParseNumber.md)
  * [SetLocale](boxlang-language/reference/built-in-functions/SetLocale.md)

[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `GetLocaleInfo`

Retrieves a struct containin info on a locale, with an optional display locale

## Method Signature
```
GetLocaleInfo(locale=[string], dspLocale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `locale` | `string` | `false` | Optional locale to retrieve information on - either a common format ( "German" ), or an ISO Directive |  |
| `dspLocale` | `string` | `false` | Optional display language locale |  |

## Examples

```
GetLocaleInfo(locale=[string], dspLocale=[string])
```

## Related
  * [GetLocale](boxlang-language/reference/built-in-functions/GetLocale.md)
  * [GetLocaleDisplayName](boxlang-language/reference/built-in-functions/GetLocaleDisplayName.md)
  * [LSCurrencyFormat](boxlang-language/reference/built-in-functions/LSCurrencyFormat.md)
  * [LSIsCurrency](boxlang-language/reference/built-in-functions/LSIsCurrency.md)
  * [LSIsNumeric](boxlang-language/reference/built-in-functions/LSIsNumeric.md)
  * [LSNumberFormat](boxlang-language/reference/built-in-functions/LSNumberFormat.md)
  * [LSParseCurrency](boxlang-language/reference/built-in-functions/LSParseCurrency.md)
  * [LSParseNumber](boxlang-language/reference/built-in-functions/LSParseNumber.md)
  * [SetLocale](boxlang-language/reference/built-in-functions/SetLocale.md)

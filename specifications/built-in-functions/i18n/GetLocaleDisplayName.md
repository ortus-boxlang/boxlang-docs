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
| `locale` | `string` | `false` | Optional locale to target - either a common format ( "German" ), or an ISO Directive | |
| `dspLocale` | `string` | `false` | Optional display language locale | |
|----------|------|----------|-------------|---------|



## Examples

```
GetLocaleDisplayName(locale=[string], dspLocale=[string])
```

## Related
  * [GetLocale](GetLocale.md)
  * [GetLocaleInfo](GetLocaleInfo.md)
  * [LSCurrencyFormat](LSCurrencyFormat.md)
  * [LSIsCurrency](LSIsCurrency.md)
  * [LSIsNumeric](LSIsNumeric.md)
  * [LSNumberFormat](LSNumberFormat.md)
  * [LSParseCurrency](LSParseCurrency.md)
  * [LSParseNumber](LSParseNumber.md)
  * [SetLocale](SetLocale.md)

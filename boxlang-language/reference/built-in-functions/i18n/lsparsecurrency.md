[comment]: # (Note: This documentation is generated dynamically in the build process.  To modify the contents, change the javadoc on the _invoke method of the BIF class)

# Function: `LSParseCurrency`

Parses a currency value in to a numeric using the specified or context locale

## Method Signature
```
LSParseCurrency(string=[string], locale=[string])
```
### Arguments

| Argument | Type | Required | Description | Default |
|----------|------|----------|-------------|---------|
| `string` | `string` | `true` | the value to be parsed |  |
| `locale` | `string` | `false` | the optional locale to apply in parsing |  |

## Examples

```
LSParseCurrency(string=[string], locale=[string])
```

## Related
  * [GetLocale](boxlang-language/reference/built-in-functions/GetLocale.md)
  * [GetLocaleDisplayName](boxlang-language/reference/built-in-functions/GetLocaleDisplayName.md)
  * [GetLocaleInfo](boxlang-language/reference/built-in-functions/GetLocaleInfo.md)
  * [LSCurrencyFormat](boxlang-language/reference/built-in-functions/LSCurrencyFormat.md)
  * [LSIsCurrency](boxlang-language/reference/built-in-functions/LSIsCurrency.md)
  * [LSIsNumeric](boxlang-language/reference/built-in-functions/LSIsNumeric.md)
  * [LSNumberFormat](boxlang-language/reference/built-in-functions/LSNumberFormat.md)
  * [LSParseNumber](boxlang-language/reference/built-in-functions/LSParseNumber.md)
  * [SetLocale](boxlang-language/reference/built-in-functions/SetLocale.md)
